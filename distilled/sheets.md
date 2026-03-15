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
related:
  - modality
  - action-sheets
  - popovers
---
# Sheets

> A sheet helps people perform a scoped task closely related to their current context, without fully leaving that context.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

**Modal by default** (macOS, visionOS, watchOS always modal). iOS/iPadOS also support **nonmodal sheets** — the sheet stays open and directly affects the parent view without requiring dismissal (e.g., Notes formatting panel).

## Best Practices

- **Simple content or tasks only** — a sheet keeps some of the parent view visible, maintaining context. For complex or long flows use full-screen modal (iOS/iPadOS), a new window (macOS), or a Full Space transition (visionOS).
- **One sheet at a time** — if a task inside a sheet spawns another sheet, close the first before showing the second (restore it after the second dismisses if needed). Never stack sheets.
- **Nonmodal sheets for supplementary items that affect the main task** — for ongoing parallel access, consider a split view (visionOS) or panel (macOS).

## Platform Considerations

### iOS, iPadOS

**Detents** — the heights at which a resizable sheet naturally rests:
- `large` (full height) — supported by default.
- `medium` (~half height) — add to support progressive disclosure.
- Specifying only `medium` prevents full expansion.

**When to use medium detent:** when the most relevant content is immediately visible at half-height (e.g., share sheet) and people expand only to see more. Don't use medium if the sheet needs full height to be usable (Mail/Messages compose = full height only).

- **Include a grabber** in resizable sheets — visible affordance for dragging; also works with VoiceOver. Tapping the grabber cycles through detents.
- **Support swipe to dismiss** — if people have unsaved changes when swiping, show an action sheet to confirm before discarding.
- **Button placement:**
  - Standard sheet: Done/Dismiss → top-right; Cancel → top-left.
  - Sheet with subviews (multi-page navigation flow): Cancel → top-right (leaves room for Back at top-left on subsequent pages); replace Cancel with Done at the end of the flow.
- **iPadOS: prefer page or form sheet presentation styles** — default size, centered with dimmed background.

### macOS

- Sheet is a card with rounded corners floating over a dimmed parent window.
- **Let people interact with other app windows without dismissing the sheet** — other windows can be brought forward even while the sheet is open.
- **Reasonable default size** — people don't expect to resize sheets, but support resize for sheets where expanded view is helpful.
- **Dismiss buttons (Done, OK, Cancel) at the bottom, in the trailing corner.**
- **Use a panel instead of a sheet** for repeated input-and-observe workflows (e.g., Find and Replace).

### visionOS

- Sheet floats in front of and dims the parent window.
- **Don't emerge from the bottom edge** — center the sheet in the field of view.
- **Default size that preserves context** — don't cover most or all of the parent window.

### watchOS

- Full-screen view that slides over the current content. Semi-transparent (blurred/desaturated background).
- **Only when a modal task requires a custom title or custom content.** For simple info or choices, use an alert or action sheet.
- **Brief and occasional** — temporary interruption only; not for app navigation.
- **Dismiss control:** default is a round Cancel button (upper-left). Use Done instead if the sheet presents info without enabling edits. Can use a toolbar for multiple buttons.
- **If changing the label, use SF Symbols** — text in the top-leading corner that looks like a title confuses people about how to dismiss.
