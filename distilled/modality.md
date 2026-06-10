---
topic: modality
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/interaction
triggers:
  - "modal"
  - "presented view"
  - "dismissal"
  - "swipe to dismiss"
  - "UIModalPresentationStyle"
related:
  - sheets
  - alerts
  - action-sheets
  - popovers
  - activity-views
---
# Modality

> Modality presents content in a separate, dedicated mode that requires an explicit action to dismiss and prevents interaction with the parent view.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Use modality to:
- Deliver critical information and require action on it
- Confirm or modify a recent action
- Focus people on a distinct, narrowly scoped task without losing previous context
- Enable an immersive or complex task experience

**Components:** alerts (all platforms), activity views, sheets, action sheets, confirmation dialogs; iPadOS/macOS/visionOS can also use separate windows for distinct tasks.

Use sheets or popovers for scoped, distinct tasks that should stay close to the current context without becoming a full navigation destination.

## Best Practices

- **Present modally only when there's a clear benefit** — it removes people from their context and requires an explicit dismissal.
- **Keep modal tasks simple, short, and streamlined** — complex modal flows cause people to lose track of the suspended context.
- **Avoid a modal-within-a-modal feel** — if subviews are necessary, provide a single path through the hierarchy. Don't include buttons that could be confused with the dismiss button.
- **Full-screen modal** is appropriate for in-depth content or complex tasks (video, photo, camera, markup, multi-step editing). In visionOS Shared Space, fills a window; in Full Space, can become a more immersive experience.
- **Always provide an obvious dismiss action**, following platform conventions:
  - iOS, iPadOS, watchOS: button in top toolbar, or swipe down
  - macOS, tvOS: button in the main content view
- **Warn before data loss** — if dismissing could destroy user-generated content, confirm with an action sheet (iOS) or dialog. Explain the situation and provide resolution options.
- **Label the modal's task** — use a title or descriptive text so people know what they're doing and can keep their place.
- **Only one modal at a time** — presenting multiple modals adds cognitive load and visual clutter. Alerts may appear on top of all content, but never show more than one alert simultaneously.

## Platform Considerations

*No additional considerations for any platform.*
