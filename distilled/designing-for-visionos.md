---
topic: designing-for-visionos
tier: 2
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: platforms
triggers:
  - "visionOS"
  - "Apple Vision Pro"
  - "spatial"
  - "immersive"
  - "mixed reality"
related:
  - spatial-layout
  - immersive-experiences
  - ornaments
  - eyes
---
# Designing for visionOS

> Apple Vision Pro places people in an infinite 3D space where they engage with apps while remaining connected to their surroundings.

**Platform:** visionOS

## Device Characteristics

| | |
|---|---|
| **Space** | Limitless canvas: windows, volumes, 3D objects; can enter fully immersive experiences |
| **Immersion levels** | Shared Space (multi-app, side-by-side) → Full Space (single app, exclusive). Full Space can blend 3D with surroundings, open portals, or enter alternate worlds |
| **Passthrough** | Live video from external cameras; Digital Crown controls passthrough amount |
| **Spatial Audio** | Acoustic + visual sensing models surroundings; apps with permission can fine-tune for custom experiences |
| **Input** | Eyes + indirect gestures (look to target, tap to activate); direct gestures (touch virtual object) |
| **Ergonomics** | Content placed relative to wearer's head automatically; people stay at rest, content comes to them; visual comfort is paramount |
| **Accessibility** | VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer, and more |

**Safety:** Not for use while operating vehicles or heavy machinery, near hazards (balconies, stairs, streets). Designed for individuals 13+.

## Best Practices

- **Embrace uniqueness** — leverage space, Spatial Audio, and immersion. Integrate passthrough and spatial input from eyes/hands naturally.
- **Choose the minimum necessary immersion level** for each moment — don't make everything fully immersive. Use windowed standard UI for standard tasks.
- **Use standard windows** for contained, UI-centric experiences — they appear as planes in space with familiar controls; system dynamically scales them for legibility at any distance.
- **Prioritize comfort:**
  - Keep content within the person's field of view (head-relative); don't require head-turning or position changes.
  - Avoid overwhelming, jarring, too-fast motion or motion without a stationary frame of reference.
  - Prefer indirect gestures (hands resting in lap/at sides).
  - If using direct gestures: keep interactive content close and don't require extended interaction periods.
  - Minimize movement during fully immersive experiences.
- **Support SharePlay** for shared activities — participants' spatial Personas appear together in the same space.
