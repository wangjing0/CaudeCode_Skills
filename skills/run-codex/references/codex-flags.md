# Codex CLI Configuration Options

## Model Selection (`-m` / `--model`)

| Model         | Description                          |
| ------------- | ------------------------------------ |
| `gpt-5-codex` | Latest frontier agentic coding model |

Model selection is restricted to the allowlist above. Requests for unlisted models must be rejected.

## Global Flags

| Flag                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `-C <dir>` / `--cd <dir>` | Set working directory                            |
| `--add-dir <DIR>`         | Additional directories that should be writable   |
| `--full-auto`             | Shorthand for workspace-write with auto-approval |

## Exec Subcommand Flags

| Flag                     | Description                       |
| ------------------------ | --------------------------------- |
| `-o <file>`              | Write output to file              |
| `--json`                 | Output in JSONL event format      |
| `--output-schema <FILE>` | Structured output schema          |
| `--skip-git-repo-check`  | Bypass git repository requirement |
