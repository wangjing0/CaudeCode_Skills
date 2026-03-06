# Quick Start Guide

Get started with the causal-inference-llm skill in 5 minutes.

## Installation

```bash
# Install skill directly
git clone https://github.com/wangjing0/causal-inference-llm.git ~/.claude/skills/causal-inference-llm

# Install causal package (required)
git clone https://github.com/yourusername/causalgraph.git
cd causalgraph
uv sync

# Set API key
export OPENAI_API_KEY='your-api-key'
```

## Basic Usage

### 1. Quick Pairwise Relationship Check

```python
from causal import ModelSuggester

modeler = ModelSuggester('gpt-5.1-mini')

# Analyze relationship between two variables
experts = modeler.suggest_domain_expertises(['smoking', 'lung cancer'], n_experts=3)
result = modeler.suggest_pairwise_relationship(experts, 'smoking', 'lung cancer')
print(result)
```

### 2. Complete Causal Analysis

```python
import asyncio
from causal import ModelSuggester, plot_interactive_graph
import networkx as nx

async def analyze():
    modeler = ModelSuggester('gpt-5.1-mini')

    # Define variables
    factors = ["smoking", "lung cancer", "genetics", "air pollution"]
    treatment = "smoking"
    outcome = "lung cancer"

    # Get experts
    experts = modeler.suggest_domain_expertises(factors, n_experts=3)

    # Find confounders
    _, confounders = modeler.suggest_latent_confounders(treatment, outcome, experts)

    # Complete factor list
    all_factors = list(set([f.lower() for f in factors + confounders]))

    # Build relationships
    edges = await modeler._suggest_pairwise_relationships(
        expert=str(experts),
        all_factors=all_factors,
        analysis_context="medical causal model"
    )

    # Create graph
    G = nx.MultiDiGraph()
    for idx, label in enumerate(all_factors):
        G.add_node(idx, desc=label)

    for edge, (conf, reason) in edges.items():
        G.add_edge(edge[0], edge[1], relationship=conf, thinking=reason)

    # Visualize
    plot_interactive_graph(G, filename="causal_graph.html")
    print(f"Graph saved to causal_graph.html")

asyncio.run(analyze())
```

### 3. Using Example Scripts

```bash
cd ~/.claude/skills/causal-inference-llm/scripts

# Run complete analysis
python basic_analysis.py

# Quick relationship check
python quick_relationship_check.py "education" "income"
```

## Using with Claude Code

Once installed, the skill automatically triggers when you ask Claude about:

- "Analyze the causal relationship between X and Y"
- "Build a causal graph for these variables"
- "What confounders might affect this relationship?"
- "Create a DAG showing how these factors interact"

Example Claude Code prompts:

```
"Analyze the causal relationship between exercise and heart health"

"Build a causal graph for: diet, exercise, stress, heart disease, age"

"What latent confounders might affect the relationship between
social media use and mental health?"
```

## Configuration

Create `~/.causal/config.yaml` (optional):

```yaml
llm:
  model: gpt-5.1-mini
  temperature: 0.7
  max_tokens: 2000

analysis:
  default_experts: 3
  confidence_threshold: 0.7
```

## Common Use Cases

### Medical Research
```python
modeler = ModelSuggester('o3-mini')
factors = ["medication", "recovery", "age", "severity"]
# Analyze causal pathways...
```

### Social Science
```python
factors = ["education", "income", "location", "occupation"]
# Study socioeconomic relationships...
```

### Business Analytics
```python
factors = ["marketing_spend", "sales", "season", "competition"]
# Understand business drivers...
```

### Environmental Studies
```python
factors = ["temperature", "ice_melt", "sea_level", "emissions"]
# Climate change causal analysis...
```

## Next Steps

1. **Read SKILL.md** - Complete usage guide
2. **Explore references/** - Detailed documentation
3. **Run examples** - Test with your data
4. **Customize** - Adjust configuration for your needs

## Troubleshooting

**Problem:** "Module 'causal' not found"
**Solution:** Install with `uv sync` from project root

**Problem:** "API key not set"
**Solution:** `export OPENAI_API_KEY='your-key'`

**Problem:** Skill not triggering
**Solution:** Verify installation: `ls ~/.claude/skills/causal-inference-llm`

## Getting Help

- **Documentation:** See `references/` folder
- **Examples:** Check `scripts/` folder
- **Issues:** GitHub repository issues
- **API Docs:** `references/api-reference.md`

## Key Concepts

**Causal Graph (DAG):** Directed acyclic graph showing causal relationships

**Confounders:** Variables affecting both treatment and outcome

**Latent Variables:** Unobserved factors inferred from domain knowledge

**Domain Experts:** LLM-generated expert perspectives for analysis

**Confidence Levels:** High/medium/low ratings for causal relationships

For complete theoretical background, see `references/causal-theory.md`.
