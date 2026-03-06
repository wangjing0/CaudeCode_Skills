# Causal Inference LLM - Claude Code Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code%20Skill-5A67D8)](https://claude.ai/code)

Discover causal relationships and generate directed acyclic graphs (DAGs) using LLM reasoning. A Claude Code skill for intelligent causal inference leveraging large language models.

## Features

- **Pairwise Causal Discovery** - Analyze causal links between treatment and outcome variables
- **Latent Confounder Identification** - Find hidden variables affecting relationships
- **Complete DAG Construction** - Build full causal graphs with confidence estimates
- **Interactive Visualization** - Generate explorable HTML graph visualizations
- **Domain Expert Perspectives** - LLM-generated expert viewpoints for analysis

## Quick Start

### Installation

**Option 1: Direct Clone (Fastest)**
```bash
git clone https://github.com/wangjing0/causal-inference-llm.git ~/.claude/skills/causal-inference-llm
```

**Option 2: From Release**
```bash
# Download the latest .skill file from releases
wget https://github.com/wangjing0/causal-inference-llm/releases/latest/download/causal-inference-llm.skill
unzip causal-inference-llm.skill -d ~/.claude/skills/
```

**Option 3: Manual Download**
```bash
# Download zip from GitHub
curl -L https://github.com/wangjing0/causal-inference-llm/archive/refs/heads/main.zip -o causal-inference-llm.zip
unzip causal-inference-llm.zip
mv causal-inference-llm-main ~/.claude/skills/causal-inference-llm
```

### Prerequisites

Install the causal package:
```bash
git clone https://github.com/yourusername/causalgraph.git
cd causalgraph
uv sync
```

Set your API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Basic Usage

```python
from causal import ModelSuggester

modeler = ModelSuggester('gpt-5.1-mini')
experts = modeler.suggest_domain_expertises(['smoking', 'lung cancer'], n_experts=3)
result = modeler.suggest_pairwise_relationship(experts, 'smoking', 'lung cancer')
print(result)
```

## Using with Claude Code

Once installed, Claude Code automatically recognizes causal inference queries:

**Example Prompts:**
- "Analyze the causal relationship between exercise and heart health"
- "Build a causal graph for: diet, exercise, stress, heart disease"
- "What confounders might affect social media use and mental health?"
- "Create a DAG showing how these economic factors interact"

## Documentation

- **[QUICKSTART.md](docs/QUICKSTART.md)** - Get started in 5 minutes
- **[INSTALL.md](docs/INSTALL.md)** - Detailed installation guide
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Publishing and distribution
- **[TEST_INSTALLATION.md](docs/TEST_INSTALLATION.md)** - Verification checklist
- **[RELEASE_NOTES](docs/RELEASE_NOTES_v0.1.0.md)** - Version history

## Repository Structure

```
causal-inference-llm/
├── SKILL.md                           # Core skill instructions
├── scripts/                           # Example scripts
│   ├── basic_analysis.py              # Complete workflow
│   └── quick_relationship_check.py    # Quick checks
├── references/                        # Detailed documentation
│   ├── causal-theory.md               # Theoretical background
│   └── api-reference.md               # API documentation
├── docs/                              # Additional documentation
│   ├── INSTALL.md                     # Installation guide
│   ├── QUICKSTART.md                  # Quick start guide
│   ├── DEPLOYMENT.md                  # Publishing guide
│   └── TEST_INSTALLATION.md           # Testing checklist
├── README.md                          # This file
├── LICENSE                            # MIT License
└── CHANGELOG.md                       # Version history
```

## Examples

### Medical Research
Analyze causal pathways in health outcomes:
```python
factors = ["medication", "recovery_time", "age", "disease_severity"]
# Build causal graph...
```

### Social Science
Study socioeconomic relationships:
```python
factors = ["education", "income", "location", "occupation"]
# Discover confounders...
```

### Business Analytics
Understand business drivers:
```python
factors = ["marketing_spend", "sales", "seasonality", "competition"]
# Create causal model...
```

## Requirements

- **Python**: 3.9+
- **Claude Code**: Latest version
- **Dependencies**: `networkx`, `openai`, `pyvis`, `pydantic`
- **API Key**: OpenAI or compatible LLM API

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test your changes thoroughly
4. Submit a pull request

## Support

- **Issues**: [GitHub Issues](https://github.com/wangjing0/causal-inference-llm/issues)
- **Discussions**: [GitHub Discussions](https://github.com/wangjing0/causal-inference-llm/discussions)
- **Documentation**: See [INSTALL.md](INSTALL.md) and skill references

## Citation

If you use this skill in your research, please cite:

```bibtex
@software{causal_inference_llm_skill,
  title = {Causal Inference LLM: Claude Code Skill for Causal Discovery},
  author = {Wang, Jing},
  year = {2026},
  url = {https://github.com/wangjing0/causal-inference-llm}
}
```

## Related Projects

- [CausalGraph](https://github.com/yourusername/causalgraph) - Main causal inference library
- [PyWhy-llm](https://github.com/py-why/pywhyllm) - Causal inference with LLMs
- [DoWhy](https://github.com/py-why/dowhy) - Python library for causal inference

## License

MIT License - See [LICENSE](LICENSE) for details.

Copyright (c) 2026 Jing Wang
