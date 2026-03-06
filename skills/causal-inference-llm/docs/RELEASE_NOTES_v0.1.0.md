# Release Notes - v0.1.0

## Causal Inference LLM - Initial Release

First public release of the causal-inference-llm skill for Claude Code.

### What's New

#### Core Features
- **Pairwise Causal Discovery**: Analyze causal relationships between treatment and outcome variables using LLM reasoning
- **Latent Confounder Identification**: Discover hidden variables that affect both treatment and outcome
- **Complete DAG Construction**: Build full causal graphs with directional relationships and confidence estimates
- **Interactive Visualization**: Generate explorable HTML graph visualizations powered by pyvis
- **Domain Expert Perspectives**: LLM-generated expert viewpoints for comprehensive causal analysis

#### Example Scripts
- `basic_analysis.py` - Complete workflow from domain experts to interactive graph
- `quick_relationship_check.py` - CLI tool for rapid pairwise causal checks

#### Documentation
- **SKILL.md**: Core skill instructions with YAML frontmatter for Claude Code integration
- **Theoretical Background**: Pearl's Ladder of Causation and key causal concepts
- **API Reference**: Complete documentation of ModelSuggester class and methods
- **Installation Guides**: Multiple installation methods with troubleshooting
- **Quick Start**: Get running in 5 minutes

### Installation

**Quick Install:**
```bash
git clone https://github.com/wangjing0/causal-inference-llm.git
cp -r causal-inference-llm/causal-inference-llm ~/.claude/skills/
```

**From Release Asset:**
```bash
wget https://github.com/wangjing0/causal-inference-llm/releases/download/v0.1.0/causal-inference-llm.skill
unzip causal-inference-llm.skill -d ~/.claude/skills/
```

### Prerequisites

- Python 3.9+
- Claude Code (latest version)
- CausalGraph package (from parent repository)
- OpenAI API key or compatible LLM access

### Quick Start

```python
from causal import ModelSuggester

modeler = ModelSuggester('gpt-5.1-mini')
experts = modeler.suggest_domain_expertises(['smoking', 'lung cancer'], n_experts=3)
result = modeler.suggest_pairwise_relationship(experts, 'smoking', 'lung cancer')
```

### Using with Claude Code

Ask Claude questions like:
- "Analyze the causal relationship between X and Y"
- "Build a causal graph for these factors: A, B, C, D"
- "What confounders might affect this relationship?"

The skill automatically triggers and guides the analysis.

### What's Included

- ✅ SKILL.md with comprehensive instructions
- ✅ 2 example Python scripts (tested)
- ✅ 2 reference documentation files
- ✅ Installation and deployment guides
- ✅ Testing checklist
- ✅ MIT License
- ✅ Packaged .skill file (8.2KB)

### Use Cases

- **Medical Research**: Analyze treatment effectiveness and health outcomes
- **Social Science**: Study socioeconomic relationships and policy impacts
- **Business Analytics**: Understand marketing effectiveness and sales drivers
- **Environmental Studies**: Model climate factors and ecological relationships
- **Economics**: Examine market dynamics and causal mechanisms

### Technical Details

**Skill Structure:**
- Progressive disclosure design for token efficiency
- Proper YAML frontmatter for Claude triggering
- References loaded on-demand
- Async processing for batch operations

**Supported LLMs:**
- OpenAI GPT models (gpt-5.1-mini, o3-mini, etc.)
- Anthropic Claude models
- Any OpenAI-compatible API

### Known Limitations

- Requires CausalGraph package installation
- API key configuration needed
- LLM reasoning should be validated with empirical methods
- Not a replacement for experimental causal analysis

### Documentation

- [README.md](README.md) - Overview and installation
- [QUICKSTART.md](QUICKSTART.md) - 5-minute guide
- [INSTALL.md](INSTALL.md) - Detailed setup
- [DEPLOYMENT.md](DEPLOYMENT.md) - Publishing guide
- [TEST_INSTALLATION.md](TEST_INSTALLATION.md) - Verification checklist

### Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Support

- **Issues**: [GitHub Issues](https://github.com/wangjing0/causal-inference-llm/issues)
- **Discussions**: [GitHub Discussions](https://github.com/wangjing0/causal-inference-llm/discussions)

### Acknowledgments

Built with guidance from the Claude Code skill-creator framework. Inspired by PyWhy-llm and Pearl's foundational work on causality.

### License

MIT License - See [LICENSE](LICENSE)

---

**Full Changelog**: https://github.com/wangjing0/causal-inference-llm/commits/v0.1.0
