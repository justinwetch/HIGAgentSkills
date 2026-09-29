#!/usr/bin/env python3
"""Capture unmodified English Apple HIG Markdown + JSON; inventory the link closure.

Uses current root links plus old inventory and distilled slugs as recovery seeds.
Does not distill, render over Apple's Markdown, or follow the entire API doc graph.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from crawl_apple_hig import extract_links, normalize_hig_path, page_title, slug_for_path

ROOT = '/design/human-interface-guidelines'
BASE = 'https://developer.apple.com'
PATH_RE = re.compile(r'/design/human-interface-guidelines(?:/[a-z0-9_-]+)*', re.I)
LINK_RE = re.compile(r'\]\(([^\s)]+)')


def now():
    return datetime.now(timezone.utc).isoformat()


def normalize(value):
    value = urllib.parse.unquote(value).split('#')[0].split('?')[0]
    if value.startswith('http'):
        url = urllib.parse.urlsplit(value)
        if url.hostname != 'developer.apple.com':
            return None
        value = url.path
    value = value.removeprefix('/tutorials/data').removesuffix('.md').removesuffix('.json')
    return normalize_hig_path(value.lower())


def fetch(path, kind, output):
    url = BASE + '/tutorials/data' + path + '.' + kind
    result = {'url': url, 'retrieved_at': now()}
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'HIGAgentSkills-source-capture/2.0'})
            with urllib.request.urlopen(req, timeout=35) as response:
                body = response.read()
                content_type = response.headers.get('Content-Type', '')
                result.update(status=response.status, final_url=response.url, content_type=content_type,
                              etag=response.headers.get('ETag'), last_modified=response.headers.get('Last-Modified'))
            text = body.decode('utf-8')
            parsed = json.loads(text) if kind == 'json' else None
            if kind == 'md' and ('text/markdown' not in content_type or not re.search(r'^# ', text, re.M)):
                raise ValueError('Response is not native Markdown with a title')
            filename = slug_for_path(path).replace('/', '__') + '.' + kind
            target = output / ('native' if kind == 'md' else 'raw') / filename
            target.write_bytes(body)
            result.pop('error', None)
            result.update(file=target.as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), attempts=attempt + 1)
            return result, text, parsed
        except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
            result.update(error=str(exc), attempts=attempt + 1)
            if isinstance(exc, urllib.error.HTTPError):
                result['status'] = exc.code
            if attempt < 2:
                time.sleep(attempt + 1)
    return result, '', None


def capture(path, output):
    md, text, _ = fetch(path, 'md', output)
    js, _, data = fetch(path, 'json', output)
    links = set(extract_links(data)) if data else set()
    links.update(filter(None, (normalize(m.group()) for m in PATH_RE.finditer(text))))
    external = set()
    for target in LINK_RE.findall(text):
        if target.startswith(('/', 'https://developer.apple.com/')) and not normalize(target):
            external.add(urllib.parse.urljoin(BASE, target))
    return {'slug': slug_for_path(path), 'path': path, 'apple_url': BASE + path,
            'json_endpoint': js['url'], 'raw_file': js.get('file'), 'source_sha256': js.get('sha256'),
            'kind': data.get('kind') if data else None,
            'distilled_file': ('distilled/' + slug_for_path(path) + '.md') if (Path('distilled') / (slug_for_path(path) + '.md')).exists() else None,
            'title': page_title(data, path) if data else slug_for_path(path),
            'role': data.get('metadata', {}).get('role') if data else None,
            'markdown': md, 'json': js, 'references_discovered': sorted(links),
            'linked_non_hig_resources': sorted(external)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--previous', type=Path, default=Path('sources/apple-hig-2026-06-09/inventory.json'))
    parser.add_argument('--workers', type=int, default=6)
    args = parser.parse_args()
    for name in ('native', 'raw', 'verification'):
        (args.output / name).mkdir(parents=True, exist_ok=True)
    previous = json.loads(args.previous.read_text(encoding='utf-8'))
    old = {r['slug']: r for r in previous}
    seeds = {ROOT, ROOT + '/designing-for-iphone-duo'}
    seeds.update(normalize(r['apple_url']) for r in previous)
    seeds.update(ROOT + '/' + p.stem for p in Path('distilled').glob('*.md'))
    pending = seeds - {None}
    records = {}
    started = now()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        while pending:
            batch = sorted(pending)
            pending = set()
            for record in pool.map(lambda p: capture(p, args.output), batch):
                records[record['path']] = record
                for link in record['references_discovered']:
                    if link not in records and link not in batch:
                        pending.add(link)
                print(f"{len(records):3} {record['slug']} md={record['markdown'].get('status')} json={record['json'].get('status')}", flush=True)
                (args.output / 'inventory.json').write_text(json.dumps(sorted(records.values(), key=lambda r: r['slug']), indent=2) + '\n', encoding='utf-8')
    reachable, queue = set(), [ROOT]
    while queue:
        path = queue.pop()
        if path in reachable:
            continue
        reachable.add(path)
        queue.extend(p for p in records.get(path, {}).get('references_discovered', []) if p not in reachable)
    failures = []
    changed, same, added = [], [], []
    for record in records.values():
        slug = record['slug']
        record['reachable_from_current_root'] = record['path'] in reachable
        record['disposition'] = 'pending-source-review'
        prior = old.get(slug)
        if prior and record['json'].get('sha256'):
            status = 'unchanged' if record['json']['sha256'] == prior['source_sha256'] else 'changed'
            record['previous_json_comparison'] = status
            (same if status == 'unchanged' else changed).append(slug)
        elif not prior:
            added.append(slug)
        for kind in ('markdown', 'json'):
            if 'error' in record[kind]:
                failures.append({'slug': slug, 'kind': kind, **record[kind]})
    summary = {'started_at': started, 'completed_at': now(), 'scope': 'English HIG link closure; prior inventory and current distilled slugs checked as recovery seeds; linked API docs and assets inventoried only',
               'records': len(records), 'root_reachable': len(reachable),
               'native_markdown_success': sum('file' in r['markdown'] for r in records.values()),
               'json_success': sum('file' in r['json'] for r in records.values()),
               'failures': len(failures), 'new_slugs': sorted(added), 'json_changed': sorted(changed),
               'json_unchanged': sorted(same), 'not_root_reachable': sorted(r['slug'] for r in records.values() if not r['reachable_from_current_root']),
               'previous_slugs_not_captured': sorted(set(old) - {r['slug'] for r in records.values()}),
               'bytes_markdown': sum(r['markdown'].get('bytes', 0) for r in records.values())}
    for name, data in [('inventory', sorted(records.values(), key=lambda r: r['slug'])), ('failures', failures), ('capture-summary', summary)]:
        (args.output / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
