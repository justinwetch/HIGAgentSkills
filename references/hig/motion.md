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
  - accessibility
  - spatial-layout
  - immersive-experiences
  - playing-haptics
  - playing-audio
---
# Motion

Fluid motion can convey status, feedback, and instruction. System components provide familiar motion and may adapt it to accessibility settings or input method (for example, Liquid Glass is more tactile with direct touch and more subdued with a trackpad).

## Best practices

- Add motion purposefully; gratuitous or excessive animation distracts and can cause physical discomfort. Make motion optional: never make it the only way to communicate important information; supplement it with haptics and audio.
- In nongame apps, make feedback realistic and consistent with gestures and expectations. Keep feedback animations brief and precise. In apps, generally avoid animation on frequently repeated custom interactions. As much as possible, let people cancel animations rather than wait for completion. Consider animated SF Symbols or custom symbols where useful; SF Symbols 5+ supports them. See [Animations](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations).
- Make sure a game’s motion looks great by default on each supported platform using the device’s graphics capabilities. In most games, a consistent **30–60 fps** typically gives smooth, visually appealing motion. Let people customize visual quality for performance or battery life, such as power modes when external power is detected.

### Platform considerations

**iOS, iPadOS, macOS, tvOS:** No additional considerations.

**visionOS:** Motion can combine with depth to communicate context and identify looked-at interactive elements, but can distract, confuse, or cause discomfort. Avoid motion at the edges of the field of view; if peripheral motion is necessary in an immersive experience, match its brightness to surrounding content. For large virtual objects that occlude most or all passthrough, increase translucency or lower contrast; people can still feel discomfort when moving the object themselves, so also consider keeping windows fairly small. Consider fading an object out before relocating it, then fading it back in, when its travel communicates nothing. In general, avoid letting people rotate a virtual world, even with subtle user-controlled rotation; consider an instantaneous directional change during a quick fade-out. A stationary frame of reference helps contain motion. Avoid sustained oscillation, especially around **0.2 Hz**; if oscillation is needed, keep amplitude low and consider translucency.

**watchOS:** SwiftUI provides a streamlined way to add motion. If you need WatchKit for layout/appearance animation or animated image sequences, see [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage). Layout- and appearance-based animations include built-in easing at start and end; easing can’t be turned off or customized.

See [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions).

Source: [Apple HIG — Motion](https://developer.apple.com/design/human-interface-guidelines/motion), captured 2026-09-12.
