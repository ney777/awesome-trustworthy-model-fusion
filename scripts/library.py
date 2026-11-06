"""Shared, dependency-free bibliography utilities (Python 3.9+)."""
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'data/papers.json'
REQUIRED = ['id', 'title', 'authors', 'venue_full_name', 'venue_abbreviation', 'year',
            'publication_type', 'ccf_rank', 'ccf_verification_source', 'doi',
            'official_url', 'pdf_url', 'code_url', 'primary_category', 'secondary_tags',
            'research_problem', 'key_idea', 'technical_mechanism', 'assumptions',
            'main_contribution', 'limitations', 'evidence_source',
            'verification_status', 'bibtex_key', 'record_type', 'review_depth']
CATEGORIES = {'representation': 'I. Fusion Representation',
              'governance': 'II. Trustworthy Fusion Governance',
              'evolution': 'III. Collaborative Evolution',
              'surveys': 'IV. Related Surveys',
              'benchmarks': 'V. Benchmarks, Datasets and Tools'}

def load():
    return json.loads(SOURCE.read_text(encoding='utf-8'))

def records():
    return load()['papers']

def digest():
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()

def normalize_title(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    return ''.join(c for c in s if c.isalnum())

def normalize_doi(s):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', (s or '').strip(), flags=re.I).lower().rstrip('/')

def formal(p):
    return p.get('verification_status') == 'verified' and p.get('ccf_verification_status') == 'verified'

def write_csv(path, rows):
    fields = list(dict.fromkeys(REQUIRED + sorted({k for p in rows for k in p})))
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in p.items()})

def tex_escape(value):
    s=str(value).replace('\\', r'\textbackslash{}').replace('&', r'\&').replace('%', r'\%').replace('_', r'\_').replace('#', r'\#')
    for old,new in [('–','--'),('—','---'),('’',"'"),('‘',"'"),('“','``'),('”',"''"),('‑','-')]:
        s=s.replace(old,new)
    accents={'\u0300':'`','\u0301':"'",'\u0302':'^','\u0303':'~','\u0308':'"','\u030a':'r','\u0327':'c','\u030c':'v','\u0304':'='}
    out=[]
    for ch in s:
        decomp=unicodedata.normalize('NFD',ch)
        if len(decomp)==2 and decomp[1] in accents:
            out.append('\\'+accents[decomp[1]]+'{'+decomp[0]+'}')
        else:out.append(ch)
    return ''.join(out)
