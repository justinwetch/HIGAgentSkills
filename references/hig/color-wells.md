---
topic: color-wells
tier: 4
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "color well"
  - "NSColorWell"
  - "UIColorWell"
  - "UIColorPickerViewController"
  - "color picker control"
related:
  - color
---

# Color wells

A color well lets people adjust the color of text, shapes, guides, and other onscreen elements. Tapping or clicking it displays a color picker, either system-provided or custom.

## Best practices

Consider the system-provided color picker for a familiar experience. The built-in picker provides consistency and lets people save colors accessible from any app; the system-defined picker can also help provide a familiar experience across iOS, iPadOS, and macOS.

## Platform considerations

No additional considerations for iOS, iPadOS, or visionOS. Color wells aren’t supported in tvOS or watchOS.

### macOS

Clicking a color well highlights it as active, opens a picker, and updates the well to show the selected color. Color wells support drag and drop: people can drag colors from one well to another or from the picker to a well.

## Resources

Related: [Color](https://developer.apple.com/design/human-interface-guidelines/color)

Developer documentation: [`UIColorWell`](https://developer.apple.com/documentation/uikit/uicolorwell) — UIKit; [`UIColorPickerViewController`](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) — UIKit; [`NSColorWell`](https://developer.apple.com/documentation/appkit/nscolorwell) — AppKit; [Color Programming Topics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html).

Source: [Apple Human Interface Guidelines — Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells) (captured 2026-09-12).
