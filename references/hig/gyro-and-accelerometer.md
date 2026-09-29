---
topic: gyro-and-accelerometer
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "gyroscope"
  - "accelerometer"
  - "motion sensor"
  - "CMMotionManager"
  - "Core Motion"
  - "Getting processed device-motion data"
  - "device tilt"
related:
  - gestures
---
# Gyroscope and accelerometer

On-device gyroscopes and accelerometers provide data about a device’s movement in the physical world. Use it for tangible, real-time motion experiences in iOS, iPadOS, and watchOS apps and games; tvOS apps can use Siri Remote gyroscope data. See [Core Motion](https://developer.apple.com/documentation/coremotion).

## Best practices

- **Use motion data only for a tangible benefit.** For example, a fitness app can give activity or general-health feedback, and a game can enhance gameplay. Don’t gather it simply to have the data.
- **Explain motion-data access.** If the experience needs device motion data, the permission copy must explain why access is needed. The system shows it the first time the app or game requests this data, allowing people to grant or deny access.
- **Outside active gameplay, avoid using accelerometers or gyroscopes for direct interface manipulation.** Motion gestures can be hard to replicate precisely, physically challenging for some people, and may affect battery usage.

No additional platform considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

## Resources

[Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) · [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) — Core Motion: retrieves motion data processed to remove environmental bias, such as gravity · [Measure health with motion (WWDC21)](https://developer.apple.com/videos/play/wwdc2021/10287)

Source: [Apple HIG — Gyroscope and accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer), captured 2026-09-12.
