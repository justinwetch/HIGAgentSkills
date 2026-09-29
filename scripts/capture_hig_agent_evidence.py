"""Retain this task's child tool traces and runtime token records, without reasoning text."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work/release-2026-09-12'
CALL_TYPES = {'function_call', 'function_call_output', 'custom_tool_call', 'custom_tool_call_output'}


def capture(sessions: Path, parent: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    target = WORK / 'agent-traces' / stamp
    records = []
    seen_threads = set()
    for path in sessions.rglob('*.jsonl'):
        with path.open(encoding='utf-8') as stream:
            first = stream.readline()
        try:
            meta = json.loads(first).get('payload', {})
            spawn = meta.get('source', {}).get('subagent', {}).get('thread_spawn', {})
        except (ValueError, AttributeError):
            continue
        if spawn.get('parent_thread_id') != parent:
            continue
        if meta['id'] in seen_threads:
            raise ValueError(f'duplicate source log identity: {meta["id"]}')
        seen_threads.add(meta['id'])
        raw = path.read_bytes()
        events = []
        usages = {}
        for line in raw.splitlines():
            try:
                item = json.loads(line)
            except ValueError:
                continue  # A currently running writer may have an incomplete last line.
            payload = item.get('payload', {})
            if item.get('type') == 'response_item' and payload.get('type') in CALL_TYPES:
                events.append(item)
            elif item.get('type') == 'token_usage_record':
                usages[payload['response_id']] = item
        target.mkdir(parents=True, exist_ok=True)
        output = target / (meta['id'] + '.json')
        data = {'agent': spawn.get('agent_path'), 'thread_id': meta['id'], 'parent_thread_id': parent,
                'source_log': str(path), 'captured_prefix_bytes': len(raw),
                'captured_prefix_sha256': hashlib.sha256(raw).hexdigest(),
                'tool_events': events, 'runtime_usage_records': list(usages.values()),
                'scope': 'Actual retained tool calls/results and runtime-reported usage. Reasoning and ordinary conversation excluded. Usage is not an invoice or billed charge; tool traces require semantic inspection to establish relevant reads.'}
        output.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        totals = {}
        for usage in usages.values():
            for key, value in usage['payload']['usage'].items():
                totals[key] = totals.get(key, 0) + value
        records.append({'agent': data['agent'], 'thread_id': meta['id'], 'trace': str(output),
                        'trace_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                        'tool_events': len(events), 'unique_responses': len(usages),
                        'runtime_reported_token_totals': totals, 'billed_usage': None})
    if not records:
        raise ValueError('no child logs matched the explicitly supplied parent task')
    index = target / 'index.json'
    index.write_text(json.dumps({'parent': parent, 'records': records}, indent=2), encoding='utf-8')
    return index


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sessions', type=Path, required=True)
    parser.add_argument('--parent', required=True)
    args = parser.parse_args()
    print(capture(args.sessions, args.parent))
