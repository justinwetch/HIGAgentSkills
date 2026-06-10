#!/usr/bin/env python3
"""Render crawled Apple HIG DocC JSON to source markdown.

This renderer is intentionally conservative: it preserves source structure for
review and distillation, but it does not try to compress or rewrite guidance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def plain_text(value: Any, references: dict[str, Any]) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "".join(plain_text(item, references) for item in value)
    if not isinstance(value, dict):
        return str(value)

    kind = value.get("type")
    if kind == "text":
        return str(value.get("text", ""))
    if kind == "codeVoice":
        return f"`{value.get('code') or value.get('text') or ''}`"
    if kind == "image":
        description = image_description(value, references)
        return f"[Image: {description}]" if description else ""
    if kind == "strong":
        inner = plain_text(value.get("inlineContent"), references)
        return f"**{inner}**" if inner else ""
    if kind == "emphasis":
        inner = plain_text(value.get("inlineContent"), references)
        return f"*{inner}*" if inner else ""
    if kind == "reference":
        identifier = value.get("identifier")
        ref = references.get(identifier, {}) if identifier else {}
        title = ref.get("title") or identifier or ""
        url = ref.get("url") or identifier or ""
        if url and str(url).startswith("/"):
            url = "https://developer.apple.com" + str(url)
        return f"[{title}]({url})" if url else str(title)
    if "inlineContent" in value:
        return plain_text(value.get("inlineContent"), references)
    if "text" in value:
        return str(value.get("text", ""))
    return ""


def image_description(value: dict[str, Any], references: dict[str, Any]) -> str:
    identifier = value.get("identifier")
    ref = references.get(identifier, {}) if identifier else {}
    parts: list[str] = []

    metadata = value.get("metadata") if isinstance(value.get("metadata"), dict) else {}
    abstract = metadata.get("abstract") if isinstance(metadata, dict) else None
    abstract_text = clean_line(plain_text(abstract, references))
    if abstract_text:
        parts.append(abstract_text)

    alt = clean_line(str(ref.get("alt") or value.get("alt") or ""))
    if alt and alt not in parts:
        parts.append(alt)

    ref_abstract = ref.get("abstract") if isinstance(ref, dict) else None
    ref_abstract_text = clean_line(plain_text(ref_abstract, references))
    if ref_abstract_text and ref_abstract_text not in parts:
        parts.append(ref_abstract_text)

    return " ".join(parts)


def clean_line(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def render_list_items(items: Any, references: dict[str, Any], ordered: bool) -> list[str]:
    lines: list[str] = []
    if not isinstance(items, list):
        return lines
    for index, item in enumerate(items, start=1):
        marker = f"{index}." if ordered else "-"
        if isinstance(item, dict):
            text = clean_line(plain_text(item.get("content") or item.get("inlineContent") or item.get("text"), references))
            lines.append(f"{marker} {text}" if text else marker)
            nested = item.get("items") or item.get("children")
            for nested_line in render_list_items(nested, references, ordered=False):
                lines.append("  " + nested_line)
        else:
            text = clean_line(plain_text(item, references))
            if text:
                lines.append(f"{marker} {text}")
    return lines


def render_table(block: dict[str, Any], references: dict[str, Any]) -> list[str]:
    rows = block.get("rows") or block.get("data") or []
    if not isinstance(rows, list) or not rows:
        return []

    rendered_rows: list[list[str]] = []
    for row in rows:
        cells = row.get("cells") if isinstance(row, dict) else row
        if not isinstance(cells, list):
            continue
        rendered = [clean_line(plain_text(cell.get("content", cell) if isinstance(cell, dict) else cell, references)) for cell in cells]
        if any(rendered):
            rendered_rows.append(rendered)

    if not rendered_rows:
        return []
    width = max(len(row) for row in rendered_rows)
    rendered_rows = [row + [""] * (width - len(row)) for row in rendered_rows]
    lines = ["| " + " | ".join(rendered_rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    for row in rendered_rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def render_block(block: Any, references: dict[str, Any], level_offset: int = 0) -> list[str]:
    if block is None:
        return []
    if isinstance(block, str):
        text = clean_line(block)
        return [text] if text else []
    if isinstance(block, list):
        lines: list[str] = []
        for item in block:
            lines.extend(render_block(item, references, level_offset))
        return lines
    if not isinstance(block, dict):
        text = clean_line(str(block))
        return [text] if text else []

    kind = block.get("type")
    if kind == "heading":
        level = int(block.get("level") or 2) + level_offset
        text = clean_line(str(block.get("text", "")))
        return [f"{'#' * max(1, min(level, 6))} {text}"] if text else []
    if kind == "paragraph":
        text = clean_line(plain_text(block.get("inlineContent"), references))
        return [text] if text else []
    if kind in {"unorderedList", "list"}:
        return render_list_items(block.get("items"), references, ordered=False)
    if kind == "orderedList":
        return render_list_items(block.get("items"), references, ordered=True)
    if kind == "table":
        return render_table(block, references)
    if kind == "links":
        lines = []
        for identifier in block.get("items") or []:
            ref = references.get(identifier, {})
            title = ref.get("title") or identifier
            url = ref.get("url") or identifier
            if isinstance(url, str) and url.startswith("/"):
                url = "https://developer.apple.com" + url
            lines.append(f"- [{title}]({url})")
        return lines
    if kind == "aside":
        style = block.get("style", "aside")
        rendered = render_block(block.get("content"), references, level_offset)
        return [f"> **{style}:**"] + ["> " + line for line in rendered]
    if kind == "tabNavigator":
        lines = []
        for tab in block.get("tabs") or []:
            if not isinstance(tab, dict):
                continue
            title = clean_line(str(tab.get("title") or "Tab"))
            lines.append(f"#### {title}")
            lines.extend(render_block(tab.get("content"), references, level_offset))
        return lines
    if kind == "codeListing":
        code = block.get("code") or block.get("syntax") or ""
        return ["```", str(code).rstrip(), "```"]
    if kind == "row":
        lines = []
        for column in block.get("columns") or []:
            content = column.get("content") if isinstance(column, dict) else column
            lines.extend(render_block(content, references, level_offset))
        return lines
    if kind == "image":
        description = image_description(block, references)
        return [f"Image: {description}"] if description else []

    for key in ("content", "items", "inlineContent", "text"):
        if key in block:
            return render_block(block[key], references, level_offset)
    return []


def render_page(raw_file: Path) -> str:
    page = json.loads(raw_file.read_text(encoding="utf-8"))
    references = page.get("references") if isinstance(page.get("references"), dict) else {}
    metadata = page.get("metadata") if isinstance(page.get("metadata"), dict) else {}
    title = metadata.get("title") or raw_file.stem.replace("-", " ").title()

    lines = [f"# {title}", ""]

    abstract = clean_line(plain_text(page.get("abstract"), references))
    if abstract:
        lines.extend([abstract, ""])

    for section in page.get("primaryContentSections") or []:
        content = section.get("content") if isinstance(section, dict) else section
        for block in content or []:
            rendered = render_block(block, references)
            if rendered:
                lines.extend(rendered)
                lines.append("")

    topic_sections = page.get("topicSections") or []
    if topic_sections:
        lines.extend(["## Topic Sections", ""])
        for section in topic_sections:
            if not isinstance(section, dict):
                continue
            anchor = section.get("anchor")
            if anchor:
                lines.append(f"### {anchor}")
            for identifier in section.get("identifiers") or []:
                ref = references.get(identifier, {})
                title = ref.get("title") or identifier
                url = ref.get("url") or identifier
                if isinstance(url, str) and url.startswith("/"):
                    url = "https://developer.apple.com" + url
                lines.append(f"- [{title}]({url})")
            lines.append("")

    changes = page.get("changeHistory") or page.get("changeHistorySections")
    if changes:
        lines.extend(["## Change History", ""])
        lines.extend(render_block(changes, references))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_all(source_dir: Path) -> int:
    raw_dir = source_dir / "raw"
    rendered_dir = source_dir / "rendered"
    rendered_dir.mkdir(parents=True, exist_ok=True)

    if not raw_dir.exists():
        print(f"missing raw directory: {raw_dir}", file=sys.stderr)
        return 1

    count = 0
    for raw_file in sorted(raw_dir.glob("*.json")):
        output_file = rendered_dir / (raw_file.stem + ".md")
        output_file.write_text(render_page(raw_file), encoding="utf-8")
        count += 1
    print(f"rendered {count} files to {rendered_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", help="Directory containing raw/ from crawl_apple_hig.py")
    args = parser.parse_args()
    return render_all(Path(args.source_dir))


if __name__ == "__main__":
    sys.exit(main())
