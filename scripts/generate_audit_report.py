"""Generate a reader-facing overview of the public collection."""
from collections import Counter
from library import ROOT, load, catalogue_rows, ccf_label


def main():
    data = load()
    rows = catalogue_rows(data['papers'])

    def table(values):
        return '\n'.join(f'| {key} | {count} |' for key, count in sorted(Counter(values).items()))

    text = f'''# Collection overview

Updated: {data['curation_date']}. This collection contains **{len(rows)} papers, surveys and tools** on model fusion. The [main catalogue](../README.md) organizes them by representation, trustworthy governance and collaborative evolution. The [federated literature table](federated-literature.md) highlights **{sum(bool(p.get('federated_view_group')) for p in rows)} records** with an explicit fusion focus in federated or distributed settings.

## Coverage

| Primary category | Records |
| --- | ---: |
{table(p['primary_category'] for p in rows)}

Each work has one primary category; secondary tags do not add records. Foundations, tools and surveys are distinguished in the record fields. The collection includes {sum(2024 <= p['year'] <= 2026 for p in rows)} records dated 2024–2026. Online/issue years, preprints and accepted papers are identified in the individual records.

| Publication type | Records |
| --- | ---: |
{table(p['publication_type'] for p in rows)}

## How to read the records

The [detailed records](papers.md) describe the problem, fusion mechanism, assumptions, contribution and evidence boundaries. Publication identity, reading depth and experimental reproduction are separate dimensions.

| Reading depth | Records |
| --- | ---: |
{table(p['review_depth'] for p in rows)}

Selected-section review does not mean the whole paper, proof or appendix was assessed. No experiments were independently reproduced for this catalogue. Code availability does not establish implementation correctness.

## Venue grades

| CCF 2026 label | Records |
| --- | ---: |
{table(ccf_label(p) for p in rows)}

Grades follow the seventh-edition directory, with sources in the [venue register](../data/venues_ccf2026.json). **—** means no grade is displayed; **None** denotes a venue or publication type outside the ranked directory. Special tracks do not automatically inherit a parent-conference grade. A venue grade does not determine inclusion or establish scientific quality.

## Explore the literature

- [Scope and definitions](scope-and-definitions.md): the fusion operations covered and boundaries with adjacent topics.
- [Related surveys](prior-surveys.md): {sum(p['record_type'] == 'survey' for p in rows)} surveys and their complementary perspectives.
- [Model conditions](model-conditions.md): selected source, target and auxiliary model configurations.
- [Benchmarks and tools](benchmarks.md): evaluation resources and their limits.
- [Search protocol](search-protocol.md): source selection and literature coverage.

This is a curated collection, not an exhaustive census. General federated learning methods are excluded unless they directly study model fusion. Corrections and relevant additions are welcome through the [contribution guide](../CONTRIBUTING.md).
'''
    (ROOT / 'docs/literature-report.md').write_text(text, encoding='utf-8')
    print('Generated collection overview from', len(rows), 'records.')


if __name__ == '__main__':
    main()
