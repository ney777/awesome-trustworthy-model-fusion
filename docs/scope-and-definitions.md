# Scope and definitions

This collection studies the reuse, combination and coordination of existing model assets when access, compatibility, trust or changing environments constrain the decision. Federated learning is a priority setting, not a synonym for the entire field.

## Operational boundaries

| Term | Working definition | Boundary |
| --- | --- | --- |
| Model asset | An existing model together with its accessible interfaces, version, provenance and supporting capability evidence. | Architecture alone is not a complete asset description. |
| Model fusion | Integration of knowledge or capability from multiple model assets into a model, representation or decision mechanism. | A broad organizing definition used by this project; the literature uses narrower definitions too. |
| Model merging | Parameter or module integration into a combined model. | Does not include every prediction ensemble or multi-agent workflow. |
| Model ensemble | Combining predictions while retaining component models. | Within scope when selection, information exchange or trust-aware composition is directly studied. |
| Federated aggregation | Combining participant updates or knowledge within a distributed training protocol. | Training-time coordination differs from reusing independently trained assets. |
| Model collaboration | Coordinated use or exchange of model knowledge, including persistent inference-time cooperation. | Generic agents, RAG and workflow automation are not automatically included. |
| Governance | A decision process that admits, combines, constrains, monitors or rejects model contributions using explicit trust requirements. | Measuring a trust metric after fusion alone is not constraint-driven governance. |
| Collaborative evolution | Changes to assets, selection or collaboration policies that are evaluated over an ordered sequence of tasks, models or feedback. | A static router or repeated offline weight search is not automatically history-based evolution. |

## Inclusion and exclusion

Core records directly study inter-model alignment, compatibility, knowledge transfer, fusion decisions, collaboration organization, trust constraints or changes to these processes. Foundational records must themselves study a fusion operation or a direct connection to model fusion; a generic federated baseline or security protocol is not included merely as background. Surveys and evaluation tools are separate record types.

For the federated method view, record the source models or modules, the fusion operation, and a primary-source passage establishing that fusion is a central contribution. Parameter alignment, explicit model/component combination, multi-teacher distillation, and constraints or attacks specific to these operations qualify. Training can be interleaved with fusion; training-free execution is not required.

General federated optimization, client scheduling, partial-submodel allocation, gradient defenses, secure-aggregation protocols, client fairness and data sharing do not qualify by themselves. A standard weighted sum inside an FL loop is not sufficient. Model-dependent fusion-coefficient or layer/component-combination studies may qualify when that operator is the central contribution; generic client participation or contribution accounting does not establish the same scope. Evidence that only establishes a publication or application domain is insufficient for method inclusion. See the [scope correction](scope-correction.md).

The explicitly requested survey comparisons remain in Related Surveys. Broader model-selection and collaboration systems remain in their established categories when supported by the original scope, but are not labeled federated fusion methods.

Ordinary single-model training, a generic mixture-of-experts architecture, task delegation among agents, or a dataset sharing only an application domain is insufficient for inclusion. Medical collaboration, scientific AI and edge deployment are possible use cases, not the organizing taxonomy.

A paper has one primary category and may have multiple secondary tags. Counts use unique studies. Related preprints and final publications are linked, and the final formal version governs venue metadata when available.

## Evidence discipline

Data remaining local does not establish a privacy theorem. Parameter compatibility does not establish behavioral compatibility. A reliable component does not establish a reliable composition. A benchmark gain does not establish stability under future changes. These distinctions are analytical rules; paper-specific conclusions remain linked to the source passages in the database.
