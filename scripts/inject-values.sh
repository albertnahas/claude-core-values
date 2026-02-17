#!/bin/bash
set -euo pipefail

# Find core-values config (project-level takes precedence over user-level)
CONFIG=""
if [ -n "${CLAUDE_PROJECT_DIR:-}" ] && [ -f "$CLAUDE_PROJECT_DIR/.claude/core-values.yml" ]; then
  CONFIG="$CLAUDE_PROJECT_DIR/.claude/core-values.yml"
elif [ -f "$HOME/.claude/core-values.yml" ]; then
  CONFIG="$HOME/.claude/core-values.yml"
fi

if [ -z "$CONFIG" ]; then
  exit 0
fi

python3 "$CLAUDE_PLUGIN_ROOT/scripts/parse-values.py" "$CONFIG"
