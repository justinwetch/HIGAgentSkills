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
# Pull-Down Buttons

> A pull-down button displays a menu of items or actions directly related to the button's purpose.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

People choose an item, the menu closes, and the app performs the action. Contrast with **pop-up buttons** (mutually exclusive state selection) — use pull-down for commands/actions, pop-up for selections.

## Best Practices

- **Commands or items directly related to the button's action** — the menu clarifies the target or customizes behavior. Examples:
  - Add button → specify what to add.
  - Sort button → select the sort attribute.
  - Back button → jump to a specific history location instead of just the previous one.
- **Don't hide all of a view's primary actions in one pull-down button** — primary actions must be easily discoverable; don't bury them.
- **Prefer at least three items** — listing a minimum of three items can make the open-and-pick interaction feel worthwhile. For 1–2 items, consider regular buttons (for actions) or toggles/switches (for selections).
- **Don't list too many items** — overly long menus make item-finding slow. Balance minimum (3) against scan time.
- **Title is optional** — only include if it adds meaning beyond the button label and menu item text.
- **Destructive items:** highlight with red text + show an action sheet (iOS) or popover (iPadOS) for confirmation before completing. This helps prevent accidental data loss.
- **Icons/symbols after labels** — use only when they clarify the item. Use SF Symbols for proper scaling alignment.

## Platform Considerations

### iOS, iPadOS

- Can also trigger the menu via a **gesture on the button** (e.g., Safari's Tabs button: touch-and-hold shows tab actions).
- **More (ellipsis) pull-down button** — presents lower-priority items in space-constrained UIs. The `…` icon doesn't hint at contents, so weigh convenience vs. discoverability carefully. Best when people already understand the context.
