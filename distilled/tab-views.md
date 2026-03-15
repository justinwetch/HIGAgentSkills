---
topic: tab-views
tier: 4
platforms: [macos, ipados, tvos]
category: components/macos
triggers:
  - "tab view"
  - "NSTabView"
  - "macOS tab view"
  - "tabbed pane"
related:
  - tab-bars
  - sidebars
---
# Tab Views

> A tab view presents multiple mutually exclusive panes of content in the same area, switchable via a tabbed control.

**Platforms:** macOS, watchOS *(not iOS, iPadOS, tvOS, or visionOS)*

- iOS/iPadOS alternative: segmented controls.
- watchOS: tab views are rendered as page-controls.

## Best Practices

- **Closely related content** — visual enclosure implies content similarity between panes.
- **Controls within a pane affect only that pane** — panes are fully self-contained.
- **Descriptive label for each tab** — nouns or short noun phrases. Title-style capitalization. Helps people predict pane content before clicking.
- **Don't use a pop-up button to switch between tabs** — requires two interactions vs. one; also hides choices. (A pop-up button can be a fallback when too many panes make tabs impractical.)
- **Max 6 tabs** — more is overwhelming and creates layout issues. For 6+ panes, consider a pop-up button menu or another layout.

## Anatomy

- Tabbed control at top edge of content area. Can be hidden (for programmatic switching).
- When hidden, content area can be: borderless (solid or transparent) or bezeled/bordered with a line.
- **Inset by a margin of window-body area on all sides** (standard layout). Extending to window edges is possible but unusual.
