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
  - image-wells
  - buttons
  - sf-symbols
---


# Image views

An image view displays one image, or sometimes an animated sequence. It can stretch, scale, fit or pin the image; it's typically not interactive.

## Best practices

- **Use an image view when the view's primary purpose is to display an image.** For a rare interactive image, configure a system button to display it instead of adding button behaviors to an image view.
- **For an icon, consider an SF Symbol or interface icon (template image) instead**; both can use people's chosen accent colors.

## Content

- Formats include PNG, JPEG and PDF.
- **Take care when overlaying text on images.** Ensure the text contrasts well with the image, and consider making the text stand out, e.g. a text shadow or background layer.
- **Aim for a consistent size for all images in an animated sequence**; prescaling to fit the view avoids system scaling. When the system must scale, same-size, same-shape images generally perform better.

## Platform considerations

No additional considerations for iOS or iPadOS.

### macOS

- **For an editable image view, use an image well** (copy, paste, drag, Delete to clear).
- **For a clickable image, use an image button instead.**

### tvOS

Many tvOS images combine transparent layers for depth; see [Layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images).

### visionOS

Window image views can show 2D and stereoscopic images and spatial photos. With RealityKit (`ImagePresentationComponent`), you can also show any image outside image views beside 3D content, or generate a spatial scene from a 2D image.

### watchOS

**Use SwiftUI for animations when possible.** If necessary, WatchKit can animate an image sequence in an image element (`WKImageAnimatable`).

## Resources

Developer: `Image` (SwiftUI), `UIImageView`, `NSImageView`.

Source: [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views), captured 2026-09-12.
