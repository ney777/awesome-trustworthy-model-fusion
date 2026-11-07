# Governance extension search audit

This is a historical search log. Inclusion decisions described here may be superseded by the [scope correction](scope-correction.md); generic FL methods no longer appear in the active catalogue.

Private knowledge transfer, fairness and provenance require different evidence. Keeping raw data local does not by itself protect released weights; source detection does not estimate contribution; and reduced class-wise error gaps do not establish demographic fairness. These distinctions govern the 18 additions in this extension.

## Evidence boundaries

Noisy teacher aggregation gives a foundation for private ensemble-to-student transfer when teachers remain hidden, training partitions are disjoint and queries are budgeted ([Papernot et al., 2018](https://research.google/pubs/scalable-private-learning-with-pate/)). Reusing released private checkpoints is a different problem. Differentially Private Model Merging uses training-mechanism information to meet a target privacy budget, whereas geometry-aware DP-Merging modifies private fine-tuning and assumes disjoint task membership for its parallel-composition argument ([Yin et al., 2026](https://neurips.cc/virtual/2026/poster/149241), [Liu et al., 2026](https://arxiv.org/abs/2608.26655)).

Privacy statements must identify the protected channel. FedAUX explicitly analyzes its scoring mechanism and leaves communicated client models as a separate privacy cost ([Sattler et al., 2023](https://doi.org/10.1109/TNNLS.2021.3129371)). PriME explicitly offers empirical membership-inference mitigation without a formal guarantee ([Kim et al., 2025](https://doi.org/10.18653/v1/2025.emnlp-main.1747)). FedXDS supplies attribution-guided feature sharing with a stated metric-privacy mechanism; it is supporting evidence, not a complete explanation of fusion decisions ([Hoefler et al., 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Hoefler_FedXDS_Leveraging_Model_Attribution_Methods_to_counteract_Data_Heterogeneity_in_ICCV_2025_paper.html)).

FairMerging defines subgroups by class labels and studies merging-induced excess-loss disparities. Its need for labeled target data, subgroup annotations and pre-merge fine-tuning remains explicit ([Liu et al., 2026](https://proceedings.mlr.press/v306/liu26dl.html)). The PACLIC study instead contributes primary experiments on social-bias/utility tradeoffs and notes the US-centric stereotype source; the word Survey in its title does not make it a secondary-only review ([Shirafuji et al., 2025](https://aclanthology.org/2025.paclic-1.24/)).

Ownership signals and contribution values answer different questions. MergePrint evaluates whether an embedded signal survives merging, while its limitations exclude knowledge-distillation theft and MoE ([Yamabe et al., 2025](https://doi.org/10.18653/v1/2025.acl-long.342)). RouteMark identifies expert reuse through routing fingerprints and remains a preprint ([He et al., 2025](https://arxiv.org/abs/2508.01784)). ShapleyFL estimates validation-dependent marginal utility for aggregation and sampling; those scores are neither authentication nor a complete provenance certificate ([Sun et al., 2023](https://doi.org/10.1145/3580305.3599500)).

Constraint-aware orchestration also requires calibrated quality information. Unified routing/cascading optimizes an expected-budget objective using estimated quantities, not a hard per-query safety guarantee ([Dekoninck et al., 2025](https://proceedings.mlr.press/v267/dekoninck25a.html)). SATER mainly evaluates one small/large model pair and uses generated tokens as a latency proxy ([Shen et al., 2025](https://doi.org/10.18653/v1/2025.emnlp-main.531)).

## Search protocol

Date: 2026-11-07. This targeted extension is not an exhaustive systematic review. Discovery used web searches, followed by primary pages from ACL Anthology, PMLR, CVF, AAAI, NeurIPS, arXiv, publisher-deposited Crossref metadata and author/institution websites. Detailed method claims require retrieved sections rather than search snippets.

Queries included “model merging fairness 2025 2026”, “model merging privacy differential”, “privacy preserving knowledge transfer”, “model merging provenance attribution watermark”, “model merging fingerprint”, “ShapleyFL”, “FedAUX”, “Cascade Routing”, and exact-title follow-ups. The 2024–2026 interval was prioritized; PATE and the 2023 items fill mechanism or contribution-estimation needs.

Backward inspection of RouteMark §2.3/references led to MergePrint and Cong et al.; final publication metadata were then recovered. FedXDS related work/references led to FedAUX. The newer RouteMark discussion checks a forward connection from MergePrint; the 2026 watermark paper extends the earlier open-source durability discussion. These are bounded reference chains, not a complete cited-by traversal or a citation-count audit.

Inclusion requires direct inter-model transfer, aggregation, merging, expert attribution or model orchestration. Generic DP training, fairness, watermarking without merging evidence and general multi-agent coordination were excluded. Exact normalized-title de-duplication was performed against the previously collected governance, representation and seed records. Preprint/formal variants are linked in one record. PATE is foundation; FedXDS is related-governance support; 16 records are core.

## Publication and reading scope

The extension contains 18 records: 15 from 2024–2026, two from 2023 and one from 2018. Seventeen received section-level reading. CKD received abstract-level reading because the publisher returned access verification and no legitimate full PDF was recovered; its detailed threat assumptions and privacy guarantee remain unextracted.

Fourteen have published venue metadata, two are accepted NeurIPS 2026 papers and two are preprints. NeurIPS' official pages schedule Differentially Private Model Merging and Making Open-Source Text LLM Watermarks Durable Against Merging for December 2026. The conference has not occurred on the audit date; final proceedings PDFs were not retrieved. Acceptance and author-PDF reading are recorded separately. RouteMark and geometry-aware DP-Merging remain explicitly Preprint.

FedAUX uses its final 2023 issue year, although the DOI contains 2021; technical reading used the author preprint. The LAMPS article has conflicting Crossref print/online dates; its accepted PDF explicitly states LAMPS 2024 with the matching DOI, which resolves the year. Minor ACL author-name variants for PhiMM, SATER and MergePrint are normalized to the PDF and documented per record.

| Record | Year / venue | Relation | Reading | Status |
|---|---|---|---|---|
| [FairMerging: Rethinking Model Merging through the Lens of Fairness](https://proceedings.mlr.press/v306/liu26dl.html) | 2026 / ICML | core | section-reviewed | published |
| [Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/) | 2025 / EMNLP | core | section-reviewed | published |
| [Be Cautious When Merging Unfamiliar LLMs: A Phishing Model Capable of Stealing Privacy](https://aclanthology.org/2025.findings-acl.713/) | 2025 / Findings of ACL | core | section-reviewed | published |
| [Complementary Knowledge Distillation for Robust and Privacy-Preserving Model Serving in Vertical Federated Learning](https://ojs.aaai.org/index.php/AAAI/article/view/29958) | 2024 / AAAI | core | abstract-reviewed | published |
| [Differentially Private Model Merging](https://neurips.cc/virtual/2026/poster/149241) | 2026 / NeurIPS | core | section-reviewed | accepted |
| [When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy](https://arxiv.org/abs/2608.26655) | 2026 / arXiv | core | section-reviewed | preprint |
| [RouteMark: A Fingerprint for Intellectual Property Attribution in Routing-based Model Merging](https://arxiv.org/abs/2508.01784) | 2025 / arXiv | core | section-reviewed | preprint |
| [Have You Merged My Model? On The Robustness of Large Language Model IP Protection Methods Against Model Merging](https://doi.org/10.1145/3689217.3690614) | 2024 / LAMPS | core | section-reviewed | published |
| [Defending Unauthorized Model Merging via Dual-Stage Weight Protection](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html) | 2026 / CVPR | core | section-reviewed | published |
| [FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Hoefler_FedXDS_Leveraging_Model_Attribution_Methods_to_counteract_Data_Heterogeneity_in_ICCV_2025_paper.html) | 2025 / ICCV | related-governance | section-reviewed | published |
| [FedAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning](https://doi.org/10.1109/tnnls.2021.3129371) | 2023 / TNNLS | core | section-reviewed | published |
| [ShapleyFL: Robust Federated Learning Based on Shapley Value](https://doi.org/10.1145/3580305.3599500) | 2023 / KDD | core | section-reviewed | published |
| [Scalable Private Learning with PATE](https://openreview.net/forum?id=rkZB1XbRZ) | 2018 / ICLR | foundation | section-reviewed | published |
| [A Unified Approach to Routing and Cascading for LLMs](https://proceedings.mlr.press/v267/dekoninck25a.html) | 2025 / ICML | core | section-reviewed | published |
| [SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading](https://aclanthology.org/2025.emnlp-main.531/) | 2025 / EMNLP | core | section-reviewed | published |
| [An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation](https://aclanthology.org/2025.paclic-1.24/) | 2025 / PACLIC | core | section-reviewed | published |
| [Making Open-Source Text LLM Watermarks Durable Against Merging](https://neurips.cc/virtual/2026/poster/155690) | 2026 / NeurIPS | core | section-reviewed | accepted |
| [MergePrint: Merge-Resistant Fingerprints for Robust Black-box Ownership Verification of Large Language Models](https://aclanthology.org/2025.acl-long.342/) | 2025 / ACL | core | section-reviewed | published |

## CCF and unresolved tracks

Ranks use CCF 2026 seventh formal edition, documented in the venue audit. RAID is B (PDF p.21, row9). CSUR and PACLIC are absent after acronym/full-name searches over all72 pages and are None. Findings and the LAMPS companion workshop do not inherit parent-conference ranks. Preprint status is distinct from venue absence. Unknown applicability remains pending.

The KDD directory row has no ADS-specific footnote, and the general scope does not expressly discuss ADS or EMNLP Industry. The [EMNLP 2024 Industry CFP](https://2024.emnlp.org/calls/industry_track/) sets a six-page limit without calling the track Short. Length alone does not resolve the mapping. Beimingwu ADS and MergeKit Industry therefore remain internally pending; this does not alter the verified parent-venue ranks.

Downloaded full texts and retrieval snapshots remain private; per-record full-text hashes are included. No experiments were reproduced. This log records discovery activity, not repository release status.
