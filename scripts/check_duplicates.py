"""Reject duplicate IDs, normalized titles, DOI identities, and official URLs."""
import sys
from library import records, normalize_doi, normalize_title

def check(rows):
    errors = []
    for field in ['id', 'bibtex_key', 'title', 'doi', 'official_url']:
        seen = {}
        for p in rows:
            v = p.get(field)
            if not v:
                continue
            key = normalize_title(v) if field == 'title' else normalize_doi(v) if field == 'doi' else v.rstrip('/')
            if key in seen:
                errors.append(f"Duplicate {field}: {seen[key]} / {p['id']}")
            seen[key] = p['id']
    return errors

if __name__ == '__main__':
    errors = check(records())
    print('\n'.join(errors) if errors else 'No duplicate identities found.')
    sys.exit(bool(errors))
