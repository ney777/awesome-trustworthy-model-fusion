# Search and verification protocol

The 7 November 2026 snapshot uses a staged, purposive search with documented backward and targeted forward citation follow-up. It is not an exhaustive systematic review, a PRISMA screening exercise, or a complete citation-graph export. The current time window is 2018–2026. General federated background methods, including the previously included 2017 aggregation/security foundations, were removed by the scope correction.

## Scope and screening

Include a study when it directly concerns knowledge interaction among reusable models, capability-based selection, fusion/alignment, constraints on model composition, or changes to a collaboration state. Related foundations and infrastructure are labeled separately and require a direct relationship to fusion or the explicitly retained model-selection/collaboration scope. General federated optimization, gradient security, client fairness or partial-model scheduling is not sufficient for inclusion. Exclude generic single-model learning, generic RAG, ordinary task-delegating agents, and trustworthiness papers without a specific connection to model combination. A method name containing “fusion,” “dynamic,” or “privacy” does not establish relevance or a guarantee.

Each study receives one primary category and multiple secondary tags. Final and preprint versions count once. Normalized titles, DOI identifiers, official URLs, author lists, and version notes are used to reconcile duplicates. Catalogue entries require verified bibliographic identity. Candidates with unresolved identities stay in local working notes until verified. A missing CCF grade does not prevent inclusion of a verified, in-scope paper.

## Discovery and citation follow-up

Primary metadata sources include PMLR, NeurIPS and ICLR proceedings/OpenReview, ACL Anthology, CVF, IJCAI, AAAI, publisher pages, and publisher-deposited Crossref records. DBLP and author/institutional pages provide bibliographic cross-checks or legitimate author versions. Search-engine results are discovery leads, not sufficient technical evidence. No institutional access restriction was bypassed.

Executed queries and bounded citation chains are in the [representation/evolution log](search-log-representation-evolution.md) and [governance log](search-log-governance.md). They include exact-title checks and combinations such as:

| Dimension | Actual query examples | Follow-up examples |
|---|---|---|
| Representation | `site:proceedings.mlr.press LEEP LogME transferability`; `"Model Spider" "Learning"`; `"Learnware" "2024" "reuse" primary paper` | LEEP → task embeddings; PLeaS → alignment predecessors; RegMean → RegMean++; learnware specifications → ELSI and label-space assembly |
| Governance | `model merging fairness 2025 2026`; `model merging privacy differential`; `model merging provenance attribution watermark`; `ShapleyFL`; `Cascade Routing` | RouteMark references → MergePrint and MergeGuard; FedXDS → FedAUX; newer watermark study → earlier durability problem |
| Evolution | `"continual model merging" "2026" site:proceedings.iclr.cc`; `"GraphRouter" LLM routing ICLR2025`; named OPCM, DOP and TIME follow-ups | OPCM/DOP → NUFILT and ODE-M; Surgery → ProbSurgery; RouteLLM/GraphRouter → MetaRouter |
| Cross-cutting surveys | DOI/title/ACL record checks; recent model-merging, MoErging, FUSE, small/large-model and edge/cloud survey searches | Survey references and named mechanisms provide candidates, followed by separate primary-source checks |

The query logs report the actual discovery branches rather than pretending every Boolean combination was executed across every database. Forward expansion used later papers and named-method searches; complete cited-by graph coverage and saturation were not established. No numerical count of all search hits or excluded hits is claimed because a comprehensive screening ledger was not maintained.

The [earlier coverage audit](coverage-audit.md) records the discovery history. The [federated crosswalk](federated-coverage-audit.md) preserves 41 source occurrences mapping to 39 unique studies; current screening retains 31 and excludes eight. Across the whole former corpus, the [scope correction](scope-correction.md) removes 17 entries. These decisions supersede the earlier all-inclusion pass. The executed queries above are historical discovery branches; encountering a title does not imply retaining it.

## Evidence extraction

For each record, store complete authors, final venue/year where resolved, identifiers, source URLs, primary question, technical mechanism, inputs, assumptions, contribution, limitations, reading depth, and precise section/page locators. The four reading-depth labels are metadata-only, abstract-reviewed, section-reviewed, and full-text-reviewed. Selected-section reading is not full-paper review or experimental reproduction.

Technical claims prefer primary methods. A publisher abstract supports only claims visible there. When a final paper cannot be retrieved, retain the author-version identity and do not infer final-version omissions. Code links need paper/author provenance; an HTTP success means availability, not execution or reproducibility. Automated page-title checks are supplementary because some official pages use scripts or access challenges.

## Version and CCF rules

Final issue year and online year are stored separately when they differ. Conference year is not replaced by a later website upload date. Official acceptance is distinguished from completed proceedings publication. Findings, companion workshops, Industry, and Applied Data Science tracks are checked explicitly. Where a grade cannot be established, tables display `—` (no grade listed); this does not mean a confirmed unranked result and does not inherit the main-conference grade.

Venue ranks use the [CCF seventh-edition release](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml) and a [formal directory copy preserved by a university research office](https://kyc.lsu.edu.cn/2026/0518/c1772a367789/page.htm). The [venue register](../data/venues_ccf2026.json) contains directory page/row evidence and the source limitation: the official PDF endpoint required access verification, so byte equality with that endpoint was not established. The university-hosted document is the CCF directory, not a third-party rank table.

## Reproducible maintenance

Edit only [data/papers.json](../data/papers.json), then validate, deduplicate, and regenerate the views. The [reference audit](reference-audit.md) records current exceptions; the [literature report](literature-report.md) gives counts. Search coverage and source reading still require human or agent judgment. Passing a schema or URL check cannot establish that every scientific statement is correct.
