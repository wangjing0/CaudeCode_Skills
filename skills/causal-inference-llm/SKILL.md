---
name: causal-inference-llm
description: Causal inference and relationship discovery using large language models. Discovers causal links between events, identifies latent confounders, and constructs directed acyclic graphs (DAGs). Use when analyzing causal relationships, building causal models, identifying confounders, or creating qualitative causal graphs from domain knowledge and LLM reasoning.
---

# Causal Inference with LLMs

Leverage reasoning LLMs to discover causal relationships and generate directed acyclic graphs (DAGs). This skill enables Pearl's Ladder of Causation "Why" level - inferring underlying data generation processes by combining observational patterns with domain expertise.

## Core Capabilities

### 1. Pairwise Causal Relationships (A → B)

Assess potential causal links between treatment and outcome variables using LLM reasoning and domain knowledge.

```python
from causal import ModelSuggester

modeler = ModelSuggester('gpt-5.1-mini')
experts = modeler.suggest_domain_expertises(event_labels, n_experts=5)

modeler.suggest_pairwise_relationship(
    experts,
    'Treatment event',
    'Outcome event'
)
```

### 2. Latent Confounder Identification (A ← C → B)

Identify unobserved variables that influence both treatment and outcome.

```python
_, latent_confounders = modeler.suggest_latent_confounders(
    treatment_variable,
    outcome_variable,
    experts
)
```

### 3. Complete Causal Graph Construction

Build full DAGs with directional relationships, reasoning, and confidence estimates.

```python
all_factors = ["factor1", "factor2", "factor3"]
pairwise_edges = await modeler._suggest_pairwise_relationships(
    expert=str(domain_expertises),
    all_factors=all_factors,
    analysis_context="causal model"
)
```

### 4. Interactive Graph Visualization

Generate interactive HTML visualizations of causal graphs.

```python
from causal import plot_interactive_graph
import networkx as nx

G = nx.MultiDiGraph()
for idx, label in enumerate(all_factors):
    G.add_node(idx, desc=label)

for edge, (confidence, thinking) in pairwise_edges.items():
    G.add_edge(edge[0], edge[1], relationship=confidence, thinking=thinking)

plot_interactive_graph(G, filename="output/causal_graph.html")
```

## Workflow

### Basic Analysis Flow

1. **Define Variables**: Specify treatment, outcome, and known factors
2. **Identify Domain Expertise**: Generate relevant expert perspectives
3. **Discover Confounders**: Find latent variables affecting both treatment and outcome
4. **Build Pairwise Relationships**: Assess all potential causal links
5. **Construct DAG**: Assemble complete causal graph
6. **Visualize**: Generate interactive graph representation

### Example: Medical Causality

```python
import asyncio
from causal import ModelSuggester, plot_interactive_graph
import networkx as nx

async def analyze_medical_causality():
    modeler = ModelSuggester('o3-mini')

    all_factors = ["smoking", "lung cancer", "air pollution", "genetics"]
    treatment = "smoking"
    outcome = "lung cancer"

    # Get domain expertise
    experts = modeler.suggest_domain_expertises(all_factors, n_experts=3)

    # Find confounders
    _, latent_confounders = modeler.suggest_latent_confounders(
        treatment, outcome, experts
    )

    # Build complete factor list
    all_factors += latent_confounders
    all_factors = list(set([f.lower() for f in all_factors]))

    # Discover pairwise relationships
    pairwise_edges = await modeler._suggest_pairwise_relationships(
        expert=str(experts),
        all_factors=all_factors,
        analysis_context="medical causal model"
    )

    # Build and visualize graph
    G = nx.MultiDiGraph()
    for idx, label in enumerate(all_factors):
        G.add_node(idx, desc=label)

    for edge, (confidence, thinking) in pairwise_edges.items():
        G.add_edge(edge[0], edge[1],
                   relationship=confidence, thinking=thinking)

    plot_interactive_graph(G, filename="medical_causal_graph.html")

asyncio.run(analyze_medical_causality())
```

## Configuration

The package uses `config.yaml` for LLM settings. Key parameters:

- **model**: LLM model name (e.g., 'gpt-5.1-mini', 'o3-mini')
- **temperature**: Reasoning randomness
- **max_tokens**: Response length limit
- **domain_expert_count**: Number of expert perspectives (default: 3-5)

## Critical Limitations

AI reasoning is based on learned patterns and may contain biases or incorrect associations. Always:

- **Validate** proposed relationships using additional causal inference techniques
- **Cross-check** with domain experts and empirical evidence
- **Test** causal hypotheses through experimentation when possible
- **Document** confidence levels and reasoning chains
- **Never treat** LLM suggestions as ground truth

## Advanced Features

### Relationship Strategies

Multiple strategies available via `RelationshipStrategy` enum:
- `parent`: Parent-child relationships
- `child`: Child-parent relationships
- `confounder`: Confounding variables
- `iv`: Instrumental variables
- `mediator`: Mediating variables
- `pairwise`: All pairwise relationships

### Async Processing

Use async methods for efficient batch processing of multiple causal pairs.

### Graph Export

Export graphs in multiple formats:
- Interactive HTML (pyvis)
- NetworkX graph objects
- JSON/GraphML for external tools

## References

For theoretical background, see [references/causal-theory.md](references/causal-theory.md).

For complete API documentation, see [references/api-reference.md](references/api-reference.md).
