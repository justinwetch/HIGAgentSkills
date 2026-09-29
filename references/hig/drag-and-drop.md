---
topic: drag-and-drop
tier: 3
platforms: [ios, ipados, macos, visionos]
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

# Drag and drop

People drag selected content from a *source* to a *destination*. As a general rule, a drop in the same container moves; in a different container, copies. Drops between apps always copy.

Input: visionOS pinch and hold, in any direction including z; iOS, iPadOS touch; pointer or full keyboard access; Mac VoiceOver; Universal Control between Mac and iPad.

## Best practices

- **As much as possible, support drag and drop throughout your app.** System components, like text fields and views, support it automatically.
- **Offer alternatives to drag and drop**, like menu commands. In iOS and iPadOS, you can expose sources and destinations to assistive technologies: `accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors`.
- **Determine whether in-app drags move or copy.** In general, move within a container, copy across containers. Before changing defaults, consider what people expect; prefer the behavior least likely to frustrate or lose data.
- **Support multi-item drags when it makes sense.** All supported platforms drag multiple selections; macOS also, selections from several apps.
- **Prefer letting people undo a drop.** You might confirm an irreversible drop first, or offer a way to reverse its results.
- **Consider offering multiple versions of dragged content, highest fidelity first**, so the destination takes the best it accepts.
- **Consider spring loading**: dragging content over certain controls, like buttons or segmented controls, can activate them: on force click with a Mac Magic Trackpad, on hover on iPad.

## Providing feedback

- **Display a drag image once a selection moves about three points**, until the drop. Translucency works well.
- **If it adds clarity, modify the drag image to predict the result**, like a photo's default size in the destination. You can *flock* multiple items, ungrouping on drop. Avoid constant, radical changes.
- **Show whether a destination accepts the content**, like an insertion point or highlight if it can; nothing or `circle.slash` if not. Show cues only while content is over it; with multiple destinations, identify one at a time.
- **Give visual feedback when a drop is invalid or fails**, like returning to a still-visible source or scaling up and fading out.

## Accepting drops

- **Scroll the destination when necessary**, only while the drag stays inside it. System text views and fields do this by default.
- **When there's a choice, pick the richest version your app accepts.**
- **Extract only the relevant portion if necessary**, like a contact's name and email for a recipient field.
- **With a physical keyboard, check for Option at drop time.** Held at drop, a same-container drag copies; otherwise it moves.
- **Show feedback for slow transfers**: progress, and in collections, lists and tables, possibly a placeholder at the drop location. The system can alert for slow transfers between apps.
- **Show feedback when a drop starts a task**, like printing, including its progress.
- **Style dropped text appropriately.** Keep original attributes if both sides support the same styles; otherwise, use the destination's.
- **Keep dropped content selected in the destination, updating the source as needed.** Deselect content left in the source after a same-container copy or a drag to another container.

## Platform considerations

Not supported in tvOS or watchOS.

### iOS, iPadOS

**Let people perform multiple simultaneous drags.** In iPadOS, let people add items mid-drag, flocking them, and accept multiple simultaneous drops.

### macOS

- **Consider supporting drags into the Finder**; if you do, use a format your app can open later (an event as `.ics`). When necessary, you can output a *clipping*, a temporary container unrelated to the Clipboard.
- **Let people drag a *background selection* (selected content in an inactive window) without activating the window.**
- **When possible, let people drag individual items from an inactive window without affecting its background selection.**
- **Consider a count badge during multi-item drags** (small filled oval), updated if a destination accepts only some.
- **Consider changing the pointer to indicate the drop result**: *copy*, *drag link*, *disappearing item*, *operation not allowed*. See [Pointers](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointers).
- **As much as possible, let people select and drag in one motion**, unless selecting multiple items.

### visionOS

**When possible, launch your app to handle content dropped into empty space.** Associate an `NSUserActivity` with draggable content so your app can open a window or scene for it; the system opens dropped URLs in Safari and Quick Look content in Quick Look.

## Resources

Developer: UIKit and AppKit drag and drop, `FileProvider`.

Source: [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), captured 2026-09-12.
