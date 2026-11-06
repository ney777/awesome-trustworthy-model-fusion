# Benchmarks and tools

Resources serve different purposes: a model pool, a replay dataset, a fusion harness, and a construction toolkit should not be treated as interchangeable benchmarks. Source versions, access rights, calibration information and search budgets define the valid comparison.

| Resource | Role | Useful evaluation | Boundary |
|---|---|---|---|
| [FusionBench](https://www.jmlr.org/papers/v26/25-1243.html) | Shared algorithm, model-pool and task interfaces | Repeatable fusion comparisons in the supplied configurations | No automatic coverage of every privacy, fairness, security or lifecycle property |
| [RouterBench](https://arxiv.org/abs/2403.12031) | Preprint benchmark using recorded model outputs | Predictive routing and cascading cost–quality studies | Fixed responses/pricing; main objectives omit latency and throughput |
| [MergeKit](https://aclanthology.org/2024.emnlp-industry.36/) | Merge recipes and memory-conscious execution | Reproducible candidate construction | A toolkit, not a quality/safety certificate; Industry CCF applicability remains pending |
| [Beimingwu](https://doi.org/10.1145/3637528.3671617) | Model specifications, organization, identification and reuse system | External capability organization and supported reuse workflows | Model-market support does not certify every contributor; ADS CCF applicability pending |
| [KnOTS](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html) | Method with per-task and joint-task protocols | Detect cross-task confusion under common-base LoRA conditions | Task identity and available labels affect the evaluated capability |
| [MergeBackdoor](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin) | Composition-attack study | Test behavior after a specified combination | Use the exact attack/model assumptions recorded in the master database; not unrestricted safety testing |

## Proposed extension

An event-indexed protocol could record arrivals, replacements, distribution changes, suspected compromise and source withdrawal. It would retain source versions, permitted access, construction/selection/test splits, decision evidence, update cost and per-event outcomes. This is a research proposal, not an implemented benchmark or a reported experiment.

Unsupported events should be marked unassessed. Removing a model from a router, deleting a checkpoint, and removing learned influence from a fused target are different tasks. Accuracy, privacy accounting, group loss, attack success, ownership detection and resource costs require separate operational definitions; no aggregate “trust score” is supplied here.
