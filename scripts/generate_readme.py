"""Generate catalogue, detailed notes, CSV, and survey view from one source."""
import json
from library import ROOT, CATEGORIES, load, catalogue_rows, ccf_label, write_csv, digest

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

def federated_catalogue(rows):
    selected = [p for p in catalogue_rows(rows) if p.get('federated_view_group')]
    lines = ['# Model fusion in federated and distributed settings', '',
             f"This focused view contains {len(selected)} records with an explicit model-fusion contribution. Each row identifies the models, modules or knowledge being combined and the fusion operation. General federated optimization, client scheduling, gradient defense and protocol security are excluded unless the work directly studies model fusion. Distributed merging foundations are labeled separately; inclusion does not establish privacy, fairness or institutional deployment.", '',
             '[Detailed records](papers.md) describe assumptions, limitations and source locators. [Model conditions](model-conditions.md) compare selected source, target and auxiliary model configurations. In the CCF column, — means no grade is displayed; None denotes a venue or publication type outside the ranked directory.', '']
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
            rank = ccf_label(p)
            status = publication_status(p) + '; ' + p['review_depth']
            lines.append(table_row([p['year'], p['title'], p['venue_abbreviation'] + ' / ' + str(rank),
                                    p['fusion_relevance'], status, paper_links(p)]))
        lines += ['']
    return '\n'.join(lines)

def main():
    from generate_model_conditions import generate
    data=load(); rows=catalogue_rows(data['papers'])
    lines=['# Awesome Trustworthy Model Fusion and Collaboration','',
           'A curated research collection on how existing models are represented, governed under explicit trust constraints, and updated through collaboration.','',
           '**Representation → Governance → Evolution**','',
           '[Scope](docs/scope-and-definitions.md) · [Taxonomy](docs/taxonomy.md) · [Federated literature](docs/federated-literature.md) · [Model conditions](docs/model-conditions.md) · [Detailed records](docs/papers.md) · [Related surveys](docs/prior-surveys.md) · [Benchmarks](docs/benchmarks.md) · [Collection overview](docs/literature-report.md) · [Contributing](CONTRIBUTING.md) · [中文](README.zh-CN.md)','',
           '## About this collection','',
           f"Updated: {data.get('curation_date','not recorded')}. Browse {len(rows)} papers, surveys and tools in the topic tables below. The [federated literature table](docs/federated-literature.md) highlights fusion methods in federated and distributed settings.",'',
           'Methods must directly concern model fusion; general federated learning methods are outside this catalogue. This is a curated collection, not an exhaustive census. Detailed records explain the fusion mechanism, assumptions and evidence boundaries.','',
           'Venue grades follow the **CCF 2026 seventh edition**. Findings, workshops and other excluded tracks do not inherit the main-conference grade. **—** means no grade is displayed; **None** denotes a venue or publication type outside the ranked directory. Grades do not determine inclusion or scientific quality. Preprints and accepted papers are labeled separately from published papers.','']
    for cat, heading in CATEGORIES.items():
        lines += ['## '+heading,'']
        group=sorted([p for p in rows if p['primary_category']==cat],key=lambda p:(-p['year'],p['title'].casefold()))
        if not group:lines += ['No entries listed in this section.','']
        subs=list(dict.fromkeys(p.get('subcategory','General') for p in group))
        for sub in subs:
            lines += ['### '+sub,'',
                      '| Year | Paper | Venue | CCF 2026 | Status | Links |',
                      '| --- | --- | --- | :---: | --- | --- |']
            for p in [p for p in group if p.get('subcategory','General')==sub]:
                lines += [table_row([p['year'], f"**{p['title']}**", p['venue_abbreviation'],
                                     ccf_label(p), publication_status(p), paper_links(p)])]
            lines += ['']
    lines += ['## Data and contributions','',
              'Download the [CSV](data/papers.csv), [BibTeX](data/references.bib) or [JSON](data/papers.json). [Detailed records](docs/papers.md) include source links, reading depth, assumptions and limitations. The [search protocol](docs/search-protocol.md) describes how literature is selected.','',
              'See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion and verification rules. Original repository materials are released under the [MIT license](LICENSE); linked publications and third-party tools retain their respective rights.','',
              '<!-- source-sha256: '+digest()+' -->','']
    (ROOT/'README.md').write_text('\n'.join(lines),encoding='utf-8')
    notes=['# Literature records','', 'Explore each work through its problem, fusion mechanism, assumptions and evidence boundaries. Reading depth describes the sources assessed for each entry; inclusion is not a universal trustworthiness endorsement. In the CCF column, — means no grade is displayed; None denotes a venue or publication type outside the ranked directory.','']
    for p in sorted(rows,key=lambda p:(p['primary_category'],-p['year'],p['title'])):
        notes += ['## '+p['title'],'', '| Field | Details |', '| --- | --- |',
                  table_row(['Venue / year', f"{p['venue_full_name']}, {p['year']}"]),
                  table_row(['Publication status', publication_status(p)]),
                  table_row(['CCF 2026', ccf_label(p)]),
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
    print(f'Generated {len(rows)} catalogue entries and detailed records.')

if __name__=='__main__':main()
