#!/usr/bin/env python3
"""Offline capture integrity, discovery closure, alias disposition, and delta triage.

Renderer comparisons are prioritization evidence, never semantic acceptance.
Native source bytes are never altered. Reference metadata is inventoried separately.
"""
import argparse
from collections import Counter
import difflib
import hashlib
import html
import json
from pathlib import Path
import re

from capture_native_hig import ROOT, normalize
from crawl_apple_hig import extract_links
from render_apple_hig import render_page


def lower_link_urls(text):
    return re.sub(r'https://developer\.apple\.com/[^\s)]+', lambda m: m.group().lower(), text)


def leaves(value):
    if isinstance(value, dict):
        for k, v in value.items():
            if k in ('text', 'code', 'title') and isinstance(v, str):
                yield v
            elif isinstance(v, (dict, list)):
                yield from leaves(v)
    elif isinstance(value, list):
        for v in value:
            yield from leaves(v)


def text_key(text):
    return re.sub(r'[^\w]+', '', html.unescape(text), flags=re.UNICODE).lower()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_dir', type=Path)
    parser.add_argument('--previous', type=Path, default=Path('sources/apple-hig-2026-06-09'))
    args = parser.parse_args()
    root = args.source_dir
    records = json.loads((root / 'inventory.json').read_text(encoding='utf-8'))
    prior = {r['slug']: r for r in json.loads((args.previous / 'inventory.json').read_text(encoding='utf-8'))}
    by_path = {r['path']: r for r in records}
    errors, aliases, deltas, resources, candidates = [], [], [], [], []
    counts = Counter()
    (root / 'diffs').mkdir(exist_ok=True)
    (root / 'supplements').mkdir(exist_ok=True)
    for r in records:
        slug = r['slug']
        if not r['markdown'].get('file') or not r['json'].get('file'):
            old = prior.get(slug, {})
            alias = old.get('alias_of')
            target = next((q for q in records if q['slug'] == alias), None)
            if target and target['markdown'].get('file') and target['json'].get('file') and all(r[k].get('status') == 404 for k in ('markdown', 'json')):
                aliases.append({'slug': slug, 'canonical': alias, 'reason': 'Previously documented same-source alias now returns 404 in both formats; canonical source captured.'})
                r.update(disposition='unavailable-historical-alias', alias_of=alias)
            else:
                errors.append({'slug': slug, 'reason': 'Unexplained capture failure'})
            continue
        for kind in ('markdown', 'json'):
            file = Path(r[kind]['file'])
            body = file.read_bytes()
            if hashlib.sha256(body).hexdigest() != r[kind]['sha256'] or len(body) != r[kind]['bytes']:
                errors.append({'slug': slug, 'reason': kind + ' checksum/byte mismatch'})
        text = Path(r['markdown']['file']).read_text(encoding='utf-8')
        page = json.loads(Path(r['json']['file']).read_text(encoding='utf-8'))
        metadata = json.loads(re.search(r'<!--\s*({.*?})\s*-->', text, re.S).group(1))
        if normalize(metadata['identifier']) != r['path'] or metadata['title'] != page['metadata']['title']:
            errors.append({'slug': slug, 'reason': 'Markdown/JSON identity mismatch'})
        missing = set(extract_links(page)) - set(by_path)
        if missing:
            errors.append({'slug': slug, 'reason': 'Uncaptured HIG references', 'paths': sorted(missing)})
        # This is a lexical export check, not a meaning/fidelity score.
        target_text = text_key(text)
        parts = set(p for p in leaves(page.get('primaryContentSections')) if len(text_key(p)) >= 30)
        absent = [p for p in parts if text_key(p) not in target_text]
        counts['source_text_segments_checked'] += len(parts)
        counts['source_text_segments_absent'] += len(absent)
        if absent:
            candidates.append({'slug': slug, 'unmatched_segments': sorted(absent)})
            supplemental = [f'# JSON export supplement: {r["title"]}', '',
                            'Generated from the captured JSON. This is source evidence, not Apple-authored Markdown or a distillation.',
                            'Blocks below contain text fragments not matched in the native Markdown by a lexical check. Read alongside native/' + slug + '.md.',
                            'Whole original blocks preserve context, captions, ordering, and metadata. They can repeat text that the Markdown does contain.', '',
                            'Source: ' + r['json']['url'], 'SHA-256: ' + r['json']['sha256'], '']
            for section_index, section in enumerate(page.get('primaryContentSections', [])):
                for block_index, block in enumerate(section.get('content', [])):
                    if any(p in absent for p in leaves(block)):
                        pointer = f'/primaryContentSections/{section_index}/content/{block_index}'
                        supplemental.extend(['## JSON pointer: ' + pointer, '', '```json', json.dumps(block, ensure_ascii=False, indent=2), '```', ''])
            (root / 'supplements' / (slug.replace('/', '__') + '.md')).write_text('\n'.join(supplemental), encoding='utf-8')
        # Keep DocC links and concrete image/video URLs available to the next pass.
        refs = page.get('references', {})
        for identifier, ref in refs.items():
            if ref.get('type') in ('image', 'video') or ('/documentation/' in identifier and not identifier.startswith('doc://com.apple.HIG/')):
                resources.append({'source_slug': slug, 'identifier': identifier, 'reference': ref})
        old_path = args.previous / 'raw' / Path(r['json']['file']).name
        if old_path.exists():
            old_render, new_render = render_page(old_path), render_page(Path(r['json']['file']))
            if old_render == new_render:
                category = 'renderer-identical'
            elif lower_link_urls(old_render) == lower_link_urls(new_render):
                category = 'renderer-url-case-only'
            else:
                category = 'renderer-other-difference'
                (root / 'diffs' / (slug.replace('/', '__') + '.diff')).write_text(''.join(difflib.unified_diff(lower_link_urls(old_render).splitlines(True), lower_link_urls(new_render).splitlines(True), fromfile='2026-06-09/' + slug, tofile='2026-09-12/' + slug)), encoding='utf-8')
        else:
            category = 'new-page'
        counts[category] += 1
        deltas.append({'slug': slug, 'category': category})
        r.update(json_endpoint=r['json']['url'], raw_file=r['json']['file'], source_sha256=r['json']['sha256'], kind=page.get('kind'),
                 distilled_file=('distilled/' + slug + '.md') if (Path('distilled') / (slug + '.md')).exists() else None)
    report = {'format': 'native-hig-capture-assessment-v1', 'capture_errors': errors, 'explained_aliases': aliases,
              'counts': dict(counts), 'deltas': deltas, 'lexical_export_check_candidates': candidates,
              'limitations': ['Renderer differences can include export structure, links, captions, ordering, and prose; they do not prove substantive changes.',
                              'Lexical segment presence does not prove table alignment, hierarchy, visual fidelity, completeness, or semantic equivalence.',
                              'External developer documentation and media are inventoried, not downloaded or reviewed.']}
    (root / 'inventory.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    (root / 'verification' / 'capture-assessment.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    (root / 'linked-resources.json').write_text(json.dumps(resources, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'capture_errors': errors, 'explained_aliases': aliases, 'counts': dict(counts), 'candidate_pages': [x['slug'] for x in candidates], 'linked_resource_records': len(resources)}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
