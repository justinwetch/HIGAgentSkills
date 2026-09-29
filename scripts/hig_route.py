#!/usr/bin/env python3
"""Resolve literal HIG triggers and exactly one related hop, without loading guidance."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path


def trigger_pattern(trigger: str) -> str:
    """Standalone match; spaces and hyphens are interchangeable, and a final word may be plural."""
    signature = re.fullmatch(r'(.+?)\(.*\)', trigger)
    if signature:
        # API symbol: match the full signature or the bare symbol name.
        return r'(?<!\w)(?:' + re.escape(trigger) + '|' + re.escape(signature[1]) + r')(?!\w)'
    words = [w for w in re.split(r'[\s-]+', trigger) if w]
    parts = [re.escape(w) for w in words]
    last = words[-1]
    if re.fullmatch(r'[a-z]*[^aeiou\W\d_]y', last, re.IGNORECASE):
        parts[-1] = re.escape(last[:-1]) + '(?:y|ies)'
    elif re.fullmatch(r'[a-z]{2,}', last, re.IGNORECASE):
        parts[-1] += '(?:s|es)?'
    return r'(?<!\w)' + r'[\s-]+'.join(parts) + r'(?!\w)'


def read_request(path: str) -> str:
    data = sys.stdin.buffer.read() if path == '-' else Path(path).read_bytes()
    for encoding in ('utf-8-sig', 'utf-16'):
        if encoding == 'utf-16' and not data.startswith((b'\xff\xfe', b'\xfe\xff')):
            continue
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    raise ValueError('request must be UTF-8 (or UTF-16 with a byte-order mark)')


def related(root: Path, topic: str) -> list[str]:
    text = (root / 'references/hig' / f'{topic}.md').read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError(f'missing frontmatter: {topic}')
    lines = text.split('---', 2)[1].splitlines()
    values, active = [], False
    for line in lines:
        if line.startswith('related:'):
            active = True
            inline = line.split(':', 1)[1].strip()
            if inline:
                if not inline.startswith('[') or not inline.endswith(']'):
                    raise ValueError(f'unsupported related syntax: {topic}')
                values.extend(x.strip().strip('\"\'') for x in inline[1:-1].split(',') if x.strip())
        elif active and line.startswith('  - '):
            values.append(line[4:].strip().strip('\"\''))
        elif active and line.strip():
            break
    return values


def route(root: Path, request: str, exclude_topics: list[str] | None = None) -> dict:
    excluded = set(exclude_topics or [])
    index = (root / 'routing-index.md').read_text(encoding='utf-8')
    tier, foundations, rows = None, [], []
    for line in index.splitlines():
        heading = re.match(r'## tier-([1-4])\b', line)
        if heading:
            tier = int(heading[1])
        elif tier == 1 and line and not line.startswith('#'):
            foundations.extend(x.strip() for x in line.split(','))
        elif tier in (2, 3, 4) and ' → ' in line:
            triggers, topic = line.split(' → ', 1)
            rows.append((tier, topic, triggers.split(', ')))
    known = set(foundations) | {topic for _, topic, _ in rows}
    if excluded - known:
        raise ValueError(f'unknown excluded topics: {sorted(excluded - known)}')
    if excluded.intersection(foundations):
        raise ValueError('mandatory foundations cannot be excluded')
    initial, direct4 = {}, {}
    for tier, topic, triggers in rows:
        if topic in excluded:
            continue
        hits = []
        for trigger in triggers:
            match = re.search(trigger_pattern(trigger), request, re.IGNORECASE)
            if match:
                hits.append({'trigger': trigger, 'matched_text': match[0], 'span': list(match.span())})
        if hits:
            (direct4 if tier == 4 else initial)[topic] = {'matches': hits}
    if 'designing-for-iphone-duo' in initial and 'designing-for-ios' not in initial and 'designing-for-ios' not in excluded:
        initial['designing-for-ios'] = {'reason': 'Duo is an iOS form factor', 'matches': []}
    expansion = {}
    for topic in sorted(initial):
        for target in related(root, topic):
            if target not in known:
                raise ValueError(f'unknown related topic: {topic} -> {target}')
            if target not in initial and target not in foundations and target not in excluded:
                expansion.setdefault(target, []).append(topic)
    topics = sorted(set(foundations) | set(initial) | set(expansion) | set(direct4))
    return {'request': request, 'excluded_topics': sorted(excluded),
            'foundations': foundations, 'initial': initial,
            'one_hop_related': expansion, 'direct_tier4': direct4,
            'files': [f'references/hig/{t}.md' for t in topics],
            'instruction': 'Read every listed guidance file. This output is routing metadata, not guidance. Specific extra clarification loads must not expand related topics.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request-file', required=True, help='UTF-8 file containing only the exact user request, or - for stdin')
    parser.add_argument('--skill-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--exclude-topic', action='append', default=[], help='Topic explicitly excluded by the user; never a foundation')
    args = parser.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    try:
        result = route(args.skill_root, read_request(args.request_file), args.exclude_topic)
    except (OSError, ValueError) as error:
        parser.exit(2, f'hig_route: error: {error}\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
