---
topic: scroll-views
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "scroll view"
  - "ScrollView"
  - "paging"
  - "scroll indicator"
  - "Look to Scroll"
  - "ScrollInputKind"
  - "PagingScrollTargetBehavior"
  - "ScrollEdgeEffectStyle"
  - "UIScrollEdgeEffect.Style"
  - "NSScrollEdgeEffectStyle"
related:
  - lists-and-tables
  - layout
  - page-controls
  - gestures
  - pointing-devices
---

# Scroll views

A scroll view moves content larger than its bounds vertically or horizontally. Its translucent *scroll indicator* typically appears once scrolling begins; outside tvOS, it shows whether content is near the beginning, middle or end.

## Best practices

- **Support default scrolling gestures and keyboard shortcuts.** Custom scrolling needs elastic scroll indicators.
- **Make scrollable content apparent**, since indicators aren't always visible; for example, show partial content at the edge.
- **Avoid nesting scroll views with the same orientation.** Horizontal in vertical (or vice versa) is alright.
- **Consider page-by-page scrolling if it suits your content** (`PagingScrollTargetBehavior`). A page is typically the view's height or width, optionally minus an overlap unit like a line of text.
- **In some cases, scroll automatically** to bring a hidden selection or insertion point into view (after a search, when typing starts, before acting on a selection); follow the pointer past the edge mid-selection. Scroll only as much as needed to keep context.
- **If you support zoom, set appropriate maximum and minimum scale values.**

## Scroll edge effects

In iOS, iPadOS and macOS, a *scroll edge effect* separates interface elements like toolbars from content scrolling behind them. With custom bars, you might add one manually if needed.

- **Prefer the automatic style** (`ScrollEdgeEffectStyle`, `UIScrollEdgeEffect.Style`, `NSScrollEdgeEffectStyle`) where possible; it separates more opaquely for top toolbars with many controls, text outside Liquid Glass controls, and pinned table headers. If you use soft (variable blur) instead of automatic or hard (opaque blur, defined edge), thoroughly test control legibility in varied contexts.
- **Only use an edge effect when a scroll view is behind floating interface elements.** It isn't decorative; it doesn't block or darken.
- **Apply one per view.** In iPad and Mac split views, each pane can have its own; keep their heights consistent.

## Platform considerations

### iOS, iPadOS

**Consider showing a page control in page-by-page mode**, and then don't show the scroll indicator on the same axis as the page control.

### macOS

Scroll indicators are *scroll bars*. **If necessary, use small or mini scroll bars in a panel** that coexists with other windows when space is tight, sizing all its controls the same.

### tvOS

No scroll indicators; when content exceeds the screen, the system automatically scrolls to keep focused items visible.

### visionOS

The small, fixed-size indicator appears when people start swiping, centered on the window's trailing edge (vertical) or bottom edge (horizontal). Looking at it and dragging makes it a jog bar controlling scrolling speed.

**If necessary, account for indicator size.** It's a little thicker than in iOS; with tight margins, consider increasing them to avoid overlap.

#### Look to Scroll

People scroll by looking near the scroll view's edges (top and bottom for vertical, sides for horizontal), alongside gestures. Add it per scroll view (`ScrollInputKind.look`).

- **Support it for reading or browsing views.**
- **Avoid it for secondary content.** In general, use only standard gestures in views with UI controls or dense information needing quick, precise scrolling.
- **Be consistent.** If one view supports it, make sure similar views do.
- **Define clear scroll areas.** Prefer views that fill the window's width or height; give inset ones clear boundaries.
- **Remove custom scroll effects or animations first**; scroll-position effects like parallax make it behave unexpectedly.

### watchOS

- **Prefer vertical scrolling.**
- **Use tab views for page-by-page scrolling.** In a vertical stack of tab views, the Crown moves through full-screen pages, with a page indicator beside it.
- **Consider limiting each page to one screen height.** The page indicator expands into a scroll indicator for longer pages. Use variable-height pages judiciously, after fixed-height pages when possible.

## Resources

Source: [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views), captured 2026-09-12.
