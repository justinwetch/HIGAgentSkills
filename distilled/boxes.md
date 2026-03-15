---
topic: boxes
tier: 4
platforms: [ios, ipados, macos]
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

> A box creates a visually distinct group of logically related information and components, using a visible border or background color.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS, watchOS)*

Optional title. iOS/iPadOS use secondary and tertiary background colors. macOS displays the title above the box by default.

## Best Practices

- **Keep boxes relatively small** relative to the containing view — as a box approaches window/screen size, it loses its grouping function and crowds other content.
- **Use padding and alignment for sub-grouping within a box** — avoid nested boxes; they feel busy and constrained. The border itself is a strong visual element.
- **Title (if needed): succinct phrase describing contents** — sentence-style capitalization. No trailing punctuation — except in settings panes, where append a colon. A title also helps VoiceOver users predict content before entering the box.
