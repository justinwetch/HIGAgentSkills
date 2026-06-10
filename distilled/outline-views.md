---
topic: outline-views
tier: 4
platforms: [macos]
category: components/content
triggers:
  - "outline view"
  - "NSOutlineView"
  - "OutlineGroup"
  - "tree view"
  - "expandable list"
related:
  - column-views
  - lists-and-tables
  - split-views
---
# Outline Views

> An outline view presents hierarchical data in a scrollable list of cells organized into columns and rows, with disclosure triangles for parent containers.

**Platforms:** macOS only

Primary column shows the hierarchy (parent containers + nested children). Additional columns display supplementary attributes (sizes, dates, etc.). Finder windows offer an outline view. Outline views often appear in the leading side of a split view.

## Best Practices

- **Use a table — not an outline view — for non-hierarchical data** (see lists-and-tables).
- **Hierarchy in first column only** — additional columns show attributes, not additional hierarchy levels.
- **Descriptive column headings** — nouns or short noun phrases, title-style capitalization, no trailing punctuation. Always include headings in multi-column outline views; for single-column, use a label if context is otherwise unclear.
- **Let people click column headings to sort** — ascending/descending toggle; secondary sort by additional columns is acceptable. Clicking the primary column heading sorts at each hierarchy level (Finder example: top-level folders sorted, then each folder's contents sorted). Clicking an already-sorted heading reverses the sort.
- **Let people resize columns** — data widths vary; adjustable columns are essential.
- **Easy expand/collapse** — clicking a disclosure triangle expands that item. For example, Option-click can expand all sub-items recursively.
- **Retain expansion state** — store and restore which items people expanded so they don't need to navigate back to the same spot.
- **Alternating row colors in multi-column views** — helps people track row values across wide columns.
- **Editable cells if applicable** — single-click to edit (vs. double-click to open, for files). Support reorder, add, remove rows where useful.
- **Centered ellipsis for cell truncation** — preserves beginning and end of text, making content more recognizable than clipping.
- **Search field for long outline views** — toolbar search helps people find values quickly.
