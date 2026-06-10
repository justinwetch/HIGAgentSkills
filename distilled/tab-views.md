---
topic: tab-views
tier: 4
platforms: [macos, watchos]
category: components/macos
triggers:
  - "tab view"
  - "TabView"
  - "NSTabView"
  - "macOS tab view"
  - "tabbed pane"
  - "watchOS page control"
related:
  - tab-bars
  - segmented-controls
---
# Tab Views

> A tab view presents multiple mutually exclusive panes of closely related content in the same area.

**Platforms:** macOS, watchOS *(not iOS, iPadOS, tvOS, or visionOS)*

- iOS/iPadOS alternative: segmented controls for similar local mutually exclusive panes.
- watchOS: `TabView` renders as page-by-page content with a page indicator.

## Best Practices

- **Closely related content** - visual enclosure implies content similarity between panes.
- **Controls within a pane affect only that pane** - panes are fully self-contained.
- **Descriptive label for each tab** - nouns or short noun phrases. Title-style capitalization.
- **Don't use a pop-up button to switch between tabs** - it takes more interactions and hides choices.
- **Max 6 tabs** - for more panes, consider a pop-up menu or another layout.

## Anatomy

- Tabbed control at top edge of content area. Can be hidden for programmatic switching.
- When hidden, content area can be borderless or bezeled/bordered.
- Standard macOS layout insets the tab view from the window-body area on all sides.
