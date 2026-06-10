#!/usr/bin/env python3
"""Report Apple HIG update progress from the crawled inventory."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


TIER_RE = re.compile(r"^tier:\s*(\d+)\s*$", re.MULTILINE)


def distilled_tiers(distilled_dir: Path) -> dict[str, int]:
    tiers: dict[str, int] = {}
    for path in distilled_dir.glob("*.md"):
        match = TIER_RE.search(path.read_text(encoding="utf-8"))
        if match:
            tiers[path.as_posix()] = int(match.group(1))
    return tiers


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path, help="Path to sources/.../inventory.json")
    parser.add_argument("--distilled-dir", type=Path, default=Path("distilled"))
    parser.add_argument("--pending", action="store_true", help="List pending current-source review records")
    parser.add_argument("--tier", type=int, choices=(1, 2, 3, 4), help="Limit pending records to a tier")
    parser.add_argument("--limit", type=int, default=0, help="Maximum pending records to print; 0 means all")
    args = parser.parse_args()

    records = json.loads(args.inventory.read_text(encoding="utf-8"))
    tiers = distilled_tiers(args.distilled_dir)

    counts = Counter(record["disposition"] for record in records)
    print("dispositions:")
    for disposition, count in sorted(counts.items()):
        print(f"  {disposition}: {count}")

    tier_files: dict[int, set[str]] = {1: set(), 2: set(), 3: set(), 4: set()}
    pending: list[dict[str, object]] = []
    for record in records:
        distilled_file = record.get("distilled_file")
        tier = tiers.get(str(distilled_file).replace("\\", "/")) if distilled_file else None
        if tier:
            tier_files[tier].add(str(distilled_file).replace("\\", "/"))
        if record["disposition"] == "needs-current-source-review":
            if args.tier is None or tier == args.tier:
                pending.append({**record, "tier": tier})

    print("\nunique distilled files in inventory by tier:")
    for tier in (1, 2, 3, 4):
        print(f"  tier {tier}: {len(tier_files[tier])}")

    print(f"\npending current-source review: {len(pending)}")
    if args.pending:
        shown = pending if args.limit == 0 else pending[: args.limit]
        for record in shown:
            tier = record.get("tier") or "?"
            print(f"  tier {tier}: {record['slug']} -> {record.get('distilled_file') or ''}")
        if args.limit and len(pending) > args.limit:
            print(f"  ... {len(pending) - args.limit} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
