---
topic: printing
tier: 4
platforms: [ios, ipados, macos, visionos]
category: patterns/system
triggers:
  - "print"
  - "UIPrintInteractionController"
  - "NSDocument"
  - "print panel"
  - "page setup"
related:
  - the-menu-bar
  - file-management
---

# Printing

When it makes sense, use system printing on iOS/iPadOS/macOS/visionOS; add printer/document options as needed.

## Best practices

- Make Print discoverable: macOS File menu; iOS/iPadOS toolbar button opening an [action sheet](https://developer.apple.com/design/human-interface-guidelines/action-sheets); optionally an addable macOS toolbar button.
- Show it only when possible. If nothing is printable or no printer exists, dim macOS File-menu Print, remove iOS/iPadOS Action-sheet Print, or dim/hide a custom button.
- In the system view, offer relevant page range, copies, and two-sided printing when supported.

No iOS/iPadOS/visionOS additions; printing isn’t supported in tvOS/watchOS.

### macOS

- If your macOS app has app-specific print options absent from the system, consider a uniquely named custom category (such as the app name); system categories include Layout, Paper Handling, and Media & Quality, while Keynote includes presenter notes, slide backgrounds, and skipped slides.
- For rarely changed, document-specific page size/orientation/scaling, consider a page setup dialog; don’t duplicate system options (orientation, reverse order).
- Clarify dependencies: if double-sided printing is available, printing on transparencies becomes unavailable.
- Separate frequent and advanced features; consider a disclosure control to hide advanced options until needed and label them *Advanced Options*.
- Consider a thumbnail preview (such as tone control) and storing modified settings with the document; at minimum retain them until it closes for reprinting.

## Resources

- Related: [File management](https://developer.apple.com/design/human-interface-guidelines/file-management), [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- APIs: [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) (iOS printing UI), [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) (macOS document interface).

Source: [Printing](https://developer.apple.com/design/human-interface-guidelines/printing) (captured 2026-09-12).
