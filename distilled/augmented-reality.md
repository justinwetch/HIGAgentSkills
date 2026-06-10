---
topic: augmented-reality
tier: 3
platforms: [ios, ipados, visionos]
category: technologies
triggers:
  - "AR"
  - "augmented reality"
  - "ARKit"
  - "3D object"
  - "world tracking"
related:
  - playing-audio
  - playing-haptics
  - gestures
---
# Augmented Reality

> AR superimposes 3D virtual objects on a live camera view of the physical world, using ARKit on iOS, iPadOS, and visionOS.

**Platforms:** iOS, iPadOS, visionOS

> **visionOS note**: most camera-view AR guidance here applies to iOS/iPadOS. ARKit in visionOS is distinct: use it for detecting surfaces, hand/finger tracking, and incorporating physical objects into immersive experiences with user permission.

## Best Practices

- **Full-screen camera view** - maximize screen real estate; minimize UI clutter.
- **60 fps minimum** - objects must not jump or flicker; update scenes every frame.
- **Convincing illusions**: use ARKit for proper scale, surface placement, environmental lighting reflection, camera grain, top-down shadows, and position updates as camera moves.
- **Reflective surfaces**: use small or coarse reflections - large mirrors reveal ARKit approximation artifacts.
- **Audio + haptics**: use sound effects and haptics when virtual objects contact surfaces. Background music helps immersion.
- **Minimal text in 3D** - only info people need for the experience.
- **Screen-space controls**: fixed to screen position, not 3D space; use translucency to avoid blocking the scene. Easier to find than embedded 3D controls.
- **Anticipate varied environments** - communicate requirements clearly; offer feature sets for constrained spaces.
- Offer AR only on ARKit-capable devices. If optional or capability-specific AR support is unavailable, don't show an error; omit that feature or entry point.
- Provide a way to get more information without leaving AR, especially when objects or environments need explanation.
- **Comfort**: avoid requiring sustained device angles that cause fatigue. Keep levels short in games.
- **Gradual motion** - introduce movement progressively; never make sudden large movements required.
- **Safety** - avoid requiring rapid, sweeping, or expansive physical movements.

## Coaching

Use the system-provided `ARCoachingOverlayView` for initialization and relocalization.

- **Hide app UI while the coaching view is active.**
- Custom coaching is acceptable if you need different visuals or additional info; use the system view as a reference.

## Object Placement

- **Visual indicator** when surface is detected and placement is possible; align it with the detected plane.
- **Place immediately when people tap** - don't wait for more accurate surface data. Subtly adjust the position afterward if needed (`ARTrackedRaycast`).
- **Use plane classification** to enforce logical placement (floor for furniture, table for game boards).
- **Avoid trying to precisely align with detected surface edges** - boundaries are approximations.
- **Guide to offscreen objects** with edge indicators or audio cues.

## Object Interactions

- **Direct touch preferred** over indirect screen-space controls - more immersive.
- Consider non-gesture interactions based on motion, distance, proximity, or physical-object relationships when they fit the experience.
- **Standard gestures**: single-finger drag = move; two-finger rotation = spin.
- **Hit-test tolerance**: respond to gestures near, not exactly on, objects.
- **Scaling**: only when it makes sense in context (imaginary environment OK; real-world furniture sizing: no).
- **Don't use scaling to simulate proximity** - large distant object still looks far away.
- **Watch for conflicting gestures** - pinch vs. rotation are similar; test carefully.
- **Physics consistency**: objects should stay attached to surfaces; no jumping/flickering during resize/rotate/move.

## Multiuser

- Maps merge automatically via ARKit.
- **Allow people occlusion** for realism.
- Use implicit map merging to let late joiners enter an ongoing session.

## Real-World Object Detection

- **<=100 reference images at once** for best detection performance. Change the active set based on context.
- **Delay before removing virtual objects** when a detected image disappears; wait up to 1 second before fading out to prevent flickering.
- Use tracked images, not just detected images, when the image may move or the attached asset is small.

## Handling Interruptions (Relocalization)

- Use the coaching view to help people return device to previous position/orientation.
- **Hide virtual objects during relocalization** to avoid flickering.
- **Provide a reset button** if relocalization doesn't succeed or if results are poor/confusing.
- If your app supports both AR and non-AR, embed non-AR tasks within the AR experience to avoid interruptions.
- Indicate when the front camera loses face tracking for more than about 0.5 seconds.

## User-Facing Language

Use approachable terminology, not ARKit jargon:

| Do | Don't |
|---|---|
| "Unable to find a surface. Try moving to the side or repositioning your phone." | "Unable to find a plane. Adjust tracking." |
| "Tap a location to place the [object]." | "Tap a plane to anchor an object." |
| "Try turning on more lights and moving around." | "Insufficient features." |
| "Try moving your phone more slowly." | "Excessive motion detected." |

**Problem suggestions:**

| Problem | Suggestion |
|---|---|
| Insufficient features | Try turning on more lights and moving around. |
| Excessive motion | Try moving your phone slower. |
| Detection too slow | Try moving around, turning on more lights, pointing at a more textured surface. |

- **Prefer 3D indicators** over 2D text overlays in a 3D environment.
- Display text labels in screen space, always facing people, consistent size regardless of distance.

## AR Icons and Badges

- **AR glyph**: use only to launch an ARKit-based experience. No alterations except size/color. Minimum clear space = 10% of glyph height.
- **AR badge**: use only to mark products viewable in AR via ARKit. Don't alter, recolor, or use for non-ARKit experiences.
- Prefer the full AR badge over the glyph-only badge; use glyph-only in constrained spaces.
- **Only badge when your app has a mix** of AR-viewable and non-AR-viewable objects; don't badge if everything supports AR.
- Place badge consistently in the same corner of a product photo; don't obscure important detail.
- Minimum clear space = 10% of badge height.
