# Productivity Agent Skills

My customized skills for Claude Code. Create with the help of latest [skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills). Each skill lives under `skills/<skill-name>/` and follows the standard agent skill format.

## Available Skills

### /run-codex

Uses OpenAI Codex CLI as a read-only oracle for planning, code review, and analysis. Codex never implements changes directly -- it provides a second opinion that Claude synthesizes and presents. Supports configurable reasoning effort levels and requires explicit user approval before each invocation.

### /guide-me

Live guidance for Claude Code. Answers questions about features, configuration, workflows, hooks, MCP servers, skills, CLAUDE.md, IDE integrations, and best practices by fetching up-to-date information from official Anthropic documentation and community discussions at runtime.


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

Once installed, exit and restart Claude Code, and skills activate automatically based on trigger phrases defined in each skill's `SKILL.md`.


To use a skill, simply mention the trigger phrase in your Claude Code session. For example, to use the `run-codex` skill, you can say:

```
/run-codex Review the code in the current directory and suggest tests and improvements.
```

To use the `guide-me` skill, you can say:

```
/guide-me What is the difference between a skill and a subagent in Claude Code?
```