#!/usr/bin/env python3
"""Generate routing-index.md from distilled file frontmatter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [item.strip().strip("\"'") for item in inner.split(",") if item.strip()]
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.isdigit():
        return int(value)
    return value


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated frontmatter")
    frontmatter = text[4:end].splitlines()

    result: dict[str, Any] = {}
    current_key: str | None = None
    for line in frontmatter:
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            result.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            result[key] = [] if value == "" else parse_scalar(value)
    return result


def triggers_for(meta: dict[str, Any]) -> str:
    triggers = meta.get("triggers") or []
    return ", ".join(str(trigger).lower() for trigger in triggers)


def generate(distilled_dir: Path) -> str:
    records = []
    for path in sorted(distilled_dir.glob("*.md")):
        meta = parse_frontmatter(path)
        records.append({"file": path.stem, "meta": meta})

    tier1 = [record["file"] for record in records if record["meta"].get("tier") == 1]
    tier2 = [record for record in records if record["meta"].get("tier") == 2]
    tier3 = [record for record in records if record["meta"].get("tier") == 3]
    tier4 = [record for record in records if record["meta"].get("tier") == 4]

    lines = [
        "# HIG Skill Routing Index",
        "",
        "_Auto-generated from frontmatter by `scripts/generate_routing_index.py`. Do not edit manually._",
        "",
        "## tier-1 (always load)",
        "",
        ", ".join(tier1),
        "",
        "## tier-2 platform-map",
        "",
    ]

    for record in tier2:
        lines.append(f"{triggers_for(record['meta'])} → {record['file']}")

    lines.extend(["", "## tier-3 trigger-map", ""])
    for record in tier3:
        lines.append(f"{triggers_for(record['meta'])} → {record['file']}")

    lines.extend(["", "## tier-4 trigger-map (on-demand)", ""])
    for record in tier4:
        lines.append(f"{triggers_for(record['meta'])} → {record['file']}")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distilled-dir", default="distilled")
    parser.add_argument("--output", default="routing-index.md")
    parser.add_argument("--check", action="store_true", help="Exit nonzero if output is stale")
    args = parser.parse_args()

    generated = generate(Path(args.distilled_dir))
    output_path = Path(args.output)
    if args.check:
        current = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        if current != generated:
            print(f"{output_path} is stale", file=sys.stderr)
            return 1
        print(f"{output_path} is current")
        return 0

    output_path.write_text(generated, encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
