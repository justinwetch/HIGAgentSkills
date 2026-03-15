---
topic: page-controls
tier: 3
platforms: [ios, ipados, tvos, visionos]
category: components/controls
triggers:
  - "page control"
  - "UIPageControl"
  - "carousel"
  - "page indicator"
  - "dot indicator"
related:
  - scroll-views
  - collections
---
# Page Controls

> A page control displays a row of indicator dots, each representing a page in a flat ordered list.

**Platforms:** iOS, iPadOS, tvOS, visionOS, watchOS *(not macOS)*

Default: small equidistant dots. Solid dot = current page. Clipped if too many to fit.

## Best Practices

- **For ordered, flat lists only** — not for hierarchical or non-sequential navigation. Use a sidebar or split view for complex navigation.
- **Center horizontally at the bottom of the view/window** — always-findable location.
- **Max ~10 pages** — more than 10 dots are hard to count at a glance. For more, use a grid or other arrangement that supports non-sequential access.

## Customizing Indicators

- System-provided dot by default, but you can supply custom images per-page (e.g., Weather uses `location.fill` for the current location page).
- **Custom images: simple and clear** — no complex shapes, negative space, text, or inner lines. These degrade at very small sizes. Prefer SF Symbols.
- **Customize the default image only when it enhances meaning** — e.g., all pages are bookmarks → use `bookmark.fill`.
- **Max 2 different indicator images** — one for general pages, one for a special page. More types = confusing and messy.
- **Don't color indicator images** — custom colors reduce contrast with the current-page indicator and make it harder to see against varied backgrounds. Let the system color them automatically.

## Platform Considerations

### iOS, iPadOS

Three interaction modes: **tap** (leading/trailing side of current indicator → next/previous page) and **scrub** (touch + drag left/right to move through pages in sequence).

Background styles:
| Style | When | Use |
|---|---|---|
| Automatic | Only during interaction | Use when page control isn't the primary nav element |
| Prominent | Always | Use when page control is the primary nav control |
| Minimal | Never | Use when you only need to show position, no scrubbing |

- **No animation during scrubbing** — people scrub fast; animated transitions cause lag and visual flashes. Animate only tap transitions.
- **Don't support scrubbing with Minimal style** — Minimal provides no scrubbing feedback.

### tvOS

- **Use on collections of full-screen pages only** — page controls are designed for full-screen, content-rich, peer-level pages. Additional nearby controls make it hard to maintain focus.

### visionOS

- Page controls indicate position only — people don't interact with them directly.

### watchOS

- Horizontal pagination: page control at the bottom of the screen.
- Vertical tab views: page control next to the Digital Crown. Transitions between scrolling within a page and scrolling to other pages.
- **Use vertical pagination** — more effective than horizontal or deep hierarchy for Watch.
- **Limit individual page content to one screen height** — encourages clear, glanceable purpose. Variable-height pages are acceptable but place after fixed-height pages.
