# Installation Test Checklist

Use this checklist to verify the skill installation works correctly.

## Pre-Installation Tests

- [ ] Verify .skill file exists: `ls -lh causal-inference-llm.skill`
- [ ] Check .skill file size: Should be ~8KB
- [ ] Verify .skill file is valid zip: `unzip -t causal-inference-llm.skill`
- [ ] List .skill contents: `unzip -l causal-inference-llm.skill`

## Installation Tests

### Test 1: Manual Directory Copy

```bash
# Backup existing (if any)
[ -d ~/.claude/skills/causal-inference-llm ] && \
  mv ~/.claude/skills/causal-inference-llm ~/.claude/skills/causal-inference-llm.backup

# Install
cp -r causal-inference-llm ~/.claude/skills/

# Verify
ls -la ~/.claude/skills/causal-inference-llm/
```

**Expected:** Directory copied with all files intact

### Test 2: Packaged File Installation

```bash
# Clean up
rm -rf ~/.claude/skills/causal-inference-llm

# Install from package
unzip causal-inference-llm.skill -d ~/.claude/skills/

# Verify
ls -la ~/.claude/skills/causal-inference-llm/
```

**Expected:** Directory extracted with correct structure

### Test 3: Verify File Structure

```bash
cd ~/.claude/skills/causal-inference-llm

# Check required files
[ -f SKILL.md ] && echo "✓ SKILL.md exists"
[ -f scripts/basic_analysis.py ] && echo "✓ basic_analysis.py exists"
[ -f scripts/quick_relationship_check.py ] && echo "✓ quick_relationship_check.py exists"
[ -f references/api-reference.md ] && echo "✓ api-reference.md exists"
[ -f references/causal-theory.md ] && echo "✓ causal-theory.md exists"
```

**Expected:** All 5 files present

### Test 4: Verify YAML Frontmatter

```bash
cd ~/.claude/skills/causal-inference-llm

# Check YAML frontmatter
head -5 SKILL.md
```

**Expected Output:**
```yaml
---
name: causal-inference-llm
description: Causal inference and relationship discovery using large language models...
---
```

## Functionality Tests

### Test 5: Python Environment Check

```bash
# Check if causal package is available
python -c "import causal; print('✓ causal package available')"

# Check if dependencies are available
python -c "import networkx; print('✓ networkx available')"
python -c "import openai; print('✓ openai available')"
```

**Expected:** All imports succeed

### Test 6: Run Quick Check Script

```bash
cd ~/.claude/skills/causal-inference-llm/scripts

# Run quick relationship check
python quick_relationship_check.py "smoking" "lung cancer"
```

**Expected:** Script runs, generates domain experts, analyzes relationship

### Test 7: Run Full Analysis (Optional - requires API key)

```bash
# Set API key if not already set
export OPENAI_API_KEY='your-api-key'

# Run full analysis
cd ~/.claude/skills/causal-inference-llm/scripts
python basic_analysis.py
```

**Expected:**
- Script completes 5 steps
- Generates causal_graph.html
- No errors

## Claude Code Integration Tests

### Test 8: Skill Triggering

Start Claude Code and try these prompts:

1. "Analyze the causal relationship between smoking and lung cancer"
2. "Build a causal graph for: diet, exercise, stress"
3. "What confounders affect the relationship between X and Y?"

**Expected:** Claude recognizes the skill and uses appropriate methods

### Test 9: Reference Loading

In Claude Code, ask:

"What are the theoretical foundations of causal inference?"

**Expected:** Claude loads references/causal-theory.md when needed

### Test 10: Script Execution

In Claude Code, ask:

"Run a quick causal relationship check between education and income"

**Expected:** Claude uses scripts/quick_relationship_check.py

## Cleanup

After testing, if everything works:

```bash
# Keep the installation
echo "Installation successful!"

# Remove backup if created
rm -rf ~/.claude/skills/causal-inference-llm.backup
```

If issues found:

```bash
# Restore backup
[ -d ~/.claude/skills/causal-inference-llm.backup ] && \
  mv ~/.claude/skills/causal-inference-llm.backup ~/.claude/skills/causal-inference-llm

# Report issues on GitHub
```

## Common Issues

### Issue: "Module 'causal' not found"

**Diagnosis:**
```bash
python -c "import sys; print('\n'.join(sys.path))"
which python
```

**Solution:**
```bash
# Ensure in correct Python environment
cd /path/to/causalgraph
source .venv/bin/activate  # or: uv run python
pip install -e .
```

### Issue: "API key not configured"

**Diagnosis:**
```bash
echo $OPENAI_API_KEY
```

**Solution:**
```bash
export OPENAI_API_KEY='your-key'
# Add to ~/.bashrc or ~/.zshrc for persistence
```

### Issue: "Skill not triggering in Claude Code"

**Diagnosis:**
```bash
ls -la ~/.claude/skills/causal-inference-llm/SKILL.md
head -10 ~/.claude/skills/causal-inference-llm/SKILL.md
```

**Solution:**
- Verify YAML frontmatter is correct
- Restart Claude Code
- Try more explicit prompts mentioning "causal inference"

## Test Results Template

```
SKILL INSTALLATION TEST RESULTS
================================

Date: _______________
Tester: _______________
Environment: _______________

Pre-Installation Tests:
[ ] .skill file exists
[ ] .skill file valid
[ ] .skill contents correct

Installation Tests:
[ ] Manual copy works
[ ] Package extraction works
[ ] File structure correct
[ ] YAML frontmatter valid

Functionality Tests:
[ ] Python imports work
[ ] Quick check script runs
[ ] Full analysis works (optional)

Claude Code Tests:
[ ] Skill triggers correctly
[ ] References load on demand
[ ] Scripts execute properly

Issues Found:
_______________________________________________
_______________________________________________
_______________________________________________

Overall Status: PASS / FAIL

Notes:
_______________________________________________
_______________________________________________
_______________________________________________
```

## Success Criteria

The installation is successful if:

✅ All files copied/extracted correctly
✅ YAML frontmatter is valid
✅ Python imports work
✅ At least one script runs successfully
✅ Skill triggers in Claude Code (if tested)
✅ No file permission issues

If all criteria met: **Installation PASSED**
