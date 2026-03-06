# Causal Theory Background

## Pearl's Ladder of Causation

The framework defines three levels of cognitive reasoning:

### Level 1: Association (How)
Finding associations between observations (e.g., smoking correlates with lung disease). Modern machine learning excels at this level with sufficient data.

### Level 2: Intervention (Why)
Inferring the underlying data generation process to build causal models. Requires combining observational patterns with domain expertise. **This is the focus of CausalGraph.**

### Level 3: Counterfactual (What If)
Running experiments and counterfactual reasoning to validate causal models and predict outcomes in unseen scenarios.

## Key Concepts

### Directed Acyclic Graph (DAG)
A graph with directed edges representing causal relationships, with no cycles. Nodes represent variables, edges represent causal influence.

### Confounders
Variables that influence both treatment and outcome, creating spurious correlations. Example: season affects both ice cream sales and shark attacks.

### Latent Confounders
Unobserved confounding variables that must be inferred from domain knowledge or data patterns.

### Instrumental Variables
Variables that affect the outcome only through the treatment, useful for identifying causal effects.

### Mediators
Variables that lie on the causal path between treatment and outcome.

## LLM-Based Causal Discovery

### Advantages
- Leverages world knowledge and domain expertise encoded in LLMs
- Rapid hypothesis generation for causal relationships
- Natural language reasoning about causality
- Identifies plausible confounders without observational data

### Limitations
- Based on learned patterns, may reflect training data biases
- Cannot replace experimental validation
- Confidence estimates are heuristic, not probabilistic
- May miss subtle or counterintuitive causal relationships

## References

- Pearl, J. (2009). *Causality: Models, Reasoning and Inference*. Cambridge University Press.
- [Pearl's Ladder of Causal Inference](https://www.pymc-marketing.io/en/0.10.0/notebooks/mmm/mmm_counterfactuals.html)
- [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://arxiv.org/pdf/2305.00050)
- [PyWhy-llm Project](https://github.com/py-why/pywhyllm)
