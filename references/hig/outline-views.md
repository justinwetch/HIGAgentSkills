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

# Outline views

An outline view presents hierarchical data in a scrolling list of cells in columns and rows. It works well for text-based content and often sits in a split view's leading side. Parent containers have disclosure triangles that reveal their children.

## Best practices

- **Use a table for nonhierarchical data.**
- **Expose hierarchy in the first column only.** Other columns can show its attributes, like size or modification date.
- **Use descriptive column headings**: nouns or short noun phrases, title-style capitalization, no punctuation (in particular, avoid a trailing colon). Always provide them in multi-column views; single-column views without one need a label or other context.
- **Consider click-to-sort column headings** (ascending or descending; you can add secondary-column sorting behind the scenes if necessary). Sorting by the primary column sorts each hierarchy level; clicking an already-sorted heading reverses the sort.
- **Let people resize columns.**
- **Make expanding and collapsing nested containers easy.** In Finder, clicking a disclosure triangle expands only that folder; Option-clicking expands all its subfolders.
- **Retain expansion state** for next time.
- **Consider alternating row colors in multi-column views**, especially wide ones.
- **Let people edit data if it makes sense in your app.** In editable cells, people expect a single click to edit; a double click can differ (e.g., open a file). You can also let people reorder, add and remove rows if useful.
- **Consider a centered ellipsis instead of clipping truncated cell text.**
- **Consider a search field** for lengthy outline views. Windows where one is the primary feature often put it in the toolbar.

## Platform considerations

Not supported in iOS, iPadOS, tvOS, visionOS or watchOS.

## Resources

Developer: `OutlineGroup`, `NSOutlineView`.

Source: [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views), captured 2026-09-12.
