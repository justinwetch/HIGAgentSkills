---
topic: focus-and-selection
tier: 3
platforms: [ipados, macos, tvos, visionos]
category: patterns/interaction
triggers:
  - "focus"
  - "focus ring"
  - "selection"
  - "keyboard navigation"
  - "directional focus"
  - "UIFocusHaloEffect"
  - "focusGroupIdentifier"
  - "UIFocusGroupPriority"
related:
  - remotes
  - keyboards
  - designing-for-tvos
---

# Focus and selection

Focus shows which component people target with inputs like a remote, game controller or keyboard. iPadOS and macOS draw a ring or highlight; tvOS generally uses parallax. Focusing often also selects, except where that might cause a distracting context shift; in tvOS, selecting opens or activates, so it takes a separate gesture.

## Best practices

- **Rely on system focus effects.** Consider custom ones only if absolutely necessary.
- **Avoid changing focus without people's interaction.** Exception: if the focused item disappears during discrete, directional input (keyboard, remote, game controller), moving focus to an item one step away keeps it findable; with other input, it's generally best to just hide the indicator.
- **Match the platform's focus reach.** In iPadOS and macOS, full keyboard access reaches controls, so you only need focus for content like list items, text fields and search fields, not buttons, sliders or toggles. In tvOS, make sure people can focus every element.
- **Indicate focus as the platform does**, like iPadOS and macOS lists: white text on an accent-color highlight when focused, standard text on gray when not (`UICollectionView`, `NSTableView`).
- **In general, ring text and search fields; highlight items in lists and collections.** You can ring an item that fills a cell, like a photo, but whole-row highlights are usually easier to view.

## Platform considerations

Not supported in iOS or watchOS.

### iPadOS

iPadOS 15 and later supports keyboard focus for text fields, text views, sidebars, collection views and custom views. Same underlying system as tvOS, but unlike tvOS *directional focus*, where one interaction reaches every component, iPadOS uses *focus groups* (areas like a sidebar, grid or list): Tab moves among groups; arrow keys move directionally only within one.

Components can show focus with a **halo** (focus ring), a customizable outline for custom views and fully opaque cell content like images, or the **highlighted appearance** (accent-colored text and icon), which isn't a focus effect and appears automatically when people select a collection view cell with content configurations (`UICollectionViewCell`).

- **Customize the halo when necessary** (`UIFocusHaloEffect`). Defaults to the item's shape; can match contours like rounded corners or Bezier paths, and can be repositioned if something occludes or clips it.
- **Ensure focus moves through custom views sensibly.** Tab follows reading order (leading to trailing, top to bottom). For example, to traverse a vertical stack before moving trailing, make its container one focus group (`focusGroupIdentifier`).
- **Prioritize items by importance within a group.** A focused group automatically focuses its *primary item*; you can raise an item's priority to make it primary (`UIFocusGroupPriority`).

### tvOS

- **In full-screen experiences, let gestures act on content, not move focus.** Full-screen items show no focus.
- **Avoid displaying a pointer.** Use focus for menus and interface elements; free-form movement might suit gameplay. If you require one, make sure it's highly visible and integrated.
- **Design for up to five visually distinct focus states.** Focusing often enlarges an item, so supply focused-size assets and make sure it doesn't crowd its surroundings.

|State|Meaning|Appearance|
|---|---|---|
|Unfocused|Less prominent|Small shadow; translucent; high-contrast text|
|Focused|Elevated, illuminated, animated|Larger; deeper shadow|
|Highlighted|Being chosen; instant feedback, like briefly inverting colors and animating, then showing Selected|Slightly deeper shadow|
|Selected|Chosen or activated, like a filled favorite heart|Small shadow|
|Unavailable|Can't be focused or chosen; looks inactive|No shadow; translucent; low-contrast text|

Highlighted, Selected and Unavailable are the unfocused size. Focused, Highlighted and Selected are opaque white with black text.

### visionOS

Supports the iPadOS and tvOS focus system through connected input devices like a keyboard or game controller. Looking at an object triggers the *hover effect* ([Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)), which is unrelated to focus.

## Resources

Source: [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection), captured 2026-09-12.
