---
name: guide-me
description: Live guidance for Claude Code (the CLI tool and agentic coding environment). Answers questions about features, configuration, workflows, hooks, MCP servers, skills, CLAUDE.md, IDE integrations, keyboard shortcuts, settings, and best practices. Fetches up-to-date information from official Anthropic documentation, blogs, and community discussions at runtime. Use when users ask "How do I...", "Can Claude Code...", "What is...", "Why isn't...", or anything about Claude Code behavior or setup.
---

# Claude Code Guide

Answer questions about Claude Code by fetching live information from authorized sources at runtime.

## Authorized Sources

| Source | URL | Use for |
|---|---|---|
| Official docs | `https://code.claude.com/docs/en/<page>` | Accurate feature info, setup, API |
| Docs index | `https://code.claude.com/docs/llms.txt` | Discover all page paths |
| Blog | `https://claude.com/blog/<slug>` | Release announcements, use cases |
| Reddit r/ClaudeCode | `https://www.reddit.com/r/ClaudeCode/` | Community tips, workarounds, real-world usage |
| Reddit r/ClaudeAI | `https://www.reddit.com/r/ClaudeAI/` | Broader community knowledge |
| Reddit r/Anthropic | `https://www.reddit.com/r/Anthropic/` | Anthropic news, model releases, company updates |
| Reddit r/claude | `https://www.reddit.com/r/claude/` | General Claude usage, prompting, community Q&A |

**Important:** Never invent URLs or fabricate documentation content. Always fetch to verify.

## Runtime Lookup Workflow

1. Identify the topic from the user's question
2. Match to a page from [references/docs-index.md](references/docs-index.md)
3. WebFetch that page for authoritative content
4. For community context, use WebSearch targeting `site:reddit.com/r/ClaudeCode`, `site:reddit.com/r/ClaudeAI`, `site:reddit.com/r/Anthropic`, or `site:reddit.com/r/claude`
5. Synthesize and cite the source URL in your answer

When the right page is unclear, fetch `https://code.claude.com/docs/llms.txt` first to browse all available pages.

## When to Fetch vs When to Know

**Always fetch for:**
- Specific CLI flags, settings keys, or environment variable names
- Installation steps or version-specific behavior
- MCP server configuration schemas
- Hook event names and payloads
- Pricing or subscription details

**Use community search for:**
- Workarounds to known issues
- Real-world integration patterns
- Tips not covered in official docs
- Questions starting with "Has anyone..."

## Key Doc Pages Quick Reference

Read [references/docs-index.md](references/docs-index.md) to find the right URL for any topic. Key areas:

- **Setup & install**: `/en/overview`, `/en/quickstart`, `/en/setup`
- **CLAUDE.md & memory**: `/en/memory`
- **Best practices**: `/en/best-practices`, `/en/common-workflows`
- **Extending Claude Code**: `/en/features-overview`, `/en/skills`, `/en/hooks`, `/en/hooks-guide`, `/en/mcp`, `/en/sub-agents`
- **CLI reference**: `/en/cli-reference`
- **IDE integrations**: `/en/vs-code`, `/en/jetbrains`
- **Settings & permissions**: `/en/settings`, `/en/permissions`
- **Troubleshooting**: `/en/troubleshooting`

## Common Questions Answered Without Fetching

These facts are stable enough to answer directly:

**Installation**: `curl -fsSL https://claude.ai/install.sh | bash` (macOS/Linux/WSL). Homebrew: `brew install --cask claude-code`. The CLI command is `claude`.

**CLAUDE.md hierarchy**: managed policy → user (`~/.claude/CLAUDE.md`) → project (`./CLAUDE.md`) → local (`CLAUDE.local.md`). Keep files under 200 lines. Run `/init` to generate a starter file.

**Context window management**: Use `/clear` between unrelated tasks. Run `/compact` to summarize. Auto-compaction triggers near context limits.

**Session resume**: `claude --continue` (most recent), `claude --resume` (picker), `claude --resume <name>`.

**Plan Mode**: `Shift+Tab` to cycle modes, or `--permission-mode plan`. Use before multi-file changes.

**Hooks vs CLAUDE.md**: Hooks are deterministic scripts that always run; CLAUDE.md is advisory context Claude may or may not follow.

**Skills vs Subagents**: Skills are reusable knowledge/workflows loaded into context. Subagents run in isolated context and return summaries.
