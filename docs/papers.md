# Literature records

Generated from `data/papers.json`. Pending ranks and incomplete reading are explicit; inclusion here is not a universal trustworthiness endorsement.

## FusionBench: A Unified Library and Comprehensive Benchmark for Deep Model Fusion

| Field | Details |
| --- | --- |
| Venue / year | Journal of Machine Learning Research, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.jmlr.org/papers/v26/25-1243.html) · [Code](https://github.com/tanganke/fusion_bench) |
| Problem | How can deep-model fusion methods be implemented and compared under shared infrastructure? |
| Mechanism | FusionBench supplies curated model/task configurations and standardized algorithm/evaluation interfaces. |
| Contribution | Provides infrastructure spanning multi-task fusion, generalization, efficiency, and selected robustness settings. |
| Assumptions | Comparable model access, task data, and evaluation configurations are available. |
| Evidence boundary | The provided task/model pools delimit comparability. Its benchmark results do not imply that every privacy, fairness, security, or continual-lifecycle property is assessed. |
| Evidence | [Official publication metadata and abstract](https://www.jmlr.org/papers/v26/25-1243.html); [§2 system design, PDF pp.2–4; Appendix E.3–E.4, PDF pp.18–25](http://jmlr.org/papers/volume26/25-1243/25-1243.pdf) |

## MergeBench: A Benchmark for Merging Domain-Specialized LLMs

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/91f7f71cb04699f387dc863da42a1fe3-Abstract-Datasets_and_Benchmarks_Track.html) |
| Problem | LLM merging needs controlled comparisons across specialist capabilities and costs. |
| Mechanism | Compare eight merging methods across five domains, forgetting and algorithm/validation runtime. |
| Contribution | A benchmark that exposes quality, retention and tuning-cost tradeoffs. |
| Assumptions | Same-base compatible specialists; method-dependent training or validation data. |
| Evidence boundary | Safety is one tested capability; this is not a comprehensive privacy/fairness/federated benchmark. |
| Evidence | [Official publication metadata](https://proceedings.neurips.cc/paper_files/paper/2025/hash/91f7f71cb04699f387dc863da42a1fe3-Abstract-Datasets_and_Benchmarks_Track.html); [§§3.1–3.3, PDF pp.3–4: compatible model construction and data-access protocol; §4.3, PDF pp.7–8: merging and validation runtime; §5, PDF p.9: limitations](https://proceedings.neurips.cc/paper_files/paper/2025/file/91f7f71cb04699f387dc863da42a1fe3-Paper-Datasets_and_Benchmarks_Track.pdf); [Full paper submission deadline; reviewing standards and accepted-paper publication paragraphs](https://nips.cc/Conferences/2025/CallForDatasetsBenchmarks) |

## Arcee’s MergeKit: A Toolkit for Merging Large Language Models

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track, 2024 |
| Publication status | Industry track |
| Bibliographic verification | verified |
| CCF 2026 | Pending verification |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2024.emnlp-industry.36/) · [Code](https://github.com/arcee-ai/mergekit) |
| Problem | How can weight-merging methods be made usable across practical hardware configurations? |
| Mechanism | YAML recipes configure interchangeable merge operations; lazy tensor loading supports memory-constrained execution. |
| Contribution | Provides reusable engineering infrastructure for composing model parameters. |
| Assumptions | Accessible model checkpoints and method-specific compatibility conditions are required. |
| Evidence boundary | Supported and anticipated merge categories are distinguished in Figure 1; method-specific architecture and initialization constraints still apply. Toolkit availability is not evidence that arbitrary merges preserve quality or safety. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2024.emnlp-industry.36/); [Official ACL abstract and publication metadata](https://aclanthology.org/2024.emnlp-industry.36/); [§2.2; §3.1–3.3 and Figure 1, PDF pp.2–4](https://aclanthology.org/2024.emnlp-industry.36.pdf) |

## Beimingwu: A Learnware Dock System

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2024 |
| Publication status | Applied Data Science track |
| Bibliographic verification | verified |
| CCF 2026 | Pending verification |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1145/3637528.3671617) · [Code](https://github.com/Learnware-LAMDA/Beimingwu) |
| Problem | How can heterogeneous trained models be submitted, identified, deployed, and reused in a common system? |
| Mechanism | Beimingwu implements submission, usability checks, organization, search, deployment, and model-reuse components. |
| Contribution | Provides a working platform for external model organization and reuse experiments. |
| Assumptions | Developers provide models and generated specifications; users retain local data for the selected reuse method. |
| Evidence boundary | System support and specification-based retrieval do not certify every submitted model’s safety or privacy. Evidence is limited to the supported workflows and evaluated model/task collections. |
| Evidence | [Official publication metadata and abstract](https://doi.org/10.1145/3637528.3671617); [§§3–5, PDF pp.3–7; §6 evaluation, PDF pp.8–9](https://www.lamda.nju.edu.cn/liujd/file/kdd24/KDD24-bmwu.pdf); [Official track listing with all ten authors](https://kdd.org/kdd2024/applied-data-science-track-papers/); [Associated earlier author version, not final metadata authority](https://arxiv.org/abs/2401.14427) |

## RouterBench: A Benchmark for Multi-LLM Routing System

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2024 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2403.12031) · [Code](https://github.com/withmartian/routerbench) |
| Problem | How can multi-LLM routing methods be compared without repeatedly paying for model inference? |
| Mechanism | RouterBench includes stored inference outcomes and evaluation of predictive and cascading routers. |
| Contribution | Offers a reusable benchmark for routing quality-cost tradeoffs. |
| Assumptions | The recorded candidate models, task distribution, and pricing assumptions define the evaluation environment. |
| Evidence boundary | Its stated limitations exclude latency and throughput from the main objectives and acknowledge incomplete task/model coverage; stored outputs cannot reproduce every live-system change. |
| Evidence | [Official publication metadata and abstract](https://arxiv.org/abs/2403.12031); [§3 benchmark; §6 Limitations and Future Work, PDF p.8](https://arxiv.org/pdf/2403.12031) |

## FedSEAM: Federated Continual Learning of LLMs via Subspace Expert Agreement Merging

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2026 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2610.33496) |
| Problem | Federated continual adaptation can erase prior expert content and drift expert routing even when earlier experts are frozen. |
| Mechanism | Clients select sparse expert tiles using corrected gradient scores and task novelty, test direction/sign compatibility for cross-task sharing, and train task experts locally. The server eigendecomposes averaged input-subspace projectors, filters directions by signed agreement, and forms partial tile merges; gate freezing, snapshots and prior-overlap acceptance restrict changes. |
| Contribution | Separates routing drift from merge erasure and implements agreement-restricted merging for federated continual LLM adaptation. |
| Assumptions | Compatible frozen backbone and tile coordinates, synchronized fixed task order, current local data and retained expert/task-start snapshots; the server inspects individual expert updates. |
| Evidence boundary | The reported clients have near-identically distributed shards; non-IID clients are explicitly future work. Selected parameter components are preserved per merge, not all earlier-task loss over an entire trajectory. Update leakage remains possible; secure aggregation and differential privacy are future work. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://arxiv.org/abs/2610.33496); [Author preprint v1, pp.3–6 §§3–5; p.9 Limitations](https://arxiv.org/pdf/2610.33496v1) |

## Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://ijcai.org/proceedings/2026/673) |
| Problem | How can a router adapt to users whose cost-performance preferences are implicit? |
| Mechanism | A meta-learned context encoder summarizes pairwise feedback; an entropy-regularized policy selects models as a contextual bandit. |
| Contribution | Adds adaptation to changing preferences beyond a fixed global cost threshold. |
| Assumptions | User feedback and candidate-model performance/cost observations are available. |
| Evidence boundary | The policy optimizes a one-step reward rather than long-term collaboration consequences. Latency and privacy preferences remain future work. |
| Evidence | [Official publication metadata and abstract](https://ijcai.org/proceedings/2026/673); [§4.1–4.2, PDF pp.3–4; §6 Conclusion, PDF p.7](https://ijcai.org/proceedings/2026/0673.pdf) |

## MoFedNet: Semantic Link is All Models Need

| Field | Details |
| --- | --- |
| Venue / year | Journal of Computer Science and Technology, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-5684-5) |
| Problem | Coordinate heterogeneous models while balancing task quality and orchestration cost. |
| Mechanism | L2L composes hypergraph workflows; CoMER retrieves structured memories; EvoLOM updates collaboration paths using performance, latency and cost feedback. |
| Contribution | A model-collaboration system with semantic contracts, memory and adaptive path optimization. |
| Assumptions | Models expose capability descriptions and interfaces; a centralized orchestration layer monitors a distributed model network. |
| Evidence boundary | Evaluation includes synthetic MCP tasks and LLM-judged ophthalmic VQA; it does not establish patient-level clinical benefit. Memory upkeep adds overhead, and aggressive forgetting may lose useful knowledge. Privacy-aware contracts are not themselves a differential-privacy guarantee. |
| Evidence | [Official citation and complete author list; final issue is March 2026, not the DOI year 2025.](https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-5684-5); [PDF pp.2–3 (printed475–476): metadata, regular-paper track and architecture; p.7 (480), Sections3.2.1–3.2.2; p.10 (483), Section3.4; p.13 (486), Sections5.1–5.2; p.16 (489), Section5.5.4; p.18 (491), references11–12.](https://jcst.ict.ac.cn/en/article/pdf/preview/10.1007/s11390-025-5684-5.pdf) |

## Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d0da30e312b75a3fffd9e9191f8bc1b0-Abstract-Conference.html) · [Code](https://github.com/zihuanqiu/NUFILT) |
| Problem | How can continual merging preserve previous behavior while accommodating a new task without task data? |
| Mechanism | NUFILT filters an update, adapts a lightweight low-rank component with a data-free objective, and fuses the result into the backbone. |
| Contribution | Combines explicit retention constraints with a plasticity adjustment during sequential fusion. |
| Assumptions | Experts share pretrained initialization and backbone; accessible weights permit subspace computation. |
| Evidence boundary | Appendix D.1 limits the evidence to shared-backbone/shared-initialization models; heterogeneous architectures and initializations remain untested extensions. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d0da30e312b75a3fffd9e9191f8bc1b0-Abstract-Conference.html); [§3.1, PDF p.3; §4.1, PDF pp.5–6; Appendix D.1, PDF p.23](https://proceedings.iclr.cc/paper_files/paper/2026/file/d0da30e312b75a3fffd9e9191f8bc1b0-Paper-Conference.pdf) |

## On The Surprising Effectiveness of a Single Global Merging in Decentralized Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/437d9bde2999f6e3e854e09f250261a5-Abstract-Conference.html) |
| Problem | Decentralized local models may perform poorly on a shared global distribution under sparse communication and heterogeneous data. |
| Mechanism | Agents alternate local updates and gossip averaging; a global linear combination at the end can improve global-distribution performance even before local models reach consensus. The paper studies mergeability and conditions for the averaged DSGD iterate to match a parallel-SGD convergence rate. |
| Contribution | Separates model mergeability from full consensus and demonstrates a final-merge route to improved decentralized global performance. |
| Assumptions | Compatible parameter coordinates and enough nonzero peer communication; theoretical results assume smoothness, bounded noise/diversity, and additional sharpening/consensus conditions. |
| Evidence boundary | Single final merge does not mean one communication over the whole run: repeated gossip precedes it. Reported global-test gains are not client-level fairness guarantees, and conditional convergence analysis is not unconditional equivalence to centralized learning. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/437d9bde2999f6e3e854e09f250261a5-Abstract-Conference.html); [ICLR-labelled author v4, p.4 Algorithm 1 and §3.2; p.6 §§4.2–4.3; pp.7–8 §5](https://arxiv.org/pdf/2507.06542v4) |

## Unlocking the Potential of Continual Model Merging: An ODE Perspective

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v306/lin26o.html) · [Code](https://github.com/yohbii/ODE-M) |
| Problem | How can the degree of retention versus incoming expertise be controlled in a long merge sequence? |
| Mechanism | Calibration-loss gradients rectify a time-dependent velocity field; a utility-aware schedule selects the deployed operating point. |
| Contribution | Introduces feedback-controlled trajectories for continual model fusion. |
| Assumptions | A small representative calibration set, loss function, first-order gradients, and compatible models are available. |
| Evidence boundary | Fully black-box use is excluded; calibration coverage and numerical integration choices matter. The reported evaluation concerns vision classification streams. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v306/lin26o.html); [§3.1–3.3, PDF pp.3–5; Limitations, PDF p.19](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lin26o/lin26o.pdf) |

## Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d79b8c42f61b51722992705022134ef3-Abstract-Conference.html) · [Code](https://github.com/aimagelab/fed-mammoth) |
| Problem | How can parameter-efficient modules accumulate knowledge across clients and class-incremental tasks? |
| Mechanism | LoRM alternately freezes a shared LoRA factor and merges the other using regression statistics, supporting federated and incremental aggregation. |
| Contribution | Connects parameter-efficient fusion with federated continual learning. |
| Assumptions | Clients share pretrained weights and architecture; local feature statistics are communicated. |
| Evidence boundary | The solution depends on the prescribed alternating-factor training protocol and shared architecture; it is not arbitrary post-hoc merging of independently trained LoRA modules. Communication of statistics is not a formal privacy guarantee. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d79b8c42f61b51722992705022134ef3-Abstract-Conference.html); [§3.1–3.3, PDF pp.3–6; §4.1 evaluation setting, PDF p.6](https://proceedings.iclr.cc/paper_files/paper/2025/file/d79b8c42f61b51722992705022134ef3-Paper-Conference.pdf) |

## Continual Model Merging without Data: Dual Projections for Balancing Stability and Plasticity

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/37d9f19150fce07bced2a81fc87d47a6-Abstract-Conference.html) |
| Problem | How can data-free continual merging balance retention of old tasks with acquisition of new tasks? |
| Mechanism | DOP approximates relevant data subspaces from parameter differences and combines conflicting objectives using multi-gradient descent. |
| Contribution | Explicitly separates the two sides of the continual-merging objective. |
| Assumptions | Sequential compatible expert weights and a shared parameter representation are available without task data. |
| Evidence boundary | Appendix A limits validation to vision and language models and identifies larger multimodal models and limited-data variants as open settings. |
| Evidence | [Official publication metadata and abstract](https://papers.nips.cc/paper_files/paper/2025/hash/37d9f19150fce07bced2a81fc87d47a6-Abstract-Conference.html); [§3–4 method; Appendix A Limitations, PDF p.23](https://proceedings.neurips.cc/paper_files/paper/2025/file/37d9f19150fce07bced2a81fc87d47a6-Paper-Conference.pdf) |

## Evolutionary optimization of model merging recipes

| Field | Details |
| --- | --- |
| Venue / year | Nature Machine Intelligence, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.nature.com/articles/s42256-024-00975-8) · [Code](https://github.com/SakanaAI/evolutionary-model-merge) |
| Problem | How can effective model combinations be found without manually choosing a merging recipe? |
| Mechanism | Evolutionary optimization evaluates candidate weight mixtures and layer paths against task fitness. |
| Contribution | Demonstrates automated cross-capability composition in language and vision-language models. |
| Assumptions | Compatible source components and an evaluation dataset are available; fitness evaluation consumes compute. |
| Evidence boundary | The authors report inherited source-model limitations, incoherent responses, and no instruction-alignment stage. Offline evolutionary search is not evidence of deployed lifelong adaptation. |
| Evidence | [Official publication metadata and abstract](https://www.nature.com/articles/s42256-024-00975-8); [Parameter-space/data-flow sections, PDF pp.2–5; Limitations, PDF pp.6–7; Methods](https://www.nature.com/articles/s42256-024-00975-8.pdf) |

## GraphRouter: A Graph-based Router for LLM Selections

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html) · [Code](https://github.com/ulab-uiuc/GraphRouter) |
| Problem | How can routing exploit past interactions while accommodating new candidate LLMs? |
| Mechanism | Graph learning predicts query-model edges using historical performance and cost information. |
| Contribution | Uses explicit external model relationships for inductive routing, including newly introduced models. |
| Assumptions | Model descriptions and historical interaction data are available. |
| Evidence boundary | The experiments cover four open-domain QA datasets. Richer path signals and simultaneous multi-agent model selection are future work, not implemented collaboration-topology guarantees. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html); [§3, PDF pp.3–5; §6 Conclusion/Limitations/Future Work, PDF p.10](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf) |

## How to Merge Your Multimodal Models Over Time?

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.html) |
| Problem | How should multimodal expert models be initialized and deployed as tasks arrive sequentially? |
| Mechanism | TIME compares these axes and derives the Best-in-TIME strategy on the FoMo-in-Flux benchmark. |
| Contribution | Shows that the temporal use of merging matters alongside the merging operator. |
| Assumptions | Successive expert training and compatible pretrained multimodal models are available. |
| Evidence boundary | The reported conclusions are conditioned on FoMo-in-Flux and the evaluated multimodal models; they do not constitute a universal ordering of strategies under arbitrary task streams. |
| Evidence | [Official publication metadata and abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.html); [§3 framework, PDF pp.3–4; §4 experiments; §5 Conclusion, PDF p.8](https://openaccess.thecvf.com/content/CVPR2025/papers/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.pdf) |

## Merging on the Fly Without Retraining: A Sequential Approach to Scalable Continual Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/7611a3cb5d733e628081431445cb01fd-Abstract-Conference.html) · [Code](https://github.com/tanganke/opcm) |
| Problem | How can a growing sequence of expert models be integrated without revisiting all previous models? |
| Mechanism | OPCM identifies weight subspaces with SVD and projects incoming updates to reduce interference. |
| Contribution | Formulates scalable continual merging rather than simultaneous batch merging. |
| Assumptions | Model weights occupy compatible parameter spaces; experts arrive sequentially and merging uses no retraining data. |
| Evidence boundary | Sequential merging is noncommutative and task order affects outcomes; SVD adds computational cost. Data-free operation does not itself guarantee privacy or retain every capability. |
| Evidence | [Official publication metadata and abstract](https://papers.nips.cc/paper_files/paper/2025/hash/7611a3cb5d733e628081431445cb01fd-Abstract-Conference.html); [§3.2–3.3; Appendix B complexity; limitations checklist, PDF p.17](https://proceedings.neurips.cc/paper_files/paper/2025/file/7611a3cb5d733e628081431445cb01fd-Paper-Conference.pdf) |

## REMEDY: Recipe Merging Dynamics in Large Vision-Language Models

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4065a881baab1744bfba208a4361bbb1-Abstract-Conference.html) |
| Problem | How can task-tuned vision-language models be combined without treating all components identically? |
| Mechanism | A modality-aware allocator generates fusion coefficients at the start of each forward pass. |
| Contribution | Provides dynamic modular fusion for seen and unseen multimodal tasks. |
| Assumptions | Compatible pretrained components and data for seen-task recipe/allocator training are available. |
| Evidence boundary | Only designated recipe components are merged; remaining weights stay pretrained. Dynamic input conditioning does not demonstrate continual retention or collaboration-history learning. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4065a881baab1744bfba208a4361bbb1-Abstract-Conference.html); [§3.1–3.3, PDF pp.4–6; §4 evaluation setup](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf) |

## RouteLLM: Learning to Route LLMs from Preference Data

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=8sSqNntaMr) · [Code](https://github.com/lm-sys/RouteLLM) |
| Problem | How can inference requests be routed between stronger and cheaper language models? |
| Mechanism | Human preference data and augmented comparisons train several routing models; a threshold controls the cost-quality tradeoff. |
| Contribution | Connects preference-based model assessment to query-dependent selection. |
| Assumptions | Preference data and a specified model pair are available; generalization to replacement pairs is evaluated. |
| Evidence boundary | The central formulation is binary and training is offline. Dynamic inference selection and transfer to new pairs do not establish continuous policy learning or long-horizon recovery. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=8sSqNntaMr); [§3.1, PDF p.3; §4, PDF pp.4–6; §5.3–5.4](https://arxiv.org/pdf/2406.18665); [Final conference bibliographic record](https://dblp.org/rec/conf/iclr/OngAWC0GKS25.html) |

## DIMAT: Decentralized Iterative Merging-And-Training for Deep Learning Models

| Field | Details |
| --- | --- |
| Venue / year | IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Saadati_DIMAT_Decentralized_Iterative_Merging-And-Training_for_Deep_Learning_Models_CVPR_2024_paper.html) |
| Problem | Decentralized parameter averaging can combine misaligned neurons and converge slowly under heterogeneous data. |
| Mechanism | Activation matching produces layerwise permutation matrices by a linear assignment problem; neighbors are aligned before weighted combination, and the procedure interleaves these merge steps with local SGD or adaptive optimization. |
| Contribution | Treats alignment and merging as a recurring operation in decentralized collaborative training. |
| Assumptions | Compatible model layers, data for activation matching and local optimization, and a connected communication graph; convergence analysis assumes smoothness, bounded stochastic/heterogeneity terms and a spectral condition on the combined mixing/permutation operator. |
| Evidence boundary | The graph and spectral assumptions limit the convergence claim. Access to activations and model parameters is not a privacy protocol, and repeated merging is not evidence of autonomous long-term trustworthy evolution. |
| Evidence | [Official publication metadata and abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Saadati_DIMAT_Decentralized_Iterative_Merging-And-Training_for_Deep_Learning_Models_CVPR_2024_paper.html); [Final CVPR PDF pp.3–5 (printed pp.27519–27521), Sections 3–4.1 and Algorithm 1: graph assumptions, activation matching, iterative mixing and local training](https://openaccess.thecvf.com/content/CVPR2024/papers/Saadati_DIMAT_Decentralized_Iterative_Merging-And-Training_for_Deep_Learning_Models_CVPR_2024_paper.pdf) |

## FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

| Field | Details |
| --- | --- |
| Venue / year | Transactions on Machine Learning Research, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=cSimKw5p6R) · [Code](https://github.com/stanford-futuredata/FrugalGPT) |
| Problem | How can multiple language-model services satisfy a cost budget while maintaining task performance? |
| Mechanism | Small scoring models estimate answer quality and optimize a cascade of LLM calls. |
| Contribution | Demonstrates cost-aware cooperative inference across heterogeneous LLM services. |
| Assumptions | Task-specific examples, candidate-model outputs, and cost information are available. |
| Evidence boundary | The discussion leaves latency, fairness, environmental costs, and uncertainty quantification open. A fitted cascade is not by itself a lifelong collaboration policy. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=cSimKw5p6R); [§4, PDF pp.5–8; §6 Discussions and Future Prospects, PDF p.12](https://lingjiaochen.com/papers/2024_FrugalGPT_TMLR.pdf) |

## Towards Making Learnware Specification and Market Evolvable

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the AAAI Conference on Artificial Intelligence, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29298) |
| Problem | How can model characterization and identification improve as a repository grows? |
| Mechanism | ELSI estimates model losses on anchor specifications, indexes these estimates with a tree and hash table, and refines them during user interactions. |
| Contribution | Implements evolving external capability descriptions and efficient retrieval from a growing model collection. |
| Assumptions | Submitted models perform well on their own tasks and supply informative reduced kernel mean embeddings. |
| Evidence boundary | The formulation evaluates single-model identification; multi-model extension is left for future work. Teacher outputs on anchor specifications serve as approximate truth, so their quality is a substantive assumption. |
| Evidence | [Official publication metadata and abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29298); [§3, PDF p.3; §4.1–4.3, PDF pp.3–6; §5.1](https://ojs.aaai.org/index.php/AAAI/article/download/29298/30448); [Final nine-page paper, author-hosted copy](https://www.lamda.nju.edu.cn/publication/aaai24liu.pdf) |

## Twin-Merging: Dynamic Integration of Modular Expertise in Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8fcd17eb91bae20d9826786d7d6be799-Abstract-Conference.html) · [Code](https://github.com/LZY-the-boys/Twin-Merging) |
| Problem | How can merging preserve specialized expertise under heterogeneous input distributions? |
| Mechanism | A trained router combines the shared model with SVD-compressed residual experts for each input. |
| Contribution | Connects modular knowledge representation with input-dependent weight composition. |
| Assumptions | Experts share pretrained initialization and architecture; router training and retained residual modules are required. |
| Evidence boundary | Appendix F retains the common-architecture restriction and incomplete theoretical understanding. Conditional inference is demonstrated; long-term feedback-driven evolution is not. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8fcd17eb91bae20d9826786d7d6be799-Abstract-Conference.html); [§3.3 and Algorithm 1, PDF pp.5–6; Appendix F Limitations, PDF p.24](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fcd17eb91bae20d9826786d7d6be799-Paper-Conference.pdf) |

## Defending Unauthorized Model Merging via Dual-Stage Weight Protection

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html) |
| Problem | Released task models can be incorporated into unauthorized parameter merges. |
| Mechanism | Use density-aware fine-tuning followed by selective adversarial weight negation. |
| Contribution | Studies proactive technical restrictions on downstream merging and evaluates utility/protection tradeoffs. |
| Assumptions | The defender controls its own checkpoint and task data; the considered merging setup uses a common pretrained origin. |
| Evidence boundary | This is usage protection through disrupted mergeability, not a provenance certificate or general safety guarantee. Applicability depends on compatible parameter-space merges and evaluated adaptive attacks. |
| Evidence | [Official publication metadata and abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html); [PDF pp.3–4 §§4–5: threat model and two-stage defense](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.pdf) |

