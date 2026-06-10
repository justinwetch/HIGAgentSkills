---
topic: lists-and-tables
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "list"
  - "table"
  - "UITableView"
  - "row"
  - "grouped list"
related:
  - outline-views
  - collections
  - layout
---
# Lists and Tables

> Lists and tables present data in one or more columns of rows, supporting navigation, selection, sorting, and editing.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Prefer lists/tables for text** — row format makes text easy to scan. For widely varying item sizes or many images, use a collection.
- **Let people edit when it makes sense** — including reordering even without full add/remove. On iOS/iPadOS, people must enter edit mode to select items.
- **Provide appropriate selection feedback:**
  - Navigation table (drill-down hierarchy) → persistently highlight selected row to show the active path.
  - Options table (choose a setting) → briefly highlight, then show a checkmark or other indicator.

## Content

- **Succinct item text** — minimizes truncation and wrapping; easier to scan. If items are large, consider title-only view with a detail view.
- **Preserve readability when truncated** — centered ellipsis (…) preserves beginning and end of text, making items more distinguishable than clipping.
- **Descriptive column headings in multi-column tables** — nouns or noun phrases, title-style capitalization, no trailing punctuation.

## Style

- Match style to data and platform:
  - iOS/iPadOS **grouped style** — headers, footers, extra spacing to separate groups.
  - watchOS **elliptical style** — items appear to roll off a rounded surface.
  - macOS **bordered style** — alternating row backgrounds for legibility in large tables.
- Choose a row style that fits the information (lead image + label, etc.).

## Platform Considerations

### iOS, iPadOS, visionOS

- **Info button** (detail disclosure) — reveals more info about the row; does not navigate into subviews. Use a disclosure indicator for drill-down navigation.
- **Avoid an index alongside disclosure indicators** — both appear on the trailing side; the index makes it hard to tap indicators without triggering the index.

### macOS

- **Sortable by clicking column headings** — click an already-sorted heading to reverse the sort.
- **Resizable columns** — data widths vary; let people adjust.
- **Alternating row colors in multicolumn tables** — helps track values across wide rows.
- **Use outline views for hierarchical data** — not a flat table view. Outline views add disclosure triangles.

### tvOS

- **Images near table rows: verify focus behavior.** Focused rows slightly increase in size and may get rounded corners — account for this in image preparation; don't add your own corner masks.

### watchOS

- **Limit rows when possible** — short lists are easier to scan. For expected long lists, provide a way to reveal more rather than truncating.
- **Constrain detail view length for vertical page-based navigation** — if detail views scroll, people can't swipe vertically between rows' detail views.
