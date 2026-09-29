---
topic: image-wells
tier: 4
platforms: [macos]
category: components/controls
triggers:
  - "image well"
  - "NSImageView"
  - "NSImageView drop target"
  - "drag image target"
related:
  - image-views
  - edit-menus
---
# Image wells

An image well is an editable version of an image view. After selecting it, people can copy/paste or delete its image; they can also drag in a new image without selecting the well first.

- If an image is required, restore the default image when people clear the well.
- If copy/paste is supported, provide the standard Copy and Paste menu items; people generally expect those items or their standard keyboard shortcuts.

Supported on macOS; not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

Resources: [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views), [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu), [`NSImageView`](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit, a display of image data in a frame.

Source: [Apple HIG — Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells), captured 2026-09-12.
