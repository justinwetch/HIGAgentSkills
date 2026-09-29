"""Measure canonical mapped source guidance against complete candidate bodies.

Never averages per-topic percentages; merged source pages enter the global
denominator once. Source accounting approval is separate from these mechanics.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import sys
from hig_source_blocks import ROOT, WORK, dump, plain, sha, word_count
from validate_corpus import parse_frontmatter, REQUIRED_FIELDS

sys.path.insert(0,str(ROOT/'work/distillation-pilot-2026-09-12/deps'))
os.environ.setdefault('TIKTOKEN_CACHE_DIR',str(ROOT/'work/distillation-pilot-2026-09-12/tokenizer-cache'))
import tiktoken

def body(text):
    # Only the existing structural routing fields are excluded. Comments and
    # resource sections are retained so they cannot hide output guidance.
    if text.startswith('---\n'):
        end=text.find('\n---',4)
        if end<0: raise ValueError('Unclosed frontmatter')
        text=text[end+4:]
    return plain(text,strip_comments=False)

def source_map(dispositions):
    mapped={}
    for record in dispositions['records']:
        if record['disposition'] not in ('retain','merge'): continue
        topics=record['target_topics']
        if len(topics)!=1: raise ValueError(f"Need explicit block allocation for {record['slug']}: {topics}")
        mapped.setdefault(topics[0],[]).append(record['slug'])
    return mapped

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidates',type=Path,required=True)
    parser.add_argument('--dispositions',type=Path,default=WORK/'disposition-review.json')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    dispositions=json.loads(args.dispositions.read_text(encoding='utf-8-sig'))
    mapping=source_map(dispositions)
    encodings={name:tiktoken.get_encoding(name) for name in ('o200k_base','cl100k_base')}
    records=[];all_source_ids=set();failures=[]
    for path in sorted(args.candidates.glob('*.md')):
        if path.stem not in mapping: raise ValueError(f'Candidate absent from approved source map: {path.stem}')
        meta=parse_frontmatter(path)
        extra=set(meta)-REQUIRED_FIELDS
        if extra: failures.append(f'{path.name}: unaccounted frontmatter fields {sorted(extra)}')
        blocks=[];source_hashes=[]
        for slug in mapping[path.stem]:
            register=json.loads((WORK/'source-blocks'/f'{slug}.json').read_text(encoding='utf-8'))
            blocks.extend(b for b in register['blocks'] if b['guidance'])
            source_hashes.append({'slug':slug,'json_sha256':register['source_json_sha256'],'native_sha256':register['source_native_sha256']})
        ids=[b['id'] for b in blocks]
        if len(ids)!=len(set(ids)): raise ValueError(f'Duplicated source block allocation: {path.stem}')
        if all_source_ids.intersection(ids): raise ValueError('Source block allocated to multiple output topics')
        all_source_ids.update(ids)
        original=plain('\n\n'.join(b['text'] for b in blocks)); full=path.read_text(encoding='utf-8'); output=body(full)
        a,b=word_count(original),word_count(output,False)
        reduction=100*(1-b/a) if a else None
        record={'topic':path.stem,'candidate_sha256':sha(path),'source_hashes':source_hashes,'source_blocks':ids,
                'source_guidance_words':a,'output_guidance_words':b,'word_reduction_percent':round(reduction,3) if reduction is not None else None,
                'compression_review_flag':reduction is None or reduction<60 or reduction>85,
                'routing_metadata_audit_required':'Reviewer must confirm excluded frontmatter fields contain only routing metadata, never hidden design guidance.',
                'tokens':{name:{'source_guidance':len(enc.encode(original)),'output_guidance':len(enc.encode(output)),
                                'candidate_full_file':len(enc.encode(full))} for name,enc in encodings.items()}}
        records.append(record)
    total_a=sum(r['source_guidance_words'] for r in records);total_b=sum(r['output_guidance_words'] for r in records)
    totals={'source_guidance_words':total_a,'output_guidance_words':total_b,'word_reduction_percent':round(100*(1-total_b/total_a),3) if total_a else None,
            'tokens':{name:{key:sum(r['tokens'][name][key] for r in records) for key in ('source_guidance','output_guidance','candidate_full_file')} for name in encodings}}
    report={'method_version':'canonical-blocks-v1','method':'Source: mapped canonical JSON primary guidance with captions/alt/footnotes/API-deprecation metadata, once per block. Excludes aliases, collection-only pages, resource link grids and change history. Output: whole Markdown body including comments and resources; only approved structural frontmatter and link destinations excluded. Tables normalize padding/HTML breaks. Global reduction is ratio of summed word counts, not average percentages.',
            'source_dispositions_sha256':sha(args.dispositions),'measurement_script_sha256':sha(Path(__file__)),
            'source_register_script_sha256':sha(ROOT/'scripts/hig_source_blocks.py'),
            'tokenizers':list(encodings),'tiktoken_version':tiktoken.__version__,'token_limit':'Named encoding file-content counts, not billed usage or every model tokenizer.',
            'candidate_count':len(records),'mapped_release_topics':len(mapping),'omitted_candidates':sorted(set(mapping)-{r['topic'] for r in records}),
            'failures':failures,'totals':totals,'topics':records}
    dump(args.output,report)
    print(json.dumps({k:v for k,v in report.items() if k in ('candidate_count','mapped_release_topics','failures','totals')},indent=2))
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
