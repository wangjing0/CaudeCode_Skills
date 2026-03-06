# Claude Code Documentation Index

Base URL: `https://code.claude.com/docs`

Fetch any page as: `https://code.claude.com/docs/en/<path>`

## Getting Started

| Path | Topic |
|---|---|
| `/en/overview` | What Claude Code is, capabilities overview, all available surfaces |
| `/en/quickstart` | First session walkthrough, essential commands table |
| `/en/setup` | Advanced install options, manual updates, uninstall |
| `/en/terminal-guide` | Terminal basics for new users |
| `/en/how-claude-code-works` | Agentic loop, built-in tools, context management internals |

## Core Usage

| Path | Topic |
|---|---|
| `/en/best-practices` | Context management, prompting patterns, verification, parallel sessions |
| `/en/common-workflows` | Codebase exploration, debugging, refactoring, tests, PRs, images, @ references |
| `/en/model-config` | Model selection, effort level (Opus 4.6 adaptive reasoning), thinking modes |
| `/en/sessions` | Session management, resume, /clear, /compact, checkpointing, /rewind |
| `/en/checkpointing` | Restore conversation and code state, rewind menu |
| `/en/costs` | Token usage, billing, reducing costs |
| `/en/headless` | Non-interactive mode (`-p` flag), CI/CD integration, output formats |

## Memory & Instructions

| Path | Topic |
|---|---|
| `/en/memory` | CLAUDE.md files (all scopes), auto memory, `.claude/rules/`, path-specific rules, `/memory` command |

## Extending Claude Code

| Path | Topic |
|---|---|
| `/en/features-overview` | Compare CLAUDE.md vs Skills vs Subagents vs MCP vs Hooks vs Plugins |
| `/en/skills` | Create skills, SKILL.md format, frontmatter fields, skill discovery, bundled skills |
| `/en/sub-agents` | Custom subagents, `.claude/agents/`, frontmatter, tool access, worktree isolation |
| `/en/agent-teams` | Coordinate multiple independent sessions, shared tasks, peer messaging |
| `/en/hooks` | Hook event reference, payload schemas, configuration |
| `/en/hooks-guide` | Step-by-step hook setup, notifications, linting examples |
| `/en/mcp` | MCP overview, adding servers (`claude mcp add`), scope hierarchy, tool search |
| `/en/plugins` | Install plugins, plugin structure, namespacing |
| `/en/plugin-marketplaces` | Browse and host plugin collections |
| `/en/discover-plugins` | Code intelligence plugins, available plugin catalog |

## Configuration & Settings

| Path | Topic |
|---|---|
| `/en/settings` | All settings keys, settings files hierarchy, environment variables |
| `/en/permissions` | Permission modes, allowlists, managed settings, `/permissions` command |
| `/en/sandboxing` | OS-level isolation, sandbox configuration |
| `/en/authentication` | Login methods, credential management, API key setup |
| `/en/third-party-integrations` | Amazon Bedrock, Google Vertex AI, Microsoft Foundry |

## IDE & Surface Integrations

| Path | Topic |
|---|---|
| `/en/vs-code` | VS Code extension install, inline diffs, @-mentions, plan review |
| `/en/jetbrains` | IntelliJ, PyCharm, WebStorm plugin, diff viewing |
| `/en/desktop` | Desktop app, parallel sessions, visual diff |
| `/en/desktop-quickstart` | Desktop app first use |
| `/en/claude-code-on-the-web` | Browser-based sessions, claude.ai/code |
| `/en/remote-control` | Continue local sessions from phone or another device |
| `/en/chrome` | Claude in Chrome extension for debugging live web apps |

## CI/CD & Automation

| Path | Topic |
|---|---|
| `/en/github-actions` | GitHub Actions integration, automated PR review |
| `/en/gitlab-ci-cd` | GitLab CI/CD integration |
| `/en/slack` | Slack integration, @Claude mentions → pull requests |

## CLI Reference

| Path | Topic |
|---|---|
| `/en/cli-reference` | All CLI flags, commands, output formats |
| `/en/statusline` | Custom status line showing context usage, model |
| `/en/terminal-config` | Terminal setup for Option key shortcuts |

## Troubleshooting

| Path | Topic |
|---|---|
| `/en/troubleshooting` | Common issues, auth problems, performance, known limitations |

## Key Blog Posts (fetch from `https://claude.com/blog/<slug>`)

| Slug | Topic |
|---|---|
| `/claude-code-on-the-web` | Claude Code web surface launch (Oct 2025) |
| `/how-anthropic-teams-use-claude-code` | Internal usage patterns from Anthropic (Jul 2025) |
| `/cowork-research-preview` | Cowork feature research preview (Jan 2026) |
| `/how-enterprises-are-building-ai-agents-in-2026` | Enterprise agent patterns (Dec 2025) |

## Community Search Queries

For community knowledge, use WebSearch with these patterns:

- Recent tips: `site:reddit.com/r/ClaudeCode <topic>`
- Known issues: `site:reddit.com/r/ClaudeAI "Claude Code" <problem>`
- Workarounds: `site:reddit.com/r/ClaudeCode workaround <feature>`
- Anthropic news/releases: `site:reddit.com/r/Anthropic <topic>`
- General Claude Q&A: `site:reddit.com/r/claude <topic>`
