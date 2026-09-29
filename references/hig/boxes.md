---
topic: boxes
tier: 4
platforms: [ios, ipados, macos, visionos]
category: components/layout
triggers:
  - "box"
  - "NSBox"
  - "group box"
  - "visual grouping container"
related:
  - layout
---
# Boxes

A box creates a visually distinct group of logically related information and components. A visible border or background color separates its contents by default; it can also have a title.

- **Prefer a relatively small box** compared with its containing view: near the containing window or screen’s size, it separates less effectively and can crowd content.
- **Consider padding and alignment** for subgroups. The border is already distinct; nested boxes can feel busy and constrained.

- When useful, add a succinct descriptive title to clarify relationships and help VoiceOver users anticipate contents. Use sentence-style capitalization; omit ending punctuation except a colon in settings panes.

**Platform:** visionOS has no additional considerations. By default, iOS and iPadOS use secondary and tertiary background [colors](https://developer.apple.com/design/human-interface-guidelines/color); macOS displays the title above by default. Boxes aren’t supported in tvOS or watchOS.

**Resources:** [Layout](https://developer.apple.com/design/human-interface-guidelines/layout). [`GroupBox`](https://developer.apple.com/documentation/swiftui/groupbox) is a SwiftUI view with an optional label collecting a logical grouping; [`NSBox`](https://developer.apple.com/documentation/appkit/nsbox) is an AppKit stylized rectangle with an optional title.

Source: [Apple HIG — Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes), captured 2026-09-12.
