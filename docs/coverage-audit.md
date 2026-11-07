# Coverage correction and omission audit

**Historical audit.** Current scope decisions are in the [scope correction](scope-correction.md). The former all-inclusion follow-up was over-broad; of the six candidates below, WB fusion and FedFTG remain included, while Buffalo, FedBone, FairFHTL and the model-heterogeneous FL attack have been removed from the catalogue. Historical counts are not current library totals.

Model Trip and PrivFusion had already been found and stored, but an incorrect metadata status hid them from the ranked README and excluded them from BibTeX. The earlier extraction step marked these two papers `partial` because method reading was unfinished, even though their bibliographic identities and CCF-A venues had been confirmed. This confused bibliographic verification with reading depth. The README filter then exposed only records with verified bibliography and CCF applicability. This was a curation error, not a relevance exclusion or a failed title search.

The correction updates the existing records without duplicating them, separates identity from reading progress, and adds a visible pending-verification table. An unavailable final PDF no longer causes otherwise confirmed metadata to be downgraded. Regression checks cover both abstract-only eligibility and visibility of unresolved records. The initial corpus had 93 records; this bounded follow-up adds 14 distinct works, producing 107 records, 106 reconciled bibliographies and 103 ranked-catalogue entries. Four records remain visibly pending for identity or track applicability.

## The two supplied papers

