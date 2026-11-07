# Awesome Trustworthy Model Fusion and Collaboration

A curated research collection on how existing models are represented, governed under explicit trust constraints, and updated through collaboration.

**Representation → Governance → Evolution**

[Scope](docs/scope-and-definitions.md) · [Taxonomy](docs/taxonomy.md) · [Federated literature](docs/federated-literature.md) · [Detailed records](docs/papers.md) · [Related surveys](docs/prior-surveys.md) · [Benchmarks](docs/benchmarks.md) · [Search protocol](docs/search-protocol.md) · [Coverage audit](docs/coverage-audit.md) · [Audit](docs/reference-audit.md) · [Report](docs/literature-report.md) · [Contributing](CONTRIBUTING.md)

## Collection status

Curation snapshot: 2026-11-07. The database contains 120 records; 116 satisfy both metadata and CCF-edition verification for the ranked catalogue. Remaining records are retained as pending, not classified as CCF-None by default.

This is a staged, evidence-tracked collection, not a claim of exhaustive coverage. Federated learning alone is not an inclusion criterion: methods must directly concern model fusion; general FL methods are excluded from the method catalogue. See the [scope correction](docs/scope-correction.md). Venue ranks use the **CCF 2026 seventh edition** only. Findings, workshop and other excluded tracks do not inherit the main-conference rank. Publication status and review depth are separate fields.

The unpublished survey manuscript is maintained locally and is not distributed in this repository.

## I. Fusion Representation

