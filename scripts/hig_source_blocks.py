"""Freeze DocC source blocks without combining native and JSON export duplicates.

The register is an accounting/read aid, not semantic acceptance. Original JSON,
native Markdown and figures remain required review inputs. Source references
retain their metadata separately; only primary guidance enters the denominator.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/apple-hig-2026-09-12'
WORK = ROOT / 'work/release-2026-09-12'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def plain(text, strip_comments=True):
    if strip_comments:
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = html.unescape(re.sub(r'<br\s*/?>', '\n', text, flags=re.I))
    text = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'(?:https?://|doc://)\S+', '', text)
    text = re.sub(r'^\s*\|?[ :|-]+\|[ :|\-]*$', '', text, flags=re.M)
    return '\n'.join('|'.join(c.strip() for c in line.split('|')) if '|' in line else line.strip() for line in text.splitlines()).strip()

def word_count(text, strip_comments=True):
    return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", plain(text, strip_comments)))

def render(value, refs):
    if value is None: return ''
    if isinstance(value, str): return value
    if isinstance(value, list): return ''.join(render(x, refs) for x in value)
    if not isinstance(value, dict): return str(value)
    kind = value.get('type')
    if kind == 'text': return value.get('text', '')
    if kind == 'codeVoice': return '`'+value.get('code', value.get('text', ''))+'`'
    if kind == 'reference':
        ref = refs.get(value.get('identifier'), {})
        label = render(value.get('overridingTitleInlineContent'), refs) or value.get('overridingTitle') or ref.get('title') or value.get('identifier', '')
        return str(label)
    if kind in ('strong', 'emphasis'):
        mark = '**' if kind == 'strong' else '*'
        return mark+render(value.get('inlineContent'), refs)+mark
    if kind in ('image', 'video'):
        ref = refs.get(value.get('identifier'), {})
        parts = [render(value.get('metadata', {}).get('abstract'), refs), str(ref.get('alt') or value.get('alt') or ''), render(ref.get('abstract'), refs)]
        unique = []
        for p in parts:
            p = p.strip()
            if p and p not in unique: unique.append(p)
        return '\n\n'.join(unique)
    if kind == 'heading': return '#'*int(value.get('level', 2))+' '+value.get('text', '')+'\n\n'
    if kind in ('paragraph', 'small'): return render(value.get('inlineContent'), refs)+'\n\n'
    if kind == 'table':
        rows=[]
        for row in value.get('rows', []):
            cells = row.get('cells', []) if isinstance(row, dict) else row
            rows.append([render(cell, refs).strip().replace('\n\n', '<br>') for cell in cells])
        if not rows: return ''
        out=['|'+'|'.join(rows[0])+'|', '|'+'|'.join('---' for _ in rows[0])+'|']
        out += ['|'+'|'.join(row)+'|' for row in rows[1:]]
        return '\n'.join(out)+'\n\n'
    if kind in ('unorderedList', 'orderedList'):
        lines=[]
        for i,item in enumerate(value.get('items',[])):
            content=item.get('content',item) if isinstance(item,dict) else item
            marker='- ' if kind=='unorderedList' else f'{i+1}. '
            lines.append(marker+render(content,refs).strip().replace('\n','\n  '))
        return '\n'.join(lines)+'\n\n'
    if kind == 'aside': return '> '+str(value.get('name') or value.get('style') or 'Note')+': '+render(value.get('content'), refs)+'\n'
    if kind == 'row': return '\n'.join(render(c.get('content', c), refs) for c in value.get('columns', []))
    if kind == 'tabNavigator':
        sections=[]
        for tab in value.get('tabs',[]):
            content=tab.get('content',[]); title=tab.get('title','')
            first=content[0] if content and isinstance(content[0],dict) else {}
            repeated=first.get('type')=='heading' and first.get('text','').strip()==title.strip()
            sections.append(('' if repeated else '#### '+title+'\n')+render(content,refs))
        return '\n'.join(sections)
    if kind == 'links': return '\n'.join(str(refs.get(i,{}).get('title', i)) for i in value.get('items',[]))+'\n'
    if kind == 'codeListing':
        code=value.get('code',[])
        return '```\n'+ ('\n'.join(code) if isinstance(code,list) else str(code))+'\n```\n'
    for key in ('content', 'inlineContent', 'text', 'items'):
        if key in value: return render(value[key],refs)
    raise ValueError(f'Unrendered source node: {value}')

def reference_nodes(value, pointer=''):
    if isinstance(value,dict):
        if value.get('type') in ('image','video','reference'):
            yield pointer,value
        for k,v in value.items(): yield from reference_nodes(v,pointer+'/'+k)
    elif isinstance(value,list):
        for i,v in enumerate(value): yield from reference_nodes(v,pointer+'/'+str(i))

def table_layouts(value,pointer=''):
    if isinstance(value,dict):
        if value.get('type')=='table' and value.get('extendedData'):
            yield {'pointer':pointer,'extendedData':value['extendedData'],
                   'warning':'Storage cells include merged/covered cells. Empty covered cells are not missing values. Apply original DocC span metadata and compare the native table before interpreting row/column relationships.'}
        for k,v in value.items(): yield from table_layouts(v,pointer+'/'+k)
    elif isinstance(value,list):
        for i,v in enumerate(value): yield from table_layouts(v,pointer+'/'+str(i))

def build_register(record):
    slug=record['slug']; raw_path=ROOT/record['json']['file']
    page=json.loads(raw_path.read_text(encoding='utf-8')); refs=page.get('references',{})
    blocks=[]; heading=[]; guidance=True
    def add(pointer,node,is_guidance=True):
        text=render(node,refs).strip()
        links=[]
        for relative,leaf in reference_nodes(node):
            identifier=leaf.get('identifier'); ref=refs.get(identifier,{})
            links.append({'pointer':pointer+relative,'identifier':identifier,'type':leaf['type'],
                          'metadata':leaf.get('metadata'), 'reference':ref})
        deprecated = sorted({r['identifier'] for r in links if r['reference'].get('deprecated')})
        if deprecated:
            text+='\n\nDeprecated API references: '+', '.join(refs[i].get('title',i) for i in deprecated)+'.'
        blocks.append({'id':slug+'#'+pointer,'pointer':pointer,'kind':node.get('type','abstract') if isinstance(node,dict) else 'abstract',
                       'headings':list(heading),'guidance':is_guidance,'text':text,'words':word_count(text),
                       'node_sha256':hashlib.sha256(json.dumps(node,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                       'references':links,'table_layouts':list(table_layouts(node,pointer)),'raw':node})
    add('/metadata/title', {'type':'heading','level':1,'text':page.get('metadata',{}).get('title',slug)})
    if page.get('abstract'): add('/abstract',page['abstract'])
    for si,section in enumerate(page.get('primaryContentSections',[])):
        for bi,node in enumerate(section.get('content',[])):
            if node.get('type')=='heading':
                level=node.get('level',2); heading=[h for h in heading if h['level']<level]
                heading.append({'level':level,'text':node.get('text','')})
                if node.get('text','').strip().lower() in ('resources','change log','change history'): guidance=False
            add(f'/primaryContentSections/{si}/content/{bi}',node,guidance and node.get('type')!='links')
    return {'slug':slug,'source_json_sha256':sha(raw_path),'source_native_sha256':sha(ROOT/record['markdown']['file']),
            'source_json':record['json']['file'],'source_native':record['markdown']['file'],
            'method':'Canonical original JSON blocks once; native export is a companion, never appended. Figures/captions and deprecated reference metadata included. Resource navigation and change history excluded from guidance.',
            'guidance_words':sum(b['words'] for b in blocks if b['guidance']), 'blocks':blocks}

def main():
    inventory=json.loads((SOURCE/'inventory.json').read_text(encoding='utf-8'))
    failures=[]; hashes=[]; counts=Counter(); registers=[]
    for row in inventory:
        for form in ('markdown','json'):
            entry=row.get(form,{})
            if entry.get('status')!=200: continue
            path=ROOT/entry['file']; actual=sha(path)
            if actual!=entry['sha256'] or path.stat().st_size!=entry['bytes']: failures.append(entry['file'])
            hashes.append({'file':entry['file'],'sha256':actual,'bytes':path.stat().st_size})
        if row.get('json',{}).get('status')!=200: continue
        register=build_register(row); registers.append(register)
        dump(WORK/'source-blocks'/f"{row['slug']}.json",register)
        text=['# Source block register: '+row['slug'], '', 'Read with the original native Markdown and JSON; this is not a distilled candidate.','']
        for block in register['blocks']:
            for layout in block['table_layouts']:
                text += ['> TABLE LAYOUT CAUTION: '+layout['warning'],
                         '> Original pointer: '+layout['pointer'],
                         '```json',json.dumps(layout['extendedData'],ensure_ascii=False,sort_keys=True),'```','']
            text += [f"<!-- {block['id']} | guidance={block['guidance']} -->", block['text'], '']
            for ref in block['references']:
                if ref['type'] in ('image','video'):
                    text += [f"<!-- Visual reference: {ref['identifier']}; inspect source metadata/visual when description is insufficient. -->"]
        path=WORK/'source-reading'/f"{row['slug']}.md";path.parent.mkdir(parents=True,exist_ok=True);path.write_text('\n'.join(text),encoding='utf-8')
        counts.update(b['kind'] for b in register['blocks'])
    pilot=json.loads((ROOT/'work/distillation-pilot-2026-09-12/evaluation/final-verification.json').read_text(encoding='utf-8'))
    pilot_checks=[]
    for r in pilot['files']:
        if r['path'].startswith('drafts/'):
            path=ROOT/'work/distillation-pilot-2026-09-12'/r['path'];match=sha(path)==r['sha256']
            pilot_checks.append({'file':str(path.relative_to(ROOT)),'sha256':sha(path),'matches':match})
            if not match: failures.append(str(path))
    summary={'snapshot':'2026-09-12','inventory_paths':len(inventory),'source_pages':len(registers),
             'verified_files':len(hashes),'failures':failures,'primary_block_kinds':dict(counts),
             'all_page_guidance_words_before_dispositions':sum(r['guidance_words'] for r in registers),
             'pilot_checks':pilot_checks,'source_files':hashes,
             'state':'Accounting candidate; independent disposition and method acceptance required'}
    dump(SOURCE/'verification/source-freeze.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in ('source_files','pilot_checks')},indent=2))
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
