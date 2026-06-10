#!/usr/bin/env python3
"""Crawl Apple HIG DocC JSON and write raw source evidence.

The crawler follows canonical HIG URLs under /design/human-interface-guidelines,
stores each raw JSON response unchanged, and emits an inventory file for later
distillation and verification.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path
from typing import Any


DATA_BASE = "https://developer.apple.com/tutorials/data"
WEB_BASE = "https://developer.apple.com"
ROOT_PATH = "/design/human-interface-guidelines"
HIG_PATH_RE = re.compile(r"/design/(?:human|Human)-(?:interface|Interface)-(?:guidelines|Guidelines)[\w\-/]*(?:#[\w\-]+)?")
USER_AGENT = "HIGAgentSkills-updater/1.0 (+https://github.com/justinwetch/HIGAgentSkills)"


def normalize_hig_path(value: str | None) -> str | None:
    if not value:
        return None

    parsed = urllib.parse.urlparse(value)
    path = parsed.path if parsed.scheme else value
    path = path.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    path = path.replace("/design/Human-Interface-Guidelines", ROOT_PATH)

    if path == ROOT_PATH or path.startswith(ROOT_PATH + "/"):
        return path
    return None


def slug_for_path(path: str) -> str:
    if path == ROOT_PATH:
        return "__root__"
    return path.removeprefix(ROOT_PATH + "/").strip("/")


def raw_filename_for_path(path: str) -> str:
    slug = slug_for_path(path)
    return slug.replace("/", "__") + ".json"


def endpoint_for_path(path: str) -> str:
    return f"{DATA_BASE}{path}.json"


def web_url_for_path(path: str) -> str:
    return f"{WEB_BASE}{path}"


def fetch_text(url: str, retries: int, delay: float) -> tuple[str | None, str | None]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8"), None
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = str(exc)
            if attempt < retries:
                time.sleep(delay * (attempt + 1))
    return None, last_error


def iter_json_values(value: Any) -> Any:
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from iter_json_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_json_values(item)


def extract_links(page: dict[str, Any]) -> list[str]:
    links: set[str] = set()

    references = page.get("references")
    if isinstance(references, dict):
        for ref in references.values():
            if isinstance(ref, dict):
                path = normalize_hig_path(ref.get("url"))
                if path:
                    links.add(path)

    text = json.dumps(
        {
            "primaryContentSections": page.get("primaryContentSections"),
            "topicSections": page.get("topicSections"),
            "sections": page.get("sections"),
            "references": page.get("references"),
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    for match in HIG_PATH_RE.finditer(text):
        path = normalize_hig_path(match.group(0))
        if path:
            links.add(path)

    return sorted(links)


def page_title(page: dict[str, Any], path: str) -> str:
    metadata = page.get("metadata")
    if isinstance(metadata, dict) and metadata.get("title"):
        return str(metadata["title"])

    identifier = page.get("identifier")
    identifier_url = identifier.get("url") if isinstance(identifier, dict) else None
    references = page.get("references")
    if isinstance(references, dict) and identifier_url in references:
        ref = references[identifier_url]
        if isinstance(ref, dict) and ref.get("title"):
            return str(ref["title"])

    slug = slug_for_path(path)
    return "Human Interface Guidelines" if slug == "__root__" else slug.replace("-", " ").title()


def page_role(page: dict[str, Any]) -> str | None:
    metadata = page.get("metadata")
    if isinstance(metadata, dict) and metadata.get("role"):
        return str(metadata["role"])
    return None


def build_disposition(slug: str, existing: set[str], role: str | None, path: str) -> str:
    if slug == "__root__":
        return "collection-only"
    if slug in existing:
        return "needs-current-source-review"
    if role == "collection" or path.count("/") <= ROOT_PATH.count("/"):
        return "needs-classification"
    return "needs-classification"


def apply_alias_dispositions(inventory: list[dict[str, Any]], existing: set[str]) -> None:
    by_hash: dict[str, list[dict[str, Any]]] = {}
    for record in inventory:
        by_hash.setdefault(record["source_sha256"], []).append(record)

    for records in by_hash.values():
        existing_records = [record for record in records if record["slug"] in existing]
        if not existing_records:
            continue
        canonical = sorted(existing_records, key=lambda record: (record["slug"].count("/"), record["slug"]))[0]
        for record in records:
            if record["slug"] in existing or record["slug"] == canonical["slug"]:
                continue
            record["distilled_file"] = canonical["distilled_file"]
            record["disposition"] = "alias-of-existing"
            record["alias_of"] = canonical["slug"]


def write_dispositions(output_dir: Path, inventory: list[dict[str, Any]]) -> None:
    counts: dict[str, int] = {}
    for record in inventory:
        counts[record["disposition"]] = counts.get(record["disposition"], 0) + 1

    lines = [
        "# Apple HIG Inventory Dispositions",
        "",
        "Generated by `scripts/crawl_apple_hig.py` from the current Apple HIG JSON crawl.",
        "",
        "## Summary",
        "",
    ]
    for disposition, count in sorted(counts.items()):
        lines.append(f"- `{disposition}`: {count}")

    lines.extend(
        [
            "",
            "## Records",
            "",
            "| Slug | Title | Disposition | Distilled file | Alias of |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for record in inventory:
        lines.append(
            "| {slug} | {title} | {disposition} | {distilled} | {alias_of} |".format(
                slug=record["slug"],
                title=str(record["title"]).replace("|", "\\|"),
                disposition=record["disposition"],
                distilled=record.get("distilled_file") or "",
                alias_of=record.get("alias_of") or "",
            )
        )

    (output_dir / "dispositions.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def apply_overrides(inventory: list[dict[str, Any]], overrides_path: Path | None) -> None:
    if not overrides_path or not overrides_path.exists():
        return

    overrides = json.loads(overrides_path.read_text(encoding="utf-8"))
    by_slug = {record["slug"]: record for record in inventory}
    for slug, override in overrides.items():
        if slug not in by_slug:
            continue
        record = by_slug[slug]
        for key in ("disposition", "distilled_file", "alias_of", "notes"):
            if key in override:
                record[key] = override[key]


def crawl(output_dir: Path, retries: int, delay: float, overrides_path: Path | None) -> int:
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    existing = {path.stem for path in Path("distilled").glob("*.md")}
    queue: deque[str] = deque([ROOT_PATH])
    seen: set[str] = set()
    failures: list[dict[str, str]] = []
    inventory: list[dict[str, Any]] = []

    while queue:
        path = queue.popleft()
        if path in seen:
            continue
        seen.add(path)

        endpoint = endpoint_for_path(path)
        raw_text, error = fetch_text(endpoint, retries=retries, delay=delay)
        if raw_text is None:
            failures.append({"path": path, "json_endpoint": endpoint, "error": error or "unknown error"})
            continue

        raw_path = raw_dir / raw_filename_for_path(path)
        raw_path.write_text(raw_text, encoding="utf-8")
        source_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

        try:
            page = json.loads(raw_text)
        except json.JSONDecodeError as exc:
            failures.append({"path": path, "json_endpoint": endpoint, "error": f"invalid json: {exc}"})
            continue

        links = extract_links(page)
        for link in links:
            if link not in seen:
                queue.append(link)

        slug = slug_for_path(path)
        role = page_role(page)
        inventory.append(
            {
                "slug": slug,
                "title": page_title(page, path),
                "apple_url": web_url_for_path(path),
                "json_endpoint": endpoint,
                "raw_file": str(raw_path.as_posix()),
                "source_sha256": source_hash,
                "kind": page.get("kind"),
                "role": role,
                "references_discovered": links,
                "distilled_file": f"distilled/{slug}.md" if slug in existing else None,
                "disposition": build_disposition(slug, existing, role, path),
            }
        )

    apply_alias_dispositions(inventory, existing)
    apply_overrides(inventory, overrides_path)
    inventory.sort(key=lambda item: (item["slug"] == "__root__", item["slug"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_dir / "failures.json").write_text(json.dumps(failures, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_dispositions(output_dir, inventory)

    print(f"wrote {len(inventory)} inventory records to {output_dir / 'inventory.json'}")
    print(f"wrote {len(failures)} failures to {output_dir / 'failures.json'}")
    print(f"wrote dispositions to {output_dir / 'dispositions.md'}")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default=f"sources/apple-hig-{dt.date.today().isoformat()}")
    parser.add_argument("--overrides", default=None, help="Optional JSON disposition overrides keyed by slug")
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()
    overrides_path = Path(args.overrides) if args.overrides else None
    return crawl(Path(args.output_dir), retries=args.retries, delay=args.delay, overrides_path=overrides_path)


if __name__ == "__main__":
    sys.exit(main())
