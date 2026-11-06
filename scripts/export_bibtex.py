"""Export verified bibliographic metadata without inventing DOI or page fields."""
import argparse
from pathlib import Path
from library import ROOT, records, tex_escape

def render(rows):
    entries=[]
    for p in rows:
        if p['verification_status'] != 'verified':
            continue
        kind = {'journal':'article','conference':'inproceedings','workshop':'inproceedings','preprint':'misc'}.get(p['publication_type'],'misc')
        fields={'title':'{'+tex_escape(p['title'])+'}', 'author':' and '.join(tex_escape(a) for a in p['authors']), 'year':p['year'], 'url':p['official_url']}
        if kind=='article': fields['journal']=tex_escape(p['venue_full_name'])
        elif kind=='inproceedings': fields['booktitle']=tex_escape(p['venue_full_name'])
        else: fields['note']='Preprint' if p['publication_type']=='preprint' else tex_escape(p['venue_full_name'])
        if p.get('publication_status')=='accepted': fields['note']='Accepted; final proceedings not yet retrieved'
        for k in ['doi','volume','number','pages']:
            if p.get(k): fields[k]=p[k] if k=='doi' else tex_escape(p[k])
        entries.append('@'+kind+'{'+p['bibtex_key']+',\n'+',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in fields.items())+'\n}')
    return '% Generated from verified official metadata in data/papers.json.\n\n'+'\n\n'.join(entries)+'\n'

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=ROOT/'data/references.bib'); args=ap.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(render(records()),encoding='utf-8')
    print('Wrote',args.output)
