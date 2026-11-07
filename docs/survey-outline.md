# Survey outline

**Working title:** Trustworthy Model Fusion and Collaboration: A Survey of Representation, Governance, and Evolution

**Updated:** 2026-11-07. This outline summarizes the survey's argument and section structure. It presents a comparative synthesis of a selective literature corpus, without claiming exhaustive coverage, taxonomic priority or a validated new framework. [Prior surveys](prior-surveys.md) document overlapping contributions; [research questions](research-gaps.md) separate existing evidence from proposed studies.

## Central argument

The comparison unit is a **fusion operation**: its source models, accessible information, integration rule and resulting deployment object. Individually useful sources may be incompatible, a feasible combination may change protected properties, and a later merge may erase earlier behavior. Representation, Governance and Evolution organize these linked problems:

1. **Representation:** What establishes executable correspondence or enables knowledge transfer between the sources?
2. **Governance:** Which trust conditions hold for the constructed model and the information released during fusion?
3. **Evolution:** What survives the next fusion update, and which earlier assessments need to be repeated?

The argument proceeds from **fusion compatibility → trust conditions of the combination → retention and reassessment after updates**. Source selection and routing provide supporting evidence or boundary comparisons. Selecting one model, varying a fixed router's choices or searching for one merge recipe does not by itself integrate new knowledge.

## Scope and comparison units

| Unit | Inclusion condition | Distinction retained |
| --- | --- | --- |
| Fusion operation | Combines parameters or modules, aligns model representations, or consolidates behavior from multiple teachers | Source-independent target versus retained branches or experts; preparation, construction and inference access |
| Federated fusion | The method directly specifies aggregation, alignment, explicit model mixtures or multi-model knowledge transfer | Coordinated training versus reuse of independently trained assets; communication and compatibility assumptions |
| Supporting or related mechanism | Helps assess a fusion candidate or provides a defined alternative to consolidation | Individual suitability, model selection and routing are not themselves evidence of fusion or continuing knowledge integration |

Generic federated optimization, client scheduling, protocol security and fairness methods fall outside the method scope unless they directly change or assess model fusion. Generic agent orchestration and prototype sharing alone also do not qualify. Model size, source/target/auxiliary roles, output interfaces, shared initialization, label space and access rights remain separate comparison conditions.

## Section structure

### I. Introduction

Motivates fusion through composition-specific failures: compatible-looking sources can interact harmfully, privacy can cover only one release channel, and later merges can degrade earlier tasks. Defines direct fusion and the limited role of selection/routing comparisons, acknowledges prior surveys, and states the three contributions as conditional technical comparisons.

### II. Foundations and Problem Formulation

Defines assets, interfaces, model roles and the fusion operation. Separates training-time aggregation, checkpoint reuse, multi-teacher transfer and source-retaining composition. Two recurring cases connect the sections: a teacher ensemble consolidated under a specified release interface, and an arriving expert merged into an accumulated checkpoint. They lead to the compatibility and transfer questions in Section III.

### III. Fusion Representation

Separates candidate suitability from construction: capability estimates support selection; weight geometry and internal correspondence support parameter fusion; statistics and calibration can repair a constructed target; behavioral transfer can consolidate sources across otherwise incompatible interfaces. Relations between models enter when they determine explicit mixtures or transfers. The synthesis distinguishes candidate ranking, an executable correspondence or transfer interface, and the resulting target. Those operations and their released information define the trust questions in Section IV.

### IV. Trustworthy Fusion Governance

Compares privacy channels, fairness units and references, composition-specific attacks, ownership signals and resource constraints. Distinguishes measured outcomes, objectives that alter a merge, mechanism-dependent guarantees and separately implemented fallback. FedAUX, PrivFusion, MergeBackdoor, DAM, SafeMERGE, LED-Merging and FairMerging illustrate different protected objects and assumptions. Model Trip remains supported by its final-publication abstract; PrivFusion's mechanism analysis uses the identified author preprint, arXiv:2311.03396v1, rather than the final TKDE text. The section ends with the dependence of an assessment on the particular source versions and constructed model.

### V. Fusion Updates and Collaborative Evolution

Centers on sequential and continual fusion: TIME examines temporal design choices; OPCM, DOP and NUFILT limit interference using parameter geometry; ODE-M uses calibration-loss gradients. LoRM and FedSEAM show how federated preparation and merging protocols affect continuing applicability and retention. FedSEAM's near-IID client evaluation does not establish arbitrary non-IID or private continual fusion.

Conditional composition and offline merge search serve as boundary comparisons. Updates to capability records or preference context are related retained-model systems, with a different state and outcome from accumulated weights. MetaRouter uses initial pairwise-feedback adaptation under stationary preferences, keeps its meta-trained encoder fixed during inference and optimizes a one-step objective; it does not establish continuous online policy learning. These distinctions determine the temporal comparisons in Section VI.

### VI. Evaluation, Benchmarks, and Applications

Matches source pools, preparation, calibration access, output systems and costs before comparing outcomes. Separates merger resources such as FusionBench and MergeBench from RouterBench and deployment toolkits. Reports task trajectories, defined subgroup losses and threat-specific outcomes alongside construction and inference costs.

The teacher-release and sequential-arrival cases connect compatibility, trust conditions and reassessment. A proposed event-indexed protocol records the incumbent, candidate, assessment and decision after specified changes; it remains an unimplemented evaluation proposal. Healthcare, scientific-model fusion and edge/cloud examples are tied to the reviewed methods and their demonstrated settings.

### VII. Challenges and Research Directions

Develops four fusion-specific questions, each with a proposed discriminating evaluation:

1. Predicting the value of a combination.
2. Combining trust conditions in a fusion operation.
3. Retaining knowledge under restricted update evidence.
4. Tracing and removing contributor influence.

The [research questions](research-gaps.md) explain their evidence and scope. Common reporting and event-protocol requirements stay in Section VI.

### VIII. Conclusion

Connects executable fusion, property-specific assessment and knowledge retention. The conclusions remain conditional on the reviewed operators, information access and evaluation settings.

## Figures and tables

| Artifact | Purpose |
| --- | --- |
| Overview and taxonomy figures | Connect fusion operations, released information and update evidence; distinguish core fusion from supporting comparisons |
| Collaboration-configuration figure | Separate construction, repeated execution and persistent updates without implying a universal progression |
| Survey comparison table | Credit prior coverage and state version-specific differences |
| Model-condition and role tables | Compare interfaces, scale, compatibility and source/target/auxiliary roles at configuration level |
| Representation, governance and evolution tables | Compare mechanism, required evidence, demonstrated outcome and limitation |
| Evaluation table | Separate existing resources and their assessed scope from proposed extensions |
