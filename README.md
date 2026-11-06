# Awesome Trustworthy Model Fusion and Collaboration

A curated research collection on how existing models are represented, governed under explicit trust constraints, and updated through collaboration.

**Representation → Governance → Evolution**

[Scope](docs/scope-and-definitions.md) · [Taxonomy](docs/taxonomy.md) · [Detailed records](docs/papers.md) · [Related surveys](docs/prior-surveys.md) · [Benchmarks](docs/benchmarks.md) · [Search protocol](docs/search-protocol.md) · [Audit](docs/reference-audit.md) · [Report](docs/literature-report.md) · [Contributing](CONTRIBUTING.md)

## Collection status

Curation snapshot: 2026-11-07. The database contains 93 records; 88 satisfy both metadata and CCF-edition verification for the ranked catalogue. Remaining records are retained as pending, not classified as CCF-None by default.

This is a staged, evidence-tracked collection, not a claim of exhaustive coverage. Venue ranks use the **CCF 2026 seventh edition** only. Findings, workshop and other excluded tracks do not inherit the main-conference rank. Publication status and review depth are separate fields.

The unpublished survey manuscript is maintained locally and is not distributed in this repository.

## I. Fusion Representation

### Parameter and Representation Alignment

- **RegMean++: Enhancing Effectiveness and Generalization of Regression Mean for Model Merging** — TMLR, 2026, CCF-None. [Paper](https://openreview.net/forum?id=H5lDsSCS9i) · [Code](https://github.com/nthehai01/RegMean-plusplus)
- **Model merging with SVD to tie the Knots** — ICLR, 2025, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html) · [Code](https://github.com/gstoica27/KnOTS)
- **PLeaS - Merging Models with Permutations and Least Squares** — CVPR, 2025, CCF-A. [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Nasery_PLeaS_-_Merging_Models_with_Permutations_and_Least_Squares_CVPR_2025_paper.html)
- **Representation Surgery in Model Merging with Probabilistic Modeling** — ICML, 2025, CCF-A. [Paper](https://proceedings.mlr.press/v267/wei25c.html)
- **Representation Surgery for Multi-Task Model Merging** — ICML, 2024, CCF-A. [Paper](https://proceedings.mlr.press/v235/yang24t.html)
- **Transformer Fusion with Optimal Transport** — ICLR, 2024, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7e0af0d1bc0ec2a90fc294be2e00447e-Abstract-Conference.html) · [Code](https://github.com/graldij/transformer-fusion)
- **ZipIt! Merging Models from Different Tasks without Training** — ICLR, 2024, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html)
- **Dataless Knowledge Fusion by Merging Weights of Language Models** — ICLR, 2023, CCF-A. [Paper](https://openreview.net/forum?id=FCnohuR6AnM) · [Code](https://github.com/bloomberg/dataless-model-merging)
- **Git Re-Basin: Merging Models modulo Permutation Symmetries** — ICLR, 2023, CCF-A. [Paper](https://openreview.net/forum?id=CQsmMYmlP5T) · [Code](https://github.com/samuela/git-re-basin)
- **Data-Free Knowledge Distillation for Heterogeneous Federated Learning** — ICML, 2021, CCF-A. [Paper](https://proceedings.mlr.press/v139/zhu21b.html) · [Code](https://github.com/zhuangdizhu/FedGen)
- **Model Fusion via Optimal Transport** — NeurIPS, 2020, CCF-A. [Paper](https://proceedings.nips.cc/paper_files/paper/2020/hash/fb2697869f56484404c8ceee2985b01d-Abstract.html) · [Code](https://github.com/sidak/otfusion)

### Model Similarity and Compatibility Assessment

- **Representational Alignment Across Model Layers and Brain Regions with Multi-Level Optimal Transport** — ICLR, 2026, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8611049567e7339a88fc68a06100fac1-Abstract-Conference.html)
- **Exploring Model Kinship for Merging Large Language Models** — Findings EMNLP, 2025, CCF-None. [Paper](https://aclanthology.org/2025.findings-emnlp.32/)
- **AdaMerging: Adaptive Model Merging for Multi-Task Learning** — ICLR, 2024, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/62868cc2fc1eb5cdf321d05b4b88510c-Abstract-Conference.html)
- **Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch** — ICML, 2024, CCF-A. [Paper](https://proceedings.mlr.press/v235/yu24p.html)
- **TIES-Merging: Resolving Interference When Merging Models** — NeurIPS, 2023, CCF-A. [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1644c9af28ab7916874f6fd6228a9bcf-Abstract-Conference.html) · [Code](https://github.com/prateeky2806/ties-merging)
- **Merging Models with Fisher-Weighted Averaging** — NeurIPS, 2022, CCF-A. [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html)
- **Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** — ICML, 2022, CCF-A. [Paper](https://proceedings.mlr.press/v162/wortsman22a.html) · [Code](https://github.com/mlfoundations/model-soups)

### Structured Model Representation and Organization

- **Identifying and Reusing Learnwares Across Different Label Spaces** — IJCAI, 2025, CCF-B. [Paper](https://ijcai.org/proceedings/2025/638)
- **Editing Models with Task Arithmetic** — ICLR, 2023, CCF-A. [Paper](https://openreview.net/forum?id=6t0Kwf8-jrj)

### Model Capability Profiling and Characterization

- **Model Spider: Learning to Rank Pre-Trained Models Efficiently** — NeurIPS, 2023, CCF-A. [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/2c71b14637802ed08eaa3cf50342b2b9-Abstract-Conference.html) · [Code](https://github.com/zhangyikaii/Model-Spider)
- **Task2Vec: Task Embedding for Meta-Learning** — ICCV, 2019, CCF-A. [Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html)

### Task–Model Association and Selection

- **LogME: Practical Assessment of Pre-trained Models for Transfer Learning** — ICML, 2021, CCF-A. [Paper](https://proceedings.mlr.press/v139/you21b.html)
- **LEEP: A New Measure to Evaluate Transferability of Learned Representations** — ICML, 2020, CCF-A. [Paper](https://proceedings.mlr.press/v119/nguyen20b.html)

### Behavioral Alignment and Distillation

- **Ensemble Distillation for Robust Model Fusion in Federated Learning** — NeurIPS, 2020, CCF-A. [Paper](https://proceedings.neurips.cc/paper/2020/hash/18df51b97ccd68128e994804f3eccc87-Abstract.html)

### Foundations and Scope

- **Communication-Efficient Learning of Deep Networks from Decentralized Data** — AISTATS, 2017, CCF-C. [Paper](https://proceedings.mlr.press/v54/mcmahan17a.html)

## II. Trustworthy Fusion Governance

### Robust and Secure Fusion

- **Defending against Backdoor Attacks via Module Switching** — ICLR, 2026, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbe25fa0e7c7084049276888a09acc8d-Abstract-Conference.html) · [Code](https://github.com/weijun-l/module-switching-defense)
- **SafeMERGE: Preserving Safety Alignment in Fine-Tuned Large Language Models via Selective Layer-Wise Model Merging** — Findings of ACL, 2026, CCF-None. [Paper](https://aclanthology.org/2026.findings-acl.1761/)
- **From Purity to Peril: Backdooring Merged Models From "Harmless" Benign Components** — USENIX Security, 2025, CCF-A. [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin) · [Code](https://github.com/wljLlla/MergeBackdoor)
- **LED-Merging: Mitigating Safety-Utility Conflicts in Model Merging with Location-Election-Disjoint** — ACL, 2025, CCF-A. [Paper](https://aclanthology.org/2025.acl-long.1055/) · [Code](https://github.com/MqLeet/LED-Merging)
- **Mitigating the Backdoor Effect for Multi-Task Model Merging via Safety-Aware Subspace** — ICLR, 2025, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36f7c3d80c1ba329ab8cf7b96e63a0fa-Abstract-Conference.html)
- **BadMerging: Backdoor Attacks Against Model Merging** — CCS, 2024, CCF-A. [Paper](https://doi.org/10.1145/3658644.3690284)
- **Here’s a Free Lunch: Sanitizing Backdoored Models with Model Merge** — Findings of ACL, 2024, CCF-None. [Paper](https://aclanthology.org/2024.findings-acl.894/)
- **Model Merging and Safety Alignment: One Bad Model Spoils the Bunch** — Findings of EMNLP, 2024, CCF-None. [Paper](https://aclanthology.org/2024.findings-emnlp.762/)
- **FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping** — NDSS, 2021, CCF-A. [Paper](https://www.ndss-symposium.org/ndss-paper/fltrust-byzantine-robust-federated-learning-via-trust-bootstrapping/)
- **The Limitations of Federated Learning in Sybil Settings** — RAID, 2020, CCF-B. [Paper](https://www.usenix.org/conference/raid2020/presentation/fung) · [Code](https://github.com/DistributedML/FoolsGold)
- **Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent** — NeurIPS, 2017, CCF-A. [Paper](https://proceedings.neurips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)

### Explainable and Auditable Fusion

- **Defending Unauthorized Model Merging via Dual-Stage Weight Protection** — CVPR, 2026, CCF-A. [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html)
- **Making Open-Source Text LLM Watermarks Durable Against Merging** — NeurIPS, 2026, CCF-A · Accepted; proceedings pending. [Paper](https://neurips.cc/virtual/2026/poster/155690)
- **FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning** — ICCV, 2025, CCF-A. [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Hoefler_FedXDS_Leveraging_Model_Attribution_Methods_to_counteract_Data_Heterogeneity_in_ICCV_2025_paper.html)
- **MergePrint: Merge-Resistant Fingerprints for Robust Black-box Ownership Verification of Large Language Models** — ACL, 2025, CCF-A. [Paper](https://aclanthology.org/2025.acl-long.342/)
- **RouteMark: A Fingerprint for Intellectual Property Attribution in Routing-based Model Merging** — arXiv, 2025, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2508.01784)
- **Have You Merged My Model? On The Robustness of Large Language Model IP Protection Methods Against Model Merging** — LAMPS, 2024, CCF-None · Workshop. [Paper](https://doi.org/10.1145/3689217.3690614) · [Code](https://github.com/ThuCCSLab/MergeGuard)
- **ShapleyFL: Robust Federated Learning Based on Shapley Value** — KDD, 2023, CCF-A. [Paper](https://doi.org/10.1145/3580305.3599500)

### Privacy-Preserving Fusion

- **Differentially Private Model Merging** — NeurIPS, 2026, CCF-A · Accepted; proceedings pending. [Paper](https://neurips.cc/virtual/2026/poster/149241)
- **When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy** — arXiv, 2026, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2608.26655)
- **Be Cautious When Merging Unfamiliar LLMs: A Phishing Model Capable of Stealing Privacy** — Findings of ACL, 2025, CCF-None. [Paper](https://aclanthology.org/2025.findings-acl.713/)
- **Personalized Language Models via Privacy-Preserving Evolutionary Model Merging** — EMNLP, 2025, CCF-B. [Paper](https://aclanthology.org/2025.emnlp-main.1747/)
- **Complementary Knowledge Distillation for Robust and Privacy-Preserving Model Serving in Vertical Federated Learning** — AAAI, 2024, CCF-A. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29958)
- **FedAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning** — TNNLS, 2023, CCF-B. [Paper](https://doi.org/10.1109/tnnls.2021.3129371)
- **RoFL: Robustness of Secure Federated Learning** — IEEE S&P, 2023, CCF-A. [Paper](https://doi.org/10.1109/sp46215.2023.10179400)
- **Scalable Private Learning with PATE** — ICLR, 2018, CCF-A. [Paper](https://openreview.net/forum?id=rkZB1XbRZ)
- **Practical Secure Aggregation for Privacy-Preserving Machine Learning** — CCS, 2017, CCF-A. [Paper](https://doi.org/10.1145/3133956.3133982)

### Fairness-Aware Fusion

- **FairMerging: Rethinking Model Merging through the Lens of Fairness** — ICML, 2026, CCF-A. [Paper](https://proceedings.mlr.press/v306/liu26dl.html)
- **An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation** — PACLIC, 2025, CCF-None. [Paper](https://aclanthology.org/2025.paclic-1.24/)
- **Ditto: Fair and Robust Federated Learning Through Personalization** — ICML, 2021, CCF-A. [Paper](https://proceedings.mlr.press/v139/li21h.html)
- **Agnostic Federated Learning** — ICML, 2019, CCF-A. [Paper](https://proceedings.mlr.press/v97/mohri19a.html)

### Constraint-Aware Fusion Optimization

- **A Unified Approach to Routing and Cascading for LLMs** — ICML, 2025, CCF-A. [Paper](https://proceedings.mlr.press/v267/dekoninck25a.html)
- **Mix Data or Merge Models? Balancing the Helpfulness, Honesty, and Harmlessness of Large Language Model via Model Merging** — NeurIPS, 2025, CCF-A. [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3948805bc5220206f5bfc465de0b1b7-Abstract-Conference.html)
- **WARM: On the Benefits of Weight Averaged Reward Models** — ICML, 2024, CCF-A. [Paper](https://proceedings.mlr.press/v235/rame24a.html)

### Trustworthy Model Selection and Orchestration

- **SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading** — EMNLP, 2025, CCF-B. [Paper](https://aclanthology.org/2025.emnlp-main.531/)

## III. Collaborative Evolution

### Adaptive Model Selection and Routing

- **Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning** — IJCAI, 2026, CCF-B. [Paper](https://ijcai.org/proceedings/2026/673)
- **GraphRouter: A Graph-based Router for LLM Selections** — ICLR, 2025, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html) · [Code](https://github.com/ulab-uiuc/GraphRouter)
- **REMEDY: Recipe Merging Dynamics in Large Vision-Language Models** — ICLR, 2025, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4065a881baab1744bfba208a4361bbb1-Abstract-Conference.html)
- **RouteLLM: Learning to Route LLMs from Preference Data** — ICLR, 2025, CCF-A. [Paper](https://openreview.net/forum?id=8sSqNntaMr) · [Code](https://github.com/lm-sys/RouteLLM)
- **FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance** — TMLR, 2024, CCF-None. [Paper](https://openreview.net/forum?id=cSimKw5p6R) · [Code](https://github.com/stanford-futuredata/FrugalGPT)
- **Twin-Merging: Dynamic Integration of Modular Expertise in Model Merging** — NeurIPS, 2024, CCF-A. [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8fcd17eb91bae20d9826786d7d6be799-Abstract-Conference.html) · [Code](https://github.com/LZY-the-boys/Twin-Merging)

### Knowledge Accumulation and Reuse

- **Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity** — ICLR, 2026, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d0da30e312b75a3fffd9e9191f8bc1b0-Abstract-Conference.html) · [Code](https://github.com/zihuanqiu/NUFILT)
- **Continual Model Merging without Data: Dual Projections for Balancing Stability and Plasticity** — NeurIPS, 2025, CCF-A. [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/37d9f19150fce07bced2a81fc87d47a6-Abstract-Conference.html)
- **Evolutionary optimization of model merging recipes** — NMI, 2025, CCF-None. [Paper](https://www.nature.com/articles/s42256-024-00975-8) · [Code](https://github.com/SakanaAI/evolutionary-model-merge)
- **How to Merge Your Multimodal Models Over Time?** — CVPR, 2025, CCF-A. [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.html)
- **Merging on the Fly Without Retraining: A Sequential Approach to Scalable Continual Model Merging** — NeurIPS, 2025, CCF-A. [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/7611a3cb5d733e628081431445cb01fd-Abstract-Conference.html) · [Code](https://github.com/tanganke/opcm)

### Continual Model Adaptation

- **Unlocking the Potential of Continual Model Merging: An ODE Perspective** — ICML, 2026, CCF-A. [Paper](https://proceedings.mlr.press/v306/lin26o.html) · [Code](https://github.com/yohbii/ODE-M)
- **Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning** — ICLR, 2025, CCF-A. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d79b8c42f61b51722992705022134ef3-Abstract-Conference.html) · [Code](https://github.com/aimagelab/fed-mammoth)

### Model Lifecycle and Evolution

- **Towards Making Learnware Specification and Market Evolvable** — AAAI, 2024, CCF-A. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29298)

## IV. Related Surveys

### Scope and Taxonomy Comparisons

- **Deep Model Fusion: A Survey** — TNNLS, 2026, CCF-B. [Paper](https://ieeexplore.ieee.org/document/11268959)
- **From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models** — Findings of EMNLP, 2026, CCF-None. [Paper](https://aclanthology.org/2026.findings-emnlp.722/)
- **Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications, and Opportunities** — CSUR, 2026, CCF-None. [Paper](https://dl.acm.org/doi/10.1145/3787849)
- **Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions** — arXiv, 2026, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2603.09938)
- **A Survey on Collaborating Small and Large Language Models for Performance, Cost-effectiveness, Cloud-edge Privacy, and Trustworthiness** — arXiv, 2025, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2510.13890)
- **A Survey on Model MoErging: Recycling and Routing Among Specialized Experts for Collaborative Learning** — TMLR, 2025, CCF-None. [Paper](https://openreview.net/forum?id=u0azVc9Y0y)
- **Collaborative Inference and Learning between Edge SLMs and Cloud LLMs: A Survey of Algorithms, Execution, and Open Challenges** — arXiv, 2025, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2507.16731)
- **From Task-Specific Models to Unified Systems: A Review of Model Merging Approaches** — arXiv, 2025, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2503.08998)
- **A Survey of Trustworthy Federated Learning: Issues, Solutions, and Challenges** — TIST, 2024, CCF-C. [Paper](https://dl.acm.org/doi/10.1145/3678181)
- **Emerging trends in federated learning: from model fusion to federated X learning** — IJMLC, 2024, CCF-None. [Paper](https://link.springer.com/article/10.1007/s13042-024-02119-1)
- **Model aggregation techniques in federated learning: A comprehensive survey** — FGCS, 2024, CCF-C. [Paper](https://www.sciencedirect.com/science/article/pii/S0167739X23003333)

## V. Benchmarks, Datasets and Tools

### Evaluation Frameworks and Tools

- **FusionBench: A Unified Library and Comprehensive Benchmark for Deep Model Fusion** — JMLR, 2025, CCF-A. [Paper](https://www.jmlr.org/papers/v26/25-1243.html) · [Code](https://github.com/tanganke/fusion_bench)
- **RouterBench: A Benchmark for Multi-LLM Routing System** — arXiv, 2024, CCF-None · Preprint. [Paper](https://arxiv.org/abs/2403.12031) · [Code](https://github.com/withmartian/routerbench)

## Verification and maintenance

Bibliographic facts, review depth, source locators, assumptions and boundaries are stored in [data/papers.json](data/papers.json). The [CSV](data/papers.csv), [BibTeX](data/references.bib), README and detailed notes are generated views. Edit the JSON source, not the generated outputs.

```sh
python scripts/validate_papers.py
python scripts/check_duplicates.py
python scripts/generate_readme.py
python scripts/export_bibtex.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion and verification rules. Original repository materials are released under the [MIT license](LICENSE); linked publications and third-party tools retain their respective rights.

<!-- source-sha256: 2df8c2faa703e872190a95145d1c6ab200113391abe1a48f55347dccc90ca586 -->
