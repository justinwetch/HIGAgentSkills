---
topic: undo-and-redo
tier: 3
platforms: [ios, ipados, macos, visionos]
category: patterns/interaction
triggers:
  - "undo"
  - "redo"
  - "UndoManager"
  - "shake to undo"
  - "Cmd-Z"
  - "three-finger swipe"
  - "edit history"
related:
  - edit-menus
  - gestures
  - file-management
  - feedback
  - pointing-devices
  - keyboards
  - the-menu-bar
---

# Undo and redo

Undo/redo reverses actions and supports safe experimentation. Since people may repeat undo without recalling its target, make results predictable and visible.

## Best practices

- Describe results where possible: iPhone’s shake alert can offer undo/cancel; menu labels can say *Undo Typing* or *Redo Bold*.
- Highlight results even when content is offscreen (scroll to a restored paragraph), or people may repeat the action.
- People generally expect undo/redo back to a logical boundary (opening/saving); avoid unnecessary limits.
- Consider reverting a related batch (incremental changes to one property) or all changes since opening/saving.
- Add buttons only when needed. Prefer system entry points (macOS Edit menu, Mac/iPad shortcuts, iPhone shake); if needed, use standard symbols in a toolbar.

There are no additional visionOS considerations; undo/redo is not supported in tvOS or watchOS.

### iOS and iPadOS

Don’t redefine the standard three-finger swipe or iPhone shake. The alert title supplies “Undo ” or “Redo ” (including trailing space); append one or two precise words, such as “Name” or “Address Change.”

### macOS

Put commands at the top of Edit; support Command–Z (undo) and Shift–Command–Z (redo).

## Resources

- Related: [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices), [Standard keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts), [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu)
- API: [UndoManager / NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager), a general-purpose operation recorder enabling undo and redo (Swift / Objective-C names).
- Video: [Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802)

Source: [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo) (captured 2026-09-12).
