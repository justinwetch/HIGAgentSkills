---
topic: playing-haptics
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "haptic"
  - "haptic feedback"
  - "CoreHaptics"
  - "UIFeedbackGenerator"
  - "NSHapticFeedbackPerformer"
  - "WKHapticType"
  - "taptic engine"
related:
  - feedback
  - gestures
---
# Playing Haptics

> Haptics engage people's sense of touch and reinforce natural cause-and-effect relationships in your app or game.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Support also available from game controllers (iPadOS, macOS, tvOS, visionOS) and Apple Pencil Pro / Force Touch trackpads on compatible iPad models.

## Best Practices

- **Use system haptics with their documented meanings** — people already associate standard haptics with standard controls. Don't use a notification haptic to mean something different.
- **Consistent cause-and-effect** — people learn to associate specific haptic patterns with specific events. Using the same pattern for both a failure and a success outcome is deeply confusing.
- **Harmonize with visual and audio feedback** — match haptic intensity and sharpness to animation intensity. Synchronize sound with haptics.
- **Don't overuse** — haptics can feel right occasionally but tiresome if constant. User test for the right balance. The best haptics are those people notice only when absent.
- **Short haptics for discrete events in apps** — long-running haptics suit gameplay but dilute meaning in apps. Apple Pencil Pro continuous haptics can make holding the pencil unpleasant.
- **Make haptics optional** — users should be able to disable or mute haptics without losing core functionality.
- **Be aware of physical interference** — haptic vibrations can disrupt camera, gyroscope, or microphone use.

## Custom Haptics

Two building blocks:
- **Transient events** — brief, compact (tap/impulse). E.g., Flashlight button on Home Screen.
- **Continuous events** — sustained vibration. E.g., lasers effect in Messages.

Both can be tuned via **sharpness** (waveform character: soft/organic vs. crisp/mechanical) and **intensity** (strength). Combine transient + continuous + optional audio for rich patterns.

## Platform Considerations

### iOS — Feedback Generators

| Category | Use case |
|---|---|
| Notification | Outcome of a task (success, warning, error) |
| Impact | Physical metaphor (snap into place, collision thud) |
| Selection | Value changing in a UI element (picker scrub) |

Also: standard controls (toggles, sliders, pickers) play system haptics automatically.

### macOS — Force Touch Trackpad Patterns

| Pattern | Use |
|---|---|
| Alignment | Dragged item snapping into alignment with another |
| Level change | Moving between discrete pressure levels (e.g., fast-forward speed) |
| Generic | General feedback when alignment/level-change don't apply |

### watchOS

Apple Watch Series 4+: Digital Crown haptic detents (linear taps as you rotate). Table views use row-based detents by default.

watchOS provides a defined set of haptic patterns conveying specific meanings (system-defined; use per their documented purpose).

Pattern names: `Notification`, `Up`, `Down`, `Success`, `Failure`, `Retry`, `Start`, `Stop`, `Click`.
