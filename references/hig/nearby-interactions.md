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
# Nearby interactions

Nearby interactions use the physical presence of people and objects to create on-device experiences. They are available on devices supporting Ultra Wideband (see [Ultra Wideband availability](https://support.apple.com/en-us/HT212274)) and use the NearbyInteraction framework. Before participating, people grant permission for their device to interact while they’re using your app; APIs use randomly generated device identifiers that last only for the interaction session, supporting privacy.

## Design

- Start from the task’s physical-world action. Bringing an iPhone close to a HomePod mini to transfer audio can feel more natural than performing the same transfer solely in UI.
- Use distance, direction, and context. Nearby, contextually relevant information can improve recipient suggestions—for example, the iOS share sheet combines on-device knowledge of a person’s most frequent and recent contacts with nearby U1 devices to suggest the closest contact the person is facing in a crowded room.
- Consider how changing physical distance can guide feedback. As a person approaches an AirTag, Find My transitions from a directional arrow to a pulsing circle, mirroring the expectation that perception sharpens as an object gets closer.
- Provide continuous feedback that responds to movement, such as uninterrupted direction/proximity updates while finding an item.
- Consider coordinated visual, audible, and haptic feedback. Visual feedback suits screen interaction; audible and haptic feedback can work better while a person attends to the environment.
- Provide another way to perform the task; avoid making a nearby interaction the sole path for everyone.

## Device usage

Landscape orientation can reduce the accuracy and availability of distance and relative-direction data. Encourage portrait use; when only portrait is supported, prefer implicit visual guidance for holding the device and avoid explicit instructions when possible.

Design for the sensor’s directional field of view, similar to the Ultra Wide camera on iPhone 11 and later. A device outside that field may still provide distance, but not relative direction. Explain that people, animals, or sufficiently large intervening objects can reduce the accuracy or availability of distance/direction data; consider adding this advice to onboarding or tutorials.

On iPhone, Nearby Interaction APIs provide a peer’s distance and direction. On Apple Watch, they provide distance only, and every participating watchOS app must be in the foreground. There are no additional iPadOS considerations; Nearby interactions aren’t supported in macOS, tvOS, or visionOS.

Source: [Apple Human Interface Guidelines — Nearby interactions](https://developer.apple.com/design/Human-Interface-Guidelines/nearby-interactions), captured 2026-09-12.
