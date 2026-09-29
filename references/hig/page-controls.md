---
topic: page-controls
tier: 3
platforms: [ios, ipados, tvos, visionos, watchos]
category: components/controls
triggers:
  - "page control"
  - "UIPageControl"
  - "carousel"
  - "page indicator"
  - "dot indicator"
  - "UIPageControl.InteractionState"
  - "backgroundStyle"
  - "preferredIndicatorImage"
  - "setIndicatorImage(_:forPage:)"
  - "PageTabViewStyle"
related:
  - scroll-views
  - collections
---

# Page controls

A page control shows one indicator per page in a flat list: by default equidistant dots, solid for the current page, clipped if they don't fit. It suits any page count, including lists people create.

## Best practices

- **Use for movement through an ordered list of pages**, not hierarchical or nonsequential ones. For complex navigation, consider a sidebar or split view.
- **Center it horizontally near the bottom of the view or window.**
- **Don't display too many**: more than about 10 dots are hard to count at a glance. For more than 10 peer pages, consider an any-order arrangement, such as a grid.

## Customizing indicators

If it enhances your app or game, you can replace the default dot for all indicators (`preferredIndicatorImage`) and for one page (`setIndicatorImage(_:forPage:)`), like Weather's current-location `location.fill`.

- **Make sure custom images are simple and clear.** Avoid complex shapes; don't include negative space, text or inner lines. Consider simple SF Symbols or your own icons.
- **Customize the default image only when it enhances the control's overall meaning** (`bookmark.fill` if every page has bookmarks).
- **Avoid more than two different indicator images.** You can give one special page a unique image.
- **Avoid coloring indicators**; let the system color them.

## Platform considerations

Not supported in macOS.

### iOS, iPadOS

The highlighted current indicator shows relative position; when indicators don't fit, the control can shrink those at both edges to signal more pages.

Tapping either side of the current indicator (discrete) shows the next or previous page, and in iPadOS the pointer can target any indicator; scrubbing, a sideways touch-and-drag (continuous), opens pages in sequence and past either edge reaches the first or last (`UIPageControl.InteractionState`).

- **Avoid animating page transitions during scrubbing**; animate only for tapping.

`backgroundStyle` sets a translucent rounded-rectangle background for indicator contrast; for scrubbing, use automatic or prominent:

|Style|Background|Use when|
|---|---|---|
|Automatic|During interaction|Control isn't primary navigation|
|Prominent|Always|Only as the screen's primary navigation|
|Minimal|Never|Just showing position; no scrubbing feedback, so avoid supporting the scrubber|

### tvOS

**Use page controls on collections of full-screen, content-rich peer pages.**

### visionOS

Page controls show pages and the current page, but people don't interact with them.

### watchOS

Page controls can appear at the bottom for horizontal pagination or beside the Digital Crown for a vertical tab view, where the indicator shows position within the current page and the set. The control transitions between scrolling within a page and between pages.

- **Use vertical pagination for distinct, purposeful pages** scrolled with the Digital Crown; in watchOS it's more effective than horizontal pagination or deep hierarchy.
- **Consider limiting each page to one screen height.** Use variable-height pages judiciously and, if possible, only after fixed-height pages.

## Resources

Developer: `PageTabViewStyle`.

Source: [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls), captured 2026-09-12.
