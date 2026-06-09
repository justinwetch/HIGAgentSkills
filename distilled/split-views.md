---
topic: split-views
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/navigation
triggers:
  - "split view"
  - "UISplitViewController"
  - "NavigationSplitView"
  - "master detail"
related:
  - sidebars
  - tab-bars
  - layout
---
# Split Views

> A split view shows multiple adjacent panes of content simultaneously, supporting navigation between hierarchy levels.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Typical use: sidebar (primary pane) → content list (secondary) → detail (tertiary). Also used for supplementary functionality panels (e.g., Keynote's slide navigator, presenter notes, inspector).

## Best Practices

- **Persistently highlight the current selection** in each pane that leads to a detail view — clarifies relationships and keeps people oriented.
- **Consider drag and drop between panes** — convenient for moving content across hierarchy levels.

## Platform Considerations

### iOS

- **Prefer regular — not compact — environments.** Compact (iPhone portrait) makes multiple panes hard to display without wrapping or truncation.

### iPadOS

- Supports 2-pane (Mail-style) or 3-pane (Keynote-style) vertical split.
- **Account for narrow, compact, and intermediate window widths** — windows are fluidly resizable; ensure logical pane navigation at all widths.

### macOS

- Panes can be arranged vertically, horizontally, or both. Includes resizable dividers.
- **Reasonable min/max pane sizes** — if a pane gets too small, the divider can appear to disappear.
- **Consider allowing pane hiding** when it helps focus (e.g., Keynote hides navigator and presenter notes for editing focus). Provide multiple ways to reveal hidden panes (toolbar button, menu command, keyboard shortcut).
- **Thin divider (1pt) preferred** — maximum content space while remaining easy to use. Thicker dividers only when thin ones would be hard to distinguish (e.g., both sides have strong linear elements).

### tvOS

- Good for content filtering: primary pane = filter categories, secondary pane = filtered results.
- **Balanced layout** — default: ⅓ primary / ⅔ secondary. Half-and-half also available.
- **Consider a single title above the split view** — people understand split views; no per-pane titles needed. Align based on secondary pane content type: center title if secondary shows a collection; leading title if secondary shows a single important item.

### visionOS

- **Prefer split view over opening a new window** for supplementary information — keeps context intact and avoids multi-window navigation confusion. Use a sheet for simple tasks requiring brief information input.

### watchOS

- Shows either list or detail as full-screen.
- **Auto-display the most relevant detail view** on launch (location, time, or recent actions).
- **Multiple detail pages: use a vertical tab view** — people use Digital Crown to scroll between pages. System shows a page indicator next to the Digital Crown.