| Work | Final publication and CCF 2026 | Placement | Evidence boundary |
|---|---|---|---|
| [Model Trip](https://doi.org/10.1109/ICDE60146.2024.00177) | ICDE 2024, 2231–2244; A | Governance: fairness-aware fusion, with privacy and multi-federation tags | Final abstract reviewed. FairFusion jointly targets utility, privacy and fairness; exact definitions and protocol await final-text review. |
| [PrivFusion](https://doi.org/10.1109/TKDE.2024.3430819) | TKDE 36(12), 9051–9064, 2024; A | Governance: privacy-preserving fusion | Selected sections of the [2023 author version](https://arxiv.org/abs/2311.03396v1) reviewed; its title and author list differ from the final paper. Activation-based matching uses inference examples; no-retraining is not data independence. |

Model Trip's FairFusion method name and PrivFusion's earlier title are search aliases, not additional papers. Final publisher-deposited author lists remain authoritative where author homepages omit names. The Model Trip author-linked code URL returned 404 at inspection; no usable code link is claimed. The unrelated [IBM PrivFusion](https://github.com/IBM/PrivFusion), about multi-agent dataset harmonization, must not be attached to the TKDE record.

## Additional missing work

The missing works form three connected groups. Classical matching and distillation explain the interfaces on which trustworthy fusion builds. Multi-federation methods distinguish repeated training or distillation from reuse without retraining. Preference-aware merging makes trade-offs explicit, but optimizing task or proxy-reward preferences does not itself establish privacy or demographic fairness.

| Work | Publication | CCF 2026 | Category | Reading depth |
|---|---|:---:|---|---|
| [MoFedNet](https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-5684-5) | JCST 2026 | B | evolution | section-reviewed |
| [Cronus](https://neurips2021workshopfl.github.io/NFFL-2021/paper.html) | NFFL at NeurIPS 2021 | None | governance | section-reviewed |
| [Rewarded soups](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e12a3b98b67e8395f639fde4c2b03168-Abstract-Conference.html) | NeurIPS 2023 | A | governance | section-reviewed |
| [MAP](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3724221b623bf1966e92cd266ac6177-Abstract-Conference.html) | ICLR 2025 | A | governance | section-reviewed |
| [Pareto Merging](https://proceedings.mlr.press/v267/chen25af.html) | ICML 2025 | A | governance | section-reviewed |
| [PFNM](https://proceedings.mlr.press/v97/yurochkin19a.html) | ICML 2019 | A | representation | section-reviewed |
| [FedMD](https://federated-learning.org/fl-neurips-2019/) | FL-NeurIPS 2019 | None | representation | section-reviewed |
| [FedMA](https://openreview.net/forum?id=BkluqlSFDS) | ICLR 2020 | A | representation | section-reviewed |
| [FedGKT](https://proceedings.neurips.cc/paper/2020/hash/a1d4c20b182ad7137ab3606f0e3fc8a4-Abstract.html) | NeurIPS 2020 | A | representation | section-reviewed |
| [FedBE](https://openreview.net/forum?id=dgtpE6gKjHn) | ICLR 2021 | A | representation | section-reviewed |
| [GAMF](https://proceedings.mlr.press/v162/liu22k.html) | ICML 2022 | A | representation | section-reviewed |
| [PANs](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Federated_Learning_With_Position-Aware_Neurons_CVPR_2022_paper.html) | CVPR 2022 | A | representation | section-reviewed |
| [FedTAM](https://ieeexplore.ieee.org/document/10476260/) | ICPADS 2023 | Pending track | representation | abstract-reviewed |
| [MetaFed](https://ieeexplore.ieee.org/document/10197230/) | TNNLS 2024 | B | representation | section-reviewed |

FedMD and Cronus are companion-workshop records and do not inherit NeurIPS A. Cronus uses the verified 2021 workshop version, not its 2019 preprint year or an ICLR 2022 under-review page. MetaFed uses its 2024 final TNNLS issue year rather than the 2023 online/DOI year. MoFedNet uses JCST 2026. ICPADS is C in the directory, but FedTAM's individual full/regular-paper applicability remains unresolved; a page count or Oral label does not settle it. JCST-B and ICPADS-C have been added to the [venue register](../data/venues_ccf2026.json).

## Why the coverage was incomplete

The earlier search was purposive and weighted toward recent checkpoint merging, routing and governance: 30 of 41 records in the representation/evolution extension and 15 of 18 in the governance extension were dated 2024–2026. The stored logs did not establish a completed foundation-level coverage check. This supports a diagnosis of insufficient classical federated matching and distillation coverage; it does not prove that those search terms were never attempted. Acronym/title differences, early-versus-final versions, and special publication tracks further complicate discovery and classification.

Reading the two seeds exposed specific broken citation chains. PrivFusion's author manuscript cites GAMF, FedMA and PANs; those records were missing. FedMA leads backward to PFNM, while GAMF and PANs provide later links to the matching family. FedBE connects FedMD, FedDF and matching; FedGKT links heterogeneous transfer and server-side learning. In the forward direction, MoFedNet's final Introduction and references explicitly cite both Model Trip and PrivFusion. Pareto Merging's related-work discussion connects Rewarded soups and MAP. These are checked, bounded citation edges, not a complete cited-by graph.

The corrective search used the following actual query families and primary-source follow-ups. Complete private working logs retain request details; this table reports the inspected branches without inventing aggregate search-hit counts.

| Branch | Executed query examples | Follow-up |
|---|---|---|
| Named seeds | `"PrivFusion" model fusion`; `"Model Trip" "fusion" "federations"` | DOI and final author metadata, author aliases, legal author version, local public-homepage bibliography |
| Multi-federation | `"multi-federation" "model fusion"`; `"cross-federation" "fusion" model paper`; `"MoFedNet" pdf`; `"MetaFed" "2023" cyclic distillation`; `"FedTAM" filetype:pdf` | JCST final PDF, IEEE-deposited metadata, accepted author manuscript, exact forward reference checks |
| Foundations | `"Probabilistic Federated Neural Matching" PMLR`; `"Federated Learning with Matched Averaging" ICLR 2020`; `"FedMD" "2019" workshop`; `"FedGKT" "FedBE" federated learning`; `"Cronus" "Robust and Heterogeneous"` | PMLR, CVF, NeurIPS, official workshop program and author manuscripts; exact GAMF/PANs title searches |
| Trade-offs | `"Rewarded soups" NeurIPS 2023`; `"Pareto" "model merging" ICLR paper` | Final NeurIPS/ICLR/PMLR pages and selected methods sections of all three papers |

## Historical screening queue — now processed

This table preserves the six candidates queued at the 107-record snapshot. All six were processed in the earlier follow-up. The corrected decisions retain two and exclude four; see the [federated follow-up audit](federated-coverage-audit.md) for current decisions. The next-check column below records the historical task, not an outstanding exclusion.

| Candidate | Next check | Current source |
|---|---|---|
| Buffalo: Biomedical Vision-Language Understanding with Cross-Modal Prototype and Federated Foundation Model Collaboration | Determine the fusion object and role of prototype exchange from the paper; final bibliography is identified. | [ACM publication](https://doi.org/10.1145/3627673.3679627) |
| FedBone: Towards Large-Scale Federated Multi-Task Learning | Assess split training and gradient combination against the broader training-time fusion scope. | [JCST publication](https://doi.org/10.1007/s11390-024-3639-x) |
| FairFHTL: Achieving Task-Agnostic Fairness in Federated Hetero-Task Learning | Verify full publication and fairness mechanism before inclusion. | [Author publication list](https://www.bj-yan.top/publications) |
| Wasserstein Barycenter-Based Model Fusion and Linear Mode Connectivity of Neural Networks | Follow PrivFusion's reference 11 and reconcile final publication. | [Seed author manuscript](https://arxiv.org/abs/2311.03396v1) |
| Fine-tuning Global Model via Data-free Knowledge Distillation for Non-IID Federated Learning | Follow PrivFusion's reference 16; compare its operator and data assumptions with FedDF/FedGen. | [Seed author manuscript](https://arxiv.org/abs/2311.03396v1) |
| Breaking Privacy in Model-Heterogeneous Federated Learning | Read the attack model and confirm applicability to the fusion threat matrix. | [USENIX RAID 2024](https://www.usenix.org/conference/raid2024) |

Generic multimodal-feature fusion and identity/cloud federation hits were excluded from this targeted branch when they did not establish interaction among independent models. Shared authors, title keywords and an impressive venue label are not inclusion criteria. This historical audit repairs demonstrated omissions; the linked follow-up closes its six-item queue. Neither pass establishes exhaustive coverage or experimental reproduction.
