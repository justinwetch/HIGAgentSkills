---
topic: column-views
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "column view"
  - "NSBrowser"
  - "Miller columns"
  - "hierarchical browser"
related:
  - sidebars
  - outline-views
---
# Column Views

> A column view (also called a *browser*) lets people navigate a data hierarchy using a series of vertical columns, each representing one level.

**Platforms:** macOS only *(iPadOS/visionOS: use split-views instead)*

Each column shows a level of the hierarchy. Parent items with children are marked with a triangle. Selecting a parent fills the next column with its children. People navigate until reaching a childless item; can go back up to explore other branches.

## Best Practices

- **Best for deep hierarchies with frequent back-and-forth navigation** (vs. sorting/filtering tasks where lists/tables work better). Classic example: Finder's column view for directory structures.
- **Root of the data hierarchy in the first column** — people can always scroll left to start over.
- **Show info about the selected item when no children remain** — e.g., Finder shows a preview and metadata (created, modified, type, size).
- **Let people resize columns** — especially important when item names exceed the default column width.
