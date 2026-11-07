"""Generate catalogue, detailed notes, CSV, and survey view from one source."""
import json
from library import ROOT, CATEGORIES, load, formal, write_csv, digest

def table_cell(value):
    """Keep text and inline links inside one GitHub Markdown table cell."""
    return str(value).replace('|', r'\|').replace('\r\n', '\n').replace('\n', '<br>')

def table_row(values):
    return '| ' + ' | '.join(table_cell(value) for value in values) + ' |'

def publication_status(p):
    if p['publication_type'] == 'preprint':
        return 'Preprint'
    if p.get('publication_status') == 'accepted':
        return 'Accepted; proceedings pending'
    if p['publication_type'] == 'workshop' or p.get('publication_track') == 'workshop':
        return 'Workshop'
    if p.get('publication_status') == 'early-access-metadata-conflict':
        return 'Early access; metadata conflict'
    tracks = {'findings': 'Findings', 'industry': 'Industry track',
              'applied-data-science': 'Applied Data Science track'}
    return tracks.get(p.get('publication_track'), 'Published')

def paper_links(p):
    links = [f"[Paper]({p['official_url']})"]
    if p.get('code_url'):
        links.append(f"[Code]({p['code_url']})")
    return ' · '.join(links)

def pending_catalogue(rows):
    """Keep unresolved identities or ranks visible without promoting their status."""
    pending = sorted((p for p in rows if not formal(p)),
                     key=lambda p: (-p['year'], p['title'].casefold()))
    if not pending:
        return []
    lines = ['## Pending verification', '',
             'These records remain visible while the stated checks are unresolved. Reading depth alone does not make bibliographic metadata pending.', '',
             '| Year | Paper | Venue | CCF 2026 | Unresolved check | Links |',
             '| --- | --- | --- | :---: | --- | --- |']
    for p in pending:
        checks = []
        if p.get('verification_status') != 'verified':
            checks.append('Bibliographic identity: ' + p.get('verification_status', 'pending'))
        if p.get('ccf_verification_status') != 'verified':
            checks.append('CCF venue/track applicability')
        rank = p.get('ccf_rank') if p.get('ccf_verification_status') == 'verified' else 'Pending'
        lines.append(table_row([p['year'], f"**{p['title']}**", p['venue_abbreviation'],
                                rank if rank is not None else 'Pending', '; '.join(checks), paper_links(p)]))
    return lines + ['']

def federated_catalogue(rows):
    selected = [p for p in rows if p.get('federated_view_group')]
    lines = ['# Model fusion in federated and distributed settings', '',
             f"This focused view contains {len(selected)} records with an explicit model-fusion contribution. Each row identifies the models, modules or knowledge being combined and the fusion operation. General federated optimization, client scheduling, gradient defense and protocol security are excluded unless the work directly studies model fusion. Distributed merging foundations are labeled separately; inclusion does not establish privacy, fairness or institutional deployment.", '',
             'See the [federated coverage audit](federated-coverage-audit.md) for the reference-list crosswalk, version reconciliation and disposition of the previous screening queue. [Detailed records](papers.md) retain assumptions, limitations and source locators. The [model-condition update](model-conditions-audit.md) records the latest bounded additions and exclusions.', '']
    group_order = ['Fusion weights and component combinations', 'Alignment and knowledge transfer',
                   'One-shot and decentralized fusion', 'Personalization and multi-federation collaboration',
                   'Privacy, fairness, robustness and attribution', 'Related foundations and model reuse',
                   'Related federated surveys']
    for group in group_order + [g for g in dict.fromkeys(p['federated_view_group'] for p in selected) if g not in group_order]:
        if not any(p['federated_view_group'] == group for p in selected):
            continue
        lines += ['## ' + group, '',
                  '| Year | Paper | Venue / CCF 2026 | Fusion object and operation | Publication / reading | Links |',
                  '| --- | --- | --- | --- | --- | --- |']
        for p in sorted((p for p in selected if p['federated_view_group'] == group),
                        key=lambda p: (-p['year'], p['title'].casefold())):
            rank = p['ccf_rank'] if p.get('ccf_verification_status') == 'verified' else 'Pending'
            status = publication_status(p) + '; ' + p['review_depth']
            if p['verification_status'] != 'verified':
                status += '; bibliography ' + p['verification_status']
            lines.append(table_row([p['year'], p['title'], p['venue_abbreviation'] + ' / ' + str(rank),
                                    p['fusion_relevance'], status, paper_links(p)]))
        lines += ['']
    return '\n'.join(lines)

