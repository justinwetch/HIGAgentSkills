---
topic: digital-crown
tier: 3
platforms: [visionos, watchos]
category: components/watchos
triggers:
  - "Digital Crown"
  - "crown"
  - "haptic detent"
  - "crown input"
  - "WKCrownDelegate"
related:
  - designing-for-watchos
  - gestures
  - feedback
  - action-button
  - immersive-experiences
---

# Digital Crown

The Digital Crown is a hardware input for Apple Vision Pro and Apple Watch. Both use it for system interaction; Apple Watch also exposes Crown input to apps. visionOS apps don’t receive direct information from the Digital Crown.

## Apple Vision Pro

People use the Digital Crown to:

- Adjust volume.
- Adjust immersion in a portal, an Environment, or an app/game running in Full Space; see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).
- Recenter content in front of them.
- Open Accessibility settings.
- Exit an app to Home View.

## Apple Watch

Turning the Crown supplies app input for scrolling, inspecting data, and operating standard or custom controls. Since watchOS 10 it is the primary navigation input: people turn it to view Smart Stack widgets from the watch face, move vertically through Home Screen apps, switch vertically paginated tabs, and scroll list views or variable-height pages. Orient these views vertically and back Crown interactions with corresponding touch interactions.

Apps don’t respond to Crown presses; watchOS reserves them for system functions such as showing Home Screen. Most models provide haptic feedback: default linear **detents** (taps) occur after a fixed rotation distance, while some table views provide detents as new items scroll onto the screen.

- Consider Crown rotation to inspect data when navigation isn’t needed (for example, advancing a selected World Clock location’s time to compare it with the current time).
- Provide visible feedback, such as updating a picker value; otherwise people may assume rotation has no effect.
- Match update speed to rotation speed so values remain precise and selectable.
- Keep default haptics when they fit the context. If haptics are inappropriate—for example, detents conflict with the app’s animation—turn them off. For tables, linear rather than row-based detents may provide a more consistent experience when rows vary greatly in height.

Not supported in iOS, iPadOS, macOS, or tvOS. Related: [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button), and [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences). [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) is a WatchKit protocol for rotation and rotation-stopped notifications.

Source: [Apple Human Interface Guidelines — Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) (captured 2026-09-12).
