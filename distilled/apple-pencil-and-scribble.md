---
topic: apple-pencil-and-scribble
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Apple Pencil"
  - "Scribble"
  - "stylus"
  - "drawing input"
  - "handwriting"
  - "PencilKit"
related:
  - gestures
  - drag-and-drop
  - entering-data
---
# Apple Pencil and Scribble

> Apple Pencil provides pixel-level precision for drawing, handwriting, and markup. Scribble enables handwriting-to-text in any text field.

**Platforms:** iPadOS only

## Best Practices

- **Support intuitive marking-instrument behaviors** — people have real-world pencil/pen habits. Proactively support expected mark-making (e.g., writing in document margins).
- **Allow switching between Pencil and finger freely** — controls must respond to Apple Pencil too, not just touch. A control that ignores Pencil looks broken/dead battery.
- **Mark the instant Apple Pencil touches the screen** — no mode-switching or button taps required. Mirrors pencil-to-paper immediacy.
- **Respond to Pencil attributes** — tilt (altitude), force (pressure), orientation (azimuth), barrel roll. Use to affect stroke thickness, opacity, brush size. Pressure should affect continuous properties intuitively.
- **Visual feedback = direct manipulation** — Pencil must appear to immediately affect the content it touches; never trigger distant or disconnected actions.
- **Left- and right-handed design** — don't obstruct controls with either hand. Let people reposition controls if needed.

## Hover

- **Show a hover preview** to help people predict the mark Pencil will make (e.g., dimensions and color for the current tool).
- **Don't change the preview based on height** — avoid distracting users with constant preview variation as Pencil height changes.
- **Don't trigger actions on hover** — hovering is imprecise; unexpected/destructive actions on hover are a serious UX risk.
- **Preview dynamic values near the middle of the range** — extreme values (max opacity occluding content; min opacity invisible) make poor previews.
- **Hover-triggered contextual menus** — display near where people are marking, not in a remote corner of the screen.
- **Hover previews for Apple Pencil only**, not a pointing device — showing the same feedback for both can be confusing.

## Double Tap

- **Respect the systemwide double-tap setting** — default: toggle current tool ↔ eraser. People can change it to toggle current ↔ previous tool, show/hide color picker, or do nothing.
- **Custom double-tap behavior**: provide a control to let people choose it. Never enable it as the default.
- **Avoid using double tap for content-modifying actions** — accidental double taps happen; especially avoid destructive actions.

## Squeeze (Apple Pencil Pro)

Squeeze performs a discrete, single action. Works when Pencil is not touching the display.

- **Treat squeeze as a single quick gesture** — don't require holding or repeated squeezing; it's tiring.
- **Display squeeze UI (e.g., contextual menu) near Apple Pencil Pro tip** — strengthens the connection between gesture and result.
- **Squeeze actions must be nondestructive and easily undoable** — accidental squeezes happen.

## Barrel Roll (Apple Pencil Pro)

Rotate to change the type of mark being made (e.g., rotate the angle of a highlighter).

- **Only for modifying marking behavior** — not for navigation or displaying controls. Barrel roll is naturally tied to the act of marking.

## Scribble

Writes directly into any text field without tapping first. Works by default in all standard text components (text fields, text views, search fields, editable web content) except password fields.

- **No tap-to-activate for custom text fields** — Scribble must work immediately on contact.
- **Available everywhere text entry is natural** — even in non-field areas (e.g., blank space below a list in Reminders).
- **Don't display autocomplete while writing** — suggestions visually interfere with handwriting in progress.
- **Hide placeholder text immediately when writing begins** — prevents visual overlap with handwriting.
- **Keep the text field stationary while people write** — if the field must move (e.g., search field expanding), delay the move until writing pauses.
- **Prevent autoscrolling while writing or selecting** — scrolling during selection causes the wrong text to be selected.
- **Size fields generously for Pencil input** — increase field size before or when input pauses; never resize during active writing.

## Custom Drawing (PencilKit)

PencilKit provides a low-latency drawing canvas with a standard tool picker and ink palette.

- **Prevent dynamic Dark Mode color adjustment on existing content** — when marking up photos or PDFs, disable dynamic color adjustment so drawing remains visible and sharp.
- **Show undo/redo in compact environments** — the tool picker includes them in regular size, but not compact. Consider adding undo/redo buttons to a toolbar in compact layouts. Also support the 3-finger undo/redo gesture.
