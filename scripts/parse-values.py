#!/usr/bin/env python3
"""Parse core-values.yml and output formatted markdown for Claude Code session injection."""
import os
import sys


def parse_yaml_simple(content):
    """Parse our constrained YAML structure without PyYAML dependency."""
    data = {"sections": []}
    current_section = None

    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Top-level key: value
        if line[0] != " " and ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            if key.strip() == "sections":
                continue
            data[key.strip()] = value
            continue

        # Section name
        if stripped.startswith("- name:"):
            name = stripped[7:].strip().strip('"').strip("'")
            current_section = {"name": name, "values": []}
            data["sections"].append(current_section)
            continue

        # Values list header
        if stripped == "values:":
            continue

        # Value item
        if stripped.startswith("- ") and current_section is not None:
            value = stripped[2:].strip().strip('"').strip("'")
            current_section["values"].append(value)

    return data


def format_markdown(data):
    """Format parsed config as markdown for session injection."""
    lines = ["## Core Values & Development Standards", ""]

    motto = data.get("motto", "")
    if motto:
        lines.extend([f"**{motto}**", ""])

    for section in data.get("sections", []):
        lines.append(f"### {section['name']}")
        for value in section.get("values", []):
            if ": " in value and not value.startswith("**"):
                key, _, rest = value.partition(": ")
                lines.append(f"- **{key}**: {rest}")
            else:
                lines.append(f"- {value}")
        lines.append("")

    return "\n".join(lines).rstrip()


def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else None
    if not config_path or not os.path.isfile(config_path):
        sys.exit(0)

    with open(config_path) as f:
        content = f.read()

    try:
        import yaml
        data = yaml.safe_load(content)
    except ImportError:
        data = parse_yaml_simple(content)

    if not data:
        sys.exit(0)

    print(format_markdown(data))


if __name__ == "__main__":
    main()
