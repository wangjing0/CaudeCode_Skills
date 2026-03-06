# Skills

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

## Usage

Skills are installed into Claude Code via the `~/.claude/` configuration directory. Once installed, they activate automatically based on trigger phrases defined in each skill's `SKILL.md`.
