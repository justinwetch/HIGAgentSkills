"""Prepare bounded source assignments without dispatching or accepting any topic."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work/release-2026-09-12'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(batch_id: str, revision: int = 1) -> Path:
    batches = json.loads((WORK / 'batches.json').read_text(encoding='utf-8-sig'))['batches']
    batch = next(b for b in batches if b['id'] == batch_id)
    queue = {t['topic']: t for t in json.loads((WORK / 'queue.json').read_text(encoding='utf-8-sig'))['topics']}
    if not batch['topics'] or len(batch['topics']) != len(set(batch['topics'])):
        raise ValueError('assignment requires unique topic identities')
    if len(batch['topics']) > 4 or sum(queue[t]['guidance_tokens_o200k'] for t in batch['topics']) > 20000:
        raise ValueError('assignment exceeds approved batch limits')
    frozen = json.loads((ROOT / 'sources/apple-hig-2026-09-12/verification/source-freeze.json').read_text(encoding='utf-8-sig'))
    approved_sources = {(ROOT / f['file']).resolve(): f['sha256'] for f in frozen['source_files']}
    if revision < 1:
        raise ValueError('revision must be positive')
    target = WORK / 'assignments' / (batch_id if revision == 1 else f'{batch_id}-v{revision}')
    if target.exists():
        raise ValueError('assignment already exists; preserve frozen input record')
    records = []
    for topic in batch['topics']:
        source = queue[topic]
        paths = []
        for slug in source['source_slugs']:
            originals = [ROOT / 'sources/apple-hig-2026-09-12/native' / f'{slug}.md',
                         ROOT / 'sources/apple-hig-2026-09-12/raw' / f'{slug}.json']
            for path in originals:
                if approved_sources.get(path.resolve()) != sha(path):
                    raise ValueError(f'original source differs from September freeze: {path}')
            paths += originals + [
                      WORK / 'source-blocks' / f'{slug}.json',
                      WORK / 'source-reading' / f'{slug}.md']
        record = {'topic': topic, 'source_slugs': source['source_slugs'],
                  'source_inputs': [{'path': str(p), 'sha256': sha(p)} for p in paths],
                  'candidate_output': str(WORK / 'candidates' / f'{topic}.md'),
                  'coverage_output': str(WORK / 'coverage' / f'{topic}.json')}
        old = ROOT / 'distilled' / f'{topic}.md'
        if old.exists():
            content = old.read_text(encoding='utf-8')
            if not content.startswith('---\n'):
                raise ValueError(f'missing frontmatter: {old}')
            record['routing_frontmatter'] = content[:content.index('\n---', 4)+4]
            record['june_continuity_path_for_reviewer_only'] = str(old)
        if source['group'] == 'pilot-starting-candidate':
            pilot = WORK / 'candidates' / f'{topic}.md'
            record['pilot_starting_artifact'] = {'path': str(pilot), 'sha256': sha(pilot)}
        records.append(record)
    target.mkdir(parents=True)
    payload = {'batch': batch, 'status': 'prepared only; calibration gate controls dispatch',
               'topics': records, 'protocols': {n: {'path': str(WORK/n), 'sha256': sha(WORK/n)}
               for n in ['CONTRACT.md', 'DRAFTER.md', 'REVIEWER.md', 'EXAMINER.md', 'BLIND-ANSWERER.md']}}
    (target / 'assignment.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch')
    parser.add_argument('--revision', type=int, default=1)
    args = parser.parse_args()
    print(prepare(args.batch, args.revision))
