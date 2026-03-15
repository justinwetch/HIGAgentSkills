---
topic: drag-and-drop
tier: 3
platforms: [ios, ipados, macos]
category: patterns/interaction
triggers:
  - "drag"
  - "drop"
  - "drag and drop"
  - "UIDragInteraction"
  - "reorder"
related:
  - gestures
  - file-management
  - edit-menus
---
# Drag and Drop

> People move or copy selected content by dragging it from a source to a destination — within a container, between containers, or between apps.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

**Move vs. copy rules:**
- Same container → move
- Different containers → copy
- Between apps → always copy

Platform interactions: visionOS — pinch and hold, drag in any direction including z-axis. iOS/iPadOS — touch gestures, pointing device, full keyboard access. macOS — pointing device, full keyboard access, VoiceOver. Universal Control: drag between Mac and iPad.

## Best Practices

- **Support drag and drop broadly** — people expect it everywhere. System components (text fields, text views) include built-in support.
- **Always provide alternative actions** — menu commands, cut/copy/paste — for when drag-and-drop is inconvenient or impossible. On iOS/iPadOS, use accessibility APIs (`accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors`).
- **Support multi-item drag** — let people select and drag a group instead of dragging one at a time. On iPadOS, people can add items to an in-progress drag without stopping. macOS allows dragging selections from multiple apps.
- **Support undo** — people drop content in wrong places accidentally. If undo isn't possible, confirm before completing irreversible drops (e.g., Finder warns before drop into write-only folder). Provide reversal mechanisms where undo is unavailable (e.g., Photos lets people cancel photo sharing after drop).
- **Offer multiple fidelity versions of dragged content**, ordered highest to lowest (e.g., PDF → lossless PNG → lossy JPEG). The destination picks the richest it can accept.
- **Support spring loading** — let people activate controls (buttons, segmented controls) by hovering over them while holding dragged content. On Mac with Magic Trackpad: force-click to activate. On iPad: hover while holding.

## Providing Feedback

- **Show a translucent drag image immediately** (~3pt of movement). Translucency lets people see destinations underneath. Keep it visible until drop.
- **Modify drag image to preview results** if it adds clarity (e.g., expand a photo to its default in-document size). Use drag flocking to visually group multi-item drags. Don't constantly and radically change the image.
- **Indicate destination acceptance** — show insertion point or highlight when content can be accepted; show nothing or `circle.slash` symbol when it can't. Remove visual feedback when the item moves away from a valid destination.
- **Animate failed/invalid drops** — snap back to source if visible, or scale-up-and-fade-out ("evaporate") to signal failure.

## Accepting Drops

- **Auto-scroll destination containers** when dragging within them; stop auto-scrolling when dragging leaves the container.
- **Accept the richest version** of dropped content your app supports.
- **Extract only relevant parts** of dropped content (e.g., Mail shows name + email from a contact drop, not full address).
- **Check for Option key at drop time** (macOS) — Option held during same-container drop forces a copy instead of a move. If Option is released before drop, it's a move.
- **Show progress for slow transfers** — progress indicator; placeholder at drop location in collections/lists/tables.
- **Show task initiation** when dropped content triggers an action (e.g., print) — confirm task start and report progress.
- **Preserve text styling** when source and destination support the same styles. Otherwise apply destination style.
- **Maintain selection state after drop** — dropped content stays selected in the destination. For same-container moves: deselect at source. For same-container copies: deselect the original. For cross-container drags: deselect in source.

## Platform Considerations

### iOS, iPadOS

- Support simultaneous multi-finger drag sessions on iPadOS — people can add items to an in-progress drag with additional fingers. Support flocking for visual grouping and accepting multiple simultaneous drops.

### macOS

- **Support drag to Finder** — output content in a format your app can reopen later. Calendar exports as `.ics`; text apps output text clippings. (Clippings ≠ Clipboard.)
- **Let people drag from an inactive window** (background selection) without activating the window.
- **Let people drag individual unselected items from inactive windows** without deselecting the existing background selection.
- **Show a count badge** on multi-item drags — filled oval with item count. Update count if destination can only accept a subset.
- **Change pointer appearance** to show intent: copy pointer, drag-link, disappearing-item, operation-not-allowed.
- **One-motion select and drag** — don't require a pause between selection and drag start for single items.

### visionOS

- When people drop content into empty space, launch your app to handle it (associate a user activity with draggable content — your app opens a window/scene for the content).