## Defending against Backdoor Attacks via Module Switching

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbe25fa0e7c7084049276888a09acc8d-Abstract-Conference.html) · [Code](https://github.com/weijun-l/module-switching-defense) |
| Problem | Backdoor repair can require too many related models or strong trusted resources. |
| Mechanism | Search module-switching combinations and select candidates using representation criteria. |
| Contribution | Studies module recombination against backdoor shortcuts, including evaluated collusive cases. |
| Assumptions | Structurally compatible models and a small clean validation set for candidate selection. |
| Evidence boundary | Architecture compatibility and validation availability constrain use; evolutionary search here is not proof of continual collaborative learning. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbe25fa0e7c7084049276888a09acc8d-Abstract-Conference.html); [PDF pp.1–3: design and setup](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbe25fa0e7c7084049276888a09acc8d-Paper-Conference.pdf) |

## Differentially Private Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2026 |
| Publication status | Accepted; proceedings pending |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://neurips.cc/virtual/2026/poster/149241) |
| Problem | Deployment privacy targets may change after several private models have already been trained. |
| Mechanism | Use Rényi-DP and privacy-loss-distribution accounting to select mixture coefficients; linear-combination analysis exploits training-mechanism structure. |
| Contribution | Analyzes privacy-adaptive reuse of existing models and establishes a mechanism-agnostic limitation. |
| Assumptions | Models are trained on the same dataset; privacy profiles or training algorithms are known. Linear combinations require additional structural assumptions. |
| Evidence boundary | The superiority of linear combination is characterized for a Gaussian mean-estimation case, not arbitrary learning problems. Stronger accounting needs mechanism metadata; conference acceptance is verified but final proceedings were not retrieved. |
| Evidence | [Official publication metadata and abstract](https://arxiv.org/abs/2604.20985); [Author PDF pp.3–4 §§3–4: problem formulation, no-free-lunch result, random selection and linear combination](https://arxiv.org/pdf/2604.20985); [Official NeurIPS 2026 poster listing, authors and abstract; scheduled 2026-12-10](https://neurips.cc/virtual/2026/poster/149241) |

## FairMerging: Rethinking Model Merging through the Lens of Fairness

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v306/liu26dl.html) |
| Problem | Merging can increase disparities between class-wise losses even when average accuracy remains useful. |
| Mechanism | Fine-tune the target checkpoint with sensitivity regularization, orthogonalize task vectors, and optimize entropy plus a fairness penalty. |
| Contribution | Connects parameter displacement and subgroup sensitivity to a merging disparity bound and evaluates a two-stage mitigation. |
| Assumptions | Compatible checkpoints from a shared pretrained model; labeled target data and subgroup annotations; unlabeled inputs from all tasks. |
| Evidence boundary | The paper defines subgroups by class labels; this does not establish general demographic fairness. Additional fine-tuning/data are required, and fairness gains trade off against the strongest accuracy baseline. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v306/liu26dl.html); [PDF pp.3–4 §3: class-defined subgroups and excessive-loss metric; pp.6–8 §§5–6: optimization, data requirements and results](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26dl/liu26dl.pdf) |

## Making Open-Source Text LLM Watermarks Durable Against Merging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2026 |
| Publication status | Accepted; proceedings pending |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://neurips.cc/virtual/2026/poster/155690) |
| Problem | Text watermarks embedded in open weights can disappear when downstream users merge checkpoints. |
| Mechanism | Backpropagate watermark-distillation objectives through a merge with an unwatermarked base checkpoint. |
| Contribution | Evaluates watermark survival under realistic merge scenarios and repeated modification chains. |
| Assumptions | Provider control over watermark training and an unwatermarked reference; downstream users can modify released weights. |
| Evidence boundary | Tested merge algorithms and chain depth are limited; adaptive/evolutionary merging and broader watermark families remain open. Acceptance is verified, but final proceedings were not retrieved. |
| Evidence | [Official publication metadata and abstract](https://arxiv.org/abs/2607.20435); [Author PDF p.3 §3.1: merge-adversarial watermark distillation; p.9 §5: limits](https://arxiv.org/pdf/2607.20435); [Official NeurIPS 2026 poster listing, authors and abstract; scheduled 2026-12-09](https://neurips.cc/virtual/2026/poster/155690) |

## SafeMERGE: Preserving Safety Alignment in Fine-Tuned Large Language Models via Selective Layer-Wise Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: ACL 2026, 2026 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2026.findings-acl.1761/) |
| Problem | Benign task fine-tuning can degrade a language model’s safety alignment. |
| Mechanism | Selectively merge layers with a safety-aligned model using activation/subspace similarity. |
| Contribution | Provides a post-fine-tuning route to recovering alignment while retaining task utility. |
| Assumptions | A compatible safety-aligned reference and safety data for preparing that reference. |
| Evidence boundary | Authors explicitly separate direct harmful prompts from jailbreak attacks; evaluation and reference-model quality limit generalization. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2026.findings-acl.1761/); [PDF p.2 Section 2; p.6 Limitations](https://aclanthology.org/2026.findings-acl.1761.pdf) |

## When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2026 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2608.26655) |
| Problem | Differentially private task fine-tuning can reduce compatibility between checkpoints. |
| Mechanism | Combine a DP-compatible sharpness-aware training objective with reference regularization before post-processing released task models. |
| Contribution | Studies the interaction between privacy noise and mergeability using a merge-gap bound and vision/language experiments. |
| Assumptions | A public pretrained model, compatible task parameters and private examples assigned to only one task for the stated parallel-composition argument. |
| Evidence boundary | Preprint. It modifies private fine-tuning rather than repairing arbitrary released assets; the no-extra-loss statement relies on the specified disjoint-task composition and post-processing setup. |
| Evidence | [Official publication metadata and abstract](https://arxiv.org/abs/2608.26655); [PDF pp.3–4 §3: private task setup, disjoint-record composition and merge-gap geometry](https://arxiv.org/pdf/2608.26655) |

## A Unified Approach to Routing and Cascading for LLMs

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v267/dekoninck25a.html) |
| Problem | Selecting and sequencing heterogeneous LLMs requires balancing answer quality against a cost budget. |
| Mechanism | Construct policies over candidate model sequences using ex-ante and post-hoc quality/cost estimates. |
| Contribution | Derives conditional optimality results and identifies estimation quality as the key determinant of effective orchestration. |
| Assumptions | Available model pool, query distribution, validation data and quality/cost estimators; optimization targets expected cost. |
| Evidence boundary | Optimality is with respect to estimated quantities and the stated model; it does not guarantee true answer quality under estimator shift or a hard per-query safety constraint. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v267/dekoninck25a.html); [PDF pp.3–5 §§2–4: expected-cost constraint, quality estimators and unified routing/cascading policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf) |

## An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 39th Pacific Asia Conference on Language, Information and Computation, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.paclic-1.24/) |
| Problem | Bias reduction through weight editing can degrade other language capabilities. |
| Mechanism | Derive a bias task vector from continued pretraining, negate it, and evaluate seven merging rules across 13 models. |
| Contribution | Provides primary comparative experiments on social-bias/utility tradeoffs despite the word Survey in its title. |
| Assumptions | Compatible model variants and a stereotypical training corpus; benchmark operationalizations of social bias and downstream utility. |
| Evidence boundary | Results depend on the evaluated bias construction, models and metrics; the authors note the US-centric stereotype source. Reduced benchmark bias is not comprehensive social fairness. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.paclic-1.24/); [PDF p.3 §3: bias-vector construction and merging; p.8 §6 and Ethics Statement: tradeoffs and scope](https://aclanthology.org/2025.paclic-1.24.pdf) |

## Be Cautious When Merging Unfamiliar LLMs: A Phishing Model Capable of Stealing Privacy

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: ACL 2025, 2025 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.findings-acl.713/) |
| Problem | An untrusted source model can increase private-data leakage from another component after merging. |
| Mechanism | Evaluate PII extraction and membership inference after merging a crafted source model into a victim-derived model. |
| Contribution | Demonstrates a model-supply-chain privacy failure specific to parameter merging. |
| Assumptions | The attacker supplies a source model and can query the merged model; auxiliary private data are required in the evaluated construction. |
| Evidence boundary | Extraction and membership attacks are trained separately; the paper proposes no corresponding defense. Its auxiliary-data and query assumptions bound the threat evidence. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.findings-acl.713/); [PDF p.3 §§3–4: merging-specific threat model; p.9 Limitations](https://aclanthology.org/2025.findings-acl.713.pdf) |

## From Purity to Peril: Backdooring Merged Models From "Harmless" Benign Components

| Field | Details |
| --- | --- |
| Venue / year | 34th USENIX Security Symposium (USENIX Security 25), 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin) · [Code](https://github.com/wljLlla/MergeBackdoor) |
| Problem | Individually inconspicuous models may become malicious after composition. |
| Mechanism | Train components to suppress pre-merge trigger behavior while exposing it after merging. |
| Contribution | Exposes a compositional supply-chain threat that component-level testing can miss. |
| Assumptions | Adversarial influence over multiple upstream components and the evaluated merging setup. |
| Evidence boundary | Evaluated model families and attacker settings bound the findings; not every possible merger is shown vulnerable. |
| Evidence | [Official publication metadata and abstract](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin); [PDF p.2 abstract; pp.9,13: scope and detection discussion](https://www.usenix.org/system/files/usenixsecurity25-wang-lijin.pdf) |

## LED-Merging: Mitigating Safety-Utility Conflicts in Model Merging with Location-Election-Disjoint

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.acl-long.1055/) · [Code](https://github.com/MqLeet/LED-Merging) |
| Problem | Task expertise and safety behavior can interfere when merging related LLMs. |
| Mechanism | Attribute task-relevant neurons, select important updates, and isolate conflicting parameters. |
| Contribution | Studies parameter selection for balancing safety and task performance. |
| Assumptions | Homologous models and task-related attribution/selection information. |
| Evidence boundary | Cross-family architectures and broader multilingual transfer remain outside the established core evidence. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.acl-long.1055/); [PDF pp.1–5 method and setup; p.10 Section 6](https://aclanthology.org/2025.acl-long.1055.pdf) |

## MAP: Low-compute Model Merging with Amortized Pareto Fronts via Quadratic Approximation

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3724221b623bf1966e92cd266ac6177-Abstract-Conference.html) |
| Problem | Repeatedly evaluating candidate merges makes multi-task trade-off search expensive. |
| Mechanism | Fit quadratic surrogates from sampled merge coefficients and observed task metrics, then search their Pareto front; Bayesian and nested variants reduce evaluation cost. |
| Contribution | Provides a family of coefficient choices rather than optimizing only average task accuracy. |
| Assumptions | Compatible task vectors around a shared reference; access to task evaluations; local approximation assumes sufficiently small parameter changes and smooth metric behavior. |
| Evidence boundary | Surrogate error can shift the true frontier; metric evaluations remain data-dependent. Task trade-offs alone do not establish privacy or group fairness. |
| Evidence | [Official proceedings metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3724221b623bf1966e92cd266ac6177-Abstract-Conference.html); [Final PDF pp.2–5, Figure 1 and §§2–3.1; Assumption 1 and surrogate fitting](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3724221b623bf1966e92cd266ac6177-Paper-Conference.pdf) |

## MergePrint: Merge-Resistant Fingerprints for Robust Black-box Ownership Verification of Large Language Models

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.acl-long.342/) |
| Problem | Black-box ownership fingerprints may be diluted by parameter merging. |
| Mechanism | Pre-optimize fingerprint inputs and train the owner model through a pseudo-merged checkpoint before output-only verification. |
| Contribution | Designs merge-resistant black-box verification and evaluates modification resistance and false-claim controls. |
| Assumptions | Compatible experts sharing a base, owner control over embedding and a secret input-output fingerprint. |
| Evidence boundary | Authors exclude knowledge-distillation theft and MoE scenarios from established coverage. Detection of an embedded signal is not a full contribution decomposition or legal ownership ruling. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.acl-long.342/); [PDF pp.3–4 §§3–5: threat model and pseudo-merge objective; p.9 §8 Limitations](https://aclanthology.org/2025.acl-long.342.pdf) |

## Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Conference on Empirical Methods in Natural Language Processing, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.emnlp-main.295/) · [Code](https://github.com/My-avenge/Merger-as-a-Stealer) |
| Problem | Malicious merger participation can expose memorized PII after fusion. |
| Mechanism | Merge a harmful-finetuned compatible model with an aligned victim, then evaluate targeted extraction. |
| Contribution | A merging-specific privacy attack distinct from PhiMM. |
| Assumptions | Attacker knows target names and base weights/architecture, supplies a source and queries the merged API; victim weights/data remain unavailable. |
| Evidence boundary | Victims are deliberately trained for memorization then aligned; outcomes depend on merging weights. This is neither a universal leakage claim nor a defense guarantee. |
| Evidence | [Official publication metadata](https://aclanthology.org/2025.emnlp-main.295/); [§§3.1–3.2, PDF p.3: merging formulation and capabilities; §4, PDF p.4: attack interface; §5.1, PDF pp.4–6: constructed victims and model sizes; Limitations, PDF p.9](https://aclanthology.org/2025.emnlp-main.295.pdf) |

## Mitigating the Backdoor Effect for Multi-Task Model Merging via Safety-Aware Subspace

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36f7c3d80c1ba329ab8cf7b96e63a0fa-Abstract-Conference.html) |
| Problem | Multi-task merging can inherit and transfer backdoors alongside task knowledge. |
| Mechanism | Optimize task-shared and backdoor-detection masks to identify a safer parameter subspace. |
| Contribution | Incorporates backdoor concerns directly into the merging procedure. |
| Assumptions | Compatible fine-tuned task vectors; the reviewed evaluation uses CLIP vision encoders. |
| Evidence boundary | Evidence is conditional on the evaluated attacks and model families; it is not a universal security certificate. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36f7c3d80c1ba329ab8cf7b96e63a0fa-Abstract-Conference.html); [PDF pp.2–3: succession/transfer and design; p.8 Section 4.1](https://proceedings.iclr.cc/paper_files/paper/2025/file/36f7c3d80c1ba329ab8cf7b96e63a0fa-Paper-Conference.pdf) |

## Mix Data or Merge Models? Balancing the Helpfulness, Honesty, and Harmlessness of Large Language Model via Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3948805bc5220206f5bfc465de0b1b7-Abstract-Conference.html) |
| Problem | Helpfulness, honesty and harmlessness can compete during alignment. |
| Mechanism | Combine separately aligned models through a merging approach targeting a balanced outcome. |
| Contribution | Studies model merging as an alternative to mixing alignment data. |
| Assumptions | Assumptions beyond the official abstract have not yet been extracted. |
| Evidence boundary | Abstract-only technical review; comparative numerical claims are not transcribed. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3948805bc5220206f5bfc465de0b1b7-Abstract-Conference.html) |

