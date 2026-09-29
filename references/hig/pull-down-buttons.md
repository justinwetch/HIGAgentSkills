---
topic: pull-down-buttons
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "pull-down button"
  - "dropdown button"
  - "UIButton menu"
  - "button menu"
  - "MenuPickerStyle"
  - "showsMenuAsPrimaryAction"
  - "pullsDown"
related:
  - buttons
  - menus
  - pop-up-buttons
---

# Pull-down buttons

A pull-down button displays a menu of items or actions directly related to its purpose. Choosing one closes the menu and performs it.

## Best practices

- **Use it to clarify the button's target or customize its behavior**, such as what Add adds or where Back goes.
- For mutually exclusive choices that aren't commands, use a pop-up button.
- **Avoid putting all of a view's actions in one pull-down button**; keep primary actions easily discoverable.
- **Balance menu length:** three or more items can help make opening it worthwhile (for one or two, consider buttons for actions and toggles or switches for selections); too many can slow people down.
- **Display a succinct menu title only if it adds meaning.**
- **Identify potentially destructive items**; they appear in red, and the system asks people to confirm or cancel in an action sheet (iOS) or popover (iPadOS).
- **Include an icon or image after an item's label when it provides value.** SF Symbols can help provide a familiar look, and they stay aligned with text at every scale.

## Platform considerations

No additional considerations for macOS or visionOS. Not supported in tvOS or watchOS.

### iOS, iPadOS

- A gesture on a button, like touch and hold (Safari's Tabs button), can also reveal the menu.
- **Consider a More pull-down button for items that don't need prominent positions.** It can save space but can hinder discoverability, since the ellipsis doesn't necessarily predict its contents; weigh the two.

## Resources

Developer: `MenuPickerStyle` (SwiftUI), `showsMenuAsPrimaryAction` (UIKit), `pullsDown` (AppKit).

Source: [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), captured 2026-09-12.