def main():
    from generate_model_conditions import generate
    data=load(); rows=data['papers']; ready=[p for p in rows if formal(p)]
    lines=['# Awesome Trustworthy Model Fusion and Collaboration','',
           'A curated research collection on how existing models are represented, governed under explicit trust constraints, and updated through collaboration.','',
           '**Representation → Governance → Evolution**','',
           '[Scope](docs/scope-and-definitions.md) · [Taxonomy](docs/taxonomy.md) · [Federated literature](docs/federated-literature.md) · [Model conditions](docs/model-conditions.md) · [Detailed records](docs/papers.md) · [Related surveys](docs/prior-surveys.md) · [Benchmarks](docs/benchmarks.md) · [Search protocol](docs/search-protocol.md) · [Coverage audit](docs/coverage-audit.md) · [Model-condition audit](docs/model-conditions-audit.md) · [Audit](docs/reference-audit.md) · [Report](docs/literature-report.md) · [Contributing](CONTRIBUTING.md)','',
           '## Collection status','',
           f"Curation snapshot: {data.get('curation_date','not recorded')}. The database contains {len(rows)} records; {len(ready)} satisfy both metadata and CCF-edition verification for the ranked catalogue. Remaining records are retained as pending, not classified as CCF-None by default.",'',
           'This is a staged, evidence-tracked collection, not a claim of exhaustive coverage. Federated learning alone is not an inclusion criterion: methods must directly concern model fusion; general FL methods are excluded from the method catalogue. See the [scope correction](docs/scope-correction.md). Venue ranks use the **CCF 2026 seventh edition** only. Findings, workshop and other excluded tracks do not inherit the main-conference rank. Publication status and review depth are separate fields.','',
           'The unpublished survey manuscript is maintained locally and is not distributed in this repository.','']
    for cat, heading in CATEGORIES.items():
        lines += ['## '+heading,'']
        group=sorted([p for p in ready if p['primary_category']==cat],key=lambda p:(-p['year'],p['title'].casefold()))
        if not group:lines += ['No entries have completed all required checks for this section yet.','']
        subs=list(dict.fromkeys(p.get('subcategory','General') for p in group))
        for sub in subs:
            lines += ['### '+sub,'',
                      '| Year | Paper | Venue | CCF 2026 | Status | Links |',
                      '| --- | --- | --- | :---: | --- | --- |']
            for p in [p for p in group if p.get('subcategory','General')==sub]:
                lines += [table_row([p['year'], f"**{p['title']}**", p['venue_abbreviation'],
                                     p['ccf_rank'], publication_status(p), paper_links(p)])]
            lines += ['']
    lines += pending_catalogue(rows)
    lines += ['## Verification and maintenance','',
              'Bibliographic facts, review depth, source locators, assumptions and boundaries are stored in [data/papers.json](data/papers.json). The [CSV](data/papers.csv), [BibTeX](data/references.bib), README and detailed notes are generated views. Edit the JSON source, not the generated outputs.','',
              '```sh','python scripts/validate_papers.py','python scripts/check_duplicates.py','python scripts/generate_readme.py','python scripts/export_bibtex.py','```','',
              'See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion and verification rules. Original repository materials are released under the [MIT license](LICENSE); linked publications and third-party tools retain their respective rights.','',
              '<!-- source-sha256: '+digest()+' -->','']
    (ROOT/'README.md').write_text('\n'.join(lines),encoding='utf-8')
    notes=['# Literature records','', 'Generated from `data/papers.json`. Pending ranks and incomplete reading are explicit; inclusion here is not a universal trustworthiness endorsement.','']
    for p in sorted(rows,key=lambda p:(p['primary_category'],-p['year'],p['title'])):
        notes += ['## '+p['title'],'', '| Field | Details |', '| --- | --- |',
                  table_row(['Venue / year', f"{p['venue_full_name']}, {p['year']}"]),
                  table_row(['Publication status', publication_status(p)]),
                  table_row(['Bibliographic verification', p['verification_status']]),
                  table_row(['CCF 2026', p['ccf_rank'] if p.get('ccf_rank') is not None else 'Pending verification']),
                  table_row(['Reading depth', p['review_depth']]),
                  table_row(['Links', paper_links(p)])]
        for k,label in [('research_problem','Problem'),('technical_mechanism','Mechanism'),('main_contribution','Contribution'),('assumptions','Assumptions'),('limitations','Evidence boundary')]:
            v=p.get(k)
            if isinstance(v,list):v='; '.join(v)
            notes += [table_row([label, v or 'Not yet assessed.'])]
        evidence='; '.join(f"[{e.get('locator','source')}]({e['url']})" if isinstance(e,dict) else str(e) for e in p['evidence_source'])
        notes += [table_row(['Evidence', evidence]), '']
    (ROOT/'docs/papers.md').write_text('\n'.join(notes),encoding='utf-8')
    (ROOT/'docs/federated-literature.md').write_text(federated_catalogue(rows),encoding='utf-8')
    write_csv(ROOT/'data/papers.csv',rows)
    (ROOT/'data/surveys.json').write_text(json.dumps({'generated_from':'papers.json','papers':[p for p in rows if p['record_type']=='survey']},ensure_ascii=False,indent=2)+'\n')
    generate()
    print(f'Generated {len(ready)} ranked entries and {len(rows)} detailed records.')

if __name__=='__main__':main()
