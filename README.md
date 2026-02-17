# Claude Core Values

A Claude Code plugin that injects configurable development standards and core values into every session. Define your team's principles once, enforce them automatically.

## Why Not Just Use CLAUDE.md?

You can — `~/.claude/CLAUDE.md` supports global instructions. But there are documented reasons why instructions placed there get ignored in practice, and this plugin addresses each one.

### The CLAUDE.md Problem

CLAUDE.md content is [injected with a disclaimer](https://github.com/anthropics/claude-code/issues/22309) that tells Claude it *"may or may not be relevant"* and should only be followed *"if highly relevant."* This framing causes Claude to [treat your rules as suggestions](https://github.com/anthropics/claude-code/issues/21119), especially as context grows. Multiple open issues ([#7777](https://github.com/anthropics/claude-code/issues/7777), [#15443](https://github.com/anthropics/claude-code/issues/15443), [#21385](https://github.com/anthropics/claude-code/issues/21385)) document Claude ignoring explicit CLAUDE.md instructions in favor of training-data patterns.

On top of that, CLAUDE.md is loaded once at session start. As the conversation grows, your values compete with thousands of tokens of code, tool output, and discussion. When the context window fills and gets [compacted](https://code.claude.com/docs/en/hooks), CLAUDE.md content gets summarized away with everything else.

### How This Plugin Fixes It

The plugin uses a **three-layer reinforcement** strategy that CLAUDE.md cannot replicate:

| Layer | Hook Event | What It Does |
|-------|-----------|-------------|
| **Full injection** | `SessionStart` | Injects all values at session start — and re-injects them fresh after every compaction (the hook fires on `compact` too) |
| **Per-prompt reminder** | `UserPromptSubmit` | Reinforces your motto on every single prompt, keeping values salient as context grows |
| **No disclaimer** | Both | Hook output arrives as a clean `system-reminder` — no *"may or may not be relevant"* framing undermining your instructions |

This means your values are injected without the disclaimer that weakens CLAUDE.md, reinforced on every interaction so they don't fade, and automatically restored after context compaction.

### Plus: Better Management

Beyond the reinforcement advantage, the plugin also provides:

- **Starter templates.** Pick `craftsman`, `startup`, `security-first`, or `minimal` — running in one command instead of staring at a blank file.
- **Team distribution.** `claude plugin add` gives everyone identical standards. No "copy these 30 lines" and no drift.
- **Per-project overrides.** Run different values per project without touching any CLAUDE.md.
- **Structured config.** YAML with typed sections, easier to diff and version than freeform markdown.

## How It Works

The plugin reads your `core-values.yml` and injects it through two hooks:

1. **SessionStart** — Full values injected when any session begins (new, resumed, or post-compaction). ~300-400 tokens depending on template.
2. **UserPromptSubmit** — Only your motto as a single-line reminder (~15 tokens per prompt). Over a 50-turn session that's ~750 tokens total — negligible against a 200k context window.

## Installation

```bash
git clone https://github.com/albertnahas/claude-core-values.git
claude plugin add ./claude-core-values
```

## Quick Start

```
/core-values init
```

Pick a template, choose where to save (user-level or project-level), done.

## Templates

| Template | Philosophy |
|----------|-----------|
| **Craftsman** | Quality-obsessed. No half solutions. No shortcuts. Zero tolerance for broken code. |
| **Startup** | Ship fast, iterate rapidly, pragmatic quality. Bias for action over perfection. |
| **Security-First** | Defense in depth, zero trust, OWASP compliance. Security as foundation. |
| **Minimal** | Simple baseline: working code, follow patterns, test before push. |

## Commands

### `/core-values init`

Interactive setup. Pick a template and install location:

- **User-level** (`~/.claude/core-values.yml`) — applies to all projects
- **Project-level** (`.claude/core-values.yml`) — applies to one project only

Project-level config takes precedence when both exist.

### `/core-values show`

Display your currently active values.

## Configuration

The config file is plain YAML:

```yaml
motto: "Excellence is not negotiable. Quality over speed."

sections:
  - name: Quality Commitment
    values:
      - "No Half Solutions: Always fix everything until it's 100% functional."
      - "No Corner Cutting: Do the real work until completion."

  - name: Code Quality
    values:
      - "Console errors are not acceptable."
      - "Verify it works before you push."
```

Edit it directly anytime. Changes take effect on the next session.

## Requirements

- Claude Code
- Python 3 (for YAML parsing; ships with macOS and most Linux distros)
- PyYAML is optional — the plugin includes a zero-dependency fallback parser

## License

MIT
