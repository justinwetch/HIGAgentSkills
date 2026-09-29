---
topic: pop-up-buttons
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "pop-up button"
  - "drop-down selection"
  - "NSPopUpButton"
  - "MenuPickerStyle"
  - "changesSelectionAsPrimaryAction"
  - "menu selection button"
related:
  - buttons
  - pickers
  - menus
  - pull-down-buttons
---
# Pop-up buttons

A pop-up button presents a flat list of mutually exclusive options; after selection, the menu closes and the button can show the current selection.

## Best practices

- Use it when those options/states affect content or the surrounding view. Use a [pull-down button](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) for actions, multiple selection, or a submenu.
- Provide a useful default (shown until selection); when possible choose what most people want.
- Make options predictable before opening with an introductory label or effect-describing button label.
- Consider it when space is limited and options needn’t stay visible; it efficiently presents many choices.
- If necessary, offer **Custom** for occasional additional items to avoid clutter; explanatory text below the list can help. Calendar’s iPhone event editor illustrates a **Repeat** menu with preset intervals plus a custom interval.

In an iPadOS popover or modal view, consider it instead of a disclosure indicator for a list item with multiple options: people avoid detail-view navigation. This works best for a fairly small, well-defined set that fits a menu.

There are no additional considerations for iOS, macOS, or visionOS. Pop-up buttons aren’t supported in tvOS or watchOS.

## Resources

[Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus). Developer documentation: [`MenuPickerStyle`](https://developer.apple.com/documentation/swiftui/menupickerstyle) (SwiftUI; presents options as a menu when pressed, or as a submenu when nested in a larger menu); [`changesSelectionAsPrimaryAction`](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) (UIKit Boolean indicating whether a button tracks a selection through a menu or toggle); [`NSPopUpButton`](https://developer.apple.com/documentation/appkit/nspopupbutton) (AppKit control for selecting an item from a list).

Source: [Apple HIG — Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), captured 2026-09-12.
