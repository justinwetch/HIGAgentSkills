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
# Image Wells

> An image well is an editable image view that supports copy, paste, drag-in, and delete.

**Platforms:** macOS only

After selecting an image well, people can copy/paste the image or delete it. Drag a new image into an unselected image well to replace it.

## Best Practices

- **Revert to default image when cleared** — if the field requires an image, restore the placeholder/default when the content is deleted.
- **Support standard copy/paste menu items and keyboard shortcuts** — people expect Edit > Copy/Paste and ⌘C/⌘V to work. See the-menu-bar#Edit-menu.
