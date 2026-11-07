# Representation, governance and evolution

The taxonomy follows three connected questions. It is an analytical organization of the reviewed literature, not a newly validated fusion algorithm or a claim that prior surveys lack these topics.

## I. Fusion Representation

**Which information makes a particular fusion operation feasible?**

1. Capability profiling and characterization: task embeddings, model specifications and model recommendation.
2. Similarity and compatibility assessment: task relationships, behavioral agreement, parameter geometry and kinship.
3. Parameter and representation alignment: permutations, transport, feature correspondence and architecture compatibility.
4. Task–model association and selection: predicting transfer and matching assets to requests.
5. Structured model organization: model pools, indexes, relationships and reusable specifications.

Internal representation alignment concerns corresponding neurons, features or coordinates. External model representation concerns what a whole model can do, where evidence comes from, and how models may collaborate. A graph can encode relationships, but a graph is not a universal assumption.

Representation outputs inform governance; similarity alone cannot determine whether fusion is acceptable under a threat model or access restriction.

## II. Trustworthy Fusion Governance

**Which properties of a fused model are supported under stated trust requirements?**

The topics include privacy of fusion releases, merge-specific attacks and defenses, safety and fairness objectives that change the combination, and the provenance of source models and validation evidence. The distinction between an observed property and a decision constraint is central. General federated optimization, security and fairness methods do not enter without an explicit model-fusion operation.

For each method, record the actor that makes the decision, information it can observe, trusted resources, attacker capabilities, protected object, enforcement mechanism and failure response. Separate cryptographic or statistical guarantees from empirical attack resistance. Multi-attribute optimization does not imply composable guarantees unless their assumptions and interactions are established.

A governance decision may accept, reject, defer, isolate or fall back. These are proposed analytical decision categories; they are attributed to a particular system only when its implementation supports them.

Static governance becomes stale when component versions, query distributions or trust evidence change, motivating the evolution dimension.

## III. Fusion Updates and Collaborative Evolution

**What changes over time, and what evidence justifies the change?**

The core is sequential knowledge integration into a fused predictor and continual fusion within a federated training protocol. Comparisons identify the incoming source or task, accumulated weights or modules, retention mechanism, information access and evaluated sequence.

Conditional module composition, fixed routing and offline merge search supply boundary comparisons. They do not establish continual knowledge retention merely because inputs, search trials or communication rounds vary. Related systems that update model indexes or initial preference context retain their separate comparison unit. In particular, MetaRouter's initial preference adaptation is not evidence of continuously updated deployment policies.

An update requires reassessment when it changes the premises of earlier fusion evidence. The proposed evaluation records retention and acquisition, changed releases or attack surfaces, and cumulative construction cost. Source withdrawal and recovery remain research questions where the reviewed evidence is incomplete; no general removal mechanism or event-based benchmark is claimed.

## Record mapping

A single primary category supports counting, while secondary tags preserve cross-stage relationships. Benchmarks/tools and surveys appear in separate sections. The detailed database retains applicability, source version, reading depth and limitations so the taxonomy does not conceal missing evidence.
