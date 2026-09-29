---
topic: disclosure-controls
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "disclosure"
  - "expand collapse"
  - "accordion"
  - "DisclosureGroup"
  - "chevron"
  - "NSButton.BezelStyle.disclosure"
  - "NSButton.BezelStyle.pushDisclosure"
related:
  - lists-and-tables
  - outline-views
  - buttons
---

# Disclosure controls

Disclosure controls reveal or hide information/functionality associated with a control or view. **Hide details until relevant:** keep most-used controls at the hierarchy’s top and advanced functionality hidden by default.

## Disclosure triangles

A disclosure triangle reveals or hides information/functionality for a view or item list, such as Keynote’s advanced export options or Finder’s folder hierarchy. Figures show collapsed Finder folders with leading-edge triangles inward; in the expanded example, the opened folder points down while others remain inward.

| State | Triangle | Button | Activation |
|---|---|---|---|
| Hidden | Inward from leading edge | Down | Clicking/tapping shows content; view expands. |
| Visible | Down | Up | Clicking/tapping hides content; view collapses. |

Provide a descriptive label indicating what is disclosed or hidden, such as “Advanced Options.”

## Disclosure buttons

A disclosure button reveals or hides functionality tied to a control. In the macOS Save sheet, it sits beside Save As and expands the dialog with advanced output-location navigation; figures show collapsed/expanded states. Place it near its content and use no more than one per view: multiple buttons add complexity and confusion.

## Platform considerations

macOS has no additional guidance. iOS, iPadOS, and visionOS provide disclosure controls through SwiftUI [`DisclosureGroup`](https://developer.apple.com/documentation/swiftui/disclosuregroup) (a view showing/hiding another content view by disclosure state). Disclosure controls aren’t supported in tvOS or watchOS.

## Resources

Related: [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

AppKit: [`NSButton.BezelStyle.disclosure`](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) (bezel button for a disclosure triangle; Objective-C `NSBezelStyleDisclosure`); [`NSButton.BezelStyle.pushDisclosure`](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) (bezel push button with a disclosure triangle; Objective-C `NSBezelStylePushDisclosure`). Video: [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031).

Source: [Apple Human Interface Guidelines — Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls), captured 2026-09-12.
