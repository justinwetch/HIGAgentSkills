"""Validate exact extracted runtime membership, routing and local Markdown/HTML links."""
from __future__ import annotations
import argparse
import hashlib
from html.parser import HTMLParser
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from markdown_it import MarkdownIt
from generate_routing_index import generate, parse_frontmatter
from package_runtime_zip import read_manifest, REFERENCE_DIR

FOUNDATIONS = {'accessibility', 'branding', 'color', 'dark-mode', 'design-principles',
               'icons', 'images', 'inclusion', 'layout', 'materials', 'motion', 'privacy',
               'right-to-left', 'sf-symbols', 'typography', 'writing'}
FIELDS = {'topic', 'tier', 'platforms', 'category', 'triggers', 'related'}
SAFE_TAGS = {'a', 'img', 'br', 'hr', 'p', 'div', 'span', 'details', 'summary', 'kbd', 'code',
             'pre', 'strong', 'em', 'b', 'i', 's', 'del', 'ins', 'sup', 'sub', 'ul', 'ol', 'li',
             'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td', 'blockquote', 'q', 'aside',
             'section', 'article', 'figure', 'figcaption', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}
SAFE_ATTRS = {'id', 'class', 'style', 'title', 'name', 'href', 'src', 'alt', 'width', 'height',
              'align', 'target', 'rel', 'download', 'loading', 'decoding', 'start', 'type',
              'reversed', 'open', 'colspan', 'rowspan', 'scope', 'headers', 'border',
              'cellpadding', 'cellspacing', 'dir', 'lang', 'hidden', 'tabindex', 'role',
              'cite', 'longdesc'}


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.unsupported = []
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag not in SAFE_TAGS:
            self.unsupported.append(f'unsupported HTML element: {tag}')
        if tag == 'style':
            self.in_style = True
        for key, value in attrs:
            if key not in SAFE_ATTRS and not key.startswith('aria-'):
                self.unsupported.append(f'unsupported HTML attribute: {key}')
            if value and key in {'href', 'src', 'poster', 'xlink:href', 'background', 'cite', 'longdesc'}:
                self.links.append(value)
            if value and key in {'srcset', 'imagesrcset', 'srcdoc'}:
                self.unsupported.append(f'unsupported HTML URL carrier: {key}')
            if value and key == 'style' and re.search(r'url\s*\(|@import|\\', value, re.I):
                self.unsupported.append('unsupported CSS resource reference')
            if value and (key == 'id' or (tag == 'a' and key == 'name')):
                self.ids.add(value)

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_style and re.search(r'url\s*\(|@import|\\', data, re.I):
            self.unsupported.append('unsupported CSS resource reference')


def markdown_links(text: str) -> tuple[list[str], set[str], list[str]]:
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end >= 0:
            text = text[end+4:]
    tokens = MarkdownIt('commonmark', {'html': True}).parse(text)
    links, anchors = [], set()
    html = HTMLLinks()
    for index, token in enumerate(tokens):
        if token.type == 'heading_open':
            inline = tokens[index+1]
            heading = ''.join(c.content for c in inline.children or [] if c.type in {'text', 'code_inline', 'image'})
            slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
            unique, count = slug, 0
            while unique in anchors:
                count += 1
                unique = f'{slug}-{count}'
            anchors.add(unique)
        for child in [token] + (token.children or []):
            if child.type == 'link_open':
                links.append(child.attrGet('href'))
            elif child.type == 'image':
                links.append(child.attrGet('src'))
            elif child.type in {'html_inline', 'html_block'}:
                html.feed(child.content)
    return links + html.links, anchors | html.ids, html.unsupported


def validate(root: Path, manifest: dict) -> dict:
    root = root.resolve()
    expected = {f['path']: f['sha256'] for f in manifest['files']}
    actual = {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file()}
    errors = []
    if set(actual) != set(expected):
        errors.append({'membership': {'missing': sorted(set(expected)-set(actual)), 'extra': sorted(set(actual)-set(expected))}})
    if len(actual) != len({p.casefold() for p in actual}):
        errors.append('case-colliding extracted files')
    for relative, path in actual.items():
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f'linked or escaped extracted file: {relative}')
        if relative in expected and hashlib.sha256(path.read_bytes()).hexdigest() != expected[relative]:
            errors.append(f'hash mismatch: {relative}')
    documents = {name: markdown_links(path.read_text(encoding='utf-8')) for name, path in actual.items() if name.endswith('.md')}
    checked = []
    for name, (links, _, unsupported) in documents.items():
        errors.extend({'from': name, 'unsupported': item} for item in unsupported)
        for href in links:
            url = urlsplit(href)
            if url.scheme and url.scheme.lower() not in {'http', 'https', 'mailto', 'tel'}:
                errors.append({'from': name, 'href': href, 'result': 'unsupported or nonportable URL scheme'})
                continue
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
            reason = None
            if path.startswith('/') or '\\' in path or target.startswith('../'):
                reason = 'unsafe or nonportable relative destination'
            elif target not in actual:
                reason = 'missing destination or incorrect path case'
            elif url.fragment and target in documents and unquote(url.fragment) not in documents[target][1]:
                reason = 'missing heading or HTML anchor'
            checked.append({'from': name, 'href': href, 'target': target, 'result': reason or 'pass'})
            if reason:
                errors.append(checked[-1])
    records = {}
    for topic in manifest['topics']:
        path = root / REFERENCE_DIR / f'{topic}.md'
        if not path.is_file():
            continue
        try:
            meta = parse_frontmatter(path)
            records[topic] = meta
            if set(meta) != FIELDS or meta.get('topic') != topic:
                errors.append(f'frontmatter schema mismatch: {topic}')
            if type(meta.get('tier')) is not int or meta['tier'] not in {1, 2, 3, 4}:
                errors.append(f'invalid tier: {topic}')
            if not isinstance(meta.get('category'), str) or not meta['category'].strip():
                errors.append(f'invalid category: {topic}')
            for field in ['platforms', 'triggers', 'related']:
                value = meta.get(field)
                if not isinstance(value, list) or any(not isinstance(s, str) or not s.strip() for s in value):
                    errors.append(f'invalid {field} list: {topic}')
                elif len(value) != len({s.casefold() for s in value}):
                    errors.append(f'duplicate {field}: {topic}')
            platforms = meta.get('platforms')
            if not isinstance(platforms, list) or not platforms or not set(platforms) <= {'ios', 'ipados', 'macos', 'tvos', 'visionos', 'watchos'}:
                errors.append(f'invalid platforms: {topic}')
            if not meta.get('triggers'):
                errors.append(f'empty triggers: {topic}')
            for related in meta.get('related', []):
                if related not in manifest['topics']:
                    errors.append(f'unknown related topic: {topic} -> {related}')
        except ValueError as exc:
            errors.append(str(exc))
    if {t for t, m in records.items() if m.get('tier') == 1} != FOUNDATIONS:
        errors.append('mandatory foundation set changed')
    routing = root / 'routing-index.md'
    if routing.is_file() and routing.read_text(encoding='utf-8') != generate(root / REFERENCE_DIR):
        errors.append('routing index differs from released frontmatter')
    return {'status': 'fail' if errors else 'pass', 'expected_files': len(expected),
            'actual_files': len(actual), 'topics': len(records), 'local_links': checked, 'errors': errors,
            'scope': 'Membership, hashes, routing structure and local links only; no source fidelity or observed agent behavior claim.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = validate(args.root, read_manifest(args.manifest))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'local_links'}, indent=2))
    raise SystemExit(0 if report['status'] == 'pass' else 1)
