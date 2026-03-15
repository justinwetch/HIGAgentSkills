---
topic: motion
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "animation"
  - "transition"
  - "motion"
  - "easing"
  - "spring"
  - "duration"
related:
  - feedback
  - gestures
---
# Motion

> Fluid motion brings interfaces to life, conveying status, providing feedback, and enriching the visual experience.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

System components include motion automatically and adjust it based on accessibility settings and input method (e.g., Liquid Glass responds with more emphasis to touch, subdued response to trackpad). For custom motion, follow the guidelines below.

## Best Practices

- Add motion purposefully — don't add it for its own sake. Gratuitous animation distracts and may cause physical discomfort.
- Never use motion as the only way to communicate information — supplement with haptics and audio.

## Providing Feedback

- Motion feedback must feel realistic and match gesture direction (e.g., a view revealed by sliding down from the top should be dismissed by sliding back up, not sideways).
- Keep feedback animations brief and precise — lightweight, unobtrusive, and more informative than prominent animation.
- Avoid adding motion to frequently occurring UI interactions — system already provides subtle animations for standard elements.
- Let people cancel animations — don't force waiting, especially for repeated animations.
- Use SF Symbols animated variants (SF Symbols 5+) where appropriate.

## Games

- Default to 30–60 fps for smooth gameplay on each supported platform.
- Use device GPU capabilities to ensure acceptable default settings without user configuration.
- Let people customize visual settings (quality, power mode) when an external power source is detected.

## Platform Considerations

### visionOS

Motion in visionOS can combine with depth to provide essential feedback when people look at interactive elements. Motion comfort is critical.

- **Avoid motion at edges of field of view** — peripheral motion is highly distracting and can cause physical discomfort (feeling of self-movement). If peripheral motion is necessary, match the object's brightness to the surrounding environment.
- **Large objects filling most of the field of view** can feel like a surroundings movement. Increase translucency or reduce contrast to distinguish object motion from environmental motion.
- **Relocating objects**: use fade-out → move → fade-in instead of direct movement when the move doesn't communicate useful information.
- **Avoid rotating the virtual world** — even subtle user-controlled world rotation causes disorientation. Use instantaneous directional changes during a quick fade instead.
- **Provide a stationary frame of reference** — containing movement within a bounded area reduces discomfort versus moving the entire surroundings.
- **Avoid sustained oscillation**, especially at ~0.2 Hz (people are very sensitive to this frequency). Keep amplitude low and consider translucency for oscillating content.

### watchOS

Use SwiftUI for animation in watchOS. WatchKit layout/appearance animations include automatic built-in easing at start and end — this cannot be disabled or customized.
