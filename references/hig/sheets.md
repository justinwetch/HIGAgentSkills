---
topic: sheets
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/presentation
triggers:
  - "sheet"
  - "bottom sheet"
  - "half-sheet"
  - "detent"
  - "UISheetPresentationController"
  - "sheet(item:onDismiss:content:)"
  - "presentAsSheet(_:)"
  - "detents"
  - "prefersGrabberVisible"
  - "UIModalPresentationStyle"
related:
  - modality
  - action-sheets
  - popovers
  - panels
---

# Sheets

A sheet requests specific information or presents a scoped, context-related task people complete before returning to the parent view.

## Anatomy

Sheets are always modal in macOS, tvOS, visionOS and watchOS. In iOS and iPadOS they can be nonmodal, letting people affect the parent view with the sheet open.

|Button|Use|
|---|---|
|Cancel (or Close)|Exits without saving; common in most sheets|
|Done|Exits after completing a task or explicitly saving|
|Back|Previous step or parent view; not for dismissing|

## Best practices

- **Consider alternatives for complex or prolonged flows:** a full-screen modal (`UIModalPresentationStyle.fullScreen`) in iOS and iPadOS for media, camera views or multistep editing; a new window (self-contained tasks) or full-screen mode (media) in macOS; a Full Space in visionOS.
- **Display only one sheet at a time from the main interface.** Close a sheet before it opens another; if necessary, you can redisplay it after the second closes.
- **Use a nonmodal view for supplementary items affecting the parent's main task**: consider a visionOS split view or macOS panel; in iOS and iPadOS, you can use a nonmodal sheet.
- **Provide an alternative to Done**: always pair it with Cancel or Back. Avoid showing all three together.

## Platform considerations

No additional considerations for tvOS.

### iOS, iPadOS

Single-view sheets: Cancel on the top toolbar's leading edge; Done, when present, trailing. Multi-step flows can vary:

|Step|Leading|Done|
|---|---|---|
|First|Cancel|Inactive (task incomplete)|
|Subsequent|Back, replacing Cancel|Inactive|
|Final confirmation|Back|Active|

Resizable sheets expand when people scroll or drag the grabber (top-edge handle) and rest at detents, designed for iPhone: large (full height, automatic), medium (about half) and one or more custom. Adding medium allows both heights; medium alone prevents full height (`detents`).

- **In an iPhone app, consider supporting medium for progressive disclosure.** You might not want it when content is more useful at full height, like compose sheets.
- **Include a grabber in a resizable sheet** (`prefersGrabberVisible`). People drag it to resize or tap it to cycle detents, including with VoiceOver.
- **Support swiping vertically to dismiss.** If changes are unsaved when swiping begins, confirm with an action sheet.
- **Prefer page or form sheet styles in an iPadOS app** (`UIModalPresentationStyle`); each uses a default size, centered over a dimmed background.

### macOS

A sheet is a rounded card floating over its dimmed parent window.

- **Present a sheet in a reasonable default size**; people rarely expect to resize sheets, but it's a good idea to support it when they need a clearer view.
- When a sheet opens, its parent window (and a document window's modeless panels) comes forward; **make sure people can still bring other app windows forward** without dismissing the sheet.
- **Use a panel instead if people need to repeatedly provide input and observe results**, like find and replace.

### visionOS

A sheet floats in front of its parent window, dims it, and receives app interactions.

- **Avoid sheets that emerge from a window's bottom edge**; prefer centering in people's field of view.
- **Use a default size that preserves context**: avoid covering most or all of the window, but consider letting people resize.

### watchOS

A sheet is a full-screen, semitransparent view that slides over current content; a system material blurs and desaturates it.

- **Use a sheet only when your modal task requires a custom title or content presentation.** For important information or choices, consider an alert or action sheet.
- **Keep sheet interactions brief and occasional**: only as a temporary interruption and only for an important task. Avoid using sheets for content navigation.
- **If you change the default label, prefer an SF Symbol.** Avoid labels implying hierarchical navigation or top-leading text resembling a page or app title, which hides how to dismiss.

## Resources

Developer: `sheet(item:onDismiss:content:)`, `UISheetPresentationController`, `presentAsSheet(_:)`.

Source: [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), captured 2026-09-12.
