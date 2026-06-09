---
topic: voiceover
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/accessibility
triggers:
  - "VoiceOver"
  - "screen reader"
  - "accessibility label"
  - "rotor"
  - "custom rotor"
  - "AccessibilityNotification"
  - "shouldGroupAccessibilityChildren"
  - "Direct Gesture mode"
  - "Unity plug-ins"
related:
  - accessibility
  - focus-and-selection
  - inclusion
  - charts
---
# VoiceOver

> VoiceOver is a screen reader that describes your app's interface audibly, enabling people who are blind or have low vision to use it without seeing the screen.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Descriptions

- **Label all key interface elements** - system controls have generic labels by default; replace with labels that convey your app's actual function.
- **Update labels when UI changes.**
- **Describe meaningful images** - focus on what the image conveys, not surrounding captions or context VoiceOver already handles.
- **Make charts and infographics accessible** - provide concise descriptions and expose interactions.
- **Mark decorative images as decorative** - reduce cognitive noise.

## Navigation

- **Use unique, descriptive page/screen titles** - first thing VoiceOver reads on arrival.
- **Use accurate section headings** - helps people build a mental model of hierarchy.
- **Describe visual relationships** - proximity, alignment, grouping, and order aren't always inferable.
- **Group related elements** - image + caption should read together; otherwise VoiceOver may read all images before captions.
- **Announce visible content and layout changes** - stale mental maps cause errors.
- **Support the VoiceOver rotor** - include heading, link, and other identifiers so people can jump by content type.

## visionOS

- **Custom gestures are not accessible by default** - VoiceOver intercepts hand input for exploration. Direct Gesture mode can bypass this, but don't depend on it.

## Games

- VoiceOver is supported in Unity apps and games through Apple's Unity plug-ins; keep custom game UI accessible through labels, grouping, and rotor/navigation support.
