---
topic: collections
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/content
triggers:
  - "collection view"
  - "UICollectionView"
  - "grid"
  - "gallery"
  - "flow layout"
related:
  - lists-and-tables
  - image-views
  - layout
---
# Collections

> A collection manages an ordered set of content in a customizable, highly visual layout — ideal for image-based content.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

## Best Practices

- **Prefer the standard row or grid layout** — people expect horizontal row or grid defaults. Avoid custom layouts that draw attention to themselves or confuse people.
- **Use a table instead of a collection for text-heavy content** — lists are easier to scan and read.
- **Easy item selection** — adequate padding around images keeps focus/hover effects visible and prevents content overlap.
- **Custom gestures when needed** — defaults: tap to select, touch-and-hold to edit, swipe to scroll.
- **Animate insert/delete/reorder** — collections support standard animations; custom animations are also supported.

## Platform Considerations

### iOS, iPadOS

- **Dynamic layout changes: use with caution** — avoid changing layout while people are actively interacting with it, unless in direct response to an explicit action.
