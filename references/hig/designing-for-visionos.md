---
topic: designing-for-visionos
tier: 2
platforms: [visionos]
category: platforms
triggers:
  - "visionOS"
  - "Apple Vision Pro"
  - "spatial"
  - "immersive"
related:
  - windows
  - spatial-layout
  - immersive-experiences
  - digital-crown
  - accessibility
  - shareplay
  - gestures
  - eyes
---

# Designing for visionOS

visionOS apps and games run in infinite 3D space within people's surroundings.

## Platform characteristics

- Apps launch in the multi-app *Shared Space* by default; people can move one to a single-app *Full Space* (3D content blended with surroundings, a portal, or another world).
- The Digital Crown adjusts passthrough.
- The system automatically tunes Spatial Audio to the room; apps with permission to access surroundings information can fine-tune it.
- In general, people look and make an *indirect* gesture like a tap, or touch objects *directly*.
- The system automatically places content relative to the head, regardless of height or posture.
- visionOS supports VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer and more; system components include support by default, and frameworks let you enhance it.

**Prioritize user safety**: not for use while operating vehicles or heavy machinery or moving near hazards like balconies, streets or stairs; ages 13+ only.

## Best practices

- **Embrace space, Spatial Audio, immersion, passthrough and eye and hand input.**
- **Find the minimum immersion, from windowed to full, each key moment needs**; don't assume every moment needs full immersion.
- **Use windows for contained, UI-centric experiences**, preferring standard windows with familiar controls for standard tasks. People can relocate windows anywhere; dynamic scaling helps keep them legible at any distance.
- **Prioritize comfort:**
  - Display content in the field of view, relative to the head; avoid placing interactive content where people must turn their head or change position.
  - Avoid motion that's overwhelming, jarring, too fast or lacks a stationary frame of reference.
  - Support indirect gestures so hands can rest in the lap or at the sides.
  - For direct gestures, make sure interactive content isn't too far and doesn't need extended interaction.
  - Avoid encouraging too much movement in full immersion.
- **Help people share activities** with SharePlay, which can show participants' *spatial Personas*.

Source: [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos), captured 2026-09-12.
