---
topic: immersive-experiences
tier: 3
platforms: [visionos]
category: patterns/visionos
triggers:
  - "immersive"
  - "Full Space"
  - "passthrough"
  - "environment"
  - "mixed immersion"
  - "ImmersionStyle.automatic"
  - "ImmersionStyle.mixed"
  - "ImmersionStyle.progressive"
  - "ImmersionStyle.full"
  - "SurroundingsEffect"
  - "SceneReconstructionProvider"
  - "CoordinateSpaceProtocol"
related:
  - spatial-layout
  - motion
  - accessibility
  - playing-audio
---
# Immersive experiences

> visionOS apps and games can extend beyond windows and volumes into content that surrounds people.

**Platform:** visionOS

Apps can launch in the *Shared Space*, alongside other experiences, or a *Full Space*, where the app runs alone and hides other experiences. They can transition between spaces and support different immersion levels.

## Immersion and passthrough

Passthrough is real-time video from external cameras that keeps people connected to their surroundings. The [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) can adjust passthrough, press-and-hold to recenter content, or double-click to briefly hide content for a clear view.

The system dims nearby mixed-immersion content when someone approaches a physical object. In `progressive` and `full`, it creates a boundary about 1.5 meters from the wearer’s initial head position: approaching it fades the experience and increases passthrough; crossing it replaces visuals with the app icon until the wearer returns to their original location or recenters with the Digital Crown.

## Immersion styles

In a Full Space, other apps are hidden, but you can still show standard windows, volumes, and unbounded 3D content. See [`ImmersionStyle.automatic`](https://developer.apple.com/documentation/swiftui/immersionstyle/automatic) for the default style.

- **Dimmed passthrough:** In Shared Space, subtly dim or tint passthrough and visible content to focus attention without hiding other apps; in Full Space, it creates a more focused experience. Passthrough is tinted black by default; use [`SurroundingsEffect`](https://developer.apple.com/documentation/swiftui/surroundingseffect) for a custom tint.
- **`mixed`:** In a Full Space, blend unbounded 3D content with passthrough. With permission, [ARKit](https://developer.apple.com/documentation/arkit) can provide nearby-object and room-layout information. There is no boundary; nearby virtual content becomes semi-opaque when a person approaches a physical object. See [`ImmersionStyle.mixed`](https://developer.apple.com/documentation/swiftui/immersionstyle/mixed).
- **`progressive`:** In a Full Space, partially replace passthrough with a custom environment. Content can be displayed in portrait or landscape orientation; you can optionally set the immersion range, and the Digital Crown adjusts immersion through the default 120°–360° range or your custom range. The system adds the approximately 1.5-meter boundary. See [`ImmersionStyle.progressive`](https://developer.apple.com/documentation/swiftui/immersionstyle/progressive).
- **`full`:** In a Full Space, display a 360° custom environment that completely replaces passthrough. The approximately 1.5-meter boundary also applies. See [`ImmersionStyle.full`](https://developer.apple.com/documentation/swiftui/immersionstyle/full).

## Best practices and comfort

- Offer multiple ways to use the app or game and support the [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) features people use to personalize interaction.
- Prefer launching in Shared Space or `mixed`. Shared Space lets people reference and switch to other running software; either a Shared Space window or a `mixed` launch lets people choose when to increase immersion when the app also offers `progressive` or `full`.
- Reserve immersion for meaningful moments. Many tasks benefit from staying grounded and using other software; for example, Photos can browse albums in a Shared Space window and open one photo more immersively in a Full Space.
- Use subtle cues—dimming, tinting, [motion](https://developer.apple.com/design/human-interface-guidelines/motion), [scale](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Scale), and [Spatial Audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio#visionOS)—to focus attention at any immersion level, strengthening them only when needed.
- In visionOS 2 and later, prefer subtle passthrough tints that coordinate surroundings and hands with the content; bright or dramatic tints distract and reduce immersion.
- Prefer placing 3D content within the [field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view) and display motion comfortably. Choose a style suited to expected movement: minor shifts, turning, or sitting/standing are fine, but avoid `progressive`/`full` (or return to `mixed`) if people may cross the 1.5-meter boundary. Don’t encourage movement in progressive or full; bring virtual objects closer instead. In `mixed`, don’t obscure enough passthrough to impair navigation—use `full` or `progressive` when substantial obstruction is required.
- Use ARKit to blend content with surroundings or use hand positions; request permission for sensitive data. See [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) and [`SceneReconstructionProvider`](https://developer.apple.com/documentation/arkit/scenereconstructionprovider).

## Transitions, hands, and environments

- Make immersion changes smooth and predictable so people can track them; avoid sudden transitions. See [`CoordinateSpaceProtocol`](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol) for developer guidance. Use a clear user action to enter or exit, and don’t require system controls to reduce immersion. An exit control must say whether it returns to a less immersive context or quits; Keynote’s prominent Exit button returns from fully immersive Rehearsal to the slide-viewing window. If exiting also quits the app or game, consider controls that pause or return somewhere people can save before quitting.
- When a Full Space app asks permission to replace real hands with virtual hands, **prefer** familiar hand positions and gestures. **Use caution** with oversized hands: they can obscure content, feel clumsy, or seem too close to the face. If hand tracking pauses, fade virtual hands out to reveal real hands, then fade them back when tracking returns.
- When an app transitions to a Full Space, a custom environment may partially or completely replace passthrough. Minimize movement and high-contrast detail around a primary task; **consider** higher-quality assets in focal areas and lower-quality assets or dimming elsewhere. Use proximity to signal which objects are interactive. Keep animation gentle; avoid too much movement near field-of-view edges, and make the environment expansive to avoid claustrophobia.
- Use [Spatial Audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio) for location-based atmosphere, avoid repetitive loops, and lower or stop the soundscape when other audio plays. Generally prefer lit object meshes and shaders for subtle motion over a flat 360° image, which gives little sense of scale. Always provide a ground-plane mesh to prevent floating; add one even when a flat image is unavoidable. Reusing assets too often reduces realism.

## Resources

- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences); [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience); [`ImmersionStyle`](https://developer.apple.com/documentation/swiftui/immersionstyle); [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces)
- [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout); [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Design immersive environments for visionOS apps and the spatial web](https://developer.apple.com/videos/play/wwdc2026/234); [Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072); [Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075)

*Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

Source: [Apple HIG — Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences), captured 2026-09-12.
