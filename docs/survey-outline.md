# Survey outline

**Working title:** Trustworthy Model Fusion and Collaboration: A Survey of Representation, Governance, and Evolution

**Status:** Phase 2 analytical outline. The comparison supports a problem-driven synthesis, not a priority claim or a validated new framework. [Prior surveys](prior-surveys.md) document substantial overlap; [research questions](research-gaps.md) distinguish observed results from proposals. The corresponding working manuscript has now been drafted locally; it is excluded from the public repository. This public outline retains the analytical plan and evidence requirements.

## Central argument

Multiple models can be useful individually without being compatible, acceptable or reliable as a changing system. The survey will examine three linked questions:

1. **Representation:** What information makes model capability, compatibility and relationships assessable?
2. **Governance:** Given that information and the permitted access, which collaborations are acceptable under specified objectives and threats?
3. **Evolution:** When models, tasks or feedback change, what must be updated and what evidence must be checked again?

The thread connecting the sections is **evidence → decision → revalidation**. This is an analytical lens for comparing existing work. It does not assume that all methods implement a loop, use a graph, or satisfy the same trust requirements.

## Scope and comparison units

| Comparison unit | Inclusion condition | Required distinction |
| --- | --- | --- |
| Fused target | Knowledge from multiple models is consolidated through parameters, modules, representations or behavior | Source-independent inference versus partially retained branches |
| Persistent collaboration system | Explicit model-selection, knowledge-exchange or composition decisions govern reusable models | Fixed input-dependent policy versus feedback-updated policy |
| Federated protocol | Autonomous participants operate under a specified information/interaction arrangement | Training-time aggregation, model-asset reuse and deployment evidence |
| Supporting mechanism | Directly informs model characterization, constraints or evaluation | Foundation or related mechanism, not automatically a complete fusion system |
| Frontier proposal | Explicit relation to the three questions, with evidence status stated | Research agenda versus implemented and evaluated capability |

Model-internal feature or tensor alignment and external task–model relationships belong to different comparison columns. Parameter count, output paradigm, shared initialization, tokenizer, label space and access rights are cross-cutting conditions. Ordinary multi-agent task assignment, generic RAG and generic online learning enter only when the model-level connection is explicit.

## Section plan

### I. Introduction

**Question:** Why is successful capability reuse insufficient to establish trustworthy collaboration over time?

Build the motivation from three contrasts: individual utility versus joint compatibility; component evaluation versus composed behavior; per-query adaptation versus continuing system improvement. Use the reviewed representation, merging-security and routing/continual examples, with source-specific bounds. Compare the nearest surveys positively before stating the scope difference. Contributions should promise comparative taxonomy, conditional technical synthesis and an evidence-grounded evaluation agenda, without “first” or “unified framework” priority claims.

**Output:** Table I, survey comparison; a short scope statement. **Transition:** Reuse requires an explicit comparison unit and information contract.

### II. Foundations and problem formulation

**Question:** What assets, interfaces, participants, decisions and changing conditions are being compared?

Define source models, optional target model, persistent system, available information, operator, trust objective, threat model and change event. Separate scientific assumptions from deployment constraints. A minimal record may contain `(sources, task, access, operator, output, trust assumptions, evidence, history)`; it is bookkeeping for analysis, not a claim that every paper solves one optimization problem.

Distinguish federated aggregation from independent checkpoint reuse, compressed fusion from source-retaining inference, and property measurement from a formal guarantee. Explain the search, version, inclusion and evidence-depth protocol. Do not label the corpus systematic or exhaustive without executing such a protocol.

**Output:** Terminology/setting table and inclusion rules. **Transition:** Different interfaces expose different evidence about capability and compatibility.

### III. Fusion Representation

**Question:** Which model descriptions are sufficient for the decision they support?

Organize the analysis by external capability characterization, task–model association, pairwise compatibility, internal alignment and structured organization. Compare Task2Vec/LEEP/LogME/Model Spider as assessment infrastructure with matching and alignment methods such as OT Fusion, Git Re-Basin, Transformer Fusion, ZipIt and KnOTS. Explain differences in labels, probe networks, features, calibration examples, weights, architecture and shared initialization.

Treat task vectors, feature correspondences and model-relationship graphs as distinct representations. A similarity score or successful individual transfer does not establish safe combination. Compare source-independent target models with partially shared or routed systems when output structure changes cost.

**Output:** Table II, representation purpose × access × compatibility × cost × demonstrated decision. **Transition:** Available evidence describes possibilities; governance determines which possibilities are acceptable.

### IV. Trustworthy Fusion Governance

**Question:** How do trust objectives alter selection, combination and acceptance decisions?

Begin with a decision distinction: post-hoc measurement, objective-driven optimization, constraint enforcement and explicit rejection/fallback. Then analyze privacy, security/robustness, fairness, reliability and provenance through their protected objects and assumptions. Compare privacy-related interfaces and proofs; source-aware versus merge-aware attacks; safety–utility procedures; client versus group versus contributor objectives; and the provenance of models, data-dependent statistics and decision evidence.

