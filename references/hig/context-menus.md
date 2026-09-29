---
topic: context-menus
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/presentation
triggers:
  - "context menu"
  - "long press menu"
  - "right-click"
  - "secondary click"
  - "UIContextMenuInteraction"
  - "UIMenuElement.Attributes.destructive"
  - "UIContextMenuInteractionDelegate"
related:
  - menus
  - edit-menus
  - pop-up-buttons
  - pull-down-buttons
---
# Context menus

A context menu exposes item-related functionality without clutter. It is hidden by default: reveal it with touch/pinch-and-hold (visionOS/iOS/iPadOS), Control-click (macOS/iPadOS), or Magic Trackpad secondary-click (macOS/iPadOS).

## Best practices

- Choose likely current-context commands, not advanced/rare actions (Mail’s message menu has Reply/Move, not mailbox management/filtering). Keep menus short and consistent wherever the item appears.
- Make every command available in the main interface too (Mail’s toolbar; macOS menu bar). If needed, use one submenu level with a predictive title.
- Show only relevant items: hide unavailable ones instead of dimming them, except macOS may show unavailable Cut/Copy/Paste. Aim to put frequent items nearest where people begin reading, near the invocation point; depending on whether the menu opens above or below, reversal may be needed.
- Put keyboard shortcuts in main menus. Use separators sparingly, generally no more than **about three groups**. In iOS/iPadOS/visionOS, put destructive commands last and mark them destructive for possible red text via [`UIMenuElement.Attributes.destructive`](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive).

## Content and previews

Menus rarely need a title; each item needs a short, clear label. Add a title only when it clarifies the effect, such as the number of selected Mail messages affected by Mark. Use familiar system icons consistently for Copy, Share, Delete, and other common actions; see [Standard icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons).

In iOS/iPadOS, a menu can show a nearby preview. In some cases, people can tap the preview to open it or drag it elsewhere. Prefer a graphical preview that confirms the target (Notes/Mail can show a condensed list item). Match its clipping path, including rounded corners, so contours don’t change as the system animates it from the content while dimming the background. [`UIContextMenuInteractionDelegate`](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate) customizes it.

## Platform considerations

**iOS/iPadOS:** Give an item either a context or edit menu, never both, so people/system can distinguish intent. On iPadOS, long press or secondary click can reveal a menu in an empty area to create an object (Files uses a new folder).

**macOS:** A context menu is also called a *contextual* menu. Use [`NSMenu.popUpContextMenu(_:with:for:)`](<https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)>) to display one over a view for an event.

**visionOS:** Consider a context menu instead of a panel/inspector for frequent functionality. Generally keep its height within the window: system controls above/below (including window management and Share) can otherwise be obscured. Specialist apps may justify larger sophisticated menus; simple apps benefit from short, scannable ones.

**tvOS:** No additional considerations. **watchOS:** Not supported.

## Resources

[`contextMenu(menuItems:)`](<https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)>) (source metadata: deprecated) adds a menu to a view; [`UIContextMenuInteraction`](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) displays relevant actions. See [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus), [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), and [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons). Source: [Apple HIG — Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus), captured 2026-09-12.
