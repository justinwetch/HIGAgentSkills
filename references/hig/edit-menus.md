---
topic: edit-menus
tier: 3
platforms: [ios, ipados, macos, visionos]
category: patterns/interaction
triggers:
  - "edit menu"
  - "cut copy paste"
  - "selection menu"
  - "text selection"
  - "callout bar"
  - "UIEditMenuInteraction"
  - "UIResponderStandardEditActions"
related:
  - context-menus
  - menus
  - text-fields
  - undo-and-redo
---

# Edit menus

An edit menu lets people change selected content (text, images, files, objects) and offers commands like Copy, Select, Translate and Look Up. In iOS, iPadOS and visionOS, the system can add actions for detected data types, like *Get directions* for an address. In visionOS it opens as a horizontal bar or a context menu.

## Best practices

- **Prefer the system-provided edit menu** (`UIResponderStandardEditActions`).
- **Reveal it with familiar system interactions**, like touch and hold, pinch and hold or secondary click, not custom ones.
- **Offer commands relevant in context, removing or dimming the rest.** For example, avoid Copy with no selection or Paste with nothing to paste.
- **List custom commands near related system ones** (e.g. formatting after system formatting); avoid too many.
- **When it makes sense, let people select and copy noneditable text**; in general, content text, not control labels.
- **Support undo and redo when possible.**
- **In general, avoid other controls that duplicate edit menu items.**
- **Differentiate deletion commands when necessary**: Delete acts like the Delete key; Cut first copies to the pasteboard.

## Content

**Label custom commands with short verbs or verb phrases.**

## Platform considerations

No additional considerations for visionOS. Not supported in tvOS or watchOS.

### iOS, iPadOS

- **Ensure your edit menu works well in both styles**: compact horizontal via touch (in iOS, touch and hold or double-tap; a trailing chevron expands it into a context menu); vertical context menu via keyboard or pointer.
- **Adjust placement if necessary**, e.g. so it doesn't cover important content. Default: above or below the selection or insertion point, depending on space; you can move it, not reshape it or its pointer.

### macOS

Context menu while editing, plus the menu bar's [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu) (see it for item order).

## Resources

Developer: `UIEditMenuInteraction`, `NSMenu`.

Source: [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus), captured 2026-09-12.
