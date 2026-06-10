#!/usr/bin/env python3
"""Validate distilled HIG corpus frontmatter and routing assumptions."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {"topic", "tier", "platforms", "category", "triggers", "related"}
VALID_TIERS = {1, 2, 3, 4}


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
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter")
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


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def validate(distilled_dir: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    records: dict[str, dict[str, Any]] = {}

    for path in sorted(distilled_dir.glob("*.md")):
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue

        slug = path.stem
        records[slug] = meta

        missing = REQUIRED_FIELDS - set(meta)
        if missing:
            errors.append(f"{path}: missing fields {', '.join(sorted(missing))}")
        if meta.get("topic") != slug:
            errors.append(f"{path}: topic {meta.get('topic')!r} does not match filename {slug!r}")
        if meta.get("tier") not in VALID_TIERS:
            errors.append(f"{path}: invalid tier {meta.get('tier')!r}")
        if not as_list(meta.get("platforms")):
            errors.append(f"{path}: platforms must be nonempty")
        if not as_list(meta.get("triggers")):
            errors.append(f"{path}: triggers must be nonempty")

        trigger_counts = Counter(str(trigger).lower() for trigger in as_list(meta.get("triggers")))
        duplicates = [trigger for trigger, count in trigger_counts.items() if count > 1]
        if duplicates:
            warnings.append(f"{path}: duplicate triggers within file: {', '.join(duplicates)}")

    known = set(records)
    global_triggers: dict[str, list[str]] = defaultdict(list)
    for slug, meta in records.items():
        for related in as_list(meta.get("related")):
            if related not in known:
                errors.append(f"distilled/{slug}.md: related file does not exist: {related}")
        for trigger in as_list(meta.get("triggers")):
            global_triggers[str(trigger).lower()].append(slug)

    for trigger, slugs in sorted(global_triggers.items()):
        unique_slugs = sorted(set(slugs))
        if len(unique_slugs) > 1:
            warnings.append(f"trigger maps to multiple files: {trigger} -> {', '.join(unique_slugs)}")

    tier_counts = Counter(meta.get("tier") for meta in records.values())
    print(f"files: {len(records)}")
    for tier in sorted(VALID_TIERS):
        print(f"tier {tier}: {tier_counts.get(tier, 0)}")
    print(f"warnings: {len(warnings)}")
    for warning in warnings[:50]:
        print(f"warning: {warning}")
    if len(warnings) > 50:
        print(f"warning: ... {len(warnings) - 50} more")

    if errors:
        print(f"errors: {len(errors)}", file=sys.stderr)
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print("errors: 0")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distilled-dir", default="distilled")
    args = parser.parse_args()
    return validate(Path(args.distilled_dir))


if __name__ == "__main__":
    sys.exit(main())
