# API Reference

## ModelSuggester

Main class for causal inference operations.

### Constructor

```python
ModelSuggester(llm: str = 'gpt-5.1-mini')
```

**Parameters:**
- `llm`: LLM model identifier (e.g., 'gpt-5.1-mini', 'o3-mini', 'claude-3.5-sonnet')

### Methods

#### suggest_domain_expertises

```python
suggest_domain_expertises(
    factors: list[str],
    n_experts: int = 3
) -> list[str]
```

Generate relevant domain expert perspectives for causal analysis.

**Parameters:**
- `factors`: List of variables/events to analyze
- `n_experts`: Number of expert perspectives to generate (default: 3)

**Returns:**
- List of expert domain titles (e.g., ['Epidemiologist', 'Biostatistician'])

**Example:**
```python
experts = modeler.suggest_domain_expertises(
    ['smoking', 'lung cancer', 'genetics'],
    n_experts=3
)
# Returns: ['Epidemiologist', 'Biostatistician', 'Geneticist']
```

#### suggest_pairwise_relationship

```python
suggest_pairwise_relationship(
    experts: list[str],
    treatment: str,
    outcome: str
) -> dict
```

Assess causal relationship between two variables.

**Parameters:**
- `experts`: List of domain expert perspectives
- `treatment`: Treatment/cause variable
- `outcome`: Outcome/effect variable

**Returns:**
- Dictionary with relationship type and reasoning

**Example:**
```python
result = modeler.suggest_pairwise_relationship(
    experts=['Epidemiologist', 'Biostatistician'],
    treatment='smoking',
    outcome='lung cancer'
)
# Returns: {'relationship': 'CAUSAL', 'reasoning': '...'}
```

#### suggest_latent_confounders

```python
suggest_latent_confounders(
    treatment: str,
    outcome: str,
    experts: list[str]
) -> tuple[dict, list[str]]
```

Identify potential unobserved confounding variables.

**Parameters:**
- `treatment`: Treatment variable
- `outcome`: Outcome variable
- `experts`: List of domain expert perspectives

**Returns:**
- Tuple of (reasoning_dict, list of confounder names)

**Example:**
```python
reasoning, confounders = modeler.suggest_latent_confounders(
    'smoking',
    'lung cancer',
    experts
)
# confounders: ['age', 'gender', 'socioeconomic status', 'genetics']
```

#### _suggest_pairwise_relationships (async)

```python
async _suggest_pairwise_relationships(
    expert: str,
    all_factors: list[str],
    analysis_context: str = "causal model"
) -> dict[tuple[int, int], tuple[str, str]]
```

Discover all pairwise causal relationships in a factor set.

**Parameters:**
- `expert`: String representation of expert perspectives
- `all_factors`: List of all variables/factors to analyze
- `analysis_context`: Context description for analysis

**Returns:**
- Dictionary mapping (source_idx, target_idx) to (confidence, reasoning)

**Example:**
```python
pairwise_edges = await modeler._suggest_pairwise_relationships(
    expert=str(experts),
    all_factors=['smoking', 'lung cancer', 'age', 'genetics'],
    analysis_context="medical causal model"
)
# Returns: {(0, 1): ('high', 'Smoking directly damages lung tissue...'),
#           (2, 0): ('medium', 'Age correlates with smoking duration...'), ...}
```

## Visualization Functions

### plot_interactive_graph

```python
plot_interactive_graph(
    G: nx.MultiDiGraph,
    filename: str = "graph.html"
) -> None
```

Generate interactive HTML visualization of causal graph.

**Parameters:**
- `G`: NetworkX MultiDiGraph with nodes and edges
- `filename`: Output HTML file path

**Node Attributes:**
- `desc`: Node label/description

**Edge Attributes:**
- `relationship`: Confidence level ('high', 'medium', 'low')
- `thinking`: Reasoning for causal link

**Example:**
```python
from causal import plot_interactive_graph
import networkx as nx

G = nx.MultiDiGraph()
G.add_node(0, desc='smoking')
G.add_node(1, desc='lung cancer')
G.add_edge(0, 1, relationship='high', thinking='Direct causal mechanism')

plot_interactive_graph(G, filename="output/causal_graph.html")
```

## Enums

### RelationshipStrategy

```python
class RelationshipStrategy(Enum):
    parent = "parent"
    child = "child"
    confounder = "confounder"
    iv = "iv"  # Instrumental variable
    mediator = "mediator"
    pairwise = "pairwise"
```

Defines different strategies for causal relationship discovery.

## Configuration

Configuration is loaded from `config.yaml` in the package directory.

**Example config.yaml:**
```yaml
llm:
  model: gpt-5.1-mini
  temperature: 0.7
  max_tokens: 2000

analysis:
  default_experts: 3
  confidence_threshold: 0.7
```

## Dependencies

Core dependencies:
- `networkx>=3.2.1`: Graph data structures
- `openai>=1.70`: LLM API access
- `pydantic>=2.11`: Data validation
- `pyvis>=0.3.2`: Interactive graph visualization
- `colorlog>=6.9.0`: Colored logging
- `pyyaml>=6.0`: Configuration management

## Error Handling

Common exceptions:
- `ValueError`: Invalid input parameters
- `openai.APIError`: LLM API failures
- `networkx.NetworkXError`: Graph construction errors

Always wrap LLM calls in try-except blocks for production use.
