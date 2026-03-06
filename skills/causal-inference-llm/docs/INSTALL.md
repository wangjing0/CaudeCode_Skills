# Installation Guide

## Prerequisites

Before using these skills, ensure you have:

1. **Claude Code CLI** installed
2. **Python 3.9+** with the causal package
3. **OpenAI API key** or compatible LLM API access

## Install the Causal Package

```bash
# Clone the repository
git clone https://github.com/yourusername/causalgraph.git
cd causalgraph

# Install with uv (recommended)
uv sync
uv sync --extra dev

# Or with pip
pip install -e .
```

## Install Skills

### Method 1: Direct Clone (Recommended)

```bash
# Clone directly to Claude skills directory
git clone https://github.com/wangjing0/causal-inference-llm.git ~/.claude/skills/causal-inference-llm

# Verify installation
ls ~/.claude/skills/causal-inference-llm/SKILL.md
```

### Method 2: Manual Download

```bash
# Download and extract
curl -L https://github.com/wangjing0/causal-inference-llm/archive/refs/heads/main.zip -o causal-inference-llm.zip
unzip causal-inference-llm.zip
mv causal-inference-llm-main ~/.claude/skills/causal-inference-llm

# Verify installation
ls ~/.claude/skills/causal-inference-llm
```

### Method 3: From .skill File

```bash
# Download from releases
wget https://github.com/wangjing0/causal-inference-llm/releases/latest/download/causal-inference-llm.skill

# Extract the packaged skill
unzip causal-inference-llm.skill -d ~/.claude/skills/
```

## Configuration

### Set up API Keys

```bash
# For OpenAI
export OPENAI_API_KEY='your-api-key-here'

# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
```

### Configure LLM Settings

Edit `~/.claude/skills/causal-inference-llm/config.yaml` (if needed):

```yaml
llm:
  model: gpt-5.1-mini  # or o3-mini, claude-3.5-sonnet
  temperature: 0.7
  max_tokens: 2000

analysis:
  default_experts: 3
  confidence_threshold: 0.7
```

## Verify Installation

Test the skill with a simple analysis:

```python
from causal import ModelSuggester

modeler = ModelSuggester('gpt-5.1-mini')
experts = modeler.suggest_domain_expertises(['smoking', 'lung cancer'], n_experts=3)
print(f"Domain experts: {experts}")
```

Or run the example scripts:

```bash
cd ~/.claude/skills/causal-inference-llm/scripts
python basic_analysis.py
```

## Troubleshooting

### Issue: "Module 'causal' not found"

**Solution:** Ensure the causal package is installed in your Python environment:

```bash
uv pip list | grep causal
# or
pip list | grep causal
```

If not found, install from the project root:

```bash
cd /path/to/causalgraph
uv sync
```

### Issue: "API key not configured"

**Solution:** Set the appropriate environment variable:

```bash
export OPENAI_API_KEY='your-key'
```

### Issue: "Skill not triggering in Claude Code"

**Solution:**
1. Verify skill is in `~/.claude/skills/` directory
2. Check SKILL.md has proper YAML frontmatter
3. Restart Claude Code session
4. Try explicit trigger: mention "causal inference" or "DAG construction"

## Publishing to npm (Maintainers)

To publish skills for npx installation:

```bash
cd skills
npm publish --access public
```

Users can then install with:

```bash
npx @anthropic-ai/claude-code-skills add @causalgraph/causal-inference-llm
```

## Next Steps

After installation:

1. Review [SKILL.md](causal-inference-llm/SKILL.md) for usage examples
2. Explore [references/](causal-inference-llm/references/) for detailed documentation
3. Run example scripts in [scripts/](causal-inference-llm/scripts/)
4. Try causal analysis on your own data

## Support

For issues or questions:
- GitHub Issues: https://github.com/yourusername/causalgraph/issues
- Documentation: See references/ directory in skill
