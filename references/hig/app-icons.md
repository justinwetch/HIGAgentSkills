---
topic: app-icons
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "app icon"
  - "icon design"
  - "icon grid"
  - "icon size"
related:
  - images
  - branding
  - icons
---
# App Icons

> A unique, memorable icon expresses an app's or game's purpose and personality and helps people recognize it at a glance.

An app icon is branding and user experience, appearing on the Home Screen, search, notifications, Settings, and share sheets. Keep its identity clear across platforms.

## Specifications

| Platform | Layout shape | System-masked shape | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024×1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800×480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024×1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088×1088 px | Layered | N/A |

Color spaces: sRGB (color), Gray Gamma 2.2 (grayscale), Display P3 (wide-gamut only on iOS/iPadOS/macOS/tvOS/watchOS). System scales icons for smaller locations such as Settings and notifications.

## Layer design

You can supply a flattened image, but layers give more control and create depth as system effects respond to environment and interaction.

- **iOS, iPadOS, macOS, watchOS:** background plus one or more foreground layers; Liquid Glass adds size-adaptive specular highlights, refraction, and translucency (which can differ by system version).
- **tvOS:** two to five layers create parallax. On focus, remote finger movement elevates the icon; it sways and illuminates, while transparent separation supplies depth.
- **visionOS:** background plus one or two upper layers form a subtly expanding 3D object. System shadows show depth and upper-layer alpha embosses it.

Craft foreground layers in a design tool. For iOS/iPadOS/macOS/watchOS, import them into **Icon Composer** (in Xcode; also on the [Apple Developer website](https://developer.apple.com/icon-composer)) to define the background, place layers, apply specular/refraction effects, annotate default/dark/mono variants, test system versions, and export to Xcode. For tvOS/visionOS, add layers directly to an Xcode image stack; [Parallax Previewer and Exporter](https://developer.apple.com/design/resources/) test parallax.

**Layer guidance:**

- Prefer clearly defined foreground edges (soft/feathered edges degrade highlights/shadows) and vary opacity for depth. Photos separates its centerpiece into translucent pieces; opaque layers adjusted in Icon Composer help assess system effects.
- Make the background stand out and emphasize foreground content. Gradients must respond to system lighting; Icon Composer supports solid/gradient backgrounds, so imported images are usually unnecessary. An imported background must be full-bleed and opaque.
- Prefer vector layers (SVG/PDF), outline artwork, and convert text to outlines. For mesh gradients and raster artwork, prefer lossless PNG.
- Provide **unmasked** layers: square for iOS/iPadOS/macOS (the system's rounded corners match other rounded elements and the device bezel) and visionOS/watchOS, rectangular for tvOS (concentric rounded edges). Let the system mask edges; pre-masking harms highlights and makes edges jagged. Center primary content, especially in visionOS/watchOS, using [Apple Design Resources](https://developer.apple.com/design/resources/) grids.

## Design

Embrace simplicity: one core concept, minimal shapes, and a solid/gradient background that emphasizes it; you don't need to fill the canvas. Fine detail becomes busy under system effects and is hard to discern small.

- Keep the design consistent across supported platforms so people find it and don't mistake it for multiple apps.
- Consider filled, overlapping foreground shapes; transparency and blurring add depth. Avoid outline-only shapes.
- Include text only when essential: it is inaccessible, not localizable, often too small, and may duplicate a nearby name. A first-letter mnemonic can aid recognition; avoid instructional/context words (“Watch,” “Play,” “New,” “For visionOS”). In tvOS, place text above other layers to avoid parallax cropping.
- Prefer illustrations to photos, which lose detail across appearances/layers/sizes. Avoid extremely thin line weights, sharp corners, UI replicas, and screenshots. Apple hardware products are copyrighted and cannot be reproduced in app icons.

## Visual effects

Let the system provide blurs, specular highlights, inter-layer shadows, bevels, glows, and similar dynamic effects; custom static effects can interfere. If intentional, test in Icon Composer, Device Hub simulator, or on-device. Group layers when effects should apply together; group-level Liquid Glass options include specular highlights, refraction, and translucency.

## Appearances

In iOS/iPadOS/macOS, people choose default, dark, clear, or tinted Home Screen icons. Supply variants as desired; the system generates omitted ones.

- Keep core features consistent; don't swap elements between variants. Dark icons are subdued and clear/tinted more so, so preserve visibility, legibility, and recognition beside system icons/widgets.
- Base dark on light with complementary colors and no excessive brightness; color backgrounds generally give greatest contrast. See [Dark Mode](https://developer.apple.com/design/Human-Interface-Guidelines/dark-mode).
- **Alternate icons:** iOS/iPadOS/tvOS and compatible visionOS apps may let people choose a related icon in settings (for example, a sports team). Keep alternates tied to the app and distinct from other apps. iOS/iPadOS alternates need dark, clear, and tinted variants; all are subject to [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#design).

## Platform considerations

### tvOS

**Include a safe zone.** Focus can scale and move the icon, cropping its edges. The safe zone varies with image size, layer depth, and motion; foreground layers crop more than background layers.

### visionOS

Avoid a background shape intended as a hole or concave area: system shadows and highlights can make it look prominent rather than recessed.

### watchOS

Avoid a black background; lighten it so the icon doesn't blend into the display background.

## Resources

[Apple Design Resources](https://developer.apple.com/design/resources/) · [Icon Composer](https://developer.apple.com/icon-composer/) · [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) · [Images](https://developer.apple.com/design/human-interface-guidelines/images) · [Creating your app icon with Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) · [Configuring your app icon](https://developer.apple.com/documentation/xcode/configuring-your-app-icon) · [WWDC25: App icons](https://developer.apple.com/videos/play/wwdc2025/220)

Source: [Apple Human Interface Guidelines — App icons](https://developer.apple.com/design/Human-Interface-Guidelines/app-icons), captured 2026-09-12.
