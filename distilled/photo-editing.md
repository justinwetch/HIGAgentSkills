---
topic: photo-editing
tier: 4
platforms: [ios, ipados, macos]
category: technologies
triggers:
  - "photo editing"
  - "App extensions"
  - "PhotoKit"
  - "filter extension"
  - "photo extension"
related: []
---
# Photo Editing

> Photo editing extensions let people modify photos and videos from within the Photos app, using filters or other changes.

**Platforms:** iOS, iPadOS, macOS *(not tvOS, visionOS, watchOS)*

Edits always save as new files — originals are always preserved. Access: photo must be in edit mode → tap extension icon in toolbar → action menu → selecting an extension presents its interface in a modal view with a top toolbar. Dismissing saves or cancels the edit.

## Best Practices

- **Confirm cancellation** — if someone taps Cancel, always ask for confirmation before discarding changes. Inform them that edits will be lost. No confirmation needed if no edits have been made yet.
- **No custom top toolbar** — the modal view already includes a toolbar. A second toolbar is confusing and wastes space.
- **Let people preview edits** — they need to see the result before committing. Show the edited state before they close and return to Photos.
- **Use your app icon as the extension icon** — builds trust that the extension belongs to your app.
