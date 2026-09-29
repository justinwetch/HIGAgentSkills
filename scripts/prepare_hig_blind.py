"""Prepare a fresh topic-only answer packet; schema guards do not certify question semantics."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work/release-2026-09-12'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def prepare(snapshot: Path, questions: Path, topic: str, name: str, *, claim_grounding: bool = False) -> Path:
    if not topic or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in topic):
        raise ValueError('Invalid topic slug')
    if topic == 'instructions':
        raise ValueError('Topic reference collides with packet instructions')
    work_root = WORK.resolve()
    frozen_root = (WORK / 'frozen').resolve()
    blind_root = (WORK / 'blind').resolve()
    if not frozen_root.is_relative_to(work_root) or not blind_root.is_relative_to(work_root):
        raise ValueError('Frozen and blind directories must stay inside project work')
    snapshot = snapshot.resolve()
    if not snapshot.is_relative_to(frozen_root):
        raise ValueError('Candidate snapshot must be under the project frozen directory')
    frozen = json.loads((snapshot / 'manifest.json').read_text(encoding='utf-8-sig'))
    entries = frozen['files']
    names = [row['path'] for row in entries]
    if len(names) != len(set(names)) or topic not in frozen['topics']:
        raise ValueError('Ambiguous manifest or topic absent from snapshot')
    candidate_name = f'candidates/{topic}.md'
    coverage_name = f'coverage/{topic}.json'
    payload = {}
    for relative in (candidate_name, coverage_name):
        matches = [r for r in entries if r['path'] == relative]
        if len(matches) != 1:
            raise ValueError(f'Missing unique frozen input: {relative}')
        path = (snapshot / relative).resolve()
        if not path.is_relative_to(snapshot):
            raise ValueError('Frozen input escapes snapshot')
        data = path.read_bytes()
        if digest(data) != matches[0]['sha256']:
            raise ValueError(f'Frozen hash mismatch: {relative}')
        payload[relative] = data
    if json.loads(payload[coverage_name].decode('utf-8-sig'))['candidate_sha256'] != digest(payload[candidate_name]):
        raise ValueError('Candidate and coverage do not bind the same bytes')

    questions = questions.resolve()
    if not questions.is_relative_to(work_root):
        raise ValueError('Questions must be a project-local exam artifact')
    question_bytes = questions.read_bytes()
    data = json.loads(question_bytes.decode('utf-8-sig'))
    if isinstance(data, dict):
        if set(data) != {'questions'}:
            raise ValueError('Questions-only object must contain only questions')
        data = data['questions']
    if not isinstance(data, list):
        raise ValueError('Questions must be a list')
    seen = set()
    for row in data:
        if not isinstance(row, dict) or set(row) != {'id', 'topic', 'question'}:
            raise ValueError('Questions-only rows must contain exactly id, topic, question; no gold fields')
        if any(not isinstance(row[k], str) or not row[k].strip() for k in row):
            raise ValueError('Question fields must be nonempty strings')
        if row['id'] in seen:
            raise ValueError('Duplicate question identity')
        seen.add(row['id'])
    selected = [row for row in data if row['topic'] == topic]
    if not selected:
        raise ValueError('No questions for topic')

    target = (WORK / 'blind' / name).resolve()
    if target == blind_root or not target.is_relative_to(blind_root):
        raise ValueError('Output must be a new project-local blind packet')
    if target.exists():
        raise ValueError('Never overwrite an existing blind packet')
    files = {
        f'{topic}.md': payload[candidate_name],
        'instructions.md': (WORK / 'BLIND-ANSWERER.md').read_bytes(),
        'questions.json': (json.dumps({'questions': selected}, indent=2, ensure_ascii=False) + '\n').encode('utf-8'),
    }
    if claim_grounding:
        # Only the reviewed generic checker is allowed; no arbitrary extra files,
        # sources, answer keys, reviewer reports, or topic-specific helpers.
        checker = ROOT / 'scripts/check_hig_claims.py'
        if checker.is_symlink() or not checker.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('Claim checker must be an ordinary project script')
        files['claim_check.py'] = checker.read_bytes()
        files['instructions.md'] += b'\n' + (WORK / 'CLAIM-GROUNDING.md').read_bytes()
    manifest = {key: digest(value) for key, value in files.items()}
    files['manifest.json'] = (json.dumps(manifest, indent=2) + '\n').encode('utf-8')
    target.mkdir(parents=True)
    for relative, contents in files.items():
        (target / relative).write_bytes(contents)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--questions', type=Path, required=True)
    parser.add_argument('--topic', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--claim-grounding', action='store_true',
                        help='Include the generic mechanical checker; semantic QA is still required')
    args = parser.parse_args()
    print(prepare(args.snapshot, args.questions, args.topic, args.name, claim_grounding=args.claim_grounding))
