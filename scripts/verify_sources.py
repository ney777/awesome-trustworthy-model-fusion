"""Optional online source audit. Never upgrades verification_status automatically."""
import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from library import ROOT, records, normalize_title, normalize_doi

def audit(p):
    result={'id':p['id'],'url':p['official_url']}
    try:
        req=urllib.request.Request(p['official_url'],headers={'User-Agent':'TrustworthyFusionBibliography/0.1 (source verification)'})
        with urllib.request.urlopen(req,timeout=25) as r:
            body=r.read(300000).decode('utf-8',errors='replace')
            result.update(http_status=r.status,resolved_url=r.url)
        result['title_seen_on_page']=normalize_title(p['title']) in normalize_title(body)
    except Exception as e:result['official_page_error']=str(e)
    if p.get('doi'):
        try:
            u='https://api.crossref.org/works/'+urllib.parse.quote(normalize_doi(p['doi']),safe='')
            with urllib.request.urlopen(u,timeout=25) as r:meta=json.load(r)['message']
            title=meta.get('title',[''])[0]
            result['crossref_title']=title
            result['crossref_title_matches']=normalize_title(title)==normalize_title(p['title'])
            result['crossref_author_count']=len(meta.get('author',[]))
            result['recorded_author_count']=len(p['authors'])
            result['crossref_years']={k:v.get('date-parts') for k,v in meta.items() if k in ['published','published-online','published-print']}
        except Exception as e:result['crossref_error']=str(e)
    result['interpretation']='Availability and identity signals only; manual source reading remains required.'
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--online',action='store_true');ap.add_argument('--id',action='append');ap.add_argument('--output',type=Path,default=ROOT/'work/source-audit.json');a=ap.parse_args()
    if not a.online:raise SystemExit('Use --online to run public network checks; local structure: validate_papers.py')
    rows=[p for p in records() if not a.id or p['id'] in a.id]
    out=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(audit,rows):
            out.append(result);print(result['id'], 'audited',flush=True)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
