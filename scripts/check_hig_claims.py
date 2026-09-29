"""Mechanical checks for a frozen, topic-only HIG answer packet. No semantic grading.

Usage: python claim_check.py --packet DIR audit SELECTION.json
       python claim_check.py --packet DIR final ANSWERS.json
Audit input: {"id": QUESTION_ID, "support_audit": [
  {"requested_part": TEXT, "reference_lines": [FIRST, LAST], "reference_quote": TEXT}]}
Line numbers are inclusive and one-based; only line-ending normalization is permitted.
The audit command must be run and its output saved before composing the answer.
The final command checks actual saved answers, not a separate surrogate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def json_file(path):
    return json.loads(path.read_text(encoding='utf-8'))


def load_packet(directory):
    directory = directory.resolve()
    manifest_path = directory / 'manifest.json'
    if manifest_path.is_symlink():
        raise ValueError('manifest must be an ordinary local file')
    manifest = json_file(manifest_path)
    if not isinstance(manifest, dict) or not all(isinstance(k, str) for k in manifest):
        raise ValueError('manifest must map local filenames to hashes')
    refs = [n for n in manifest if n.endswith('.md') and n != 'instructions.md']
    if len(refs) != 1:
        raise ValueError('packet must contain one topic reference')
    expected = {refs[0], 'instructions.md', 'questions.json'}
    # A prospectively approved checker may be a fourth manifest input.
    if set(manifest) not in (expected, expected | {'claim_check.py'}):
        raise ValueError('unexpected packet input membership')
    contents = {}
    for name, expected_hash in manifest.items():
        path = directory / name
        if Path(name).name != name or path.is_symlink() or not path.resolve().is_relative_to(directory):
            raise ValueError('packet input must be an ordinary local file')
        data = path.read_bytes()
        if sha(data) != expected_hash:
            raise ValueError(f'packet hash mismatch: {name}')
        contents[name] = data
    questions = json.loads(contents['questions.json'].decode('utf-8'))
    if not isinstance(questions, dict) or set(questions) != {'questions'} or not isinstance(questions['questions'], list):
        raise ValueError('invalid questions-only object')
    ids = []
    topic = refs[0][:-3]
    for row in questions['questions']:
        if not isinstance(row, dict) or set(row) != {'id', 'topic', 'question'}:
            raise ValueError('question must contain exactly id, topic, question')
        if not all(nonempty(row[k]) for k in row) or row['topic'] != topic or row['id'] in ids:
            raise ValueError('invalid or duplicate question identity/topic')
        ids.append(row['id'])
    if not ids:
        raise ValueError('empty exam')
    text = contents[refs[0]].decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
    return {'reference': refs[0], 'reference_sha256': sha(contents[refs[0]]),
            'lines': text.split('\n'), 'ids': ids, 'topic': topic,
            'manifest_sha256': sha((directory / 'manifest.json').read_bytes())}


def audit_errors(audit, packet):
    errors = []
    if not isinstance(audit, list) or not audit:
        return ['support_audit must be a nonempty list']
    for i, item in enumerate(audit):
        prefix = f'audit[{i}]'
        if not isinstance(item, dict):
            errors.append(f'{prefix}: object required')
            continue
        if not nonempty(item.get('requested_part')) or not nonempty(item.get('reference_quote')):
            errors.append(f'{prefix}: nonempty requested_part and quote required')
        span = item.get('reference_lines')
        if (not isinstance(span, list) or len(span) != 2
                or any(type(n) is not int for n in span)
                or not 1 <= span[0] <= span[1] <= len(packet['lines'])):
            errors.append(f'{prefix}: invalid inclusive one-based line range')
            continue
        quote = item.get('reference_quote')
        if nonempty(quote) and quote not in '\n'.join(packet['lines'][span[0]-1:span[1]]):
            errors.append(f'{prefix}: quote differs from indicated reference lines')
    return errors


def validate_selection(doc, packet):
    if not isinstance(doc, dict):
        return ['selection must be an object']
    errors = []
    if doc.get('id') not in packet['ids']:
        errors.append('unknown question ID')
    return errors + audit_errors(doc.get('support_audit'), packet)


def validate_final(doc, packet):
    if not isinstance(doc, dict):
        return ['answers document must be an object']
    answers = doc.get('answers')
    if not isinstance(answers, list):
        return ['answers must be a list']
    errors = []
    ids = [a.get('id') if isinstance(a, dict) else None for a in answers]
    if ids != packet['ids']:
        errors.append('answer IDs/order must equal the complete expected question IDs')
    for i, answer in enumerate(answers):
        if not isinstance(answer, dict):
            errors.append(f'answer[{i}]: object required')
            continue
        current = validate_selection(answer, packet)
        if answer.get('topic') != packet['topic']:
            current.append('wrong topic')
        for field in ('requested_parts', 'reference_sections'):
            values = answer.get(field)
            if not isinstance(values, list) or not values or not all(nonempty(x) for x in values):
                current.append(f'{field} must contain nonempty strings')
        actual = answer.get('answer')
        if not nonempty(actual):
            current.append('answer must be nonempty')
        audits = answer.get('support_audit')
        if isinstance(audits, list):
            for j, item in enumerate(audits):
                quote = item.get('reference_quote') if isinstance(item, dict) else None
                if nonempty(quote) and (not isinstance(actual, str) or quote not in actual):
                    current.append(f'audit[{j}]: verified quote absent from actual answer')
        errors.extend(f'answer[{i}]: {e}' for e in current)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path, required=True)
    parser.add_argument('mode', choices=('audit', 'final'))
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    # Read-only; caller saves stdout to its assigned evidence path.
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'mode': args.mode, 'scope': 'mechanical only; no semantic or provenance pass'}
    try:
        packet = load_packet(args.packet)
        data = args.input.read_bytes()
        doc = json.loads(data.decode('utf-8'))
        errors = (validate_selection if args.mode == 'audit' else validate_final)(doc, packet)
        report.update(input_sha256=sha(data), reference=packet['reference'],
                      reference_sha256=packet['reference_sha256'],
                      manifest_sha256=packet['manifest_sha256'], errors=errors)
        if args.mode == 'audit' and not errors:
            report.update(id=doc['id'], verified_clauses=[x['reference_quote'] for x in doc['support_audit']])
    except (ValueError, OSError, TypeError, KeyError, UnicodeError) as exc:
        report['errors'] = [f'{type(exc).__name__}: {exc}']
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
