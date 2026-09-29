---
topic: apple-pencil-and-scribble
tier: 3
platforms: [ipados]
category: technologies
triggers:
  - "Apple Pencil"
  - "Scribble"
  - "stylus"
  - "drawing input"
  - "handwriting"
  - "PencilKit"
  - "PaperKit"
related:
  - gestures
  - entering-data
---

# Apple Pencil and Scribble

Apple Pencil supports pixel-level drawing, handwriting, marking up, pointing, and UI interaction. Scribble uses fast, private, on-device handwriting recognition to enter text in text fields. See [Apple Pencil](https://www.apple.com/apple-pencil/) for features and compatibility.

## Best practices

- **Support marking behaviors people expect from real tools.** Consider natural actions such as writing in document margins.
- **Let people choose when to use Pencil or a finger.** If Pencil marks content, controls should also respond to Pencil so people don’t have to switch inputs or mistake an unresponsive control for a malfunction. Scribble supports Apple Pencil input only.
- **Mark immediately on contact.** Don’t require a button or special mode before the first mark.
- **Use Pencil input to express the mark.** Depending on the model, Apple Pencil may sense tilt (altitude), pressure, orientation (azimuth), and Apple Pencil Pro barrel roll. Map these to intuitive stroke properties such as thickness, intensity, opacity, or brush size; continuous properties work well for pressure.
- **Keep feedback directly connected.** Pencil should immediately appear to manipulate the content it touches, rather than initiating a disconnected action elsewhere.
- **Support both hands.** Don’t put controls where either hand can obscure them; let people reposition controls when needed.

## Hover

- Use hover to preview what contact will do, such as the current tool’s mark size and color. Avoid continually changing the preview as Pencil height changes; frequent variation distracts and may not clarify the result.
- Don’t use hover to initiate actions. The distance is imprecise, so accidental activation—especially destructive activation—is possible.
- Prefer a preview value near the middle of a dynamic range such as opacity or flow. A maximum-pressure preview can occlude the mark area; a minimum-pressure preview may be hard to see or invisible.
- Consider a contextual tool menu near the marking location in response to hover plus a gesture such as [squeeze](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze) or a keyboard modifier.
- Prefer hover previews for Apple Pencil over a pointing device when the same cue would be confusing. See [Adopting hover support for Apple Pencil](https://developer.apple.com/documentation/uikit/adopting-hover-support-for-apple-pencil).

## Double tap

Respect system double-tap settings on supported Apple Pencil models: by default, people toggle between the current tool and eraser; they can instead toggle between the current and previous tool, show or hide the color picker, or do nothing. If those settings don’t fit the app, double tap can change an interaction mode (for example, raise/lower in a 3D mesh editor). For custom behavior alongside defaults, provide a discoverable control to choose the custom mode; don’t enable it by default, and make the current mode clear. Avoid double tap for content-modifying or potentially destructive actions; accidental taps should at most trigger actions that are easy to undo.

## Squeeze and barrel roll

Apple Pencil Pro squeeze can run a custom action, but people may configure it for an [App Shortcut](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts). Squeeze is available only while the paired iPad screen is on and Pencil Pro isn’t touching it, so people may not see its result.

- Treat squeeze as one quick, discrete action; respond promptly rather than to a hold or rapid repeats.
- Make squeeze actions nondestructive and easy to undo. If it reveals UI, such as a contextual menu, place it near the Pencil Pro tip.
- Use barrel roll only to modify marking (for example, rotate a highlight’s angle), never to navigate or reveal other controls.

## Scribble

Scribble is integrated into iPadOS and enabled for all apps by default. Let people write wherever text is naturally accepted without tapping or switching modes first. Standard text fields, text views, search fields, and editable web content support Scribble; password fields are the exception. Custom text fields should also accept writing without a preliminary tap. Make Scribble available in natural areas that lack a visible field—for example, the blank space below the last reminder can create a new reminder; see [UIIndirectScribbleInteraction](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-1nfjm).

Keep writing fluid: avoid autocompletion text that interferes with strokes, hide placeholder text once writing starts, and keep the active field stationary. Delay movement or resizing until people pause if it can’t be avoided. Prevent autoscrolling while transcribing or selecting text. Give people enough writing room by enlarging a likely field before writing or when paused, never while they are writing; see the UIScribbleInteraction API below.

## Custom drawing

[PencilKit](https://developer.apple.com/documentation/pencilkit) captures touch and Apple Pencil input as a drawing, displays it in the app, and provides a low-latency custom drawing canvas with a tool picker and ink palette for notes, annotations, and drawing. Its canvas colors adapt to Dark Mode; when drawing over a PDF or photo, prevent that dynamic color adjustment so markup stays sharp and visible. A regular-environment tool picker includes undo/redo; a compact one doesn’t, so **consider** custom buttons (for example, in a toolbar) and the standard three-finger undo/redo gesture. [UIScribbleInteraction](https://developer.apple.com/documentation/uikit/uiscribbleinteraction) customizes Scribble on text-input views or suppresses it in specific cases. [PaperKit](https://developer.apple.com/documentation/paperkit) adds drawings, shapes, and a consistent markup experience.

## Platform considerations

Not supported in iOS, macOS, tvOS, visionOS, or watchOS.

## Resources

[Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) · [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)

Source: [Apple Human Interface Guidelines — Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble) (captured 2026-09-12).
