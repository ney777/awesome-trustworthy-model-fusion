# Prior surveys and positioning

Existing surveys already connect model compatibility, safety, adaptive routing and continuing reuse. A new survey cannot establish its contribution merely by combining these words or claiming that earlier work lacks a unified framework. The strongest confirmed scope distinction is between fusion that produces an inference-independent target and collaboration that continues to invoke multiple models; the proposed survey can compare both, then investigate whether a common account of acceptance conditions and revalidation adds useful analysis.

The original Phase 1–2 assessment below covers 12 distinct surveys: the six requested seeds and six recent extensions. It is a purposive comparison with one-step backward citation expansion, not an exhaustive systematic review. Nine PDFs were inspected in selected definition, taxonomy, evaluation, governance, evolution and limitation sections. Two records use publisher HTML excerpts, and one uses only the publisher abstract. The [structured bibliography](../data/papers.json) records titles, authors, publication status and evidence sources. The venue-ranking audit is separate from this scientific comparison.

The later [One-shot Federated Learning Methods: A Practical Guide](https://www.ijcai.org/proceedings/2025/1174) adds a thirteenth survey record. Selected taxonomy passages separate prediction-, model-, and data-transfer arrangements, but its categories mix operators, auxiliary-model roles and communication constraints. It informs comparison conditions; its full list is not imported wholesale as fusion methods. Publication is IJCAI 2025 Survey Track, with CCF applicability pending.

## Seed reconciliation

All six supplied identifiers point to matching titles. Several details need qualification before these records become manuscript citations.

| Seed | Reconciliation | Reading status |
| --- | --- | --- |
| [Deep Model Fusion](https://ieeexplore.ieee.org/document/11268959) | TNNLS 37(5), 2008–2024, 2026; online publication was 25 November 2025. | Final metadata/abstract; selected sections of the 2023 author version. Final-text omissions cannot be inferred. |
| [From Parameters to Behaviors](https://aclanthology.org/2026.findings-emnlp.722/) | Formal Findings of EMNLP 2026 record now exists. PDF p.15178 gives **Ming Li**; landing page/export instead gives **Li Ming**. Canonical author list follows the authoritative PDF, while the raw export is preserved for audit. | Selected sections of the final 25-page PDF. |
| [Trustworthy Federated Learning](https://doi.org/10.1145/3678181) | ACM TIST 15(6), article 112, 2024. | Publisher HTML sections; PDF retrieval denied. |
| [Model Aggregation Techniques](https://doi.org/10.1016/j.future.2023.09.008) | FGCS 150, 272–293, 2024. DOI's 2023 component is not the issue year. | Abstract/highlights only. |
| [Emerging Trends](https://doi.org/10.1007/s13042-024-02119-1) | IJMLC 15, 3769–3790, 2024. | Selected sections of the final 22-page PDF. |
| [Knowledge Transmission and Fusion](https://doi.org/10.1016/j.inffus.2026.104819) | Publisher preview reports online 29 September 2026 and pre-proof status. Crossref schedules volume 139 for March 2027. Publisher/author page list Haonan Wu, while Crossref omits that author. Keep as a **metadata-conflict candidate**; record online and scheduled issue years separately. | Publisher abstract/introduction excerpts, not complete text. |

No seed was silently replaced by a similar title. The unresolved Fan record stays in the comparison because its announced scope is directly relevant, but it must not be counted as fully reconciled metadata or fully read evidence.

## Coverage comparison

The following cells report observed coverage. “Unassessed” means that access or reading depth was insufficient, not that the survey omits the topic. The [bibliography](../data/papers.json) supplies source links and further qualifications.

| Survey / year / venue | Primary scope and taxonomy | Representation | Governance | Evolution | Federated/decentralized setting |
| --- | --- | --- | --- | --- | --- |
| Li / 2026 / TNNLS | Deep fusion; four mechanism families | Geometry, matching, averaging, ensembles | Motivations and robustness; final breadth unassessed | Repeated fusion/forgetting in author version | FL application |
| Cai / 2026 / Findings EMNLP | Independent target; parameter/representation/behavior signals | Compatibility and alignment | Risk transfer, provenance, privacy, safety | Continual fusion and forgetting | Broad model reuse |
| Zhang / 2024 / TIST | Trustworthy FL; four trust dimensions | FL actors and exposed signals | Threats, defenses, fairness, explainability | Dynamic clients/threats discussed | Direct FL |
| Qi / 2024 / FGCS | FL aggregation; detailed taxonomy unassessed | Aggregation/heterogeneity | Malicious models/privacy explicit | Unassessed | Direct FL |
| Ji / 2024 / IJMLC | Fusion improvements plus federated X | Weighting, matching, clustering | Fairness/privacy/security | Learning-paradigm intersections | Direct FL |
| Fan / 2026 online / Information Fusion, candidate | Coupled transmission/fusion; states and decisions | Carriers and knowledge states | Constraints, unreliable knowledge | Explicit closed-loop interactions | Distributed clients among settings |
| [Yadav / 2025 / TMLR](https://openreview.net/forum?id=u0azVc9Y0y) | Expert/routing/application design choices | Interfaces and routing granularity | Access assumptions, malicious sources | Addition/removal and continual loop agenda | Decentralized development; FL comparison |
| [Yang / 2026 / CSUR](https://doi.org/10.1145/3787849) | Pre-merging/during-merging plus applications | Architecture/alignment/subspaces | Attacks, ownership, trustworthy merging | Dedicated continual-learning subsection | FL application |
| [Song / 2026 / Preprint](https://arxiv.org/abs/2603.09938) | FUSE: foundations/strategies/scenarios/ecosystem | Geometry and guided merging | Safety, bias, failure diagnostics | Dynamic merging and feedback | FL application |
| [Ruan / 2025 / Preprint](https://arxiv.org/abs/2503.08998) | Seven mechanism families | Alignment and interference | Detailed multi-property analysis not established | Continual interference noted | FL background |
| [Wang / 2025 / Preprint](https://arxiv.org/abs/2510.13890) | SLM–LLM objectives | Guidance, roles and fusion | Privacy, safety decoding, guardians | Interoperable/adaptive ecosystem agenda | Cloud-edge; not necessarily FL |
| [Li / 2025 / Preprint](https://arxiv.org/abs/2507.16731) | Edge-cloud inference/learning architectures | Task/token interfaces and compatibility | Privacy/security/resources | Dynamic transfer and feedback | Includes federated edge-cloud |

| Survey | Evaluation framework observed | Limitation of this comparison | Potential distinction to test |
| --- | --- | --- | --- |
| Li TNNLS | Mechanism-specific comparisons | Older author text is not final text | Decision and revalidation account across interfaces |
| Cai | Model/task pools; retention, access, costs, safety | Broad risk/evaluation coverage already present | Include persistent source-model collaboration excluded by its definition |
| Zhang | Attribute-specific evaluation and benchmark challenges | Full PDF unavailable | Transfer guarantees from training protocols to model assets |
| Qi | Review reports 201 studies | Detailed comparison requires full text | Separate iterative training from reuse of existing assets |
| Ji | Heterogeneous protocol comparability | Trust topics must receive credit | Connect decisions to evidence validity after change |
| Fan | Benchmark map/checklist/constraint lookup announced | Full text and author reconciliation still needed | Strongest competing loop; no novelty claim yet |
| Yadav | Shared benchmark/comparison agenda | Continual loop proposed, not established deployment | Property-specific acceptance and revalidation evidence |
| Yang | Benchmarks and empirical comparison | Detailed reading is author version | Cross-operator obligations and guarantee assumptions |
| Song | Benchmarks, costs and failure diagnostics | Preprint; primary references need verification | Trace obligations through operator and model changes |
| Ruan | Method-level descriptions | Short preprint and selected sections | Structured governance and collaboration comparison |
| Wang | Datasets and system-level evaluation agenda | Under-review preprint | Extend beyond SLM–LLM roles without losing trust specificity |
| Li edge-cloud | Dual-model benchmarks and deployment frameworks | Edge-cloud focus; preprint | Compare deployment with merging/distillation obligations |

## Positioning supported by evidence

### A confirmed scope difference

Cai et al. explicitly exclude inference-time ensembles and source-model routing from their operational fusion definition (§2, pp.15179–15180). This provides a concrete reason to retain **“and Collaboration”** in the new title, provided that the corpus actually includes reusable model assets, explicit knowledge interfaces or capability-based decisions. It does not justify including all multi-agent systems, RAG or MoE papers. [Final paper](https://aclanthology.org/2026.findings-emnlp.722.pdf)

### Overlap requiring acknowledgment

The nearest competitors are substantive. Fan et al.'s introduction already presents coupled knowledge states, decisions, diagnostics and feedback under practical constraints. Yadav et al. discuss malicious contributors, adding/removing experts and continual development (§7, pp.23–24). Yang et al. explicitly discuss trustworthy merging from owner and combiner perspectives (§6, p.29 of the author version). Song and Zheng include failure diagnostics, dynamic merging and safety-preserving directions (§§7.4–7.5). These findings rule out a defensible claim that earlier surveys collectively ignore governance or lifecycle issues. [Fan publisher preview](https://www.sciencedirect.com/science/article/pii/S1566253526006950), [MoErging author PDF](https://arxiv.org/pdf/2408.07057), [Yang author PDF](https://arxiv.org/pdf/2408.07666), [FUSE preprint](https://arxiv.org/pdf/2603.09938)

### Candidate analytical contribution

A useful candidate is a **traceable decision record** linking what is known about a source model, which operations the access conditions permit, which property is guaranteed or merely measured, what decision follows, and which later changes invalidate that evidence. Representation supplies information for a decision; governance specifies acceptance, rejection or fallback; evolution tracks whether the evidence remains applicable. This is a proposed organizing device, not an experimentally validated algorithm or an established original contribution.

Its value must be demonstrated in method-level comparison: for example, whether the same privacy statement applies to parameter merging, distillation and persistent routing; whether a guarantee survives new sources or changed routing; and whether withdrawal means removal of a component or removal of its learned influence. Existing surveys must receive credit wherever they already answer these questions. A topic's appearance in a future-work paragraph also must not be mistaken for an implemented solution.

### Evaluation hypothesis

The evaluation section should test evidence validity across a sequence of collaboration decisions, including capability retention, worst-party loss, threat-specific outcomes, access budgets, change detection, rollback and post-update revalidation. This does **not** imply that these metrics are new: Cai et al. already relate access and safety goals to evaluation metrics, while the collaboration surveys discuss system-level evaluation. The possible increment is a clear mapping from a change event to the assumptions and measurements that must be checked again. The synthesis uses that mapping as an analytical and evaluation proposal, not an experimentally validated result.

## Title and drafting gate

Recommended working title: **Trustworthy Model Fusion and Collaboration: A Survey of Representation, Governance, and Evolution**. It accurately preserves the user's broad scope and distinguishes persistent collaboration from inference-independent fusion. “Federated” should remain a priority setting and explicit protocol tag; using it in the main title would unnecessarily narrow the confirmed scope. The alternative “From Aggregation to Governed Knowledge Collaboration” can serve as framing, but it risks implying a universal chronological progression.

Before treating the three proposed contributions as established, obtain the complete Fan and Qi texts, inspect the final TNNLS and CSUR versions where material, reconcile Fan's author list and scheduled year, and build several fully grounded cross-operator comparisons. Then test whether the proposed decision record reveals a distinction not already supplied by the nearest surveys. The current evidence supports a promising positioning hypothesis and an auditable comparison; it does not yet establish originality or justify full manuscript drafting.

## Scope of the assessment

The comparison credits positively observed coverage and does not treat inaccessible text as missing content. The distinction proposed here is comparative and problem-driven; novelty of the framework has not been established. Full-text reconciliation of the nearest overlapping surveys and primary-paper comparisons remain prerequisites for strong differentiation claims. The [research questions](research-gaps.md) and [working outline](survey-outline.md) specify what the next synthesis must demonstrate.
