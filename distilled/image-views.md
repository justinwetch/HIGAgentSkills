---
topic: image-views
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "image view"
  - "UIImageView"
  - "NSImageView"
  - "image display"
related:
  - images
  - scroll-views
---
# Image Views

> An image view displays a single image (or an animated image sequence) on a transparent or opaque background.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Supports stretch, scale, size-to-fit, or pinned positioning. Typically not interactive.

## Best Practices

- **Use when the primary purpose is simply displaying an image.** For interactive images, configure a system button to display the image instead of adding button behavior to an image view.
- **Prefer symbols or interface icons over image views for icons** — SF Symbols are vector-based, scalable, support accent colors; interface icons (template images) allow any color.
- **Text over images: ensure contrast** — compositing text on images can harm both legibility and clarity. Add a text shadow or background layer to help text stand out.
- **Consistent image sizes in animated sequences** — pre-scaled images avoid runtime scaling; same size and shape across frames gives best performance.

## Platform Considerations

### macOS

- **Image well** for editable image views — supports copy, paste, drag, and Delete to clear.
- **Image button** (not image view) for clickable images — image buttons initiate app-specific actions.

### tvOS

- Many tvOS images use layered images with transparency for a parallax depth effect. See images#Layered-images.

### visionOS

- Image views support 2D images, stereoscopic images, and spatial photos.
- Using RealityKit: can display images alongside 3D content outside of image views, or generate a spatial scene from a 2D image (`ImagePresentationComponent`).

### watchOS

- **Prefer SwiftUI for animations.** WatchKit image-element animation sequences are an alternative if SwiftUI isn't available.
