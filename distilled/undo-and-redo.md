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
# Undo and Redo

> Undo and redo lets people safely reverse actions and explore interfaces without fear of making permanent mistakes.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

People expect to undo repeatedly. They may not remember exactly which action an undo will target, so clarity about the outcome is essential.

## Best Practices

- **Predict the result** — describe what will be undone before it happens. On iPhone shake-to-undo, show the result in the alert text. In menu items, use descriptive labels: "Undo Typing", "Redo Bold".
- **Show the result after undo/redo** — if the affected content is no longer on screen, scroll to reveal the restored content. Invisible results cause people to assume the action had no effect and repeat it.
- **Avoid unnecessary undo limits** — people expect to undo back to when they opened or last saved a document when feasible.
- **Offer batch undo when useful** — let people undo groups of related discrete changes (e.g., incremental slider adjustments) at once. Consider "Revert to Last Save" as a convenience option.
- **Only add dedicated undo/redo buttons when necessary** — people expect system-standard methods (Edit menu, keyboard shortcuts, iPhone shake, three-finger swipe). If you do add buttons, use standard system-provided symbols and place them in a toolbar.

## Platform Considerations

### iOS, iPadOS

- **Don't override standard undo/redo gestures** — three-finger swipe and shake-to-undo are standard. Redefining them causes confusion and unpredictability.
- **Describe the undo/redo operation precisely** — the system prepends "Undo " or "Redo " automatically. Supply a short descriptor word or phrase for the alert title: "Undo Name", "Redo Address Change".

### macOS

- **Place undo/redo in the Edit menu at the top** — this is where Mac users always look for them.
- **Support expected shortcuts** — Command-Z for undo and Shift-Command-Z for redo on macOS.
