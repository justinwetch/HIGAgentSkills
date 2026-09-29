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

# Photo editing

Photo-editing extensions let people modify photos and videos inside Photos with filters or other changes. Edits always save in Photos as new files, preserving originals. A photo must be in edit mode; tapping the toolbar extension icon opens an action menu, and selecting an extension opens its interface in a modal view with a top toolbar. Dismissing confirms and saves the edit, or cancels and returns to Photos. [PhotoKit](https://developer.apple.com/documentation/photokit) works with image/video assets managed by Photos, including iCloud Photos and Live Photos.

## Best practices

- Confirm cancellation when edits exist: editing may take time, so a Cancel tap should ask whether the person really wants to discard changes and explain that edits will be lost. Confirmation is unnecessary if no edits have been made.
- Do not provide a custom top toolbar. The modal already supplies one; a second toolbar is confusing and removes editing space.
- Let people preview the result before closing the extension and returning to Photos.
- Use your app icon as the photo-editing extension icon to establish that the extension comes from your app.

## Platform

There are no additional considerations for iOS, iPadOS, or macOS. Photo-editing extensions are unsupported in tvOS, visionOS, and watchOS.

Source: [Photo editing](https://developer.apple.com/design/human-interface-guidelines/photo-editing), captured 2026-09-12. Resources: [App extensions](https://developer.apple.com/app-extensions/), [Introducing Photo Segmentation Mattes](https://developer.apple.com/videos/play/wwdc2019/260).
