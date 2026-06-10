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
# Context Menus

> A context menu provides quick access to functionality directly related to an item, without cluttering the interface.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

Hidden by default. Revealed by: touch/pinch-and-hold (visionOS, iOS, iPadOS); Control-click or secondary click on trackpad (macOS, iPadOS).

## Best Practices

- **Only the most relevant, frequently-used items** — no advanced or rare commands. Example: Mail message context menu has Reply and Move, not mailbox or filter commands.
- **Small number of items** — long menus are hard to scan and scroll.
- **Apply consistently throughout your app** — inconsistent coverage makes people think the feature is broken or missing.
- **All context menu items must also exist in the main interface** — toolbar, menu bar, or other primary location.
- **Max one level of submenus** — more than one level is too hard to navigate. Give submenu items intuitive titles that hint at their contents.
- **Context menus: hide unavailable items** (don't dim them). Exception on macOS: Cut, Copy, Paste may appear dimmed when inapplicable.
- **Order items starting from the point of interaction** — context menus can open above or below; account for position when ordering to put the most-frequent item where the finger or pointer first lands.
- **No keyboard shortcuts** — context menus are already a shortcut; displaying keyboard shortcuts is redundant.
- **Max ~3 separator groups** in a context menu.
- **Destructive items (iOS, iPadOS, visionOS):** list at bottom, mark as destructive — the system renders them in red.

## Content

- **No title by default.** Add a title only when it clarifies the menu's context/effect — e.g., "3 Messages Selected" to remind people the action affects all selected items.
- **Short, descriptive labels** for each item (see menus#Labels).
- **Use familiar system icons** for Copy, Share, Delete, etc.

## Platform Considerations

### iOS, iPadOS

- **Context menu OR edit menu — not both** for the same item. System can't reliably detect intent when both are offered.
- **iPadOS:** context menus can trigger creation of new objects (Files: long press in empty space → "New Folder").
- **Preview:** iOS/iPadOS context menus can show a preview of the content near the command list. People can tap the preview to open it or drag it elsewhere.
  - Prefer graphical previews that confirm the target — condensed actual content (Notes, Mail).
  - **Match the preview's clipping path to its shape** — rounded corners must not change shape during the open animation.

### macOS

Also called a *contextual menu*.

### visionOS

- **Prefer context menus over panels/inspector windows** for frequently used functionality — keeps the space uncluttered.
- **Avoid menus taller than the window** — system components appear above and below the window (window controls, Share menu); a too-tall menu obscures them.
