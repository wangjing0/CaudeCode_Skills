---
name: run-codex
description: Read-only oracle using OpenAI Codex CLI. NOT for implementation, writing code, or fixing bugs -- analysis and recommendations only. Trigger on "use Codex", "ask Codex", "consult Codex", "run Codex", "have Codex look at", "Codex review", "get Codex opinion", "what does Codex think", "second opinion", "consult the oracle", "ask the oracle", or any mention of using Codex or GPT for planning, review, or analysis.
---

# Run Codex

Use OpenAI Codex CLI as a **read-only oracle** for planning, review, and analysis. Codex provides its perspective; synthesize and present results to the user.

**Sandbox is always `read-only`**. Codex must never implement changes.

## User Approval Requirement

**ALWAYS ask the user for permission before running any Codex-related Bash command.** This includes `scripts/check-codex.sh`, `scripts/run-codex-exec.sh`, and any other `codex` CLI invocation. Before executing, show the user what will be run (the constructed prompt, effort level, and timeout) and wait for explicit approval. Never auto-execute Codex calls.

## Arguments

Parse `$ARGUMENTS` for:

- **query** -- the main question or task (everything not a flag). If empty, ask the user to provide a query and stop.
- `--reasoning <level>` -- override reasoning effort (`none`, `low`, `medium`, `high`, `xhigh`). Default is auto-selected based on complexity.

## Prerequisites

Run the check script before any Codex invocation:

```bash
scripts/check-codex.sh
```

If it exits non-zero, display the error and stop. Use the wrapper for all `codex exec` calls:

```bash
scripts/run-codex-exec.sh
```

### Upgrading Codex CLI

The model allowlist in this skill is version-sensitive — an outdated CLI may reject newer models or effort levels. If `scripts/check-codex.sh --verbose` reports an old version, the user must upgrade manually. Do not run upgrade commands automatically; show the appropriate command and wait for the user to confirm and run it themselves.

**npm (recommended):**
```bash
npm install -g @openai/codex@latest
```

**Homebrew:**
```bash
brew upgrade codex
```

After upgrading, re-run `scripts/check-codex.sh --verbose` to confirm the new version.

## Configuration

| Setting   | Default           | Override                                        |
| --------- | ----------------- | ----------------------------------------------- |
| Model     | `gpt-5.3-codex`   | Allowlist only (see `references/codex-flags.md`) |
| Reasoning | Auto              | `--reasoning <level>` or user prose             |
| Sandbox   | `read-only`       | Not overridable                                 |

### Reasoning Effort

| Complexity | Effort   | Timeout  | Criteria                             |
| ---------- | -------- | -------- | ------------------------------------ |
| Trivial    | `none`   | 300000ms | Single question, no files            |
| Simple     | `low`    | 300000ms | <3 files, quick question             |
| Moderate   | `medium` | 300000ms | 3-10 files, focused analysis         |
| Complex    | `high`   | 600000ms | Multi-module, architectural thinking |
| Critical   | `xhigh`  | 600000ms | Deep architectural or security work  |

For `high` or `xhigh` effort tasks that may exceed 10 minutes, use `run_in_background: true` on the Bash tool and set `CODEX_OUTPUT` so the output can be read later.

See `references/codex-flags.md` for full flag documentation.

## Workflow

### 1. Parse and Validate

1. Parse `$ARGUMENTS` for query and `--reasoning`
2. Ask the user for permission, then run `scripts/check-codex.sh` -- abort on failure
3. Assess complexity to select reasoning effort (unless overridden)

### 2. Construct Prompt

Build a focused prompt by assembling relevant context before the ask. Include only what Codex needs to answer well -- more context is not always better.

**Context checklist** (include each item only when relevant to the query):

1. **Objective** -- one sentence stating what the user wants analyzed and why
2. **Files / code** -- inline the relevant snippets or file paths Codex should inspect; for large files, excerpt the key sections rather than dumping everything
3. **Diffs** -- include `git diff` output when reviewing recent changes or PRs
4. **Constraints** -- mention language version, framework, performance budget, or compliance requirements that should shape the analysis
5. **Prior context** -- summarize any earlier conversation decisions or rejected approaches so Codex does not retread them
6. **Desired output format** -- state explicitly what you want back (e.g., "bullet list of issues with file:line references", "pros/cons table", "implementation plan with phases")

**Prompt structure**:

```
[Objective -- what to analyze and why]

[Context -- code, diffs, constraints, prior decisions]

[Ask -- what output format and depth you expect]
```

Keep it direct. Do not ask Codex to implement changes -- request analysis and recommendations only.

### 3. Execute

Before running, present the user with a summary of what will be sent:
- The effort level and timeout
- A preview of the constructed prompt (or a summary if very long)

Wait for explicit user approval before invoking the wrapper.

Invoke via the wrapper with HEREDOC. Set the Bash tool timeout per the reasoning effort table above.

```bash
EFFORT="<effort>" \
CODEX_OUTPUT="/tmp/codex-${RANDOM}${RANDOM}.txt" \
scripts/run-codex-exec.sh <<'EOF'
[constructed prompt]
EOF
```

For long-running `high` effort queries, consider `run_in_background: true` on the Bash tool call, then read `CODEX_OUTPUT` when done.

### 4. Present Results

Read the output file and present with attribution:

```
## Codex Analysis

[Codex output -- summarize if >200 lines]

---
Model: gpt-5.3-codex | Reasoning: [effort level]
```

Synthesize key insights and actionable items for the user.
