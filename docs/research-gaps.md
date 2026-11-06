# Research questions and evidence gaps

The present evidence supports a comparative survey of how source-model information justifies a collaboration decision, and when changes require that decision to be reconsidered. It does not establish that a Representation → Governance → Evolution framework is unprecedented. Earlier surveys already cover compatibility, trustworthy merging, dynamic routing and continual development; their positive coverage is documented in [the survey comparison](prior-surveys.md).

The questions below distinguish observed limitations of specific studies, inferences from comparison, and proposed evaluation work. They are not claims that no method anywhere addresses the problem. The bibliography remains selective, and some relevant records are only abstract-reviewed or metadata candidates.

## From representation to decisions

### 1. Individual utility versus joint suitability

Task2Vec, LEEP and LogME characterize a task or estimate the suitability of an individual pretrained model. Their inputs and proxies differ: probe-network sensitivity, source-label probabilities and Bayesian evidence over target features. Alignment methods answer another question. Optimal-transport fusion and Git Re-Basin require structural or symmetry conditions; those conditions are not established by a high transferability score. [Task2Vec, §§3–4](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html), [LEEP, §§2–3 and §6](https://proceedings.mlr.press/v119/nguyen20b.html), [LogME, §3](https://proceedings.mlr.press/v139/you21b.html), [OT Fusion, §§3–4](https://proceedings.nips.cc/paper_files/paper/2020/hash/fb2697869f56484404c8ceee2985b01d-Abstract.html), [Git Re-Basin, §§3–4](https://openreview.net/forum?id=CQsmMYmlP5T)

The comparative inference is that **individual transfer utility, pairwise compatibility and marginal contribution to a model set need separate evidence**. A proposed evaluation would ask whether a representation predicts actual combination outcomes on held-out model pairs or sets, with task labels and calibration access matched. This protocol has not been implemented in this project. It should record confidence and failure cases rather than convert similarity into a safety certificate.

### 2. Access conditions constrain safeguards

“Dataless” and “data-free” describe different access arrangements. RegMean uses statistics computed from examples even when raw examples are unavailable at merging. FedGen removes the need for an external proxy dataset but still exchanges model-derived knowledge. RoFL addresses a distinct tension: encrypted contributions can conceal information needed to enforce robustness constraints, motivating protected checks of particular update bounds. [RegMean, §3](https://openreview.net/forum?id=FCnohuR6AnM), [FedGen, pp.1–2](https://proceedings.mlr.press/v139/zhu21b.html), [RoFL, §§I–III of the reviewed author version](https://doi.org/10.1109/SP46215.2023.10179400)

A useful comparison therefore starts with the available information and the actor allowed to inspect it. The proposed synthesis will map each safeguard to its required signals, protected object, trust assumptions and cost. An unresolved question is how these requirements change when switching between weight merging, distillation and persistent routing. A cross-operator guarantee is not established by the current records, and absence of raw-data sharing is not a substitute for a privacy argument.

## From constraints to acceptance

### 3. Trust objectives require compatible meanings

SafeMERGE and LED-Merging bring safety considerations into the merge procedure, with reference-model and architecture conditions. Ditto studies performance differences across devices and poisoning robustness; agnostic federated learning considers a specified family of client-distribution mixtures. These are different units of protection and different notions of success. [SafeMERGE, §2 and Limitations](https://aclanthology.org/2026.findings-acl.1761/), [LED-Merging, method and §6](https://aclanthology.org/2025.acl-long.1055/), [Ditto, §§2–3](https://proceedings.mlr.press/v139/li21h.html), [Agnostic FL, agnostic objective](https://proceedings.mlr.press/v97/mohri19a.html)

The analysis should distinguish multi-objective empirical trade-offs from formal composition of guarantees. It should also separate a property measured after fusion from a constraint that changes source selection, coefficients or fallback behavior. The current evidence does not justify a field-wide assertion that combined guarantees are impossible or absent. The proposed contribution is a transparent account of which combinations are supported, which assumptions conflict, and which remain untested. A weighted average of unrelated trust scores would not supply that account.

### 4. Component checks do not settle composition

MergeBackdoor demonstrates an evaluated setting in which components suppress trigger behavior before merging but expose it after composition. DAM incorporates backdoor concerns into the merging subspace. These results make the tested unit important: evaluating source models and evaluating the composed model answer different questions. They do not imply that every combination is vulnerable or that one defense covers every attacker. [MergeBackdoor, threat/scope discussion](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin), [DAM, §§2–4](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36f7c3d80c1ba329ab8cf7b96e63a0fa-Abstract-Conference.html)

A proposed acceptance protocol would retain source-level and system-level outcomes, test the declared attacker capabilities, and record rejection or fallback when evidence is inadequate. This is a suggested evaluation design, not a deployed defense. Its value must be tested against credible baselines and its detection errors, validation-data requirements and overhead reported.

## From adaptation to revalidation

### 5. Adaptation has different temporal meanings

RouteLLM learns a routing rule from preferences and selects models per query; that does not imply online policy learning. GraphRouter uses historical interactions and supports newly introduced models in its evaluated setting. MetaRouter adapts to implicit preferences but optimizes a one-step reward. LoRM, TIME and OPCM instead study explicit sequences of training or merging operations under their respective compatibility and protocol assumptions. [RouteLLM, §3.1 and §5](https://openreview.net/forum?id=8sSqNntaMr), [GraphRouter, §3 and §6](https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html), [MetaRouter, §4 and §6](https://ijcai.org/proceedings/2026/673), [LoRM, §3](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d79b8c42f61b51722992705022134ef3-Abstract-Conference.html), [TIME, §§3–4](https://openaccess.thecvf.com/content/CVPR2025/html/Dziadzio_How_to_Merge_Your_Multimodal_Models_Over_Time_CVPR_2025_paper.html), [OPCM, §3](https://papers.nips.cc/paper_files/paper/2025/hash/7611a3cb5d733e628081431445cb01fd-Abstract-Conference.html)

The proposed classification records **what changes**, **which history is retained**, **what feedback updates the policy**, and **which guarantees or measurements are checked again**. A fixed router with input-dependent choices, a periodically refitted router and a stateful continual system should not receive the same label. Long-horizon reliability is a hypothesis to evaluate under model arrivals, task shifts and delayed feedback; it cannot be inferred from one-step utility or a static task average.

### 6. Comparable evaluation needs explicit events

Existing infrastructure should be reused. FusionBench separates model pools, algorithms and task evaluation. RouterBench reuses recorded model outputs to compare cost–quality trade-offs, while acknowledging limits such as missing live latency and throughput. KnOTS highlights a different protocol issue: per-task evaluation can conceal confusion when task-specific label sets are not supplied. [FusionBench, §2](https://www.jmlr.org/papers/v26/25-1243.html), [RouterBench, §§3 and 6](https://arxiv.org/abs/2403.12031), [KnOTS, §5.3](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d4f8a5109c5083b5307fcd0bddae7a7-Abstract-Conference.html)

The proposed extension is an event-indexed evaluation record: initial composition, source addition, source replacement, distribution shift, detected compromise and requested withdrawal. At each event, report task utility, per-source or per-group losses where defined, threat-specific outcomes, decision changes and total selection/query/update cost. Mark unsupported events as unassessed. This is a future protocol proposal, not a new benchmark or an executed experiment, and it does not make heterogeneous methods comparable without matching their access budgets and output systems.

## Coverage debts and decisions

Provenance, licensing, contributor withdrawal and removal of learned influence need stronger primary-paper coverage. A model pool dropping a component is not evidence that a distilled or merged model has forgotten it. Existing surveys already raise removal and continuing development; the present corpus is insufficient to decide how completely those obligations are solved across operators. [MoErging, §7](https://arxiv.org/pdf/2408.07057)

The closest overlapping surveys also require further reconciliation: complete text for the transmission–fusion survey and the FGCS aggregation review, and final-version checks where analysis currently uses older author manuscripts. These are limitations of this review, not deficiencies attributed to those papers. The working contribution is therefore **a problem-driven comparative synthesis of evidence, decisions and revalidation**. A stronger novelty statement is neither needed nor supported at this stage.
