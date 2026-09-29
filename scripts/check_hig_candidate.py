"""Check candidate structure, routing, writer coverage and exact file bindings.

These mechanical checks do not establish semantic fidelity or independent QA.
"""
import argparse
import json
from pathlib import Path
from hig_source_blocks import ROOT, WORK, dump, sha
from measure_hig_release import source_map
from validate_corpus import parse_frontmatter, REQUIRED_FIELDS, VALID_TIERS

def check(topic):
    path=WORK/'candidates'/f'{topic}.md';coverage_path=WORK/'coverage'/f'{topic}.json'
    errors=[];meta=parse_frontmatter(path)
    if set(meta)!=REQUIRED_FIELDS: errors.append('Frontmatter must contain exactly the six routing fields')
    if meta.get('topic')!=topic: errors.append('Topic/filename mismatch')
    if meta.get('tier') not in VALID_TIERS: errors.append('Invalid tier')
    mapping=source_map(json.loads((WORK/'disposition-review.json').read_text(encoding='utf-8-sig')))
    if topic not in mapping: errors.append('Topic absent from approved release source mapping')
    for related in meta.get('related',[]):
        if related not in mapping: errors.append(f'Unknown related topic: {related}')
    triggers=meta.get('triggers',[])
    if not triggers or len({str(t).casefold() for t in triggers})!=len(triggers): errors.append('Empty or duplicated triggers')
    allowed_platforms={'ios','ipados','macos','tvos','watchos','visionos'}
    if not meta.get('platforms') or not set(meta['platforms'])<=allowed_platforms: errors.append('Invalid platforms')
    expected=set();all_ids=set();required_reads={}
    for slug in mapping.get(topic,[]):
        register_path=WORK/'source-blocks'/f'{slug}.json'
        reg=json.loads(register_path.read_text(encoding='utf-8'))
        all_ids.update(b['id'] for b in reg['blocks'])
        expected.update(b['id'] for b in reg['blocks'] if b['guidance'])
        source_root=ROOT/'sources/apple-hig-2026-09-12'
        required_reads[(source_root/'native'/f'{slug}.md').resolve()]=reg['source_native_sha256']
        required_reads[(source_root/'raw'/f'{slug}.json').resolve()]=reg['source_json_sha256']
        required_reads[register_path.resolve()]=sha(register_path)
        reading_path=WORK/'source-reading'/f'{slug}.md'
        required_reads[reading_path.resolve()]=sha(reading_path)
    covered=set()
    if not coverage_path.exists(): errors.append('Writer coverage missing')
    else:
        def coverage_object(pairs):
            obj={}
            for key,value in pairs:
                if key in obj: errors.append(f'Duplicate JSON member in writer coverage: {key}')
                obj[key]=value
            return obj
        cov=json.loads(coverage_path.read_text(encoding='utf-8-sig'),object_pairs_hook=coverage_object)
        if cov.get('candidate_sha256','').lower()!=sha(path): errors.append('Writer candidate hash stale or absent')
        if not cov.get('source_reads'): errors.append('Actual source read provenance missing')
        recorded_reads={}
        for read in cov.get('source_reads',[]):
            p=Path(read['path'])
            if not p.is_absolute(): p=ROOT/p
            p=p.resolve()
            recorded_reads[p]=read.get('sha256','').lower()
            if not p.exists() or sha(p)!=read.get('sha256','').lower(): errors.append(f'Source read hash mismatch: {p}')
        for p,expected_hash in required_reads.items():
            if recorded_reads.get(p)!=expected_hash:
                errors.append(f'Required assigned source provenance absent or mismatched: {p}')
        for row in cov.get('coverage',[]):
            if row.get('disposition') not in ('retained','redundant','non-guidance'): errors.append('Invalid coverage disposition')
            if not row.get('reason') or not row.get('destination'): errors.append('Coverage row needs destination and specific reason')
            covered.update(row.get('source_ids',[]))
        unknown=covered-all_ids
        if unknown: errors.append(f'Unknown source IDs: {sorted(unknown)}')
    missing=expected-covered
    if missing: errors.append(f'Unmapped guidance source IDs: {sorted(missing)}')
    result={'topic':topic,'candidate_sha256':sha(path),'coverage_sha256':sha(coverage_path) if coverage_path.exists() else None,
            'guidance_blocks_expected':len(expected),'guidance_blocks_mapped':len(expected&covered),
            'required_source_reads':[{ 'path':str(p),'sha256':h} for p,h in required_reads.items()],
            'errors':errors,'status':'PASS' if not errors else 'FAIL',
            'limit':'Mechanical structure/provenance only. Content correctness, metadata-only routing and independent numeric/fidelity/answer QA remain separate gates.'}
    dump(WORK/'mechanical'/f'{topic}.json',result)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('topics',nargs='+');args=p.parse_args()
    results=[check(t) for t in args.topics]
    for r in results: print(json.dumps(r,indent=2))
    if any(r['errors'] for r in results): raise SystemExit(1)

if __name__=='__main__': main()