Use FedAUX and PrivFusion for channel-specific fusion privacy, MergeBackdoor and DAM for composition-specific threats, SafeMERGE and LED-Merging for safety-conditioned merging, and FairMerging for a fusion-specific fairness objective. Model Trip remains abstract-reviewed; PrivFusion mechanism reading is explicitly tied to its identified author version. General FL security, optimization and fairness methods are outside the method scope.

**Output:** Table III, objective × protected object × threat × mechanism × decision × evidence × residual risk. **Transition:** Accepted decisions remain conditional on the model pool, task and trust assumptions.

### V. Collaborative Evolution

**Question:** What persists, what changes, and what is learned from collaboration history?

Separate fixed input-dependent routing, feedback-conditioned selection, sequential incorporation of experts and continuing updates to representations or policies. Compare RouteLLM, GraphRouter and MetaRouter with LoRM, TIME, OPCM and DOP using explicit state, feedback, update and evaluation horizons. An evolutionary search algorithm for a single merge is not automatically a long-running collaborative system.

Discuss retention, order effects, new-source adaptation and resource growth within demonstrated settings. Treat dynamic topology, source withdrawal, rollback and revalidation according to evidence status; do not portray all as solved by continual merging. Attribute any proposed event-based evaluation to this survey's agenda.

**Output:** Table IV, change event × persistent state × feedback × update × retention/risk evidence. **Transition:** Different histories and interfaces demand condition-matched evaluation.

### VI. Evaluation, benchmarks and applications

**Question:** Under what conditions do comparisons support a meaningful conclusion?

Distinguish a task dataset, a source-model pool, a merger benchmark, a router benchmark and a deployment toolkit. Use FusionBench, RouterBench and method-specific protocols to analyze model/task access, labels, query cost, candidate selection and data separation. Report target inference cost alongside teacher, calibration, search and update costs. Discuss per-task or per-source retention, group losses when defined, threat-specific outcomes and uncertainty rather than one aggregate trust score.

Propose an event-indexed extension for arrivals, replacements, shifts, compromise and withdrawal, explicitly labeled unimplemented. Applications should expose constraints: medical centers, scientific collaboration and edge/cloud systems are illustrative settings, not claims of clinical benefit or real federation without protocol evidence.

**Output:** Table V, benchmark capabilities and limits; a separate proposed-protocol panel. **Transition:** The gaps follow from mismatches between needed decisions and available evidence.

### VII. Open challenges and research agenda

**Question:** Which failures motivate specific, testable research priorities?

Derive the agenda from the six questions in [research-gaps.md]: joint suitability, access-dependent safeguards, compatible trust objectives, composition-level acceptance, temporal adaptation and event-indexed evaluation. For each, state what is already addressed, what remains unresolved in the reviewed evidence, a possible approach and a falsifiable validation plan. Place provenance/withdrawal and federated-agent networks in clearly marked coverage-debt or frontier subsections until supported by primary evidence.

**Output:** Challenge–evidence–validation map. **Transition:** Summarize conditional design lessons, not unsupported universals.

### VIII. Conclusion

Summarize which information supports which decisions and why later changes can require revalidation. Preserve scope conditions and acknowledge the bounds of the corpus. Do not introduce new results, new taxonomic branches or claims that the framework itself has been experimentally validated.

## Planned figures and tables

| Artifact | Analytical purpose | Evidence requirement |
| --- | --- | --- |
| Figure 1: Representation → Governance → Evolution | Show information, decisions and feedback, including reject/fallback possibilities | Mark the drawing as the survey's conceptual synthesis |
| Figure 2: Research taxonomy | Distinguish model-internal alignment from external capability/relationship descriptions and link both to decisions | Every populated branch has primary examples and boundaries |
| Figure 3: Collaboration configurations | Compare static composition, persistent inference and history-dependent update | Conceptual configurations, not a universal chronological progression |
| Table I: Related surveys | Give prior work positive coverage and exact scope differences | Version-specific locators; unknown is not absence |
| Table II: Representation methods | Compare what the representation predicts and what it cannot justify | Inputs, costs, shared-base/architecture assumptions |
| Table III: Governance | Distinguish measured properties, optimization and guarantees | Protected object, threat, premises and decision consequence |
| Table IV: Evolution | Separate runtime selection from learned continuing change | Persistent state, feedback and evaluation horizon |
| Table V: Evaluation | Separate existing resources from proposed extensions | Source pools, tasks, budgets, metrics and unsupported events |

## Drafting prerequisites

Before making strong differentiation claims, reconcile the nearest survey versions and metadata and complete cross-operator method comparisons. Before drafting each subsection, require its evidence table and allowed/forbidden claims to be ready. Coverage that remains thin should be stated as limited or removed from the contribution claim; it should not be filled with unsupported prose. These prerequisites are scientific checks, not evidence that the current project has already completed the full survey.