### Parameter and Representation Alignment

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Bi-level Personalization for Federated Foundation Models: A Task-vector Aggregation Approach** | AAAI | A | Published | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39991) |
| 2026 | **Breaking the Aggregation Bottleneck in Federated Recommendation: A Personalized Model Merging Approach** | AAAI | A | Published | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/38472) |
| 2026 | **Communication-Efficient Personalized Adaptation via Federated-Local Model Merging** | NeurIPS | A | Published | [Paper](https://neurips.cc/virtual/2026/poster/150059) |
| 2026 | **FedMerge: Federated Model Merging for Personalization** | AAAI | A | Published | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39113) · [Code](https://github.com/shutong043/FedMerge) |
| 2026 | **RegMean++: Enhancing Effectiveness and Generalization of Regression Mean for Model Merging** | TMLR | None | Published | [Paper](https://openreview.net/forum?id=H5lDsSCS9i) · [Code](https://github.com/nthehai01/RegMean-plusplus) |
| 2025 | **FedAWA: Adaptive Optimization of Aggregation Weights in Federated Learning Using Client Vectors** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Shi_FedAWA_Adaptive_Optimization_of_Aggregation_Weights_in_Federated_Learning_Using_CVPR_2025_paper.html) |
| 2025 | **Intrinsic Training Signals for Federated Learning Aggregation** | ICIAP | None | Published | [Paper](https://link.springer.com/chapter/10.1007/978-3-032-10185-3_11) |
| 2025 | **Many-Task Federated Fine-Tuning via Unified Task Vectors** | FedGenAI-IJCAI | None | Workshop | [Paper](https://federated-learning.org/FedGenAI-ijcai-2025/) |
| 2025 | **Model merging with SVD to tie the Knots** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html) · [Code](https://github.com/gstoica27/KnOTS) |
| 2025 | **PLeaS - Merging Models with Permutations and Least Squares** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Nasery_PLeaS_-_Merging_Models_with_Permutations_and_Least_Squares_CVPR_2025_paper.html) |
| 2025 | **Representation Surgery in Model Merging with Probabilistic Modeling** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v267/wei25c.html) |
| 2024 | **FedFisher: Leveraging Fisher Information for One-Shot Federated Learning** | AISTATS | C | Published | [Paper](https://proceedings.mlr.press/v238/jhunjhunwala24a.html) |
| 2024 | **FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Model Fusion** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/31e6e0c09325a3be16d93f84e40e0c7e-Abstract-Conference.html) · [Code](https://github.com/wizard1203/FuseFL) |
| 2024 | **Local Superior Soups: A Catalyst for Model Merging in Cross-Silo Federated Learning** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/24f7b98aef14fcd68acf3c941af1b59e-Abstract-Conference.html) · [Code](https://github.com/ubc-tea/Local-Superior-Soups) |
| 2024 | **Representation Surgery for Multi-Task Model Merging** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v235/yang24t.html) |
| 2024 | **Transformer Fusion with Optimal Transport** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7e0af0d1bc0ec2a90fc294be2e00447e-Abstract-Conference.html) · [Code](https://github.com/graldij/transformer-fusion) |
| 2024 | **ZipIt! Merging Models from Different Tasks without Training** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html) |
| 2023 | **Dataless Knowledge Fusion by Merging Weights of Language Models** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=FCnohuR6AnM) · [Code](https://github.com/bloomberg/dataless-model-merging) |
| 2023 | **Git Re-Basin: Merging Models modulo Permutation Symmetries** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=CQsmMYmlP5T) · [Code](https://github.com/samuela/git-re-basin) |
| 2022 | **Deep Neural Network Fusion via Graph Matching with Applications to Model Ensemble and Federated Learning** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v162/liu22k.html) · [Code](https://github.com/Thinklab-SJTU/GAMF) |
| 2022 | **Federated Learning With Position-Aware Neurons** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Federated_Learning_With_Position-Aware_Neurons_CVPR_2022_paper.html) |
| 2022 | **Wasserstein Barycenter-based Model Fusion and Linear Mode Connectivity of Neural Networks** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2210.06671) · [Code](https://github.com/SixuLi/WBFusionAndLMC) |
| 2021 | **Data-Free Knowledge Distillation for Heterogeneous Federated Learning** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v139/zhu21b.html) · [Code](https://github.com/zhuangdizhu/FedGen) |
| 2020 | **Federated Learning with Matched Averaging** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=BkluqlSFDS) · [Code](https://github.com/IBM/FedMA) |
| 2020 | **Model Fusion via Optimal Transport** | NeurIPS | A | Published | [Paper](https://proceedings.nips.cc/paper_files/paper/2020/hash/fb2697869f56484404c8ceee2985b01d-Abstract.html) · [Code](https://github.com/sidak/otfusion) |
| 2019 | **Bayesian Nonparametric Federated Learning of Neural Networks** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v97/yurochkin19a.html) · [Code](https://github.com/IBM/probabilistic-federated-neural-matching) |

### Foundations and Scope

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Can Model Merging Improve Aggregation in DiLoCo?** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2607.03011) |
| 2025 | **Task Arithmetic Through The Lens Of One-Shot Federated Learning** | TMLR | None | Published | [Paper](https://openreview.net/forum?id=Cgyo7S7Oy0) · [Code](https://github.com/SilviaTao/one_shot_fl_task_arithmetic) |
| 2023 | **lo-fi: distributed fine-tuning without communication** | TMLR | None | Published | [Paper](https://openreview.net/forum?id=1U0aPkBVz0) |

### Model Similarity and Compatibility Assessment

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Representational Alignment Across Model Layers and Brain Regions with Multi-Level Optimal Transport** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8611049567e7339a88fc68a06100fac1-Abstract-Conference.html) |
| 2025 | **Exploring Model Kinship for Merging Large Language Models** | Findings EMNLP | None | Findings | [Paper](https://aclanthology.org/2025.findings-emnlp.32/) |
| 2024 | **AdaMerging: Adaptive Model Merging for Multi-Task Learning** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/62868cc2fc1eb5cdf321d05b4b88510c-Abstract-Conference.html) |
| 2024 | **Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v235/yu24p.html) |
| 2023 | **TIES-Merging: Resolving Interference When Merging Models** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1644c9af28ab7916874f6fd6228a9bcf-Abstract-Conference.html) · [Code](https://github.com/prateeky2806/ties-merging) |
| 2022 | **Merging Models with Fisher-Weighted Averaging** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html) |
| 2022 | **Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v162/wortsman22a.html) · [Code](https://github.com/mlfoundations/model-soups) |

### Structured Model Representation and Organization

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2025 | **Identifying and Reusing Learnwares Across Different Label Spaces** | IJCAI | B | Published | [Paper](https://ijcai.org/proceedings/2025/638) |
| 2023 | **Editing Models with Task Arithmetic** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=6t0Kwf8-jrj) |

### Task–Model Association and Selection

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2025 | **Never Start from Scratch: Expediting On-Device LLM Personalization via Explainable Model Selection** | MobiSys | B | Published | [Paper](https://dl.acm.org/doi/10.1145/3711875.3729132) |
| 2021 | **LogME: Practical Assessment of Pre-trained Models for Transfer Learning** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v139/you21b.html) |
| 2020 | **LEEP: A New Measure to Evaluate Transferability of Learned Representations** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v119/nguyen20b.html) |

