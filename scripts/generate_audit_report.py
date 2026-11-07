"""Generate corpus counts from the master; exclude local manuscript from public output."""
from collections import Counter
from library import ROOT, load, formal

def main():
    d=load();rs=d['papers'];ready=[r for r in rs if formal(r)]
    verified=[r for r in rs if r['verification_status']=='verified']
    def tab(field, rows):
        c=Counter(str(r.get(field) if r.get(field) is not None else 'pending') for r in rows)
        return '\n'.join(f'| {k} | {v} |' for k,v in sorted(c.items()))
    text=f'''# Literature discovery report

Snapshot: {d['curation_date']}. The master contains **{len(rs)} distinct records**, including **{len(verified)} with reconciled bibliographic metadata** and **{len(ready)} eligible for the ranked README catalogue**. These counts describe verified records, not all search hits. Verification of identity, CCF applicability, reading depth and experimental reproduction are separate dimensions.

## Coverage

| Primary category | Records |
|---|---:|
{tab('primary_category',rs)}

Related foundations, tools and surveys are included in these counts and are distinguished in the record fields. Each study has one primary category; secondary tags do not add papers. The database includes {sum(2024<=r['year']<=2026 for r in rs)} records dated 2024–2026, with exact online/issue and accepted/preprint distinctions retained where needed.

| Reading depth | Records |
|---|---:|
{tab('review_depth',rs)}

Selected-section review does not mean the whole paper, proof or appendix was assessed. No experiments were independently reproduced. Code provenance and availability do not establish implementation correctness.

## CCF 2026 distribution

The following distribution covers all records, including bibliography candidates. Pending is an internal unresolved state and is not a fifth CCF grade.

| Recorded rank | All records |
|---|---:|
{tab('ccf_rank',rs)}

| Recorded rank | Ranked catalogue only |
|---|---:|
{tab('ccf_rank',ready)}

The [venue register](../data/venues_ccf2026.json) gives seventh-edition directory evidence. A venue grade is not a scientific quality score. Unresolved special-track or full/regular-paper applicability remains pending rather than inheriting a parent-conference grade.

## Synthesis and positioning

The retained title is **Trustworthy Model Fusion and Collaboration: A Survey of Representation, Governance, and Evolution**. Persistent source-model collaboration is materially different from source-independent fused inference; keeping both terms supports the verified scope. Federated protocols remain a priority setting, while a federated-only title would exclude relevant checkpoint reuse and routing work.

The comparative contribution is an explicit link between capability/compatibility evidence, the decisions permitted by access and trust conditions, and the evidence that may need reassessment after change. Existing surveys already discuss safety, provenance, continual fusion and feedback; no first-framework claim is supported. The event-indexed evaluation is proposed and unimplemented.

All six supplied survey seeds and six recent extensions are compared in [prior-surveys.md](prior-surveys.md). The nearest overlaps include From Parameters to Behaviors, MoErging, the CSUR model-merging survey, FUSE, and the unresolved Knowledge Transmission and Fusion preview. The last record is not counted as fully reconciled metadata.

The [federated table](federated-literature.md) groups {sum(bool(r.get('federated_view_group')) for r in rs)} records by protocol setting and access conditions. The [federated audit](federated-coverage-audit.md) records a bounded reference-list crosswalk and completed candidate screening.

## Recheck and continuation

See the [executed search protocol](search-protocol.md), [source-level records](papers.md), [research questions](research-gaps.md), [outline](survey-outline.md) and [reference audit](reference-audit.md). Priority improvements are final-version access for several surveys, reconciliation of the Information Fusion author/year record, explicit CCF track applicability, and stronger cross-operator evidence on withdrawal and long-term recovery. The collection is purposive, not exhaustive.
'''
    (ROOT/'docs/literature-report.md').write_text(text)
    print('Generated literature report from',len(rs),'records.')
if __name__=='__main__':main()
