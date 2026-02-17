---
name: core-values
description: Initialize or view your core development values
argument-hint: "[init|show]"
allowed-tools: ["Read", "Write", "Bash", "Glob", "AskUserQuestion"]
---

Manage the user's core development values configuration.

## Determine Action

Check the user's argument:
- **No argument or "show"**: Display current values
- **"init"**: Initialize or reinitialize values from a template

## Show Current Values

1. Look for the config file in this order:
   - Project-level: `<current working directory>/.claude/core-values.yml`
   - User-level: `~/.claude/core-values.yml`
2. If found, read the file and display the values in a nicely formatted summary
3. If not found, tell the user no core values are configured and offer to run `/core-values init`

## Initialize Values

1. Read all template files from `$CLAUDE_PLUGIN_ROOT/templates/` using Glob for `$CLAUDE_PLUGIN_ROOT/templates/*.yml`, then Read each file
2. Present the available templates to the user using AskUserQuestion with these options:
   - **Craftsman** — Quality-obsessed. No half solutions. No shortcuts. Zero tolerance for broken code.
   - **Startup** — Ship fast, iterate rapidly, pragmatic quality. Bias for action.
   - **Security-First** — Defense in depth, zero trust, OWASP compliance. Security as foundation.
   - **Minimal** — Simple baseline: working code, follow patterns, test before push.
3. After the user picks a template, read the chosen template YAML from `$CLAUDE_PLUGIN_ROOT/templates/<name>.yml`
4. Ask the user where to install using AskUserQuestion:
   - **User-level (~/.claude/core-values.yml)** — Applies to all projects (Recommended)
   - **Project-level (.claude/core-values.yml)** — Only this project
5. Create the `.claude/` directory if it doesn't exist, then write the template content to the chosen path
6. Tell the user:
   - Their values are now active and will load on every new session
   - They can edit the YAML file directly to customize sections, add values, or change the motto
   - Project-level config takes precedence over user-level if both exist
   - Restart Claude Code (or start a new session) for values to take effect