### Behavioral Alignment and Distillation

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2024 | **MetaFed: Federated Learning Among Federations With Cyclic Knowledge Distillation for Personalized Healthcare** | TNNLS | B | Published | [Paper](https://ieeexplore.ieee.org/document/10197230/) · [Code](https://github.com/microsoft/PersonalizedFL) |
| 2022 | **DENSE: Data-Free One-Shot Federated Learning** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/868f2266086530b2c71006ea1908b14a-Abstract-Conference.html) |
| 2022 | **Fine-tuning Global Model via Data-Free Knowledge Distillation for Non-IID Federated Learning** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_Fine-Tuning_Global_Model_via_Data-Free_Knowledge_Distillation_for_Non-IID_Federated_CVPR_2022_paper.html) |
| 2021 | **FedBE: Making Bayesian Model Ensemble Applicable to Federated Learning** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=dgtpE6gKjHn) · [Code](https://github.com/hongyouc/FedBE) |
| 2020 | **Ensemble Distillation for Robust Model Fusion in Federated Learning** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper/2020/hash/18df51b97ccd68128e994804f3eccc87-Abstract.html) |
| 2020 | **Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper/2020/hash/a1d4c20b182ad7137ab3606f0e3fc8a4-Abstract.html) |
| 2019 | **FedMD: Heterogenous Federated Learning via Model Distillation** | FL-NeurIPS | None | Workshop | [Paper](https://federated-learning.org/fl-neurips-2019/) |

### Model Capability Profiling and Characterization

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2023 | **Model Spider: Learning to Rank Pre-Trained Models Efficiently** | NeurIPS | A | Published | [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/2c71b14637802ed08eaa3cf50342b2b9-Abstract-Conference.html) · [Code](https://github.com/zhangyikaii/Model-Spider) |
| 2019 | **Task2Vec: Task Embedding for Meta-Learning** | ICCV | A | Published | [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html) |

## II. Trustworthy Fusion Governance

### Robust and Secure Fusion

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Defending against Backdoor Attacks via Module Switching** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbe25fa0e7c7084049276888a09acc8d-Abstract-Conference.html) · [Code](https://github.com/weijun-l/module-switching-defense) |
| 2026 | **SafeMERGE: Preserving Safety Alignment in Fine-Tuned Large Language Models via Selective Layer-Wise Model Merging** | Findings of ACL | None | Findings | [Paper](https://aclanthology.org/2026.findings-acl.1761/) |
| 2025 | **From Purity to Peril: Backdooring Merged Models From "Harmless" Benign Components** | USENIX Security | A | Published | [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin) · [Code](https://github.com/wljLlla/MergeBackdoor) |
| 2025 | **LED-Merging: Mitigating Safety-Utility Conflicts in Model Merging with Location-Election-Disjoint** | ACL | A | Published | [Paper](https://aclanthology.org/2025.acl-long.1055/) · [Code](https://github.com/MqLeet/LED-Merging) |
| 2025 | **Mitigating the Backdoor Effect for Multi-Task Model Merging via Safety-Aware Subspace** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36f7c3d80c1ba329ab8cf7b96e63a0fa-Abstract-Conference.html) |
| 2024 | **BadMerging: Backdoor Attacks Against Model Merging** | CCS | A | Published | [Paper](https://doi.org/10.1145/3658644.3690284) |
| 2024 | **Here’s a Free Lunch: Sanitizing Backdoored Models with Model Merge** | Findings of ACL | None | Findings | [Paper](https://aclanthology.org/2024.findings-acl.894/) |
| 2024 | **Model Merging and Safety Alignment: One Bad Model Spoils the Bunch** | Findings of EMNLP | None | Findings | [Paper](https://aclanthology.org/2024.findings-emnlp.762/) |
| 2021 | **Cronus: Robust and Heterogeneous Collaborative Learning with Black-Box Knowledge Transfer** | NFFL at NeurIPS | None | Workshop | [Paper](https://neurips2021workshopfl.github.io/NFFL-2021/paper.html) |

### Explainable and Auditable Fusion

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Defending Unauthorized Model Merging via Dual-Stage Weight Protection** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html) |
| 2026 | **Making Open-Source Text LLM Watermarks Durable Against Merging** | NeurIPS | A | Accepted; proceedings pending | [Paper](https://neurips.cc/virtual/2026/poster/155690) |
| 2025 | **MergePrint: Merge-Resistant Fingerprints for Robust Black-box Ownership Verification of Large Language Models** | ACL | A | Published | [Paper](https://aclanthology.org/2025.acl-long.342/) |
| 2025 | **RouteMark: A Fingerprint for Intellectual Property Attribution in Routing-based Model Merging** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2508.01784) |
| 2024 | **Have You Merged My Model? On The Robustness of Large Language Model IP Protection Methods Against Model Merging** | LAMPS | None | Workshop | [Paper](https://doi.org/10.1145/3689217.3690614) · [Code](https://github.com/ThuCCSLab/MergeGuard) |

### Privacy-Preserving Fusion

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Differentially Private Model Merging** | NeurIPS | A | Accepted; proceedings pending | [Paper](https://neurips.cc/virtual/2026/poster/149241) |
| 2026 | **When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2608.26655) |
| 2025 | **Be Cautious When Merging Unfamiliar LLMs: A Phishing Model Capable of Stealing Privacy** | Findings of ACL | None | Findings | [Paper](https://aclanthology.org/2025.findings-acl.713/) |
| 2025 | **Personalized Language Models via Privacy-Preserving Evolutionary Model Merging** | EMNLP | B | Published | [Paper](https://aclanthology.org/2025.emnlp-main.1747/) |
| 2024 | **Complementary Knowledge Distillation for Robust and Privacy-Preserving Model Serving in Vertical Federated Learning** | AAAI | A | Published | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29958) |
| 2024 | **PrivFusion: Privacy-Preserving Model Fusion via Decentralized Federated Graph Matching** | TKDE | A | Published | [Paper](https://doi.org/10.1109/tkde.2024.3430819) |
| 2023 | **FedAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning** | TNNLS | B | Published | [Paper](https://doi.org/10.1109/tnnls.2021.3129371) |
| 2018 | **Scalable Private Learning with PATE** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=rkZB1XbRZ) |

### Fairness-Aware Fusion

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **FairMerging: Rethinking Model Merging through the Lens of Fairness** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v306/liu26dl.html) |
| 2025 | **An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation** | PACLIC | None | Published | [Paper](https://aclanthology.org/2025.paclic-1.24/) |
| 2024 | **Model Trip: Enhancing Privacy and Fairness in Model Fusion Across Multi-Federations for Trustworthy Global Healthcare** | ICDE | A | Published | [Paper](https://doi.org/10.1109/icde60146.2024.00177) |

### Constraint-Aware Fusion Optimization

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2025 | **A Unified Approach to Routing and Cascading for LLMs** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v267/dekoninck25a.html) |
| 2025 | **MAP: Low-compute Model Merging with Amortized Pareto Fronts via Quadratic Approximation** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3724221b623bf1966e92cd266ac6177-Abstract-Conference.html) |
| 2025 | **Mix Data or Merge Models? Balancing the Helpfulness, Honesty, and Harmlessness of Large Language Model via Model Merging** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3948805bc5220206f5bfc465de0b1b7-Abstract-Conference.html) |
| 2025 | **Pareto Merging: Multi-Objective Optimization for Preference-Aware Model Merging** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v267/chen25af.html) |
| 2024 | **DapperFL: Domain Adaptive Federated Learning with Model Fusion Pruning for Edge Devices** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/17a1a1439421f1837e10cd612bf92861-Abstract-Conference.html) · [Code](https://github.com/jyzgh/DapperFL) |
| 2024 | **WARM: On the Benefits of Weight Averaged Reward Models** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v235/rame24a.html) |
| 2023 | **Revisiting Weighted Aggregation in Federated Learning with Neural Networks** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v202/li23s.html) |
| 2023 | **Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e12a3b98b67e8395f639fde4c2b03168-Abstract-Conference.html) |
| 2019 | **Learning Private Neural Language Modeling with Attentive Aggregation** | IJCNN | C | Published | [Paper](https://doi.org/10.1109/IJCNN.2019.8852464) · [Code](https://github.com/shaoxiongji/fed-att) |

### Trustworthy Model Selection and Orchestration

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2025 | **SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading** | EMNLP | B | Published | [Paper](https://aclanthology.org/2025.emnlp-main.531/) |

## III. Collaborative Evolution

### Continual Model Adaptation

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **FedSEAM: Federated Continual Learning of LLMs via Subspace Expert Agreement Merging** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2610.33496) |
| 2026 | **Unlocking the Potential of Continual Model Merging: An ODE Perspective** | ICML | A | Published | [Paper](https://proceedings.mlr.press/v306/lin26o.html) · [Code](https://github.com/yohbii/ODE-M) |
| 2025 | **Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d79b8c42f61b51722992705022134ef3-Abstract-Conference.html) · [Code](https://github.com/aimagelab/fed-mammoth) |

### Adaptive Model Selection and Routing

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning** | IJCAI | B | Published | [Paper](https://ijcai.org/proceedings/2026/673) |
| 2025 | **GraphRouter: A Graph-based Router for LLM Selections** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html) · [Code](https://github.com/ulab-uiuc/GraphRouter) |
| 2025 | **REMEDY: Recipe Merging Dynamics in Large Vision-Language Models** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4065a881baab1744bfba208a4361bbb1-Abstract-Conference.html) |
| 2025 | **RouteLLM: Learning to Route LLMs from Preference Data** | ICLR | A | Published | [Paper](https://openreview.net/forum?id=8sSqNntaMr) · [Code](https://github.com/lm-sys/RouteLLM) |
| 2024 | **FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance** | TMLR | None | Published | [Paper](https://openreview.net/forum?id=cSimKw5p6R) · [Code](https://github.com/stanford-futuredata/FrugalGPT) |
| 2024 | **Twin-Merging: Dynamic Integration of Modular Expertise in Model Merging** | NeurIPS | A | Published | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8fcd17eb91bae20d9826786d7d6be799-Abstract-Conference.html) · [Code](https://github.com/LZY-the-boys/Twin-Merging) |

### Model Collaboration and Network Evolution

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **MoFedNet: Semantic Link is All Models Need** | JCST | B | Published | [Paper](https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-5684-5) |
| 2026 | **On The Surprising Effectiveness of a Single Global Merging in Decentralized Learning** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/437d9bde2999f6e3e854e09f250261a5-Abstract-Conference.html) |
| 2024 | **DIMAT: Decentralized Iterative Merging-And-Training for Deep Learning Models** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Saadati_DIMAT_Decentralized_Iterative_Merging-And-Training_for_Deep_Learning_Models_CVPR_2024_paper.html) |

### Knowledge Accumulation and Reuse

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity** | ICLR | A | Published | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d0da30e312b75a3fffd9e9191f8bc1b0-Abstract-Conference.html) · [Code](https://github.com/zihuanqiu/NUFILT) |
| 2025 | **Continual Model Merging without Data: Dual Projections for Balancing Stability and Plasticity** | NeurIPS | A | Published | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/37d9f19150fce07bced2a81fc87d47a6-Abstract-Conference.html) |
| 2025 | **Evolutionary optimization of model merging recipes** | NMI | None | Published | [Paper](https://www.nature.com/articles/s42256-024-00975-8) · [Code](https://github.com/SakanaAI/evolutionary-model-merge) |
| 2025 | **How to Merge Your Multimodal Models Over Time?** | CVPR | A | Published | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.html) |
| 2025 | **Merging on the Fly Without Retraining: A Sequential Approach to Scalable Continual Model Merging** | NeurIPS | A | Published | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/7611a3cb5d733e628081431445cb01fd-Abstract-Conference.html) · [Code](https://github.com/tanganke/opcm) |

### Model Lifecycle and Evolution

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2024 | **Towards Making Learnware Specification and Market Evolvable** | AAAI | A | Published | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29298) |

## IV. Related Surveys

### Scope and Taxonomy Comparisons

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Deep Model Fusion: A Survey** | TNNLS | B | Published | [Paper](https://ieeexplore.ieee.org/document/11268959) |
| 2026 | **From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models** | Findings of EMNLP | None | Findings | [Paper](https://aclanthology.org/2026.findings-emnlp.722/) |
| 2026 | **Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications, and Opportunities** | CSUR | None | Published | [Paper](https://dl.acm.org/doi/10.1145/3787849) |
| 2026 | **Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2603.09938) |
| 2025 | **A Survey on Collaborating Small and Large Language Models for Performance, Cost-effectiveness, Cloud-edge Privacy, and Trustworthiness** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2510.13890) |
| 2025 | **A Survey on Model MoErging: Recycling and Routing Among Specialized Experts for Collaborative Learning** | TMLR | None | Published | [Paper](https://openreview.net/forum?id=u0azVc9Y0y) |
| 2025 | **Collaborative Inference and Learning between Edge SLMs and Cloud LLMs: A Survey of Algorithms, Execution, and Open Challenges** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2507.16731) |
| 2025 | **From Task-Specific Models to Unified Systems: A Review of Model Merging Approaches** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2503.08998) |
| 2024 | **A Survey of Trustworthy Federated Learning: Issues, Solutions, and Challenges** | TIST | C | Published | [Paper](https://dl.acm.org/doi/10.1145/3678181) |
| 2024 | **Emerging trends in federated learning: from model fusion to federated X learning** | IJMLC | None | Published | [Paper](https://link.springer.com/article/10.1007/s13042-024-02119-1) |
| 2024 | **Model aggregation techniques in federated learning: A comprehensive survey** | FGCS | C | Published | [Paper](https://www.sciencedirect.com/science/article/pii/S0167739X23003333) |

## V. Benchmarks, Datasets and Tools

### Evaluation Frameworks and Tools

| Year | Paper | Venue | CCF 2026 | Status | Links |
| --- | --- | --- | :---: | --- | --- |
| 2025 | **FusionBench: A Unified Library and Comprehensive Benchmark for Deep Model Fusion** | JMLR | A | Published | [Paper](https://www.jmlr.org/papers/v26/25-1243.html) · [Code](https://github.com/tanganke/fusion_bench) |
| 2024 | **RouterBench: A Benchmark for Multi-LLM Routing System** | arXiv | None | Preprint | [Paper](https://arxiv.org/abs/2403.12031) · [Code](https://github.com/withmartian/routerbench) |

## Pending verification

These records remain visible while the stated checks are unresolved. Reading depth alone does not make bibliographic metadata pending.

| Year | Paper | Venue | CCF 2026 | Unresolved check | Links |
| --- | --- | --- | :---: | --- | --- |
| 2026 | **Knowledge transmission and fusion in large models: research advances and challenges** | Information Fusion | None | Bibliographic identity: partial | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253526006950) |
| 2024 | **Arcee’s MergeKit: A Toolkit for Merging Large Language Models** | EMNLP Industry | Pending | CCF venue/track applicability | [Paper](https://aclanthology.org/2024.emnlp-industry.36/) · [Code](https://github.com/arcee-ai/mergekit) |
| 2024 | **Beimingwu: A Learnware Dock System** | KDD Applied | Pending | CCF venue/track applicability | [Paper](https://doi.org/10.1145/3637528.3671617) · [Code](https://github.com/Learnware-LAMDA/Beimingwu) |
| 2023 | **FedTAM: Decentralized Federated Learning with a Feature Attention Based Multi-teacher Knowledge Distillation for Healthcare** | ICPADS | Pending | CCF venue/track applicability | [Paper](https://ieeexplore.ieee.org/document/10476260/) |

## Verification and maintenance

Bibliographic facts, review depth, source locators, assumptions and boundaries are stored in [data/papers.json](data/papers.json). The [CSV](data/papers.csv), [BibTeX](data/references.bib), README and detailed notes are generated views. Edit the JSON source, not the generated outputs.

```sh
python scripts/validate_papers.py
python scripts/check_duplicates.py
python scripts/generate_readme.py
python scripts/export_bibtex.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion and verification rules. Original repository materials are released under the [MIT license](LICENSE); linked publications and third-party tools retain their respective rights.

<!-- source-sha256: 0b5d69bf5c166e5aa4b0ca2eb9ac0ea3486a0be0e52d417c5a37033ff49089c5 -->
