---
topic: edit-menus
tier: 3
platforms: [ios, ipados, macos]
category: patterns/interaction
triggers:
  - "edit menu"
  - "cut copy paste"
  - "selection menu"
  - "text selection"
  - "callout bar"
related:
  - context-menus
  - menus
  - text-fields
  - undo-and-redo
---
# Edit Menus

> An edit menu lets people make changes to selected content and access related commands like Copy, Select, Translate, and Look Up.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS — editing is rare there)*

Applies to text and other selectable content: images, files, contact cards, charts, map locations. System auto-adds actions based on data type (e.g., selecting an address adds "Get Directions").

**How it appears by platform:**
- **iOS:** compact horizontal list, appears on touch-and-hold or double-tap. Tap trailing chevron to expand to context menu.
- **iPadOS:** compact horizontal (touch) or vertical context menu (keyboard/trackpad).
- **macOS:** in context menu during editing tasks + the Edit menu in the menu bar.
- **visionOS:** horizontal bar on pinch-and-hold, or as a context menu.

## Best Practices

- **Use the system-provided edit menu** — people know its contents and behavior. Custom menus duplicating the same commands are redundant and confusing.
- **Use system-defined interactions** — touch-and-hold, secondary click, pinch-and-hold. Don't require a custom interaction for a standard task.
- **Show only contextually relevant commands** — don't show Copy when nothing is selected, or Paste when clipboard is empty.
- **List custom commands near related system commands** — e.g., custom format commands after system-provided format section. Don't overwhelm with too many custom entries.
- **Let people select and copy noneditable text when useful** — captions, statuses, etc. Copy content text; don't copy control labels.
- **Support undo/redo** — edit menus don't confirm before acting; undo is essential for recovery (see undo-and-redo).
- **Avoid duplicate controls** for the same edit functions — use the menu/keyboard shortcuts. Redundant buttons crowd the UI.
- **Differentiate deletion types** — Delete = same as Delete key; Cut = copy to pasteboard then delete.

## Content

Short labels for custom commands — verbs or short verb phrases describing the action.

## Platform Considerations

### iOS, iPadOS

- **Support both compact (touch) and vertical (keyboard/trackpad) menu styles.** Each may appear in a given session.
- **Adjust placement if needed** — default is above or below the insertion point/selection. You can reposition to avoid covering important content. You can't change menu shape or pointer shape.

### macOS

Edit menu item order is defined by the system menu bar. See `the-menu-bar#Edit-menu`.
