# Claude Code Custom Skills

Custom skills for Claude Code. Each skill lives under `skills/<skill-name>/` and follows the standard `SKILL.md` format.

## Available Skills

### run-codex

Uses OpenAI Codex CLI as a read-only oracle for planning, code review, and analysis. Codex never implements changes directly -- it provides a second opinion that Claude synthesizes and presents. Supports configurable reasoning effort levels and requires explicit user approval before each invocation.

## Structure

```
skills/
  <skill-name>/
    SKILL.md            # Skill definition (required)
    scripts/            # Helper scripts
    references/         # Reference docs
```

## Installation

Skills need to be copied (or symlinked) into `~/.claude/skills/` so Claude Code can discover them. To install all skills from this repo at once:

```bash
# Create the skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Symlink each skill (recommended -- stays in sync with the repo)
for skill in skills/*/; do
  ln -sfn "$(pwd)/$skill" ~/.claude/skills/"$(basename "$skill")"
done
```

Alternatively, copy them if you prefer a standalone install:

```bash
for skill in skills/*/; do
  cp -r "$skill" ~/.claude/skills/"$(basename "$skill")"
done
```

Once installed, skills activate automatically based on trigger phrases defined in each skill's `SKILL.md`.
