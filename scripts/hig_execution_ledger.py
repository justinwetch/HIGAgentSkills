"""Record observed dispatch/completion and file-content volumes, never billing estimates."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from hig_source_blocks import ROOT, WORK
import measure_hig_release  # Configures the project-local tokenizer dependency.
import tiktoken

LEDGER = WORK / 'execution-ledger.json'


def artifacts(paths):
    result=[]
    enc={n:tiktoken.get_encoding(n) for n in ('o200k_base','cl100k_base')}
    for name in paths:
        path=Path(name)
        if not path.is_absolute(): path=ROOT/path
        path=path.resolve()
        if not path.is_relative_to(ROOT) or not path.is_file(): raise ValueError(f'Invalid project artifact: {path}')
        data=path.read_bytes()
        try: text=data.decode('utf-8-sig')
        except UnicodeDecodeError: text=None
        result.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
                       'file_tokens':{n:len(e.encode(text)) for n,e in enc.items()} if text is not None else None})
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='action',required=True)
    start=sub.add_parser('start');start.add_argument('id');start.add_argument('--agent',required=True)
    start.add_argument('--batch',required=True);start.add_argument('--attempt',type=int,required=True)
    start.add_argument('--context',choices=['fresh','continuation'],required=True)
    start.add_argument('--tier',choices=['drafting','review'],required=True,help='Drafting tier for routine work; stronger review tier for independent QA')
    start.add_argument('--reasoning',choices=['high','xhigh'],required=True)
    start.add_argument('--phase',choices=['draft','source-exam','review','answer','grade','correction','method'],required=True)
    start.add_argument('--topics',nargs='*',default=[]);start.add_argument('--inputs',nargs='*',default=[])
    finish=sub.add_parser('finish');finish.add_argument('id');finish.add_argument('--status',choices=['completed','failed','interrupted'],required=True)
    finish.add_argument('--outputs',nargs='*',default=[])
    args=parser.parse_args();now=datetime.now(timezone.utc)
    data=json.loads(LEDGER.read_text(encoding='utf-8')) if LEDGER.exists() else {'records':[],
        'measurement_scope':'Observed dispatch-to-completion wall time includes scheduling and tool time. File-content tokens and mapped source volumes are not billed usage or proof of actual model context; retain agent read logs separately.',
        'historical_limit':'Earlier calibration timing is incomplete and preserved separately; this ledger does not backfill invented history.'}
    records=data['records']
    if args.action=='start':
        if args.attempt<1: raise ValueError('Attempt must be positive')
        if any(r['id']==args.id for r in records): raise ValueError('Duplicate dispatch identity')
        if sum(r['status']=='running' for r in records)>=3: raise ValueError('Three recorded workers already active; verify completions before dispatch')
        q={t['topic']:t for t in json.loads((WORK/'queue.json').read_text(encoding='utf-8'))['topics']}
        if any(t not in q for t in args.topics): raise ValueError('Topic outside approved queue')
        tokens=sum(q[t]['guidance_tokens_o200k'] for t in set(args.topics))
        if len(args.topics)!=len(set(args.topics)) or len(args.topics)>4 or tokens>20000: raise ValueError('Batch exceeds topic/token bounds or repeats topics')
        if args.phase in ('draft','answer') and (args.tier!='drafting' or args.reasoning!='high'): raise ValueError('Routine draft/answer work must use the drafting tier at high reasoning')
        if args.phase in ('draft','answer','source-exam') and args.context!='fresh': raise ValueError('Initial drafting, blind answers and source-only exams require fresh context')
        if args.phase in ('source-exam','review','grade','method') and args.tier!='review': raise ValueError('Independent QA requires the review tier')
        if args.phase=='correction' and args.attempt>2 and args.tier!='review': raise ValueError('Correction after two drafting-tier attempts requires the review tier')
        record={'id':args.id,'batch':args.batch,'attempt':args.attempt,'context':args.context,'agent':args.agent,'tier':args.tier,'reasoning':args.reasoning,'phase':args.phase,'topics':args.topics,
                'mapped_source_guidance_tokens_o200k':tokens,'observed_dispatch_at':now.isoformat(),'observed_completion_at':None,
                'observed_elapsed_seconds':None,'status':'running','inputs':artifacts(args.inputs),'outputs':[], 'billing_usage':None}
        records.append(record)
    else:
        matches=[r for r in records if r['id']==args.id and r['status']=='running']
        if len(matches)!=1: raise ValueError('No unique active dispatch to finish')
        record=matches[0];record.update(status=args.status,observed_completion_at=now.isoformat(),
             observed_elapsed_seconds=round((now-datetime.fromisoformat(record['observed_dispatch_at'])).total_seconds(),3),outputs=artifacts(args.outputs))
    temporary=LEDGER.with_suffix('.json.tmp');temporary.write_text(json.dumps(data,indent=2),encoding='utf-8');temporary.replace(LEDGER)
    print(json.dumps(record,indent=2))

if __name__=='__main__': main()
