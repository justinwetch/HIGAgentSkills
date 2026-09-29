---
topic: spatial-layout
tier: 3
platforms: [visionos]
category: patterns/visionos
triggers:
  - "spatial layout"
  - "field of view"
  - "depth"
  - "scale"
  - "z-axis"
  - "3D layout"
  - "RealityKit"
  - "volume"
  - "volumes"
  - "dynamic scale"
  - "fixed scale"
  - "Digital Crown recenter"
related:
  - designing-for-visionos
  - immersive-experiences
  - layout
  - eyes
---
# Spatial layout

> Spatial layout uses Apple Vision Pro’s infinite canvas to present content in engaging, comfortable ways.

**Platform:** visionOS

## Field of view

A person’s *field of view* is the space visible without moving the head. Its dimensions vary with Light Seal configuration and peripheral acuity; the system doesn’t provide this information.

- The field-of-view diagram illustrates 30°, 60°, and 90° concentric angles; these are illustrations, not reported device limits. In upright and reclining examples, the window is centered in the viewer’s field of view; in the reclining example it is raised and tilted toward the viewer.
- Center important content in the field of view. visionOS initially places an app directly in front of the person. In immersive experiences, keep attention centered and avoid distracting motion or bright, high-contrast peripheral objects.
- Don’t statically anchor content to the wearer’s head. Although content should generally remain within the field of view, a fixed, head-locked display can feel confining, obscure passthrough, and reduce apparent environmental stability. Anchor content in the person’s space so they can look around naturally.

## Depth

Distance, occlusion, and shadow communicate depth. Vision Pro also uses color temperature, reflections, and shadow; these cues change as an object or viewer moves. Small amounts of depth can make even 2D windows feel natural, and SwiftUI adds depth effects to window views. Use [RealityKit](https://developer.apple.com/documentation/realitykit) for 3D objects; a [volume](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-volumes) displays 3D content without a visible window frame.

- Provide visual cues that accurately communicate depth; missing or conflicting cues can cause visual discomfort.
- Use depth for hierarchy (for example, a sheet can come forward while its window recedes on the z-axis).
- Generally keep depth out of text: hovering text is harder to read and can cause discomfort.
- Add depth only when it clarifies or delights. It works well for large, important elements such as a tab bar or toolbar, but can make small controls—such as a button symbol—less legible. Frequent or rapid depth changes tire the eyes because people must refocus.

## Scale

visionOS uses two scale models:

- **Dynamic scale:** A window automatically grows as it moves away and shrinks as it moves closer, preserving apparent size and comfortable legibility/interactivity.
- **Fixed scale:** An object keeps the same scale, appearing smaller with distance along the z-axis like a physical object. visionOS defines a point as an angle to support these behaviors, rather than as a resolution-dependent pixel count.

Use fixed scale sparingly for noninteractive objects that must look physical—for example, a life-size product. Interactive content should generally use scaling that preserves usability.

## Best practices

- Avoid too many windows: they can obscure surroundings, feel constricting, and make relocation cumbersome.
- Prefer standard indirect gestures, which work at any distance with hands outside the field of view. A direct gesture touches a virtual object with a finger; if you support direct gestures, consider reserving them for nearby objects inviting brief inspection or manipulation, because extended interaction—especially at or above eye level—is tiring. See [Gestures > visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS).
- People can press the [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) to recenter content in their field of view; the app needs no special support.
- Leave enough space around interactive components for comfortable gaze hover and to keep hover from crowding other content. Regular-size buttons should have centers at least 60 points apart, leaving 16 points or more between them; controls must not overlap other interactive elements or views. See [Buttons > visionOS](https://developer.apple.com/design/human-interface-guidelines/buttons#visionOS).
- Let people use the app with minimal or no physical movement unless movement is essential.
- Place a large immersive experience that rises from the floor using a flat horizontal plane aligned with the floor, helping it blend with surroundings and feel intuitive.

For related window and layout guidance, see [Windows > visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS), [Layout > visionOS](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS), and [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes).

## Resources

- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces); [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows); [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app)
- [Meet SwiftUI spatial layout](https://developer.apple.com/videos/play/wwdc2025/273); [Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072); [Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076)

Source: [Apple HIG — Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout), captured 2026-09-12.
