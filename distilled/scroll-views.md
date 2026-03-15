---
topic: scroll-views
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "scroll view"
  - "ScrollView"
  - "pull to refresh"
  - "paging"
  - "scroll indicator"
related:
  - lists-and-tables
  - layout
---
# Scroll Views

> A scroll view lets people view content larger than the view's boundaries by moving it vertically or horizontally.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

No visual appearance of its own. Shows a translucent scroll indicator after scrolling begins. Indicator shows the relative position of visible content (beginning / middle / end).

## Best Practices

- **Support default scrolling gestures and keyboard shortcuts** — people expect consistent system behavior; custom scrolling must use the same elastic behavior.
- **Make scrollability apparent** — scroll indicators aren't always visible. Show partial content at the edge to signal more is available.
- **No nested scroll views with the same orientation** — creates unpredictable, hard-to-control interfaces. Orthogonal nesting is fine (horizontal inside vertical or vice versa).
- **Page-by-page scrolling** — define a page size (usually current view height/width) and an overlap unit (a line of text, a row of glyphs) to maintain context across page boundaries.
- **Automatic scrolling — only as much as necessary:**
  - App selects content/places insertion point outside the current view → scroll to bring it in.
  - Insertion point is on another page when typing begins → scroll back.
  - Pointer moves past view edge during selection → follow the pointer.
  - People scroll away while content is selected → scroll selection back into view before acting.
- **Zoom: set appropriate min/max scale values** — zooming until one character fills the screen rarely makes sense.

## Scroll Edge Effects (iOS, iPadOS, macOS)

A *scroll edge effect* is a variable blur that transitions between a content area and a Liquid Glass control area (toolbar). System applies it automatically in most cases; add manually for custom controls or layouts.

| Style | Use |
|---|---|
| Soft | Default for most cases (iOS, iPadOS) — subtle transition for toolbars and interactive elements |
| Hard | Primarily macOS — stronger, more opaque boundary for interactive text, backless controls, or pinned table headers |

- **Only use scroll edge effects adjacent to floating interface elements** — not decorative. They exist where controls and content meet.
- **One scroll edge effect per view** — in split views, each pane can have its own but keep heights consistent.

## Platform Considerations

### iOS, iPadOS

- **Show a page control for page-by-page mode** — don't show both the page control and the scroll indicator on the same axis.

### macOS

- Scroll indicator is called a *scroll bar*.
- **Small or mini scroll bars in tight panels** — use consistent size for all controls in the panel.

### tvOS

- Not treated as distinct objects with indicators. System automatically scrolls to keep focused items visible.

### visionOS

- **Fixed-size indicator, always predictable position** — vertical: centered at trailing edge; horizontal: centered at bottom edge.
- Looking at the indicator and starting a drag reveals a **jog bar** with tick marks — people adjust scrolling speed rather than content position.
- **Account for indicator size in tight margins** — slightly thicker than iOS; may overlap content with very tight margins.

### watchOS

- **Prefer vertical scrolling** — Digital Crown naturally navigates vertically.
- **Use tab views for page-by-page scrolling** — tab views become pages in watchOS. Stack vertically; Digital Crown scrolls between them. System shows a page indicator next to the Digital Crown.
- **Limit individual page height to one screen** — clearest/most glanceable design. Variable-height pages okay but use judiciously, placed after fixed-height pages.
