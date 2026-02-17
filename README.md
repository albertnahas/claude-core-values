# Claude Core Values

A Claude Code plugin that injects configurable development standards and core values into every session. Define your team's principles once, enforce them automatically.

## How It Works

On every session start, the plugin reads your `core-values.yml` config and injects it as a system-level context message. Claude operates under these values for the entire session — no manual reminders needed.

## Installation

```bash
claude plugin add /path/to/claude-core-values
```

Or clone and add:

```bash
git clone https://github.com/albertonahas/claude-core-values.git
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
