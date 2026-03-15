---
topic: color-wells
tier: 4
platforms: [ios, ipados, macos]
category: components/controls
triggers:
  - "color well"
  - "NSColorWell"
  - "color picker control"
related:
  - color
---
# Color Wells

> A color well lets people adjust the color of text, shapes, guides, and other onscreen elements.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

Tapping/clicking a color well displays a color picker — either the system-provided one or a custom interface.

## Best Practices

- **Prefer the system-provided color picker** — familiar to users, lets people save reusable color swatches accessible across all apps, and provides a consistent cross-platform experience between iOS, iPadOS, and macOS.

## Platform Considerations

### macOS

- Clicking a color well highlights it (visual confirmation it's active) and opens the color picker.
- After selection, the well updates to show the chosen color.
- **Supports drag and drop** — drag colors between color wells, and from the color picker into a color well.
