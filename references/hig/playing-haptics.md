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

# Playing haptics

Haptics add touch-based feedback to visual and auditory feedback. Availability depends on platform and device: supported iPhone controls (switches, sliders, pickers) provide system haptics; Apple Watch’s Taptic Engine combines patterns with an audible tone; Force Touch trackpads can respond to drags/force clicks. Game controllers in iPadOS, macOS, tvOS, and visionOS, Apple Pencil Pro, and some trackpads connected to certain iPad models can also provide haptics.

## Principles

- Use system patterns only for their documented meanings. If a meaning doesn’t fit, use a generic or custom pattern where supported; don’t redefine a recognized pattern.
- Keep a causal, consistent mapping from action to haptic. Match haptic intensity and sharpness to accompanying animation and synchronize sound when useful.
- Avoid frequent or gratuitous haptics; user testing can find a tolerable balance. In most apps prefer short events for discrete actions. Long-running haptics can enhance a gameplay flow, but in an app they can dilute meaning and distract, and can make Apple Pencil Pro less pleasant for writing/drawing.
- Let people mute haptics and keep the experience usable without them. Ensure haptic vibrations don’t disrupt experiences involving the camera, gyroscope, or microphone.

## Custom haptics

Custom patterns can vary with context (a character’s jump from a tree can feel stronger than a jump in place; a collision or hit can differ from footsteps or looming danger). A **transient** is a brief tap/impulse, like tapping the Home Screen Flashlight button; a **continuous** event is a sustained vibration, like the laser effect in Messages. Both support **sharpness** (the intended character, such as soft/organic or crisp/mechanical) and **intensity** (strength). Combine either event type, vary those parameters, and optionally add audio with [`Core Haptics`](https://developer.apple.com/documentation/corehaptics).

## Platform considerations

### iOS

On supported iPhone models, prefer standard toggles, sliders, and pickers for Apple-designed haptics. Where appropriate, [`UIFeedbackGenerator`](https://developer.apple.com/documentation/uikit/uifeedbackgenerator) (an abstract superclass) provides predefined **notification**, **impact**, and **selection** patterns:

|Pattern|Meaning|
|---|---|
|Notification: Success / Warning / Error|Task completed / produced a warning / an error occurred|
|Impact: Light / Medium / Heavy|Collision between small/light, medium, or large/heavy UI objects|
|Impact: Rigid / Soft|Collision between hard/inflexible or soft/flexible UI objects|
|Selection|A UI element’s values are changing|

Impact feedback provides a physical metaphor: a tap when a view snaps into place or a thud when two heavy objects collide.

Success and Warning each use 2 pulses; Error uses 4; each Impact (Light, Medium, Heavy, Rigid, Soft) and Selection uses 1.

### macOS

With a Magic Trackpad, [`NSHapticFeedbackPerformer`](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer) (a protocol) supports these patterns during a drag or force click:

|Pattern|Meaning and example|
|---|---|
|Alignment|Dragged item reaches alignment; also useful for target dimensions/locations or scrubber beginning/end/minimum/maximum|
|Level change|Movement between discrete pressure levels, such as fast-forward speed changes|
|Generic|General feedback when the others don’t apply|

### watchOS

Apple Watch Series 4 and later provides Digital Crown detents. By default, the system supplies linear detents as people rotate the Crown; table views can provide detents as items enter the screen. Use [`WKHapticType`](https://developer.apple.com/documentation/watchkit/wkhaptictype) (an enum) meanings consistently:

|Haptic|Meaning|
|---|---|
|Notification|Something significant or unusual needs attention; also used for local/remote notifications|
|Up / Down|An important value increased above / decreased below a significant threshold|
|Success / Failure / Retry|An action completed successfully / failed / failed but can be retried|
|Start / Stop|An explicitly started activity began / stopped; Stop usually follows Start (for example, a timer)|
|Click|Dial-like progress at predefined increments or intervals; overuse or overlapping clicks confuses and weakens it|

## Resources

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls), [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble)
- [Delivering rich app experiences with haptics](https://developer.apple.com/documentation/corehaptics/delivering-rich-app-experiences-with-haptics), [playing haptics on game controllers](https://developer.apple.com/documentation/corehaptics/playing-haptics-on-game-controllers)
- [*Introducing Core Haptics*](https://developer.apple.com/videos/play/wwdc2019/520), [*Practice audio haptic design*](https://developer.apple.com/videos/play/wwdc2021/10278)

Source: [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) (captured 2026-09-12).
