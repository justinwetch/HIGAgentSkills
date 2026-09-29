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

A collection manages ordered content in a customizable, highly visual layout and is generally ideal for image-based content.

## Best practices

- Prefer the familiar standard horizontal row or grid; custom layouts can confuse people or draw undue attention.
- Consider a table for text, which is generally simpler and more efficient to view and digest in a scrollable list.
- Make items easy to choose: difficult-to-reach items frustrate people and may lose their interest. Give images enough padding for focus or hover effects to remain visible and to prevent overlap.
- By default, people tap to select, touch and hold to edit, and swipe to scroll. Add gestures for app-specific actions when necessary.
- Consider animations as feedback for insertion, deletion, or reordering; standard and custom animations are supported.

## Platform considerations

There are no additional considerations for macOS, tvOS, or visionOS. Collections aren’t supported in watchOS. On iOS and iPadOS, make dynamic layout changes sensible and easy to track; when possible, avoid changing layout while people view or interact with it unless an explicit action caused the change.

## Resources

- Related: [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).
- [`UICollectionView`](https://developer.apple.com/documentation/uikit/uicollectionview) (UIKit); [`NSCollectionView`](https://developer.apple.com/documentation/appkit/nscollectionview) (AppKit).

Source: [Apple Human Interface Guidelines — Collections](https://developer.apple.com/design/human-interface-guidelines/collections) (captured 2026-09-12).
