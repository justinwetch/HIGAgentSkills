"""Freeze candidate and coverage bytes into a new immutable review-input directory."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work/release-2026-09-12'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name')
    parser.add_argument('topics', nargs='+')
    args = parser.parse_args()
    target = (WORK / 'frozen' / args.name).resolve()
    if not target.is_relative_to((WORK / 'frozen').resolve()) or target == (WORK / 'frozen').resolve():
        raise ValueError('freeze name must be project-local')
    if target.exists():
        raise ValueError('freeze destination exists; never overwrite review inputs')
    payload = {}
    for topic in args.topics:
        if not topic or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in topic):
            raise ValueError('invalid topic')
        candidate = (WORK / 'candidates' / f'{topic}.md').read_bytes()
        coverage = (WORK / 'coverage' / f'{topic}.json').read_bytes()
        expected = json.loads(coverage.decode('utf-8-sig'))['candidate_sha256']
        if hashlib.sha256(candidate).hexdigest() != expected:
            raise ValueError(f'{topic}: candidate/coverage are not a stable matching pair')
        payload[f'candidates/{topic}.md'] = candidate
        payload[f'coverage/{topic}.json'] = coverage
    target.mkdir(parents=True)
    manifest = {'frozen_at': datetime.now(timezone.utc).isoformat(), 'topics': args.topics, 'files': []}
    for relative, data in payload.items():
        p = target / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        manifest['files'].append({'path':relative,'sha256':hashlib.sha256(data).hexdigest()})
    (target / 'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps({'frozen':str(target),**manifest},indent=2))

if __name__ == '__main__':
    main()
