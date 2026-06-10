---
topic: nearby-interactions
tier: 4
platforms: [ios, ipados, watchos]
category: technologies
triggers:
  - "Nearby Interactions"
  - "Nearby Interaction"
  - "UWB"
  - "ultra-wideband"
  - "spatial awareness between devices"
related:
  - feedback
---
# Nearby Interactions

> Nearby Interactions use Ultra Wideband (UWB) technology to enable experiences based on the physical presence and proximity of people and objects.

**Platforms:** iOS, iPadOS, watchOS *(not macOS, tvOS, visionOS)*

Requires user permission to interact. Uses randomly generated device identifiers that expire with the interaction session.

- **iOS**: provides peer device's distance and direction.
- **watchOS**: provides peer device's distance only. watchOS apps must be in the foreground.

## Best Practices

- **Look for real-world physical actions** that map naturally to the task (e.g., bringing two devices together to transfer playback).
- **Use distance, direction, and context together** — combine UWB data with on-device knowledge (contacts, recency) for better results.
- **Vary feedback with proximity** — mirror physical world expectations (perception sharpens as distance decreases).
- **Continuous feedback** — reflect the dynamism of the physical environment; don't interrupt updates.
- **Multi-modal feedback** — combine visual, audible, and haptic based on context (screen → visual; environment → haptic + audio).
- **Always provide a non-UWB fallback** — not all devices support nearby interactions.

## Device Guidance

- **Encourage portrait orientation** — landscape decreases distance/direction accuracy. Prefer implicit visual cues over explicit instructions to hold device upright.
- **Field of view**: hardware sensor FOV similar to Ultra Wide camera; outside it, direction info may be unavailable.
- **Warn about intervening objects** — people, animals, large objects between devices reduce accuracy. Mention this in onboarding.