## Pareto Merging: Multi-Objective Optimization for Preference-Aware Model Merging

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v267/chen25af.html) |
| Problem | One merged checkpoint can conceal competing task preferences. |
| Mechanism | Combine a preference-independent merged base with a low-rank tensor component conditioned on task preferences; formulate parameter-distance or prediction-entropy objectives. |
| Contribution | Constructs multiple trade-offs from one learned parameter-efficient structure. |
| Assumptions | Models fine-tuned from a common base; the entropy-based setting uses unlabeled task inputs, while a separate parameter-distance setting does not. |
| Evidence boundary | Parameter distance and entropy are surrogate objectives, not guarantees of true task Pareto optimality, calibrated prediction or demographic fairness; model-family learning has optimization cost. |
| Evidence | [Official proceedings metadata and abstract](https://proceedings.mlr.press/v267/chen25af.html); [Final PDF pp.2–4, §§2.1 and 3.1–3.2; data-free versus unlabeled-data settings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25af/chen25af.pdf) |

## Personalized Language Models via Privacy-Preserving Evolutionary Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.emnlp-main.1747/) |
| Problem | Personalized merging may expose information about users who contributed adapters. |
| Mechanism | Select nearby user LoRAs and use evolutionary optimization of task utility minus similarity to sharing users. |
| Contribution | Integrates a task-dependent privacy surrogate into personalized model merging and evaluates the resulting utility–attack-risk tradeoff. |
| Assumptions | Consenting adapter donors, compatible LoRAs, user embeddings and target-user history; evaluated black-box membership inference threat. |
| Evidence boundary | The authors explicitly state that membership-inference mitigation is empirical and provides no formal privacy guarantee; larger-scale generalization remains open. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.emnlp-main.1747/); [PDF pp.3–4 §§2–3: LoRA selection, privacy objective and threat model; p.9 Limitations](https://aclanthology.org/2025.emnlp-main.1747.pdf) |

## RouteMark: A Fingerprint for Intellectual Property Attribution in Routing-based Model Merging

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2025 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2508.01784) |
| Problem | A merged expert system obscures which source experts have been reused or modified. |
| Mechanism | Probe reference and suspect merged systems and match expert-specific routing statistics. |
| Contribution | Provides expert-level attribution and tampering detection for routing-based model merging. |
| Assumptions | Access to routing observations on fixed probes and suitable reference experts; evaluated task-vector MoE and CLIP-based architecture. |
| Evidence boundary | Preprint. Evidence concerns specific routing interfaces and tampering operations; it does not establish cryptographic provenance, legal ownership or arbitrary black-box attribution. |
| Evidence | [Official publication metadata and abstract](https://arxiv.org/abs/2508.01784); [PDF pp.2–3 §§1–3: fingerprint definitions, routing architecture and tampering model](https://arxiv.org/pdf/2508.01784) |

## SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.emnlp-main.531/) |
| Problem | Small-to-large model delegation can waste tokens and delay responses when the small model should abstain. |
| Mechanism | Combine shortest-correct-response preference learning with refusal supervision and confidence-based routing/cascading. |
| Contribution | Integrates response generation and abstention to improve evaluated cost–quality tradeoffs. |
| Assumptions | Training responses with correctness signals and a small/large model pair; evaluations use output-token count as a latency proxy. |
| Evidence boundary | Evidence is mainly for one small and one large model. Token latency is a proxy, low thresholds are challenging, and mandatory-response settings without fallback remain problematic. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.emnlp-main.531/); [PDF p.4 §3: concise-response preference and refusal training; p.9 Limitation](https://aclanthology.org/2025.emnlp-main.531.pdf) |

## BadMerging: Backdoor Attacks Against Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://doi.org/10.1145/3658644.3690284) |
| Problem | A malicious contributed model can compromise merged task behavior. |
| Mechanism | Train a backdoor using a merging-aware, feature-interpolation objective. |
| Contribution | A malicious contributed model can compromise merged task behavior. |
| Assumptions | Not yet fully extracted in this pass. |
| Evidence boundary | Author-version abstract reviewed; final publication metadata is confirmed by Crossref; full threat-model extraction remains pending. |
| Evidence | [Publisher-deposited bibliographic metadata](https://api.crossref.org/works/10.1145/3658644.3690284); [Abstract](https://arxiv.org/abs/2408.07362) |

## Complementary Knowledge Distillation for Robust and Privacy-Preserving Model Serving in Vertical Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the AAAI Conference on Artificial Intelligence, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29958) |
| Problem | Vertical federated model serving must transfer knowledge despite incomplete alignment and stragglers without revealing active-party labels. |
| Mechanism | Complementary label coding guides transfers from passive models to the active model and among passive models. |
| Contribution | Proposes a cross-party knowledge-transfer framework and reports four-dataset robustness and label-leakage evaluations. |
| Assumptions | Active/passive vertical federation with complementary features and partially overlapping sample identities. |
| Evidence boundary | Abstract-level review only. The precise leakage guarantee, threat assumptions and full experimental limitations remain to be extracted; no formal DP claim is made here. |
| Evidence | [Official indexed article metadata and abstract; direct page returned an access-verification response.](https://ojs.aaai.org/index.php/AAAI/article/view/29958); [Official AAAI-24 main-track acceptance list, paper 9635](https://aaai.org/wp-content/uploads/2024/02/AAAI-24_Main_2024-02-01.pdf); [Author publication list confirms title, authors and AAAI 2024](https://dashangao.github.io/) |

## DapperFL: Domain Adaptive Federated Learning with Model Fusion Pruning for Edge Devices

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/17a1a1439421f1837e10cd612bf92861-Abstract-Conference.html) · [Code](https://github.com/jyzgh/DapperFL) |
| Problem | Resource-constrained clients have unequal model capacity while data domains differ. |
| Mechanism | Each round mixes a briefly fine-tuned local model with the global model using a decaying coefficient, prunes channels to the device budget, and trains with a representation-norm penalty. The server restores missing coordinates from the previous global model before aggregation. |
| Contribution | Couples fusion, resource-aware pruning and domain-adaptive local optimization within repeated federated rounds. |
| Assumptions | A common backbone with identifiable channel masks, local data for adaptation, and client capacity/pruning-rate information available to the server. |
| Evidence boundary | The masked shared-backbone construction does not establish fusion of arbitrary unrelated architectures. Performance under evaluated domain shifts does not imply universal robustness, and local data retention is not formal privacy protection. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/17a1a1439421f1837e10cd612bf92861-Abstract-Conference.html); [Final proceedings PDF pp.3–6, Sections 3.1–3.4 and Algorithm 1: fusion schedule, pruning, domain regularization and masked-model restoration](https://proceedings.neurips.cc/paper_files/paper/2024/file/17a1a1439421f1837e10cd612bf92861-Paper-Conference.pdf) |

## FedDRL: Trustworthy Federated Learning Model Fusion Method Based on Staged Reinforcement Learning

| Field | Details |
| --- | --- |
| Venue / year | Computing and Informatics, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.cai.sk/ojs/index.php/cai/article/view/2024_1_1) |
| Problem | How to select reliable models and assign quality-sensitive fusion weights? |
| Mechanism | A2C selects clients; TD3 outputs positive coefficients summing to one. Section 3.2.2 Eq. (15) fuses client parameters; Eqs. (16)–(18) use model accuracy and server validation rewards to learn coefficients. |
| Contribution | Joint selection and learned source-model weighting for global fusion. |
| Assumptions | Server-held labeled validation data, individual model access and compatible parameter tensors. |
| Evidence boundary | Reward data representativeness and RL cost constrain use; evaluated attacks do not establish universal trustworthiness. |
| Evidence | [Author/publication metadata](https://www.cai.sk/ojs/index.php/cai/article/view/2024_1_1); [PDF pp.7–13, Sections 3.2.1–3.2.2, Eqs. (14)–(18); pp.16–19, Algorithm 3 and model/agent setup](https://www.cai.sk/ojs/index.php/cai/article/download/2024_1_1/1271/19580) |

## Have You Merged My Model? On The Robustness of Large Language Model IP Protection Methods Against Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the 1st ACM Workshop on Large AI Systems and Models with Privacy and Safety Analysis, 2024 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1145/3689217.3690614) · [Code](https://github.com/ThuCCSLab/MergeGuard) |
| Problem | Model modification can erase ownership signals embedded in upstream LLMs. |
| Mechanism | Compare quantization watermarking and instructional fingerprints over multiple parameter-merging rules and blending ratios. |
| Contribution | Supplies direct evidence that merging belongs in the robustness evaluation of model ownership methods. |
| Assumptions | Compatible LLM pairs and the selected ownership methods; experiments focus on two-model merges. |
| Evidence boundary | Workshop study with a limited method/model-pair scope; survival of tested fingerprints is not a universal provenance guarantee. Crossref print-year metadata conflict is resolved using the accepted PDF. |
| Evidence | [Official publication metadata and abstract](https://doi.org/10.1145/3689217.3690614); [Author accepted PDF p.1: formal workshop citation; p.3 §3.1: two-model merging setup](https://arxiv.org/pdf/2404.05188) |

## Here’s a Free Lunch: Sanitizing Backdoored Models with Model Merge

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: ACL 2024, 2024 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://aclanthology.org/2024.findings-acl.894/) |
| Problem | Backdoored models require repair when original training resources are unavailable. |
| Mechanism | Merge a compromised model with homogeneous auxiliary models. |
| Contribution | Studies merging as a means of suppressing backdoor behavior across evaluated NLP tasks. |
| Assumptions | Access to multiple compatible models. |
| Evidence boundary | Abstract-level review; observed mitigation is not a guarantee against colluding or merge-aware attackers. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2024.findings-acl.894/) |

## Model Merging and Safety Alignment: One Bad Model Spoils the Bunch

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: EMNLP 2024, 2024 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://aclanthology.org/2024.findings-emnlp.762/) |
| Problem | A misaligned expert can transmit unsafe behavior through model merging. |
| Mechanism | Generate safety/domain examples and incorporate alignment into data-aware merging. |
| Contribution | Demonstrates that task capability and misalignment can both transfer during merging. |
| Assumptions | At least one useful aligned source and access to generated alignment/domain evidence. |
| Evidence boundary | Abstract-level review here; detailed attack coverage and experimental limitations still require extraction. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2024.findings-emnlp.762/) |

## Model Trip: Enhancing Privacy and Fairness in Model Fusion Across Multi-Federations for Trustworthy Global Healthcare

| Field | Details |
| --- | --- |
| Venue / year | 2024 IEEE 40th International Conference on Data Engineering (ICDE), 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://doi.org/10.1109/icde60146.2024.00177) |
| Problem | Reuse federation-pretrained healthcare models across federations while addressing privacy, population shift, fairness, and data dependency. |
| Mechanism | Publisher/institutional abstract: cross-federation model fusion combined with multi-objective quantification and optimization. The detailed fusion operator, privacy mechanism, fairness objective, and optimization protocol were not verified from the full text. |
| Contribution | A privacy-and-fairness-oriented cross-federation model-fusion framework (FairFusion), evaluated according to the abstract on three public healthcare datasets across model structures and sensitive-attribute subgroups. |
| Assumptions | Cross-federation access to pretrained models is part of the stated setting. Precise trust, architecture compatibility, calibration-data, sensitive-attribute, and privacy-accounting assumptions remain pending full-text review. |
| Evidence boundary | Abstract reviewed only: neither exact datasets/splits, threat model, privacy guarantees, fairness definitions, quantitative results, nor deployed multi-institutional federation execution are verified. The coauthor-provided code URL https://github.com/beiyuouo/ModelTrip returned HTTP 404 on 2026-11-07; no usable public code or full-text link was established. |
| Evidence | [Publisher-deposited final title, 11 authors, ICDE 2024, pp.2231–2244, DOI; published-print 13 May 2024.](https://api.crossref.org/works/10.1109/icde60146.2024.00177); [IEEE abstract/metadata retrieved in search index; FairFusion, multi-objective privacy/utility/fairness; three public healthcare datasets; Date Added to IEEE Xplore 23 July 2024.](https://doi.org/10.1109/ICDE60146.2024.00177); [Institutional publication record and abstract; final title, authors, pages, DOI, method name, broad study scope.](https://researchportal.hkust.edu.hk/en/publications/model-trip-enhancing-privacy-and-fairness-in-model-fusion-across--2/); [Coauthor selected-publication entry: Model Trip/FairFusion; publisher Paper link and unavailable ModelTrip Code link.](https://www.bj-yan.top/) |

## PrivFusion: Privacy-Preserving Model Fusion via Decentralized Federated Graph Matching

| Field | Details |
| --- | --- |
| Venue / year | IEEE Transactions on Knowledge and Data Engineering, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1109/tkde.2024.3430819) |
| Problem | Fuse independently trained models while limiting disclosure of model activations and weights to other model owners. |
| Mechanism | Author preprint arXiv:2311.03396v1, Sections III–IV: represent neurons/channels as nodes and weights as edges; perturb activation features with Laplace noise and bounded weight features with a multi-bit mechanism; combine activation/weight affinities for graph matching; align neurons, apply Gaussian perturbation and smoothing, and average aligned weights. |
| Contribution | A decentralized privacy-aware graph-matching fusion procedure, with author-stated local-DP mechanisms and privacy–utility experiments on image tasks and a two-party healthcare construction. |
| Assumptions | Author preprint: honest-but-curious model owners; agreed tasks and compatible public architectures; aligned input/output neurons; a few inference examples to obtain activation features; bounded weight features and calibrated sensitivities/privacy budgets. The fusion stage avoids retraining but is not strictly data-free. |
| Evidence boundary | Content reviewed in arXiv:2311.03396v1 only; the final TKDE text was not accessed. Small-network evaluations and graph-matching memory cost limit scalability evidence. The healthcare data originate from 17 hospitals but the reported experiment groups 15 regions into two parties; this is not evidence of a live 17-hospital federation. Strong regional heterogeneity can degrade fusion substantially (preprint Table IV). Privacy unit, sensitivity calibration, approximate-DP delta, and composition across releases require explicit accounting before asserting end-to-end patient-level privacy. |
| Evidence | [Publisher-deposited final bibliographic metadata; TKDE 36(12), 9051–9064; published-print December 2024; 10 authors.](https://api.crossref.org/works/10.1109/tkde.2024.3430819); [Author preprint, submitted 5 November 2023; different title and 8 authors; uses the method name PrivFusion.](https://arxiv.org/abs/2311.03396v1); [Author-preprint PDF pp.4–8, Sections III–IV (threat model, assumptions, mechanisms); pp.8–13, Section V and Table IV (experimental setup and limitations).](https://arxiv.org/pdf/2311.03396v1); [Coauthor publication list identifies final PrivFusion and summarizes the same decentralized matching/local-DP/perturbation-filter components; this supports association, not exact version equivalence.](https://www.bj-yan.top/publications) |

## WARM: On the Benefits of Weight Averaged Reward Models

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v235/rame24a.html) |
| Problem | Reward models can fail under policy-induced shift and inconsistent preferences. |
| Mechanism | Average reward-model weights after diverse fine-tuning from shared initialization. |
| Contribution | Studies weight averaging as an efficient approach to reward reliability. |
| Assumptions | Compatible reward models and a common pretrained origin. |
| Evidence boundary | Shared systematic preference biases may persist; architecture/pretraining diversity and uncertainty access are narrower than prediction ensembles. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v235/rame24a.html); [PDF p.4 Section 3; p.9 limitations](https://raw.githubusercontent.com/mlresearch/v235/main/assets/rame24a/rame24a.pdf) |

## FedAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | IEEE Transactions on Neural Networks and Learning Systems, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1109/tnnls.2021.3129371) |
| Problem | Uniform prediction aggregation can perform poorly with heterogeneous federated clients. |
| Mechanism | Combine public-data self-supervised initialization with certainty-weighted ensemble distillation and privatized scoring classifiers. |
| Contribution | Provides a model-heterogeneous aggregation mechanism that separates private scoring from predictive knowledge transfer. |
| Assumptions | Public unlabeled auxiliary data available to clients/server and compatible prediction interfaces; heterogeneous client architectures are supported through distillation. |
| Evidence boundary | The DP analysis explicitly covers only the scoring mechanism; communicating client models adds a separate privacy cost. Formal journal metadata are verified, but section reading used the author preprint. |
| Evidence | [Official publication metadata and abstract](https://doi.org/10.1109/tnnls.2021.3129371); [Author preprint PDF pp.3–5 §3: auxiliary-data distillation, certainty weights and scoped privacy analysis](https://arxiv.org/pdf/2102.02514) |

## Revisiting Weighted Aggregation in Federated Learning with Neural Networks

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v202/li23s.html) |
| Problem | Conventional normalized client weights can miss beneficial shrinkage and interactions among client models. |
| Mechanism | Factor the aggregate into a positive global shrinking factor and simplex-constrained relative weights, and optimize them on proxy data before constructing the global model. Client coherence motivates the weighting analysis. |
| Contribution | Separates overall shrinkage from relative weighting and makes both part of federated aggregation optimization. |
| Assumptions | Aligned client parameterizations, continuing local training, and server-held proxy data for the aggregation objective. |
| Evidence boundary | Weight quality depends on the size and representativeness of the server proxy set. Client coherence is an optimization interaction rather than certified data contribution or demographic fairness; learned weighting supplies no formal privacy or Byzantine guarantee. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v202/li23s.html); [Final PMLR PDF pp.3–4, Sections 3–4.2: shrinkage and coherence; p.8, Section 6.1 and Algorithm 1: proxy-data optimization and FedLAW](https://proceedings.mlr.press/v202/li23s/li23s.pdf) |

## Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e12a3b98b67e8395f639fde4c2b03168-Abstract-Conference.html) |
| Problem | A single reward weighting cannot express diverse user preferences. |
| Mechanism | Fine-tune one policy per proxy reward from a shared initialization, then interpolate weights and select coefficients using validation rewards. |
| Contribution | Evaluates weight interpolation as a cheaper alternative to separately training policies for many scalarized rewards. |
| Assumptions | Compatible architecture and common pretrained initialization; training resources for reward specialists and samples for coefficient selection. |
| Evidence boundary | Linear connectivity and Pareto coverage are working hypotheses with restricted theoretical support; proxy-reward alignment is not demographic fairness or a universal safety guarantee. |
| Evidence | [Official proceedings metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e12a3b98b67e8395f639fde4c2b03168-Abstract-Conference.html); [Final PDF pp.2–4, Figure 1 and §§2.1–2.2; working hypotheses and training/selection phases](https://proceedings.neurips.cc/paper_files/paper/2023/file/e12a3b98b67e8395f639fde4c2b03168-Paper-Conference.pdf) |

## Cronus: Robust and Heterogeneous Collaborative Learning with Black-Box Knowledge Transfer

| Field | Details |
| --- | --- |
| Venue / year | NeurIPS Workshop on New Frontiers in Federated Learning: Privacy, Fairness, Robustness, Personalization and Data Ownership, 2021 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://neurips2021workshopfl.github.io/NFFL-2021/paper.html) |
| Problem | Parameter exchange exposes heterogeneous collaboration to poisoning and inference risks. |
| Mechanism | Clients predict on unlabeled public data; the server applies RobustFilter per sample; clients retrain on private data and aggregated public predictions. |
| Contribution | Connects heterogeneous knowledge transfer with robust aggregation and membership-inference evaluation. |
| Assumptions | Shared classification task, unlabeled public data, and malicious-client/covariance conditions required by robust mean estimation. |
| Evidence boundary | Privacy evidence is empirical, not standalone differential privacy. Robust mean bounds do not certify every downstream model or arbitrary attacks. Public-data and robust-estimation assumptions matter. |
| Evidence | [Official publication metadata / workshop program](https://neurips2021workshopfl.github.io/NFFL-2021/paper.html); [Workshop PDF pp.1–5, §§1–4, threat models and Algorithm 1.](https://neurips2021workshopfl.github.io/NFFL-2021/papers/2021/Chang2021.pdf) |

## Learning Private Neural Language Modeling with Attentive Aggregation

| Field | Details |
| --- | --- |
| Venue / year | International Joint Conference on Neural Networks, 2019 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | C |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1109/IJCNN.2019.8852464) · [Code](https://github.com/shaoxiongji/fed-att) |
| Problem | Uniform model averaging can overlook layer-specific differences among locally trained language models. |
| Mechanism | Compute layerwise Lp distances from the global model, apply softmax to these positive distance scores, and move the server model toward the attention-weighted client parameters. A separate extension adds Gaussian noise to uploaded parameters. |
| Contribution | An early train-time aggregation method separating layerwise attention weights from optional parameter perturbation. |
| Assumptions | Aligned language-model layers, local text data for repeated training, and server access to received client parameters; the reported partitioning is IID random shards. |
| Evidence boundary | The stated formula uses positive distance in softmax, so it should not be described as automatically upweighting the closest clients. The selected privacy section describes Gaussian perturbation without a complete sensitivity, clipping and composition/accounting specification; no calibrated end-to-end DP guarantee is inferred here. IID language-model results do not establish robustness to clinical non-IID data. |
| Evidence | [Publisher DOI identity](https://doi.org/10.1109/IJCNN.2019.8852464); [Publisher-deposited title, complete author list, IJCNN 2019 venue, pages 1–8 and DOI](https://api.crossref.org/works/10.1109/IJCNN.2019.8852464); [Author list, preprint history and final DOI](https://arxiv.org/abs/1812.07108); [v2 pp.3–5, III.A–D, Equations 2–6, Algorithms 1–3, IV.A](https://arxiv.org/pdf/1812.07108v2) |

## Scalable Private Learning with PATE

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2018 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=rkZB1XbRZ) |
| Problem | Knowledge transfer from models trained on sensitive data needs an auditable privacy budget. |
| Mechanism | Train teachers on disjoint private subsets; aggregate votes with Gaussian noise and confidence filtering; use data-dependent privacy accounting. |
| Contribution | Provides a foundational mechanism for formally private ensemble-to-student knowledge transfer. |
| Assumptions | Private teachers and data remain inaccessible; public unlabeled inputs support student training; each record belongs to one teacher subset. |
| Evidence boundary | Teacher consensus, disjoint partitions and query accounting are essential. It is a controlled training protocol rather than arbitrary reuse of already-public model weights. |
| Evidence | [Author organization publication metadata confirms ICLR 2018 and all authors](https://research.google/pubs/scalable-private-learning-with-pate/); [Author conference PDF pp.4,6 §3 and §4: private teacher aggregation, student release and GNMax](https://arxiv.org/pdf/1802.08908) |

## Bi-level Personalization for Federated Foundation Models: A Task-vector Aggregation Approach

| Field | Details |
| --- | --- |
| Venue / year | AAAI Conference on Artificial Intelligence, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39991) |
| Problem | A single global foundation-model update can obscure different client tasks and adaptation directions. |
| Mechanism | FedBip forms each client task vector as its current locally trained model minus its prior personalized starting model, uses cosine similarities to assign client-specific aggregation weights, and maintains personalized aggregate models; FedBip-L applies the procedure by layer. |
| Contribution | Uses task vectors as a client-relation signal for personalized foundation-model aggregation. |
| Assumptions | A shared pretrained model with compatible coordinates, local fine-tuning data, repeated communication, and server access to individual model updates. |
| Evidence boundary | Task-vector similarity is a surrogate for useful collaboration, not a privacy or fairness certificate. Personalized server state and repeated fine-tuning remain necessary; the selected technical sections were reviewed in the preprint rather than the final publisher PDF. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://ojs.aaai.org/index.php/AAAI/article/view/39991); [Author preprint v1, pp.4–5 Methodology, task-vector similarity and layer-wise extension](https://arxiv.org/pdf/2509.12697v1) |

## Breaking the Aggregation Bottleneck in Federated Recommendation: A Personalized Model Merging Approach

| Field | Details |
| --- | --- |
| Venue / year | AAAI Conference on Artificial Intelligence, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/38472) |
| Problem | Replacing local item embeddings by a global aggregate can discard personalized recommendation information. |
| Mechanism | A local MLP generates item-specific mixing weights from local embeddings and global/local differences. The client trains the resulting mixture; the server balances sample-size weights with an inverse-distance similarity between uploaded item tables. An optional privacy-enhanced variant adds Laplace noise to uploaded embeddings. |
| Contribution | Couples personalized local initialization and server aggregation for recommendation and reports a separate noise–utility study. |
| Assumptions | Compatible item identities and embedding dimensions, local interaction data and alternating adapter/model training; the stated noise calibration uses gradient clipping and a sensitivity bound. |
| Evidence boundary | The base merge is not by itself a formal privacy guarantee. The appendix reports a clipped-sensitivity Laplace construction; selected-section reading did not establish a complete multi-round privacy accountant or independently validate the local-DP claim. Evaluation uses offline recommendation datasets, and conditional local-loss analysis should not be generalized to arbitrary nonconvex models. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38472); [Author preprint v1, pp.3–5 method and privacy discussion; p.12 Appendix C; p.15 Table 7](https://arxiv.org/pdf/2508.12386v1) |

## Can Model Merging Improve Aggregation in DiLoCo?

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2026 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2607.03011) |
| Problem | Averaged worker pseudo-gradients can limit low-communication language-model pretraining as the number of workers grows. |
| Mechanism | IsoLoCo averages local pseudo-gradients, replaces singular values of each two-dimensional update matrix by their mean, and applies a Nesterov outer update. The paper compares merging rules and describes a faster approximate implementation. |
| Contribution | Connects model-merging mechanisms to iterative distributed optimization and evaluates spectral aggregation across worker counts. |
| Assumptions | Workers use the same model coordinates and objective with periodic synchronization; experiments partition a common language-model pretraining corpus. |
| Evidence boundary | This is distributed pretraining, not evidence of privacy-preserving or cross-institutional federated deployment. It still exchanges updates periodically and requires local optimization; stronger compression and theoretical explanations are identified as future work. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://arxiv.org/abs/2607.03011); [Author preprint v1, p.5 §2.3; p.7 §4 Algorithm 2; p.10 §5](https://arxiv.org/pdf/2607.03011v1) |

## Communication-Efficient Personalized Adaptation via Federated-Local Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://neurips.cc/virtual/2026/poster/150059) |
| Problem | Federated adapters encode shared knowledge while local adapters retain client specialization; heuristic mixing can waste communication or harm personalization. |
| Mechanism | Potara combines compatible federated and local task vectors. A same-basin analysis yields weights from marginal and cross-covariance traces; diagonal Fisher and per-sample gradient correlations estimate these quantities using local data. |
| Contribution | Links personalized adapter mixing to a conditional loss bound and measures communication–accuracy trade-offs in simulated vision and language federations. |
| Assumptions | Common pretrained model, separately trained local and federated adapters, local gradient access; analysis assumes smooth same-basin behavior and constrained joint task-vector covariance. |
| Evidence boundary | A tighter upper bound does not guarantee uniformly lower realized task loss. Mixing still needs gradient-based covariance estimation and prior local/federated training; experiments partition benchmarks rather than establish live multi-institution deployment. No formal privacy mechanism follows from local data retention. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://neurips.cc/virtual/2026/poster/150059); [Author preprint v1, pp.4–6 §§3.2–3.5 and §4.1–4.2; official NeurIPS 2026 Poster page](https://arxiv.org/pdf/2602.18658v1) |

## FedMerge: Federated Model Merging for Personalization

| Field | Details |
| --- | --- |
| Venue / year | AAAI Conference on Artificial Intelligence, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39113) · [Code](https://github.com/shutong043/FedMerge) |
| Problem | One or a few global models restrict client-specific behavior, while independently fine-tuning many candidates increases client cost. |
| Mechanism | Each client receives one weighted mixture of the server model bank and trains it locally. Returned model changes update both the bank and client mixing weights by the chain rule; softmax normalizes the coefficients and reduced layer subsets can approximate inner products. |
| Contribution | Jointly optimizes shared source models and personalized mixtures with ordinary local training communication. |
| Assumptions | Compatible model parameterization, repeated access to client training data, and a server that stores the model bank and per-client coefficients. |
| Evidence boundary | The method is an iterative training scheme, not a training-free post-hoc merge. Server model storage and weight learning add cost; keeping raw data local does not itself establish formal privacy or demographic fairness. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://ojs.aaai.org/index.php/AAAI/article/view/39113); [Author version v3, p.1 code; pp.3–4 Backgrounds and Methodology, Eqs.3–11 and Algorithm 1](https://arxiv.org/pdf/2504.06768v3) |

## G-Merging: Graph Models Merging for Parameter-Efficient Multi-Task Knowledge Consolidation

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5acb720a361eecb34ee62d356859d246-Abstract-Conference.html) · [Code](https://github.com/cjcj46262/G-Merging) |
| Problem | Task arithmetic alone loses domain-specific graph representations when merging fine-tuned graph models. |
| Mechanism | Task vectors from a common pretrained GNN create a coarse merged backbone. Train node/graph adapters against each task teacher using topology-constrained Wasserstein and graph-embedding losses. A parameter-free router mixes adapter outputs by input-dependent similarity to the target-task adapter. |
| Contribution | A graph-specific hybrid fusion system combining a merged backbone and multiple small adapters under topology-aware composition. |
| Assumptions | A common pretrained GNN and compatible fine-tuned parameters, task graph datasets, teacher embeddings, and target-task identity for the routing reference are available. |
| Evidence boundary | The overall method is not training-free: task adapters require graph data and optimization. Its router is training-free but uses a target-task adapter reference; it does not establish arbitrary unseen-task discovery or a federated privacy protocol. |
| Evidence | [Official publication identity and authors](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5acb720a361eecb34ee62d356859d246-Abstract-Conference.html); [Sections 3–4, Algorithm 1, Eqs. (1)–(9), PDF pp. 3–7; Section 5.1](https://proceedings.iclr.cc/paper_files/paper/2026/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf) |

## GFFMERGE: Efficient Merging of Graph Neural Force Fields and Beyond

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v306/verma26b.html) · [Code](https://github.com/idea-iitd/GFFMerge) |
| Problem | Combining specialized graph neural force fields must preserve sensitive continuous energy/force predictions and molecular simulation behavior. |
| Mechanism | A source-domain-conditioned least-squares objective yields analytical linear-block weights. Targeted fine-tuning updates later interaction layers and energy/force heads. The paper also extends the mechanism to generic GNNs and selected heterogeneous architectures. |
| Contribution | A direct force-field model-merging framework, with continuous-regression and simulation evaluation beyond classification-oriented graph merging. |
| Assumptions | Source models and domain graph inputs are available for activation extraction; block correspondences and compatible physical outputs are needed. The complete force-field procedure includes supervised targeted refinement, distinct from the closed-form merge alone. |
| Evidence boundary | The force-field pipeline is not wholly data-free or training-free. Selected heterogeneous GNN constructions in Appendix C do not establish universal architecture compatibility; numerical and physical stability remain evaluation obligations. |
| Evidence | [Official publication identity and authors](https://proceedings.mlr.press/v306/verma26b.html); [Sections 2–3, especially 3.2–3.4 and Eq. (11), PDF pp. 2–5; Section 5; Appendix C and E.3](https://raw.githubusercontent.com/mlresearch/v306/main/assets/verma26b/verma26b.pdf) |

## RegMean++: Enhancing Effectiveness and Generalization of Regression Mean for Model Merging

| Field | Details |
| --- | --- |
| Venue / year | Transactions on Machine Learning Research, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=H5lDsSCS9i) · [Code](https://github.com/nthehai01/RegMean-plusplus) |
| Problem | How can regression-based merging account for representation changes caused by earlier merged layers? |
| Mechanism | RegMean++ collects statistics through the evolving merged model rather than treating each candidate layer independently. |
| Contribution | Addresses a mismatch between independent layer fitting and the actual merged network. |
| Assumptions | Compatible models and representative examples for statistics collection are available. |
| Evidence boundary | Statistic collection becomes sequential and requires an additional merged-model forward pass; the authors report roughly doubled merging time and limited evaluation up to nine-billion-parameter models. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=H5lDsSCS9i); [§3 methodology; Appendix E Limitations and Future Work, PDF p.46](https://arxiv.org/pdf/2508.03121) |

## Representational Alignment Across Model Layers and Brain Regions with Multi-Level Optimal Transport

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8611049567e7339a88fc68a06100fac1-Abstract-Conference.html) |
| Problem | How can representational similarity be measured when network depth and feature dimensions differ? |
| Mechanism | Nested transport couplings combine local feature alignment with global layer correspondences. |
| Contribution | Provides an alignment measure that relaxes one-to-one layer matching. |
| Assumptions | Representations on comparable stimuli and transport cost choices are available. |
| Evidence boundary | Computation grows rapidly with width and depth, and evaluation covers a limited model/brain dataset collection. This is a related measurement foundation, not a model-fusion or trust guarantee. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8611049567e7339a88fc68a06100fac1-Abstract-Conference.html); [§3 method; Discussion/Limitations, PDF p.10](https://proceedings.iclr.cc/paper_files/paper/2026/file/8611049567e7339a88fc68a06100fac1-Paper-Conference.pdf) |

## Symmetry-Aware Graph Metanetwork Autoencoders: Model Merging through Parameter Canonicalization

| Field | Details |
| --- | --- |
| Venue / year | Conference on Topology, Algebra, and Geometry in Data Science, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v321/boufalis26a.html) · [Code](https://github.com/odyboufalaki/Symmetry-Aware-Graph-Metanetwork-Autoencoders) |
| Problem | Permutation and activation-dependent scaling symmetries make direct interpolation of independently trained neural networks cross high-loss regions. |
| Mechanism | A symmetry-invariant ScaleGMN encoder maps model parameters to latent codes and an MLP decoder reconstructs canonical weights. Functional reconstruction losses train the autoencoder. Interpolation of decoded CNN weights is assessed on pairs of functionally distinct classifiers. |
| Contribution | A learned parameter-canonicalization mechanism directly evaluated for model merging, including pairwise merging of distinct CNN classifiers, beyond generic graph representation learning. |
| Assumptions | A training model zoo and functional input probes are available; each tested interpolation combines compatible CNNs or INRs with matching parameter shapes and activation-specific symmetry assumptions. |
| Evidence boundary | The evidence concerns small CNNs and INRs, not federated protocols or LLM merging. INR endpoints are symmetry-related versions of the same function, so that experiment is not independent-skill combination. Canonicalization training uses model-zoo weights and input data; low interpolation barriers do not establish exact functional equivalence or trusted behavior. |
| Evidence | [Official PMLR identity, complete authors, volume 321, pages 217–235, publication year 2026; event name includes TAG-DS 2025](https://proceedings.mlr.press/v321/boufalis26a.html); [Sections 4–5 and Appendix C.1 as specified in full_text_locators](https://raw.githubusercontent.com/mlresearch/v321/main/assets/boufalis26a/boufalis26a.pdf); [All 72 pages, normalized conference abbreviation and full-name absence check](https://kyc.lsu.edu.cn/_upload/article/files/20/77/2cbaa3754eb9aff9ed74cafed8ff/23a8de02-594c-445f-b084-69b0193c05b3.pdf) |

## A Unified Solution to Diverse Heterogeneities in One-Shot Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://doi.org/10.1145/3711896.3736825) · [Code](https://github.com/Jun-B0518/FedHydra) |
| Problem | Knowledge distillation from heterogeneous client classifiers can be dominated by uneven class competence and sample distributions. |
| Mechanism | Model Stratification derives class-conditioned aggregation weights from generator-training losses; Heterogeneity-Aware Stratified Aggregation alternates synthetic-data generation and global-classifier distillation using weighted client logits. |
| Contribution | A direct one-shot behavioral fusion mechanism that adjusts how heterogeneous classifier knowledge contributes to a global classifier. |
| Assumptions | Uploaded trained classifiers can process a common input representation and share class semantics. The server can query their logits and differentiate the generation objective. |
| Evidence boundary | Generator optimization and repeated local-model evaluation occur centrally after one upload. Raw training-data exclusion does not establish a privacy guarantee; cross-task label mismatch is not resolved. |
| Evidence | [Official publication identity and authors](https://doi.org/10.1145/3711896.3736825); [Author accepted version, Sections 3.1–3.3; Algorithms 1–3; PDF pp. 2–5](https://arxiv.org/pdf/2410.21119v3); [Research Track Papers, exact title and DOI entry](https://kdd.org/kdd2025/research-track-papers-2/) |

## Exploring Model Kinship for Merging Large Language Models

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: EMNLP 2025, 2025 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2025.findings-emnlp.32/) |
| Problem | Can relatedness between source models guide repeated model merging? |
| Mechanism | Task-vector relatedness informs top-k greedy merging of a candidate pool. |
| Contribution | Provides empirical links between candidate similarity and merge outcomes. |
| Assumptions | Comparable source weights and evaluation tasks are available. |
| Evidence boundary | Validation covers two architectures and community-derived data. The limitations explicitly state that current kinship-guided merging does not support sustained evolution; environmental feedback remains future work. |
| Evidence | [Official publication metadata and abstract](https://aclanthology.org/2025.findings-emnlp.32/); [§3.2; §4.1–4.2, PDF pp.3–5; Limitations, PDF p.9](https://aclanthology.org/2025.findings-emnlp.32.pdf) |

## FedAWA: Adaptive Optimization of Aggregation Weights in Federated Learning Using Client Vectors

| Field | Details |
| --- | --- |
| Venue / year | IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Shi_FedAWA_Adaptive_Optimization_of_Aggregation_Weights_in_Federated_Learning_Using_CVPR_2025_paper.html) |
| Problem | Fixed client aggregation weights can neglect client-update directions under heterogeneous data. |
| Mechanism | FedAWA subtracts the incoming global model from each locally trained model, optimizes normalized client coefficients to align the merged update with client vectors, and adds alignment to the current global model; a layer-wise variant chooses coefficients separately by layer. |
| Contribution | Uses update geometry to adapt server aggregation weights without extra runtime proxy examples. |
| Assumptions | Common compatible model coordinates, iterative client training and a server able to inspect client updates; runtime weighting does not require a separate validation/proxy dataset. |
| Evidence boundary | The method still requires local training and repeated communication. Directional alignment is a proxy for generalization; raw update access is not automatically compatible with secure aggregation, and no formal privacy or demographic-fairness guarantee follows from it. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Shi_FedAWA_Adaptive_Optimization_of_Aggregation_Weights_in_Federated_Learning_Using_CVPR_2025_paper.html); [Author preprint v1, pp.4–5 client vectors, aggregation-weight objective and layer-wise extension](https://arxiv.org/pdf/2503.15842v1) |

## GNNMerge: Merging of GNN Models Without Accessing Training Data

| Field | Details |
| --- | --- |
| Venue / year | ICLR Workshop on Neural Network Weights as a New Data Modality, 2025 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2503.03384) |
| Problem | Independently initialized GNNs can be difficult to merge using methods developed for shared-initialization vision/language models. |
| Mechanism | On same-domain inference graphs, source activations define embedding targets; independent layer-wise alignment relaxes sequential dependencies and yields analytical weight solutions for supported GNN blocks. |
| Contribution | A direct GNN parameter-merging mechanism and benchmark for same-architecture models without original training labels. |
| Assumptions | The models have the same GNN architecture and compatible dimensions; an inference graph from the target domain and source activations are accessible. Shared initialization and training labels are not required. |
| Evidence boundary | Not data-free: same-domain unlabeled inference graphs are required. The relaxation does not establish exact preservation of all source behaviors, and this is a workshop publication, not an ICLR main-conference paper. |
| Evidence | [Official publication identity and authors](https://arxiv.org/abs/2503.03384); [PDF p. 1 workshop acceptance header; Section 2 Problem 1 and assumptions, pp. 3–4; Sections 3.2–3.4, pp. 4–6](https://arxiv.org/pdf/2503.03384v2) |

## Identifying and Reusing Learnwares Across Different Label Spaces

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://ijcai.org/proceedings/2025/638) |
| Problem | How can models trained with different label spaces be selected and assembled for a new task? |
| Mechanism | Class-wise reduced kernel mean embeddings define similarities; minimum-cost maximum-flow selects combinations, followed by local supervised reuse. |
| Contribution | Connects external capability specifications to heterogeneous model combinations. |
| Assumptions | Developers compute specifications locally; users have labeled local data for adaptation and assembly. |
| Evidence boundary | The identification phase avoids central raw-data access, but reuse still trains on user labels. This operational restriction is not a differential-privacy guarantee; utility depends on specification fidelity. |
| Evidence | [Official publication metadata and abstract](https://ijcai.org/proceedings/2025/638); [§3.1–3.3, PDF pp.2–4; §4.1, PDF p.5](https://ijcai.org/proceedings/2025/0638.pdf) |

## InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/ad7c21456da003836ef6be2261e940df-Abstract-Conference.html) |
| Problem | Token-wise distillation neglects relations among logit dimensions. |
| Mechanism | Top-k logit graphs and an approximate Gromov-Wasserstein loss complement ULD and supervised training. |
| Contribution | Multi-source heterogeneous LLM fusion into a fixed pivot architecture. |
| Assumptions | Instruction-response data and source internals/logits are available. |
| Evidence boundary | Graph agreement does not guarantee factual consistency, privacy or fairness; offline source-state storage is substantial. |
| Evidence | [Official publication metadata](https://papers.nips.cc/paper_files/paper/2025/hash/ad7c21456da003836ef6be2261e940df-Abstract-Conference.html); [§3, PDF pp.3–6: GLD and multi-source loss; §4.1/Table 2, PDF pp.6–7: source/pivot configuration; Appendix D, PDF pp.29–30: data and offline states; Appendix K, PDF pp.36–37: separate single-teacher compression](https://papers.nips.cc/paper_files/paper/2025/file/ad7c21456da003836ef6be2261e940df-Paper-Conference.pdf) |

## Intrinsic Training Signals for Federated Learning Aggregation

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Image Analysis and Processing, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://link.springer.com/chapter/10.1007/978-3-032-10185-3_11) |
| Problem | Uniformly aggregating layers and classes overlooks different local learning dynamics in heterogeneous clients. |
| Mechanism | LIVAR weights LoRA layers through a learned mapping from gradient/update importance and combines classifier information using local class statistics. Its calibration trains a reference on pooled TinyImageNet proxy data, fits optimal layer weights, and derives a random-forest/SHAP mapping for runtime aggregation. |
| Contribution | Makes aggregation responsive to layer and class learning signals and examines an interpretable calibration model. |
| Assumptions | Compatible LoRA/classifier coordinates, shared label meaning, client training statistics, and a proxy-data calibration stage with a centrally trained reference. |
| Evidence boundary | The overall method is not proxy-data-free: its layer-weight calibration explicitly uses a proxy dataset and reference model. SHAP here explains the fitted mapping, not causal fairness or privacy; transmitted statistics and updates need a separate privacy assessment. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://link.springer.com/chapter/10.1007/978-3-032-10185-3_11); [Author preprint v2, pp.4–6 method and proxy calibration; p.10 §6](https://arxiv.org/pdf/2507.06813v2) |

## Many-Task Federated Fine-Tuning via Unified Task Vectors

| Field | Details |
| --- | --- |
| Venue / year | Workshop on Federated Learning in the Age of Generative AI (FedGenAI), co-located with IJCAI 2025, 2025 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://federated-learning.org/FedGenAI-ijcai-2025/) |
| Problem | Clients with multiple distinct tasks can make per-task or per-client model storage and communication expensive. |
| Mechanism | MaTU unifies task-vector signs and magnitudes, sends the resulting vector plus binary masks and rescalers, and aggregates same-task and selected cross-task information according to known client/task assignments and sign compatibility. |
| Contribution | Offers a compact representation for iterative many-task federated adaptation without retaining a separate server model for every client. |
| Assumptions | Shared pretrained backbone and compatible task vectors, local per-task fine-tuning, known task assignments at the server, and communicated masks/rescalers. |
| Evidence boundary | Task labels, masks and updates may disclose information; local data retention is not a formal privacy guarantee. Experiments on 30 benchmark datasets do not establish live cross-institution federation. This is a companion-workshop paper and does not inherit IJCAI A. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://federated-learning.org/FedGenAI-ijcai-2025/); [Author preprint v3, pp.3–4 method; official FedGenAI-IJCAI 2025 accepted-paper programme](https://arxiv.org/pdf/2502.06376v3) |

## Model merging with SVD to tie the Knots

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html) · [Code](https://github.com/gstoica27/KnOTS) |
| Problem | Why can existing weight-merging methods struggle with low-rank task updates? |
| Mechanism | Joint SVD produces a shared basis; model-specific factors are merged and reconstructed in that basis. |
| Contribution | Provides an alignment step and a joint-task evaluation that does not assume the task-specific label set is known. |
| Assumptions | LoRA models share architecture and pretrained initialization. |
| Evidence boundary | The demonstrated setting remains shared-base LoRA fusion. A stronger joint-task protocol reveals that per-task scores alone can hide cross-task confusion. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html); [§3, PDF p.3; §4, PDF pp.5–6; §5.3, PDF p.8](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4f8a5109c5083b5307fcd0bddae7a7-Paper-Conference.pdf) |

## Never Start from Scratch: Expediting On-Device LLM Personalization via Explainable Model Selection

| Field | Details |
| --- | --- |
| Venue / year | ACM International Conference on Mobile Systems, Applications, and Services, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://dl.acm.org/doi/10.1145/3711875.3729132) |
| Problem | Starting every mobile user from the same base LLM wastes adaptation compute and scarce personal data. |
| Mechanism | XPerT probes cached and base models, summarizes behavioral differences into a decomposed latent basis, maps user data to that basis, and selects suitable personalized checkpoints. When needed, it composes multiple candidates by task arithmetic before local fine-tuning. |
| Contribution | Connects behavioral model selection with explicit multi-model composition in an implemented smartphone personalization system. |
| Assumptions | A compatible common LLM base, a cloud cache of personalized checkpoints, probe/summarization access and local user data for matching and adaptation. |
| Evidence boundary | This is a cloud-cache/on-device collaboration design, not a conventional federated aggregation protocol. Explainability coordinates and local data retention are not formal fairness or privacy guarantees; language-style benchmark evidence should not be generalized to unrestricted personal data. |
| Evidence | [Primary publication/acceptance metadata and abstract](https://dl.acm.org/doi/10.1145/3711875.3729132); [Author-hosted ACM paper, p.1 bibliographic header; pp.3–4 §3; p.7 §5.2](https://sites.pitt.edu/~weigao/publications/mobisys25_xpert.pdf) |

## PLeaS - Merging Models with Permutations and Least Squares

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Nasery_PLeaS_-_Merging_Models_with_Permutations_and_Least_Squares_CVPR_2025_paper.html) |
| Problem | How can models trained from different initializations and tasks be merged at a chosen compute budget? |
| Mechanism | Permutations identify corresponding features; regression fits merged layers to source-model behavior. |
| Contribution | Integrates alignment and regression for flexible model compression through merging. |
| Assumptions | Compatible architectures and calibration inputs are available; the data-free-task variant substitutes public data. |
| Evidence boundary | PLeaS-free removes dependence on original task data, not all calibration data. Generality remains conditioned on supported architectures and the selected calibration distribution. |
| Evidence | [Official publication metadata and abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Nasery_PLeaS_-_Merging_Models_with_Permutations_and_Least_Squares_CVPR_2025_paper.html); [§3 and Figure 1, PDF pp.2–4; §4 experiments](https://openaccess.thecvf.com/content/CVPR2025/papers/Nasery_PLeaS_-_Merging_Models_with_Permutations_and_Least_Squares_CVPR_2025_paper.pdf) |

## Representation Surgery in Model Merging with Probabilistic Modeling

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v267/wei25c.html) |
| Problem | Can a deterministic correction adequately describe merging-induced representation distortion? |
| Mechanism | ProbSurgery learns sampled representation corrections and extends the correction module toward a shared multi-task setting. |
| Contribution | Extends representation repair with probabilistic modeling and task-sharing variants. |
| Assumptions | Compatible expert models and unlabeled test/validation examples support feature-alignment learning. |
| Evidence boundary | Performance depends on available adaptation examples; the paper explicitly studies validation-set size. Representation uncertainty is not a calibrated safety guarantee. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v267/wei25c.html); [§3; §4.1–4.3, PDF pp.3–6; Appendix C.3, PDF p.15](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25c/wei25c.pdf) |

## Task Arithmetic Through The Lens Of One-Shot Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | Transactions on Machine Learning Research, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=Cgyo7S7Oy0) · [Code](https://github.com/SilviaTao/one_shot_fl_task_arithmetic) |
| Problem | The relationship between task-vector merging and federated optimization needs explicit conditions. |
| Mechanism | Compare common-base local-SGD equations, with outer step size beta=lambda*T, then apply heterogeneity analysis and federated aggregation alternatives. |
| Contribution | Separates data heterogeneity from differences in local training when interpreting merge behavior. |
| Assumptions | Common initialization and compatible parameters; transferred bounds impose their own SGD, smoothness, noise and objective assumptions. |
| Evidence boundary | Algebraic correspondence does not certify a federated deployment or transfer convergence guarantees to arbitrary optimizers, architectures or adapters. Proofs were not independently rederived. |
| Evidence | [Official bibliographic identity](https://openreview.net/forum?id=Cgyo7S7Oy0); [Accepted author version v2, publication header TMLR 05/2025; pp.4–6 §§3–4, equations 2–4 and assumptions 4.2–4.5](https://arxiv.org/pdf/2411.18607v2); [Indexed final PDF first page, Published in Transactions on Machine Learning Research (05/2025)](https://openreview.net/pdf?id=Cgyo7S7Oy0) |

## AdaMerging: Adaptive Model Merging for Multi-Task Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/62868cc2fc1eb5cdf321d05b4b88510c-Abstract-Conference.html) |
| Problem | How can merging coefficients adapt to heterogeneous tasks? |
| Mechanism | Entropy minimization updates coefficients of task vectors, with an optional TIES preprocessing variant. |
| Contribution | Automates coefficient selection for multi-task model merging. |
| Assumptions | Compatible task vectors and unlabeled test samples are available. |
| Evidence boundary | The optimization is transductive and depends on test-distribution access. Entropy is a surrogate objective, not a general reliability or safety guarantee; adaptive weights alone do not establish continual collaboration. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/62868cc2fc1eb5cdf321d05b4b88510c-Abstract-Conference.html); [§3, PDF pp.4–6; §4.1, PDF p.7](https://proceedings.iclr.cc/paper_files/paper/2024/file/62868cc2fc1eb5cdf321d05b4b88510c-Paper-Conference.pdf) |

## AgentMerge: Enhancing Generalization in Fine-Tuned LLM Agents

| Field | Details |
| --- | --- |
| Venue / year | NeurIPS 2024 Workshop on Adaptive Foundation Models, 2024 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=nZmAwmi2gr) |
| Problem | Agentic fine-tuning can overfit expert trajectories and lose general capabilities. |
| Mechanism | Interpolate the two vectors, then add their interpolation to the pretrained base. |
| Contribution | Direct parameter fusion for agent generalization, beyond a multi-agent dialogue alone. |
| Assumptions | Compatible weights and the common pretrained base are available; successful trajectories train the agent branch. |
| Evidence boundary | Workshop evidence on WorkArena; no guarantee of heterogeneous-weight merging or federated trustworthiness. |
| Evidence | [Official publication metadata](https://openreview.net/forum?id=nZmAwmi2gr); [§§2.2–2.3 and §3, PDF p.2: trajectory pipeline, vector interpolation and Llama3.1-8B; Appendix E, PDF p.9: trajectory generators and inconsistent size annotation](https://openreview.net/attachment?id=nZmAwmi2gr&name=pdf); [Official workshop accepted-paper list](https://adaptive-foundation-models.org/papers.html); [Author publication page explicitly labels Type: Workshop](https://www.servicenow.com/research/publication/megh-thakkar-agen-neurips-workshops2024.html) |

## FedFisher: Leveraging Fisher Information for One-Shot Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Artificial Intelligence and Statistics, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | C |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v238/jhunjhunwala24a.html) |
| Problem | Averaging locally trained models can lose accuracy when only one model-upload round is allowed. |
| Mechanism | Clients train from a common initialization and send weights with Fisher approximations; the server minimizes a Fisher-weighted quadratic discrepancy. Diagonal and KFAC variants reduce the cost of the full Fisher matrix. |
| Contribution | Connects one-shot aggregation to local posterior curvature, with restricted theory and practical approximations. |
| Assumptions | Compatible parameter coordinates and common initialization; clients retain data to estimate Fisher information; the server receives weights and Fisher summaries. |
| Evidence boundary | The overparameterized two-layer ReLU result uses full Fisher information and does not directly establish the same guarantee for diagonal/KFAC variants. KFAC factors require individual server access in the discussed implementation. Inversion experiments and optional secure aggregation are not a differential-privacy guarantee; closeness to local models is not demographic fairness. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v238/jhunjhunwala24a.html); [Final proceedings PDF pp.3–4, Section 2 and Algorithm 1: local posteriors, Fisher fusion and common initialization; pp.6–7, Section 4: approximations and secure-aggregation distinction](https://proceedings.mlr.press/v238/jhunjhunwala24a/jhunjhunwala24a.pdf) |

## FedTAD: Topology-aware Data-free Knowledge Distillation for Subgraph Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Joint Conference on Artificial Intelligence, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.ijcai.org/proceedings/2024/632) |
| Problem | Label-distribution and graph-homophily variation make client GNNs unequally reliable by class, distorting global model fusion. |
| Mechanism | Clients upload local GNNs and class-wise reliability statistics. A server generator synthesizes node attributes and a k-nearest-neighbor pseudo graph; weighted teacher divergences transfer reliable local knowledge into the aggregated global GNN. |
| Contribution | A topology-aware multi-teacher fusion post-processor with an explicit class-weighted distillation objective. |
| Assumptions | Compatible GNNs for the preceding aggregation, common feature/label semantics, access to uploaded local models and reliability statistics; local graph and labels are needed to estimate reliability. |
| Evidence boundary | The demonstrated setting is compatible subgraph node classification, not arbitrary heterogeneous graph architectures. Generated graphs and local-data retention do not establish differential privacy or secure aggregation. |
| Evidence | [Official publication identity and authors](https://www.ijcai.org/proceedings/2024/632); [Sections 4.1–4.3, Eq. (5), Eqs. (8)–(11), Algorithm 1; printed pp. 5718–5720](https://www.ijcai.org/proceedings/2024/0632.pdf) |

## FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Model Fusion

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/31e6e0c09325a3be16d93f84e40e0c7e-Abstract-Conference.html) · [Code](https://github.com/wizard1203/FuseFL) |
| Problem | One-shot federation under distribution heterogeneity can retain spurious local features and poorly combine independently learned representations. |
| Mechanism | Partition networks into blocks; train, exchange and concatenate a block across clients, adapt its output, freeze it, and continue local training on later blocks. Width adjustment controls fused-model growth. |
| Contribution | Makes module composition and progressive local retraining an alternative to terminal weight averaging under a one-shot communication budget. |
| Assumptions | Local training data remain available between block-fusion stages; block interfaces must be compatible through the prescribed adapters; staged communication and training are coordinated. |
| Evidence boundary | The one-shot description refers to the overall communication budget and does not mean a single final exchange of fully trained checkpoints: fusion and local retraining occur in successive block stages. The causal motivation is not clinical causal identification or a general privacy guarantee. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/31e6e0c09325a3be16d93f84e40e0c7e-Abstract-Conference.html); [Final proceedings PDF pp.6–7, Section 4 and Figure 4: progressive block fusion, retraining, adapters and complexity](https://proceedings.neurips.cc/paper_files/paper/2024/file/31e6e0c09325a3be16d93f84e40e0c7e-Paper-Conference.pdf) |

## Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v235/yu24p.html) |
| Problem | How can interference among fine-tuned language-model updates be reduced? |
| Mechanism | DARE sparsifies task deltas before applying existing merging operators. |
| Contribution | Provides a lightweight preprocessing step for ability composition. |
| Assumptions | Models are fine-tuned from a shared pretrained backbone and have compatible parameter spaces. |
| Evidence boundary | The method targets small supervised fine-tuning deltas from homologous models; experiments explicitly avoid merging checkpoints with different base initializations. Hyperparameter search and evaluation access must be accounted for separately. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v235/yu24p.html); [§3 Methodology, PDF pp.3–4; §4.2 setup, PDF p.6](https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24p/yu24p.pdf) |

## Local Superior Soups: A Catalyst for Model Merging in Cross-Silo Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/24f7b98aef14fcd68acf3c941af1b59e-Abstract-Conference.html) · [Code](https://github.com/ubc-tea/Local-Superior-Soups) |
| Problem | Local models trained on heterogeneous silo data may occupy incompatible regions of the loss landscape and merge poorly. |
| Mechanism | Initialize from a pretrained or previous global model, build local candidate models sequentially, and train interpolated weights with affinity/diversity regularization. A local soup becomes the client contribution to subsequent global aggregation. |
| Contribution | Shows how training can prepare models for subsequent averaging in cross-silo federation with limited communication. |
| Assumptions | A shared architecture and meaningful common pretrained/global initialization; local data and extra training of several local candidates are available. |
| Evidence boundary | This changes local training and creates multiple candidates, so it is not a training-free post-hoc merger. The convex/smooth analysis should not be presented as a general guarantee for deep nonconvex networks; benefits depend on initialization and evaluated heterogeneity. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/24f7b98aef14fcd68acf3c941af1b59e-Abstract-Conference.html); [Final proceedings PDF pp.3–5, Sections 3.1–3.3 and Algorithm 1: soup construction, interpolation, affinity/diversity terms and theorem assumptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/24f7b98aef14fcd68acf3c941af1b59e-Paper-Conference.pdf) |

## MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v235/chen24ah.html) · [Code](https://github.com/dinobby/MAGDi) |
| Problem | Compress the reasoning of interacting LLMs into one deployable student. |
| Mechanism | Next-token, contrastive and graph node-classification losses train a student with a temporary GCN. |
| Contribution | A concrete multi-model behavioral fusion mechanism with a single-model inference artifact. |
| Assumptions | Teacher-generated trajectories, answer correctness labels and student training access are available. |
| Evidence boundary | Benchmarks test reasoning and transfer; they do not establish privacy, fairness or federated guarantees. |
| Evidence | [Official publication metadata](https://proceedings.mlr.press/v235/chen24ah.html); [§§3.1–3.4, PDF pp.4–6: MAG construction, losses and GCN removal; §4, PDF p.6: student families/sizes](https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ah/chen24ah.pdf) |

## MetaFed: Federated Learning Among Federations With Cyclic Knowledge Distillation for Personalized Healthcare

| Field | Details |
| --- | --- |
| Venue / year | IEEE Transactions on Neural Networks and Learning Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://ieeexplore.ieee.org/document/10197230/) · [Code](https://github.com/microsoft/PersonalizedFL) |
| Problem | Combine knowledge across independent federations without a higher-level aggregation server. |
| Mechanism | Pass models around a cycle; minimize local classification loss plus feature-distillation loss. Validation performance controls model inheritance and the personalization distillation weight. |
| Contribution | Serverless cross-federation knowledge transfer with adaptive personalization and an extensible grouped MetaFed++ topology. |
| Assumptions | The stated problem uses shared input/output spaces and local training and validation data; feature distillation requires compatible representations. |
| Evidence boundary | This is training-based knowledge fusion, not training-free parameter merging. Keeping data local does not establish differential privacy. Evaluations and assumptions should not be generalized to arbitrary incompatible architectures. |
| Evidence | [IEEE-deposited Crossref metadata: complete author list, DOI, final volume35 issue11, pages16671–16682 and publication November2024.](https://api.crossref.org/works/10.1109/TNNLS.2023.3297103); [Author manuscript v3; accepted TNNLS comment and author list; earlier preprint/workshop are versions of this work, not extra papers.](https://arxiv.org/abs/2206.08516); [SectionsIII-A–III-D, equations2–4, Algorithms1–2; SectionIII-F MetaFed++; SectionIV evaluation setup.](https://arxiv.org/html/2206.08516v3) |

## One-shot Federated Learning via Synthetic Distiller-Distillate Communication

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ba0ad9d1e0c737800b2340b9cd68c208-Abstract-Conference.html) · [Code](https://github.com/Carkham/FedSD2C) |
| Problem | Uploading classifiers then reconstructing knowledge can lose client information and incur communication costs. |
| Mechanism | Local models select informative coresets and guide latent synthesis through a pretrained VAE. Each local model labels its synthetic latents; the server unions these latent/soft-label pairs, decodes them, and minimizes a KL distillation loss. |
| Contribution | A one-shot behavioral fusion route that transfers multiple client-model outputs through synthetic latent/soft-label pairs rather than uploading model weights. |
| Assumptions | Clients access private examples and pretrained local classifiers; a shared pretrained VAE and common prediction-label semantics are available. |
| Evidence boundary | Not an entirely data-free pipeline: private examples are needed for coreset selection and synthesis. The VAE is auxiliary, and neither synthetic-data transmission nor reduced visual similarity alone is a formal privacy guarantee. |
| Evidence | [Official publication identity and authors](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ba0ad9d1e0c737800b2340b9cd68c208-Abstract-Conference.html); [Sections 3.1–3.3, especially Algorithm 1 lines 14–20 and Eq. (8), PDF pp. 4–6](https://proceedings.neurips.cc/paper_files/paper/2024/file/ba0ad9d1e0c737800b2340b9cd68c208-Paper-Conference.pdf) |

## Representation Surgery for Multi-Task Model Merging

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v235/yang24t.html) |
| Problem | How can representation distortion introduced by weight merging be corrected? |
| Mechanism | An adapter-like module predicts representation bias and is fitted with an unlabeled feature-alignment objective. |
| Contribution | Adds a method-agnostic representation repair stage after parameter merging. |
| Assumptions | Merged and individual expert features are accessible on task-associated test examples. |
| Evidence boundary | Task-specific correction and expert feature access are required; the objective uses unlabeled test data, so this is neither data-free merging nor evidence of general continual adaptation. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v235/yang24t.html); [§3 representation bias; §4.1–4.2, PDF pp.4–6; §5.1](https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24t/yang24t.pdf) |

## Transformer Fusion with Optimal Transport

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7e0af0d1bc0ec2a90fc294be2e00447e-Abstract-Conference.html) · [Code](https://github.com/graldij/transformer-fusion) |
| Problem | How can optimal-transport alignment respect transformer computation? |
| Mechanism | The transport-map flow graph handles attention, residuals, normalization, and other transformer components. |
| Contribution | Extends transport-based fusion to ViT and BERT experiments. |
| Assumptions | Weights, activation statistics, and supported architecture operations are accessible. |
| Evidence boundary | The flow graph represents internal tensor alignment, not an external collaboration network. Supported transformer experiments do not establish arbitrary cross-architecture fusion. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7e0af0d1bc0ec2a90fc294be2e00447e-Abstract-Conference.html); [§4.1–4.2, PDF pp.4–6; experimental setup](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e0af0d1bc0ec2a90fc294be2e00447e-Paper-Conference.pdf) |

## ZipIt! Merging Models from Different Tasks without Training

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html) |
| Problem | How can separately trained models with different tasks be merged without retraining? |
| Mechanism | Generalized zipping combines feature matching with partial merging so unmatched task-specific layers can remain separate. |
| Contribution | Exposes a continuum between shared computation and separate task heads. |
| Assumptions | Models have the same architecture; representative inputs are available for feature correlations. |
| Evidence boundary | Partial merging retains branches and changes deployment cost; its results are not equivalent to a single fully shared model. The method retains architecture and calibration-data constraints. |
| Evidence | [Official publication metadata and abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html); [§4.1–4.2, PDF pp.4–6; §5.2 and Table 2, PDF p.8](https://proceedings.iclr.cc/paper_files/paper/2024/file/7dbb5bfab324e3b86af9bd0df15498dd-Paper-Conference.pdf) |

## Dataless Knowledge Fusion by Merging Weights of Language Models

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=FCnohuR6AnM) · [Code](https://github.com/bloomberg/dataless-model-merging) |
| Problem | How can language models be merged while preserving their local layer behavior? |
| Mechanism | RegMean combines weight matrices using input inner-product statistics and adjusts off-diagonal correlations. |
| Contribution | Introduces a closed-form, statistics-based fusion mechanism. |
| Assumptions | Models use the same architecture and pretrained checkpoint; local examples are needed to produce statistics even when raw examples are unavailable at merging. |
| Evidence boundary | The architecture and common-checkpoint assumptions are explicit. Dataless merging does not imply no data-dependent preprocessing or a formal privacy guarantee. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=FCnohuR6AnM); [§3, PDF pp.3–5; §4 setup](https://arxiv.org/pdf/2212.09849); [Author publication page confirms ICLR 2023 and code](https://pxch.github.io/publication/iclr2023/) |

## Editing Models with Task Arithmetic

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=6t0Kwf8-jrj) |
| Problem | How can task-specific changes in model behavior be represented and combined? |
| Mechanism | Add, negate, or compose task vectors, then apply the result to the base model. |
| Contribution | Provides a compositional weight-space representation for editing and multi-task reuse. |
| Assumptions | Experiments use identical architectures and the same pretrained initialization. |
| Evidence boundary | Elementwise operations require matching architectures; shared initialization and the fine-tuning trajectory constrain the demonstrated behavior. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=6t0Kwf8-jrj); [§2; §§3–5; §6 Limitations, PDF pp.2–8](https://arxiv.org/pdf/2212.04089); [Final conference bibliographic record; six-author list](https://dblp.org/rec/conf/iclr/IlharcoRWSHF23.html) |

## FedTAM: Decentralized Federated Learning with a Feature Attention Based Multi-teacher Knowledge Distillation for Healthcare

| Field | Details |
| --- | --- |
| Venue / year | IEEE International Conference on Parallel and Distributed Systems, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | Pending verification |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://ieeexplore.ieee.org/document/10476260/) |
| Problem | Transfer useful knowledge across non-IID clients without a trusted central server. |
| Mechanism | The abstract describes selecting relevant teacher knowledge for each student using feature attention; detailed objectives and update rules have not been inspected. |
| Contribution | Personalized decentralized knowledge fusion evaluated on healthcare and feature-shift image benchmarks. |
| Assumptions | Decentralized non-IID federated learning; architecture compatibility and precise data-access assumptions require full-text checking. |
| Evidence boundary | Abstract reviewed only. Formal privacy guarantees, attack resistance, fairness outcomes and detailed ablations are not verified; retaining local data alone is not evidence of differential privacy. |
| Evidence | [IEEE-deposited metadata: title, nine authors, ICPADS2023, pages1246–1253 and DOI.](https://api.crossref.org/works/10.1109/ICPADS60453.2023.00180); [Indexed paper abstract; DBLP-imported record, not a peer-review acceptance record.](https://openreview.net/forum?id=6OKD4xshNb); [Coauthor publication entry FedTAM (2023): cyclic transfer and feature-attention multi-teacher distillation.](https://www.bj-yan.top/publications) |

## Git Re-Basin: Merging Models modulo Permutation Symmetries

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=CQsmMYmlP5T) · [Code](https://github.com/samuela/git-re-basin) |
| Problem | Can hidden-unit permutation symmetry explain barriers between independently trained models? |
| Mechanism | Activation matching, weight matching, and a straight-through estimator search for corresponding units. |
| Contribution | Links practical model merging to symmetry-aware loss geometry. |
| Assumptions | The relevant layers admit compatible permutation symmetries. |
| Evidence boundary | The paper presents counterexamples to a universal single-basin hypothesis; empirical mode connectivity must not be read as a guarantee for every architecture or pair of models. |
| Evidence | [Official publication metadata and abstract](https://openreview.net/forum?id=CQsmMYmlP5T); [§3; §4; counterexample discussion, PDF pp.3–8](https://arxiv.org/pdf/2209.04836) |

## Model Spider: Learning to Rank Pre-Trained Models Efficiently

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/2c71b14637802ed08eaa3cf50342b2b9-Abstract-Conference.html) · [Code](https://github.com/zhangyikaii/Model-Spider) |
| Problem | How can many pretrained models be ranked for new tasks under limited evaluation resources? |
| Mechanism | A two-stage ranker first uses task-agnostic model representations, then optionally reranks shortlisted models using forward-pass information. |
| Contribution | Connects model capability representation to budget-dependent recommendation. |
| Assumptions | Historical model-task evaluation data and target examples are available. |
| Evidence boundary | The learned ranker relies on the coverage of its model/task training collection. It predicts individual transfer utility rather than proving compatibility among multiple selected models. |
| Evidence | [Official publication metadata and abstract](https://papers.nips.cc/paper_files/paper/2023/hash/2c71b14637802ed08eaa3cf50342b2b9-Abstract-Conference.html); [§3 methodology, PDF pp.3–5; §6 Conclusion, PDF p.10](https://proceedings.neurips.cc/paper_files/paper/2023/file/2c71b14637802ed08eaa3cf50342b2b9-Paper-Conference.pdf) |

## Personalized Federated Learning with Feature Alignment and Classifier Collaboration

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=SXZr8aDKia) · [Code](https://github.com/JianXu95/FedPAC) |
| Problem | How to share feature information while combining useful personalized heads? |
| Mechanism | Section 3.3 Eq. (4): phi_hat_i=sum_j alpha_ij phi_j, alpha_i on the simplex. Section 4.1 Eq. (11) estimates coefficients via a quadratic testing-loss objective; Section 5 uses transmitted statistics, shared feature aggregation and centroid alignment. |
| Contribution | Explicit classifier-head fusion accompanies feature regularization. |
| Assumptions | Compatible linear heads and shared feature coordinates; local labeled data and feature statistics. |
| Evidence boundary | The analytic derivation assumes identical input marginals and zero-centered features; prototype alignment alone is not the inclusion basis. |
| Evidence | [Author/publication metadata](https://openreview.net/forum?id=SXZr8aDKia); [PDF pp.4–7, Sections 3.3, 4.1 and 5; Eqs. (4),(5),(11); p.1 header/code footnote](https://arxiv.org/pdf/2306.11867v1) |

## Personalized Subgraph Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v202/baek23a.html) · [Code](https://github.com/JinheonBaek/FED-PUB) |
| Problem | Global parameter averaging mixes GNN knowledge from incompatible graph communities and suppresses personalized performance. |
| Mechanism | The server probes uploaded GNNs on a stochastic-block-model random graph and compares averaged node embeddings. Normalized similarities weight the source model parameters separately for each client; trainable local sparse masks filter the resulting parameters. |
| Contribution | Direct function-guided personalized model fusion coupled with element-wise selection of fused parameters. |
| Assumptions | Client GNNs share a compatible parameterization and input feature dimensions; server can run uploaded models on common synthetic random graphs, and clients can optimize masks on local subgraphs. |
| Evidence boundary | Model-coordinate compatibility is still needed despite graph-structure heterogeneity. Personalized output is a family of client models, and random probes/local graph retention alone do not provide a formal privacy guarantee. |
| Evidence | [Official publication identity and authors](https://proceedings.mlr.press/v202/baek23a.html); [Sections 3–4, especially 4.1 Personalized Weight Aggregation and 4.2 Adaptive Weight Masking, PDF pp. 4–5; Appendix B.3](https://proceedings.mlr.press/v202/baek23a/baek23a.pdf) |

## TIES-Merging: Resolving Interference When Merging Models

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1644c9af28ab7916874f6fd6228a9bcf-Abstract-Conference.html) · [Code](https://github.com/prateeky2806/ties-merging) |
| Problem | How can conflicting task updates be combined more reliably? |
| Mechanism | TIES trims task vectors, elects a sign per parameter, and merges only sign-consistent values. |
| Contribution | Identifies sign disagreement as an actionable source of merging interference. |
| Assumptions | Models share architecture and pretrained initialization. |
| Evidence boundary | Appendix A notes incomplete theory, dependence on shared initialization, and a remaining gap to joint multi-task training. Choosing suitable checkpoints is also unresolved. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1644c9af28ab7916874f6fd6228a9bcf-Abstract-Conference.html); [§§3–4; Appendix A Limitations and Future Works, PDF p.17](https://proceedings.neurips.cc/paper_files/paper/2023/file/1644c9af28ab7916874f6fd6228a9bcf-Paper-Conference.pdf) |

## lo-fi: distributed fine-tuning without communication

| Field | Details |
| --- | --- |
| Venue / year | Transactions on Machine Learning Research, 2023 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=1U0aPkBVz0) |
| Problem | Synchronizing gradients across device groups can make fine-tuning expensive when interconnect communication is limiting. |
| Mechanism | Partition devices into groups, perform group-local fine-tuning without inter-group updates, then average the final group models. Synchronous communication can still occur among devices within a group. |
| Contribution | Provides a distributed-training foundation for terminal model averaging and a comparison point for one-shot federation. |
| Assumptions | Compatible parameters from a shared pretrained checkpoint; data and training configuration that allow averaging to remain effective; within-group communication may be available. |
| Evidence boundary | The reviewed experiments primarily use IID data partitioning and do not establish performance in non-IID cross-hospital federation. Communication is removed between groups during fine-tuning, not necessarily within groups or at the final merge. Speedup is hardware/task dependent and the protocol supplies no formal privacy guarantee. |
| Evidence | [Official OpenReview publication identity](https://openreview.net/forum?id=1U0aPkBVz0); [Indexed official PDF text: title, authors and Published in Transactions on Machine Learning Research (01/2023); direct download access challenge](https://openreview.net/pdf?id=1U0aPkBVz0); [Author list and v2 revision dated 2022-11-12](https://arxiv.org/abs/2210.11948); [v2 pp.1–3 Section 2; p.7 Section 3.4; method reading version differs from final publication](https://arxiv.org/pdf/2210.11948v2); [Author-hosted PDF read for methods; bytes identical to downloaded arXiv v2](https://www.arimorcos.com/static/pdfs/wortsman_lofi.pdf) |

## DENSE: Data-Free One-Shot Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/868f2266086530b2c71006ea1908b14a-Abstract-Conference.html) |
| Problem | One-shot federation needs to combine heterogeneous client models without a shared auxiliary dataset or repeated client communication. |
| Mechanism | Train a server generator using ensemble classification, batch-normalization statistics and a teacher-student boundary-disagreement objective; alternate generation and KL-based ensemble-to-student distillation after the client models are uploaded once. |
| Contribution | Supplies a one-shot behavioral-fusion route across differing architectures and a contrast to coordinate averaging or curvature-weighted fusion. |
| Assumptions | Server access to client models and their BN statistics for the stated generation loss, compatible input/output-label semantics and server-side generation/distillation compute; raw auxiliary examples are not required at the server. |
| Evidence boundary | Data-free refers to the absence of raw auxiliary training data at the server, not absence of local training data, BN statistics or server optimization. Visual dissimilarity of generated images does not establish privacy: the paper leaves additional privacy mechanisms and attack analysis for future work. Model access and synthesis quality remain substantive assumptions. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2022/hash/868f2266086530b2c71006ea1908b14a-Abstract-Conference.html); [Final NeurIPS PDF pp.3–6, Sections 2.2–2.3, Equations 1–6 and Algorithm 1: generator losses, client BN statistics, ensemble distillation and explicit privacy discussion](https://proceedings.neurips.cc/paper_files/paper/2022/file/868f2266086530b2c71006ea1908b14a-Paper-Conference.pdf) |

## Deep Neural Network Fusion via Graph Matching with Applications to Model Ensemble and Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v162/liu22k.html) · [Code](https://github.com/Thinklab-SJTU/GAMF) |
| Problem | Layerwise linear matching misses structural relations across neural channels. |
| Mechanism | Quadratic graph matching with graduated assignment, sparse slice-and-scan updates and cycle-consistent multi-model permutations precedes weight fusion. |
| Contribution | GAMF adds second-order structural matching to model fusion and federated aggregation. |
| Assumptions | Accessible compatible layer weights; input/output order is fixed and cross-layer matches are excluded. Multi-model fusion assumes equal model importance. |
| Evidence boundary | The matching problem remains combinatorial and uses an approximate solver. Data-free alignment is not a privacy guarantee, and does not imply all local training or downstream fine-tuning is data-free. |
| Evidence | [Official publication metadata / workshop program](https://proceedings.mlr.press/v162/liu22k.html); [Final proceedings PDF pp.2–5, §2 and §§3.1–3.3, Algorithms 1–2.](https://proceedings.mlr.press/v162/liu22k/liu22k.pdf) |

## Federated Learning With Position-Aware Neurons

| Field | Details |
| --- | --- |
| Venue / year | IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Federated_Learning_With_Position-Aware_Neurons_CVPR_2022_paper.html) |
| Problem | Non-IID local training misaligns neurons before coordinate averaging. |
| Mechanism | Add or multiply fixed sinusoidal encodings at hidden neurons/channels, controlling permutation sensitivity before federated averaging. |
| Contribution | PANs complements post-hoc matching with training-time pre-alignment. |
| Assumptions | Clients use compatible architectures, shared position encodings and a training process that can be modified. |
| Evidence boundary | Not a general merger for existing arbitrary checkpoints. Encoding strength trades alignment against trainability; the paper notes activation/gradient scale and optimizer issues. No privacy mechanism is established. |
| Evidence | [Official publication metadata / workshop program](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Federated_Learning_With_Position-Aware_Neurons_CVPR_2022_paper.html); [Final CVF PDF pp.2–4 (printed 10083–10085), §§2–4; p.8 (10089), Disadvantages and Conclusions.](https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Federated_Learning_With_Position-Aware_Neurons_CVPR_2022_paper.pdf) |

## Fine-tuning Global Model via Data-Free Knowledge Distillation for Non-IID Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_Fine-Tuning_Global_Model_via_Data-Free_Knowledge_Distillation_for_Non-IID_Federated_CVPR_2022_paper.html) |
| Problem | Direct aggregation can lose client knowledge under non-IID data. |
| Mechanism | Alternate conditional-generator training and distillation from client models into the global model; label sampling and class-weighted teacher contributions address label imbalance. |
| Contribution | Adds server-side knowledge transfer after averaging, unlike FedGen generator feedback to clients. |
| Assumptions | Server receives compatible client models and client label-distribution statistics; local training remains data-dependent. |
| Evidence boundary | No raw server training set is required, but models/statistics are exposed and extra generator/student optimization is required. This access arrangement alone is not differential privacy. |
| Evidence | [Publisher-deposited final title, all authors, DOI and pages](https://api.crossref.org/works/10.1109/CVPR52688.2022.00993); [CVF accepted record; alternative pagination 10174–10183](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_Fine-Tuning_Global_Model_via_Data-Free_Knowledge_Distillation_for_Non-IID_Federated_CVPR_2022_paper.html); [PDF pp.3–5, §3, Algorithms 1–2](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Fine-Tuning_Global_Model_via_Data-Free_Knowledge_Distillation_for_Non-IID_Federated_CVPR_2022_paper.pdf) |

## Merging Models with Fisher-Weighted Averaging

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html) |
| Problem | How can weight averaging account for unequal parameter importance? |
| Mechanism | Diagonal Fisher estimates yield a weighted parameter average motivated by a Laplace approximation. |
| Contribution | Provides an importance-aware alternative to uniform averaging. |
| Assumptions | Models share architecture and initialization; Fisher statistics require gradient computations on examples. |
| Evidence boundary | Diagonal local approximations do not capture full parameter interactions; widely separated solutions and statistical estimation cost restrict applicability. |
| Evidence | [Official publication metadata and abstract](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html); [§§2.1–2.4, PDF pp.2–5](https://proceedings.neurips.cc/paper_files/paper/2022/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf) |

## Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2022 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v162/wortsman22a.html) · [Code](https://github.com/mlfoundations/model-soups) |
| Problem | Can models from a fine-tuning hyperparameter sweep be combined instead of selecting only one? |
| Mechanism | Uniform, validation-guided greedy, and learned recipes construct a single weight-space model. |
| Contribution | Establishes a practical connection between compatible fine-tuning solutions and inexpensive deployment. |
| Assumptions | Models share initialization and architecture; greedy selection uses held-out validation data. |
| Evidence boundary | The paper reports weaker gains for some pretraining regimes and shows that weight soups do not inherit ensembles’ calibration improvement. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v162/wortsman22a.html); [§2 Method, PDF pp.2–3; §5 Scope and limitations, PDF p.8](https://proceedings.mlr.press/v162/wortsman22a/wortsman22a.pdf) |

## Wasserstein Barycenter-based Model Fusion and Linear Mode Connectivity of Neural Networks

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2022 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2210.06671) · [Code](https://github.com/SixuLi/WBFusionAndLMC) |
| Problem | Network parameters cannot be directly compared across unaligned hidden units. |
| Mechanism | Alternate weight and transport-coupling updates layerwise; recurrent extensions add Gromov-Wasserstein terms for hidden-to-hidden relations. |
| Contribution | Connects multi-model fusion with Wasserstein/Gromov-Wasserstein barycenters and empirical mode-connectivity analysis. |
| Assumptions | Shared input layer and layer count in the stated fully connected construction; chosen target widths and accessible weights. |
| Evidence boundary | A related alignment foundation, not a complete federated protocol. Architecture-specific constructions and empirical connectivity do not guarantee arbitrary network compatibility or privacy. |
| Evidence | [Official bibliographic identity](https://arxiv.org/abs/2210.06671); [Author preprint pp.4–6, §§2–3; same-input/depth assumption and alternating solver](https://arxiv.org/pdf/2210.06671); [Author publication list, Others: Preprint](https://sixuli.github.io/); [PDF p.1, author code footnote](https://arxiv.org/pdf/2210.06671) |

## Data-Free Knowledge Distillation for Heterogeneous Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2021 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v139/zhu21b.html) · [Code](https://github.com/zhuangdizhu/FedGen) |
| Problem | Federated distillation may require unavailable proxy inputs. |
| Mechanism | Learn a lightweight generator from client predictors and distribute generated latent knowledge. |
| Contribution | Provides a federated knowledge-transfer mechanism without an external proxy dataset. |
| Assumptions | Access to client prediction rules and compatible interfaces for generated latent representations. |
| Evidence boundary | Data-free does not mean information-free or a formal privacy guarantee; the generator is auxiliary, not a generative target model. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v139/zhu21b.html); [PDF pp.1–2: abstract and method overview](https://proceedings.mlr.press/v139/zhu21b/zhu21b.pdf) |

## FedBE: Making Bayesian Model Ensemble Applicable to Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2021 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=dgtpE6gKjHn) · [Code](https://github.com/hongyouc/FedBE) |
| Problem | Averaging local weights loses ensemble information under non-IID client data. |
| Mechanism | Fit Gaussian weights or Dirichlet mixing coefficients; ensemble sampled/client/averaged models and distill to a global student using stochastic weight averaging. |
| Contribution | Combines Bayesian ensemble aggregation with multi-round federated distillation. |
| Assumptions | Compatible weight architectures, local weight access, common initialization and unlabeled server data. |
| Evidence boundary | Requires server data/computation. Robustness concerns non-IID aggregation, not a general Byzantine defense; §6 acknowledges malicious-server privacy vulnerabilities. |
| Evidence | [Official publication metadata / workshop program](https://openreview.net/forum?id=dgtpE6gKjHn); [Author arXiv PDF v4 pp.2–6, §§2–4 and Algorithm 1; p.9, §6.](https://arxiv.org/pdf/2009.01974); [Indexed official PDF first page: Published as a conference paper at ICLR 2021](https://openreview.net/pdf?id=dgtpE6gKjHn) |

## LogME: Practical Assessment of Pre-trained Models for Transfer Learning

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2021 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v139/you21b.html) |
| Problem | How can pretrained feature extractors be assessed efficiently for a new labeled task? |
| Mechanism | Extract target features, estimate maximum marginal likelihood with a Bayesian linear model, and aggregate the evidence into LogME. |
| Contribution | Extends efficient model assessment to classification and regression. |
| Assumptions | Labeled target examples and feature access are available; a linear predictive surrogate is meaningful. |
| Evidence boundary | The score evaluates a linear surrogate on target features; it is not a certificate of fine-tuning outcomes, model complementarity, or trustworthy collaboration. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v139/you21b.html); [§3; §4.1, PDF pp.3–5](http://proceedings.mlr.press/v139/you21b/you21b.pdf) |

## Personalized Cross-Silo Federated Learning on Non-IID Data

| Field | Details |
| --- | --- |
| Venue / year | AAAI Conference on Artificial Intelligence, 2021 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/16960) |
| Problem | How to combine models for clients with different distributions? |
| Mechanism | Section 4 Eqs. (5),(7): u_i=sum_j xi_ij w_j, with off-diagonal xi_ij=alpha A_prime(\|\|w_i-w_j\|\|^2) and a complementary self-weight. A sufficiently small step yields a convex combination, followed by local proximal training. HeurFedAMP substitutes cosine-based attention. |
| Contribution | Similarity-driven mixtures implement personalized inter-model collaboration. |
| Assumptions | Server receives individual parameter sets; clients retain private training data. |
| Evidence boundary | Parameter similarity depends on coordinates; convergence assumptions and the DNN heuristic must be distinguished. Data locality alone is not a formal privacy guarantee. |
| Evidence | [Author/publication metadata](https://ojs.aaai.org/index.php/AAAI/article/view/16960); [PDF pp.3–4, Section 4, Eqs. (5)–(7), Algorithm 1; p.5, Section 6 (HeurFedAMP)](https://cdn.aaai.org/ojs/16960/16960-13-20454-1-2-20210518.pdf) |

## Personalized Federated Learning with First Order Model Optimization

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2021 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=fiHpzZ4ABdk) |
| Problem | Which peer models benefit each client? |
| Mechanism | Section 3 Eq. (3): score peer n by [L_i(theta_i_previous)-L_i(theta_n)] / \|\|theta_n-theta_i_previous\|\|. Clip negative scores, normalize positive scores, and combine received parameters; retain previous parameters when no positive contribution exists. |
| Contribution | Direct first-order approximation for personalized source-model combination. |
| Assumptions | Client-specific validation data and access to received model parameters. |
| Evidence boundary | Validation quality and multiple-model download cost matter; parameter compatibility is required. |
| Evidence | [Author/publication metadata](https://openreview.net/forum?id=fiHpzZ4ABdk); [PDF pp.3–5, Section 3, Eq. (3) and communication/affinity sampling paragraphs; p.1 publication header](https://arxiv.org/pdf/2012.08565v4) |

## Ensemble Distillation for Robust Model Fusion in Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2020 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper/2020/hash/18df51b97ccd68128e994804f3eccc87-Abstract.html) |
| Problem | Combine heterogeneous client models through their predictions. |
| Mechanism | Students learn from averaged teacher logits on unlabeled or generated inputs. |
| Contribution | Supports heterogeneous architecture groups in a federated fusion protocol. |
| Assumptions | Server access to client models and compatible prediction semantics; auxiliary distillation inputs. |
| Evidence boundary | Model exchange can leak information; privacy protections are extensions, not a guarantee of the base algorithm. |
| Evidence | [PDF pp.3–4, §3 algorithm and privacy discussion; §4.1 experimental setup](https://proceedings.neurips.cc/paper/2020/file/18df51b97ccd68128e994804f3eccc87-Paper.pdf) |

## Federated Learning with Matched Averaging

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Learning Representations, 2020 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=BkluqlSFDS) · [Code](https://github.com/IBM/FedMA) |
| Problem | Coordinate averaging ignores hidden-unit permutations in federated CNNs and LSTMs. |
| Mechanism | Bayesian matching aligns channels/hidden states; broadcast and freeze each fused layer while clients retrain later layers, then aggregate the output layer. |
| Contribution | Extends matching-based aggregation beyond PFNM-style fully connected networks. |
| Assumptions | Local weights and retraining data are available; layer types and input/output semantics must support the matching construction. |
| Evidence boundary | Requires layerwise communication and retraining; it is not arbitrary architecture fusion or a model-only one-shot method. No formal privacy mechanism is supplied. |
| Evidence | [Official publication metadata / workshop program](https://openreview.net/forum?id=BkluqlSFDS); [Author arXiv PDF v1 pp.1–5, §§1–2; header states ICLR 2020.](https://arxiv.org/pdf/2002.06440); [Conference paper, ICLR 2020; complete author list; publication/code links](https://research.ibm.com/publications/federated-learning-with-matched-averaging) |

## Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge

| Field | Details |
| --- | --- |
| Venue / year | Conference on Neural Information Processing Systems, 2020 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.neurips.cc/paper/2020/hash/a1d4c20b182ad7137ab3606f0e3fc8a4-Abstract.html) |
| Problem | Small edge devices cannot train a large shared CNN. |
| Mechanism | Alternating optimization combines supervised loss with bidirectional KL distillation; clients transmit extracted features, labels and predictions. |
| Contribution | Group knowledge transfer fuses client knowledge while reducing edge training requirements. |
| Assumptions | Supervised local data, agreed feature tensor dimensions and a server capable of training the larger network. |
| Evidence boundary | Section 5 explicitly leaves privacy analysis unresolved; feature/label exchange is not a privacy guarantee. Communication scales with data volume; very large client counts remain challenging. |
| Evidence | [Official publication metadata / workshop program](https://proceedings.neurips.cc/paper/2020/hash/a1d4c20b182ad7137ab3606f0e3fc8a4-Abstract.html); [Final proceedings PDF p.2 overview; pp.3–5, §3; p.9, §5; p.10 Broader Impact.](https://proceedings.neurips.cc/paper/2020/file/a1d4c20b182ad7137ab3606f0e3fc8a4-Paper.pdf) |

## LEEP: A New Measure to Evaluate Transferability of Learned Representations

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2020 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v119/nguyen20b.html) |
| Problem | How can a pretrained classifier be ranked for a target task without repeated fine-tuning? |
| Mechanism | Compute a log expected empirical prediction score from pretrained classifier outputs and an empirical source-to-target label mapping. |
| Contribution | Provides an inexpensive transferability surrogate. |
| Assumptions | Target labels and pretrained class probabilities are available. |
| Evidence boundary | The discussion notes that architecture and model size also affect transfer but are not captured by the considered scores. Transfer ranking does not establish pairwise fusion compatibility. |
| Evidence | [Official publication metadata and abstract](https://proceedings.mlr.press/v119/nguyen20b.html); [§§2–3; §5.7; §6 Discussions, PDF pp.2–3,8–9](http://proceedings.mlr.press/v119/nguyen20b/nguyen20b.pdf) |

## Model Fusion via Optimal Transport

| Field | Details |
| --- | --- |
| Venue / year | Advances in Neural Information Processing Systems, 2020 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.nips.cc/paper_files/paper/2020/hash/fb2697869f56484404c8ceee2985b01d-Abstract.html) · [Code](https://github.com/sidak/otfusion) |
| Problem | How can neuron correspondences be recovered before averaging independently trained networks? |
| Mechanism | Layerwise transport plans use weight or activation distances and align adjacent-layer parameters before averaging. |
| Contribution | Introduces transport-based alignment, including unequal layer widths. |
| Assumptions | Compatible network structure and output semantics are required; activation-based costs use samples. |
| Evidence boundary | The procedure is greedy by layer because joint alignment is intractable. Weight-only and activation-based variants have different data requirements; arbitrary architectural compatibility is not established. |
| Evidence | [Official publication metadata and abstract](https://proceedings.nips.cc/paper_files/paper/2020/hash/fb2697869f56484404c8ceee2985b01d-Abstract.html); [§§3–4.1, PDF pp.3–6](https://proceedings.neurips.cc/paper_files/paper/2020/file/fb2697869f56484404c8ceee2985b01d-Paper.pdf) |

## Bayesian Nonparametric Federated Learning of Neural Networks

| Field | Details |
| --- | --- |
| Venue / year | International Conference on Machine Learning, 2019 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://proceedings.mlr.press/v97/yurochkin19a.html) · [Code](https://github.com/IBM/probabilistic-federated-neural-matching) |
| Problem | Independently trained neurons are permutation-ambiguous. |
| Mechanism | Beta-Bernoulli priors and MAP assignments solved with the Hungarian algorithm; infer global width and extend matching greedily across layers. |
| Contribution | PFNM connects model-only fusion, neuron matching and adaptive global capacity. |
| Assumptions | Accessible local weights, common input/output semantics and compatible MLP layers; fusion can operate without auxiliary data. |
| Evidence boundary | Demonstrated on relatively small MLPs; CNN/RNN extensions are future work. Weight sharing is not a formal privacy guarantee. |
| Evidence | [Official publication metadata / workshop program](https://proceedings.mlr.press/v97/yurochkin19a.html); [PDF pp.1–5, §§1–3; p.8, §5 Discussion.](https://proceedings.mlr.press/v97/yurochkin19a/yurochkin19a.pdf) |

## FedMD: Heterogenous Federated Learning via Model Distillation

| Field | Details |
| --- | --- |
| Venue / year | International Workshop on Federated Learning for User Privacy and Data Confidentiality at NeurIPS, 2019 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://federated-learning.org/fl-neurips-2019/) |
| Problem | Participants want collaboration while retaining different private architectures. |
| Mechanism | Public-data transfer learning precedes private training; each round averages class scores, distills the consensus locally and revisits private data. |
| Contribution | Early black-box heterogeneous-model collaboration through output consensus. |
| Assumptions | Large labeled public pretraining data, local labeled data and compatible output scores for the collaboration task. |
| Evidence boundary | Sharing predictions is not a formal privacy guarantee. Public-data dependence and repeated local retraining limit applicability. |
| Evidence | [Official publication metadata / workshop program](https://federated-learning.org/fl-neurips-2019/); [Author arXiv PDF v1 pp.1–4, §§1–3 and Algorithm 1.](https://arxiv.org/pdf/1910.03581) |

## Knowledge Amalgamation from Heterogeneous Networks by Common Feature Learning

| Field | Details |
| --- | --- |
| Venue / year | International Joint Conference on Artificial Intelligence, 2019 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.ijcai.org/proceedings/2019/428) |
| Problem | How to consolidate heterogeneous task-specific teachers into one student? |
| Mechanism | Section 4 combines teacher-student MMD feature losses, feature reconstruction, and distillation from concatenated teacher scores. Independently parameterized adapters and a shared extractor align feature interfaces. |
| Contribution | Explicit heterogeneous multi-teacher knowledge amalgamation into one student. |
| Assumptions | Unlabeled input images and access to teacher features and outputs. |
| Evidence boundary | Unlabeled data are still required; overlapping class outputs need explicit handling. The reviewed method is not a federated protocol. |
| Evidence | [Author/publication metadata](https://www.ijcai.org/proceedings/2019/428); [PDF pp.2–4, Sections 3 and 4, Eqs. (1)–(6); official main-track metadata](https://www.ijcai.org/proceedings/2019/0428.pdf) |

## Task2Vec: Task Embedding for Meta-Learning

| Field | Details |
| --- | --- |
| Venue / year | Proceedings of the IEEE/CVF International Conference on Computer Vision, 2019 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | A |
| Reading depth | section-reviewed |
| Links | [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html) |
| Problem | How can tasks be compared to support pretrained-model selection? |
| Mechanism | A diagonal Fisher-information embedding supports task distances; Model2Vec associates candidate models with this task space. |
| Contribution | Connects task characterization with model recommendation. |
| Assumptions | Labeled examples and a specified probe architecture are available. |
| Evidence boundary | Probe choice and task collection affect the representation; the authors identify broader real-world task coverage as an open question. This is selection infrastructure, not evidence that selected models can safely be fused. |
| Evidence | [Official publication metadata and abstract](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html); [§§3–4; §4.1; §5 Discussion, PDF pp.3–8](http://openaccess.thecvf.com/content_ICCV_2019/papers/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.pdf) |

## One-Shot Federated Learning

| Field | Details |
| --- | --- |
| Venue / year | 2nd Workshop on Machine Learning on the Phone and other Consumer Devices at NeurIPS, 2018 |
| Publication status | Workshop |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/1902.11175) |
| Problem | How to combine fully trained local models in one communication round? |
| Mechanism | Section 3 averages predictions of selected local models. With unlabeled server proxy data, Eq. (3) fits an SVM student to ensemble scores by squared-error minimization. |
| Contribution | Early explicit one-shot federated ensemble-to-student formulation. |
| Assumptions | Selected model access; proxy data for compression; common prediction semantics. |
| Evidence boundary | Experiments focus on binary RBF-SVM tasks. Retaining an ensemble differs from producing one compressed model; model access is not inherently private. |
| Evidence | [Author/publication metadata](https://arxiv.org/abs/1902.11175); [PDF pp.2–3, Section 3, ensemble-selection rules and distillation Eq. (3)](https://arxiv.org/pdf/1902.11175v2); [One-shot Federated Learning entry: workshop at NeurIPS, 2018](https://www.cs.cmu.edu/~atalwalk/research.html) |

## Deep Model Fusion: A Survey

| Field | Details |
| --- | --- |
| Venue / year | IEEE Transactions on Neural Networks and Learning Systems, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | B |
| Reading depth | section-reviewed |
| Links | [Paper](https://ieeexplore.ieee.org/document/11268959) |
| Problem | Deep parameter and prediction fusion. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Alignment, loss geometry, averaging and output combination. Robustness and privacy motivations; final-version breadth remains unassessed. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Reading of the 2023 author version cannot establish omissions in the 2026 version. |
| Evidence | [Sections 2–6; pp. 27–29](https://arxiv.org/pdf/2309.15698); [Abstract; publication metadata](https://ieeexplore.ieee.org/document/11268959) |

## From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models

| Field | Details |
| --- | --- |
| Venue / year | Findings of the Association for Computational Linguistics: EMNLP 2026, 2026 |
| Publication status | Findings |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://aclanthology.org/2026.findings-emnlp.722/) |
| Problem | Fusion producing one target independent of complete source models at inference. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Alignment and source compatibility across all three signals. Risk transfer, privacy, ownership, screening and safety metrics. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Explicitly excludes ordinary source-retaining ensembles and routing. |
| Evidence | [§2, pp.15179–15180](https://aclanthology.org/2026.findings-emnlp.722.pdf); [§5 p.15186; Tables 8–9 p.15202](https://aclanthology.org/2026.findings-emnlp.722.pdf) |

## Knowledge transmission and fusion in large models: research advances and challenges

| Field | Details |
| --- | --- |
| Venue / year | Information Fusion, 2026 |
| Publication status | Early access; metadata conflict |
| Bibliographic verification | partial |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253526006950) |
| Problem | Knowledge transmission and fusion across six learning paradigms. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Knowledge states and heterogeneous carriers. Privacy, unreliable sources, resources and constrained decisions. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Only publisher abstract/introduction excerpts inspected; metadata conflict unresolved. |
| Evidence | [Introduction, numbered contributions (1)–(3)](https://www.sciencedirect.com/science/article/pii/S1566253526006950); [Publication entry for DOI 104819](https://weiping-ding.github.io/) |

## Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications, and Opportunities

| Field | Details |
| --- | --- |
| Venue / year | ACM Computing Surveys, 2026 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://dl.acm.org/doi/10.1145/3787849) |
| Problem | Model-merging mechanisms, theory and cross-domain applications. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Architecture transformation, alignment, subspaces and routing. Adversarial learning, ownership and trustworthy merging explicit. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Final-version differences remain unassessed; trustworthy merging is already a named agenda. |
| Evidence | [§§2–3, pp.4–14](https://arxiv.org/pdf/2408.07666); [§5.1 p.21; §5.6 pp.27–28; §6 p.29](https://arxiv.org/pdf/2408.07666) |

## Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2026 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2603.09938) |
| Problem | LLM-era parameter merging and supporting ecosystem. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Geometry, compatibility, alignment and representation-guided methods. Safety, bias, failure diagnostics and alignment preservation. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Preprint; cited method claims require primary-paper checks. |
| Evidence | [§6.2 p.37; §§7.3–7.5 pp.46–49](https://arxiv.org/pdf/2603.09938) |

## A Survey on Collaborating Small and Large Language Models for Performance, Cost-effectiveness, Cloud-edge Privacy, and Trustworthiness

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2025 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2510.13890) |
| Problem | Small/large language-model collaboration. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Role allocation, guidance and fusion architectures. Privacy, safety-guided decoding and guardian–generator designs. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Preprint explicitly marked under review; no publication inferred. |
| Evidence | [§§2–5 pp.3–13; §7 p.14](https://arxiv.org/pdf/2510.13890) |

## A Survey on Model MoErging: Recycling and Routing Among Specialized Experts for Collaborative Learning

| Field | Details |
| --- | --- |
| Venue / year | Transactions on Machine Learning Research, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://openreview.net/forum?id=u0azVc9Y0y) |
| Problem | Recycling and routing among pretrained expert models. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Data access, granularity, selection and aggregation interfaces. Malicious additions and access assumptions are discussed. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Proposed continual infrastructure is not evidence it is already implemented. |
| Evidence | [§2 pp.2–8](https://arxiv.org/pdf/2408.07057); [§7 pp.23–24](https://arxiv.org/pdf/2408.07057) |

## Collaborative Inference and Learning between Edge SLMs and Cloud LLMs: A Survey of Algorithms, Execution, and Open Challenges

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2025 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2507.16731) |
| Problem | Edge/cloud language-model inference and learning. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Task/token interfaces, parameter compatibility and bidirectional transfer. Privacy/security mechanisms and resource constraints. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Preprint; edge-cloud scope does not establish general model-network guarantees. |
| Evidence | [§3.3; §3.5; §§4–5 pp.19–25](https://arxiv.org/pdf/2507.16731) |

## From Task-Specific Models to Unified Systems: A Review of Model Merging Approaches

| Field | Details |
| --- | --- |
| Venue / year | arXiv, 2025 |
| Publication status | Preprint |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://arxiv.org/abs/2503.08998) |
| Problem | Parameter merging approaches. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Parameter correspondence and interference. No dedicated multi-property governance analysis established in inspected text. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Short preprint; negative coverage judgments remain limited to inspected sections. |
| Evidence | [§2 pp.2–7; §3 p.7](https://arxiv.org/pdf/2503.08998) |

## One-shot Federated Learning Methods: A Practical Guide

| Field | Details |
| --- | --- |
| Venue / year | International Joint Conference on Artificial Intelligence, 2025 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | Pending verification |
| Reading depth | section-reviewed |
| Links | [Paper](https://www.ijcai.org/proceedings/2025/1174) |
| Problem | How single-round federated methods address data/model heterogeneity and communication constraints. |
| Mechanism | Comparative survey; it proposes no new model fusion operator. |
| Contribution | A related survey for comparing the one-shot protocol axis, synthesis/ensembling roles, and heterogeneity assumptions. |
| Assumptions | Taxonomy covers broader one-shot federation, including data-level approaches outside the present repository's fusion-method scope. |
| Evidence boundary | Its four categories mix operators, auxiliary-model roles and communication protocols; copying every covered FL method would exceed the user's fusion-only scope. |
| Evidence | [Official publication identity and authors](https://www.ijcai.org/proceedings/2025/1174); [Official Survey Track; Section 3 taxonomy, Figure 1 and Table 1; Sections 3.1–3.4 and 4; printed pp. 10575–10579](https://www.ijcai.org/proceedings/2025/1174.pdf) |

## A Survey of Trustworthy Federated Learning: Issues, Solutions, and Challenges

| Field | Details |
| --- | --- |
| Venue / year | ACM Transactions on Intelligent Systems and Technology, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | C |
| Reading depth | section-reviewed |
| Links | [Paper](https://dl.acm.org/doi/10.1145/3678181) |
| Problem | Trustworthiness throughout federated learning. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | FL actors, gradients and model interfaces support the threat analysis. Detailed threats, defenses and fairness notions. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Publisher HTML sections inspected; PDF fetch denied. No exhaustive absence claim. |
| Evidence | [§§3–6](https://dl.acm.org/doi/10.1145/3678181); [§4 future directions; §5 contribution fairness](https://dl.acm.org/doi/10.1145/3678181) |

## Emerging trends in federated learning: from model fusion to federated X learning

| Field | Details |
| --- | --- |
| Venue / year | International Journal of Machine Learning and Cybernetics, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | None |
| Reading depth | section-reviewed |
| Links | [Paper](https://link.springer.com/article/10.1007/s13042-024-02119-1) |
| Problem | FL aggregation and intersections with other learning paradigms. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Adaptive weighting, attention, clustering and Bayesian correspondence. Fairness and privacy/security receive explicit sections. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Its learning-paradigm taxonomy should not be mislabeled as trust-blind. |
| Evidence | [§1.1 and Table 1, pp.3770–3771](https://link.springer.com/content/pdf/10.1007/s13042-024-02119-1.pdf); [§3.7; §5.2; §6.5](https://link.springer.com/content/pdf/10.1007/s13042-024-02119-1.pdf) |

## Model aggregation techniques in federated learning: A comprehensive survey

| Field | Details |
| --- | --- |
| Venue / year | Future Generation Computer Systems, 2024 |
| Publication status | Published |
| Bibliographic verification | verified |
| CCF 2026 | C |
| Reading depth | abstract-reviewed |
| Links | [Paper](https://www.sciencedirect.com/science/article/pii/S0167739X23003333) |
| Problem | Federated aggregation methods and applications. |
| Mechanism | Survey synthesis; not a new fusion algorithm. |
| Contribution | Aggregation and data heterogeneity are explicit scope. Low-quality/malicious contributions and privacy/security are explicit. |
| Assumptions | Coverage statements apply only to the explicitly inspected version and sections. |
| Evidence boundary | Publisher abstract only; full text retrieval failed. Unknown coverage is not absence. |
| Evidence | [Abstract and highlights](https://www.sciencedirect.com/science/article/pii/S0167739X23003333) |
