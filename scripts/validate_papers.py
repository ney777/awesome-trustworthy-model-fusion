"""Validate local evidence records; structural validity is not a truth guarantee."""
import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from library import ROOT, REQUIRED, CATEGORIES, load, formal
from check_duplicates import check

def validate(rows):
    errors = check(rows)
    for p in rows:
        pid = p.get('id', '<missing-id>')
        for field in REQUIRED:
            if field not in p:
                errors.append(f'{pid}: missing {field}')
        if not isinstance(p.get('authors'), list) or not p.get('authors') or any('et al' in a.lower() for a in p.get('authors', [])):
            errors.append(f'{pid}: complete author list required')
        if not isinstance(p.get('year'), int) or not 1900 <= p['year'] <= date.today().year:
            errors.append(f'{pid}: invalid year')
        if p.get('primary_category') not in CATEGORIES:
            errors.append(f'{pid}: invalid primary category')
        if p.get('ccf_rank') not in [None, 'A', 'B', 'C', 'None']:
            errors.append(f'{pid}: invalid CCF rank')
        if p.get('ccf_verification_status') == 'verified':
            if p.get('ccf_rank') is None or not p.get('ccf_verification_source'):
                errors.append(f'{pid}: verified CCF requires rank and source')
            if p.get('ccf_edition') != 'CCF 2026, 7th edition':
                errors.append(f'{pid}: wrong or missing CCF edition')
        elif p.get('ccf_rank') is not None:
            errors.append(f'{pid}: unverified CCF must be null, never None/A/B/C')
        if p.get('publication_type') == 'preprint' and p.get('ccf_rank') not in [None, 'None']:
            errors.append(f'{pid}: preprint cannot inherit venue rank')
        if p.get('publication_track') in ['findings','workshop','short','demo'] and p.get('ccf_rank') not in [None,'None']:
            errors.append(f'{pid}: excluded publication track cannot inherit venue rank')
        if p.get('verification_status') == 'verified':
            for field in ['title','venue_full_name','venue_abbreviation','official_url','research_problem','main_contribution','evidence_source']:
                if not p.get(field):
                    errors.append(f'{pid}: verified record lacks {field}')
        for field in ['official_url','pdf_url','code_url']:
            if p.get(field) and urlparse(p[field]).scheme not in ['http','https']:
                errors.append(f'{pid}: invalid {field}')
        if p.get('code_url') and not p.get('code_verification_source'):
            errors.append(f'{pid}: code URL needs provenance')
        if p.get('review_depth') not in ['metadata-only','abstract-reviewed','full-text-reviewed','section-reviewed']:
            errors.append(f'{pid}: invalid review depth')
        if p.get('review_depth') in ['full-text-reviewed','section-reviewed'] and not p.get('full_text_locators'):
            errors.append(f'{pid}: full-text/section review requires source locators')
    return errors

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--report', type=Path)
    ap.add_argument('--require-all-verified', action='store_true')
    args = ap.parse_args()
    rows = load()['papers']
    errors = validate(rows)
    if args.require_all_verified and not all(formal(p) for p in rows):
        errors.append('Some records are not ready for the formal ranked catalogue.')
    report = {'structural_validation_passed':not errors,'record_count':len(rows),
              'formal_catalogue_count':sum(formal(p) for p in rows),
              'ccf_counts':dict(Counter(p.get('ccf_rank') or 'unverified' for p in rows)),
              'category_counts':dict(Counter(p.get('primary_category') for p in rows)),
              'review_depth_counts':dict(Counter(p.get('review_depth') for p in rows)),
              'errors':errors, 'limit':'This check validates recorded structure and consistency, not external truth or exhaustive coverage.'}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    sys.exit(bool(errors))
