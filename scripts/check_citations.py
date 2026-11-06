"""Check local LaTeX citation keys and BibTeX identity consistency."""
import argparse
import re
import sys
from pathlib import Path
from library import ROOT

def check(folder):
    bib=folder/'references.bib'
    if not bib.exists():return ['Missing '+str(bib)]
    keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib.read_text())
    errors=[]
    if len(keys)!=len(set(keys)):errors.append('Duplicate BibTeX keys')
    cited=set()
    for path in folder.rglob('*.tex'):
        text=re.sub(r'(?<!\\)%[^\n]*','',path.read_text())
        for group in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
            cited.update(k.strip() for k in group.split(','))
    errors += ['Undefined citation: '+k for k in sorted(cited-set(keys))]
    return errors

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--survey',type=Path,default=ROOT/'survey');a=ap.parse_args()
    errors=check(a.survey);print('\n'.join(errors) if errors else 'All LaTeX citation keys resolve.')
    sys.exit(bool(errors))
