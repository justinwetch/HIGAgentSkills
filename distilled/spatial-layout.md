---
topic: spatial-layout
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/visionos
triggers:
  - "spatial layout"
  - "field of view"
  - "depth"
  - "scale"
  - "z-axis"
  - "3D layout"
related:
  - designing-for-visionos
  - immersive-experiences
  - layout
---
# Spatial Layout

> Spatial layout techniques help you take advantage of visionOS's infinite canvas — placing content comfortably within the field of view, at appropriate depth and scale.

**Platforms:** visionOS only

## Field of View

- The system doesn't report the wearer's field of view dimensions.
- **Center important content** — visionOS launches apps directly in front of people. In immersive experiences, keep critical content centered; avoid distracting periphery motion or high-contrast objects.
- **Anchor in space, not to the head.** Head-anchored content causes discomfort. Let people look around naturally.

## Depth

- visionOS automatically applies depth cues (color temperature, reflections, shadow) to virtual content.
- SwiftUI adds visual depth effects to 2D window views automatically.
- For additional depth: use RealityKit 3D objects or volumes (a frame-less window for 3D content).
- **Visual cues must be accurate** — conflicting depth cues cause discomfort.
- **Use depth to communicate hierarchy** (e.g., sheets come forward; underlying window recedes along z-axis).
- **Avoid adding depth to text** — hovering text is hard to read and can cause vision discomfort.
- **Use depth where it adds value** — needed for large, important elements (toolbars, tab bars). Not ideal for small elements like button symbols.
- **Don't overuse** — people must refocus eyes for each depth change. Too many or too rapid depth changes = fatiguing.

## Scale

| Scale type | Behavior | When to use |
|---|---|---|
| Dynamic scale | Window auto-scales as distance changes — appears same size at all distances | Default for interactive content; maintains usability |
| Fixed scale | Object appears smaller as it moves farther away — physically realistic | Noninteractive objects that need to look life-sized (e.g., product previews) |

visionOS defines a point as an **angle** (not pixels) to support dynamic scaling and depth appearance.

## Best Practices

- **Avoid displaying too many windows** — overwhelms and obscures surroundings; makes relocating content cumbersome.
- **Prioritize indirect gestures** — indirect = no need to move hand into field of view; works at any distance. Direct gestures (touching the virtual object) are tiring, especially for objects at or above eye level. Reserve direct gestures for nearby objects inviting close manipulation.
- **Let the Digital Crown recenter** — people press it to recenter windows. Your app doesn't need to handle this.
- **Minimum 60 pt between centers of interactive buttons** — leaving ≥16 pt between them. Ensures hover effect (shown on look) doesn't crowd adjacent elements.
- **Don't let controls overlap other interactive elements** — makes selecting individual items difficult.
- **Let people use your app with minimal physical movement.** If movement isn't essential, don't require it.
- **Use a flat horizontal plane for large immersive experiences** aligned to the floor, so virtual content blends naturally with the physical space.
