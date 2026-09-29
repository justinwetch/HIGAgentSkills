---
topic: privacy
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "privacy"
  - "permission request"
  - "permissions"
  - "purpose string"
  - "usage description"
  - "App Tracking Transparency"
  - "tracking request"
  - "pre-alert"
  - "location button"
  - "protected resources"
  - "data collection"
  - "Keychain"
  - "passkeys"
  - "sandbox"
  - "ARKit privacy"
related:
  - entering-data
  - eyes
  - gestures
  - managing-accounts
  - onboarding
  - shareplay
  - sign-in-with-apple
---

# Privacy

Each new or updated app submission must declare your privacy practices and collected data for your App Store product page (editable anytime in App Store Connect).

## Best practices

- **Request access only to data you actually need.** Asking for more, or before people show interest, can undermine trust. Make requests as specific as possible.
- **Be transparent about how your app collects and uses data.** Always respect choices like Hide My Email and Mail Privacy Protection; understand your app-tracking obligations.
- **Process data on the device where possible**, such as with the Apple Neural Engine and custom CreateML models in iOS.
- **Adopt system-defined privacy protections and follow security best practices**, such as CloudKit encryption and key management for additional data types like strings, numbers and dates (iOS 15 and later).

## Requesting permission

Permission is required for, among others: personal data (location, health, financial, contact, identifying info); user content (email, messages, calendar, contacts, gameplay, Apple Music activity, HomeKit data, audio, video, photos); Bluetooth peripherals, home automation, Wi-Fi and local networks; camera; microphone; visionOS Full Space ARKit data; the advertising identifier.

The standard system alert shows your reason for access; people can review it and change their choice in Settings > Privacy.

- **Request permission only when your app clearly needs access.** Ideally, wait until people use a feature that requires it (for location, you can use the location button).
- **Avoid requesting permission at launch unless your app can't function without it**, as a navigation app needs location.
- **Write copy that clearly describes how your app uses what you request.** The alert shows this *purpose string* (*usage description string*) after your app name, before the buttons. Aim for a brief, complete, specific sentence in sentence case, avoiding passive voice, ending with a period.

|Purpose string|Verdict|
|---|---|
|The app records during the night to detect snoring sounds.|Good: active; how and why|
|Microphone access is needed for a better experience.|Bad: passive; vague reason|
|Turn on microphone access.|Bad: imperative; no reason|

### Pre-alert screens

Ideally, context explains the request. If more detail is essential, you can show a custom screen, window or view before a permission or tracking alert (camera, microphone, location, contacts, calendar, tracking).

- **Include only one button, clearly opening the system alert.** Title it with a term like "Continue" or "Next", not "Allow": a button similar in meaning or visual weight to the alert's allow button can make people more likely to allow unintentionally.
- **Don't include additional actions**; for example, no close or cancel option that leaves without showing the alert.

### Tracking requests

To track from launch, you must show the system alert (`AppTrackingTransparency`) before collecting any tracking data.

**Never precede the system alert with a custom screen that could confuse or mislead people.** Such screens are rejected (App Review Guidelines 5.1.1(iv)), including:

- **Incentive.** Don't offer compensation for permission, or withhold functionality or content or make the app unusable until people allow tracking.
- **Imitation request.** Don't mirror the system alert's function or use "Allow" or similar in a button title.
- **Alert image.** Don't show an image of the standard alert and modify it in any way.
- **Alert annotation.** Don't add visual cues that draw attention to the alert's Allow buttons.

## Location button

In iOS, iPadOS and watchOS, Core Location's button (`LocationButton` in SwiftUI, `CLLocationButton`) grants temporary location access when a task needs it.

- The first tap shows a system alert. Afterward, each tap grants one-time permission, expiring when people stop using the app, without reconfirmation.
- With no authorization status, a tap equals *Allow Once*; after *While Using the App*, a tap doesn't change status.
- **Consider the location button for lightweight location sharing in specific features** (tagging a post, finding a store), and when people often grant *Allow Once*.
- **Consider customizing the location button to harmonize with your UI.** You can set only: a system-provided title ("Current Location", "Share My Current Location"), filled or outlined glyph, background and title/glyph colors, and corner radius. Fix system warnings like low contrast or excess translucency, and make text fit untruncated at all accessibility text sizes and in translation.
- If the system finds consistent problems with a customized button, tapping it won't grant location access.

## Protecting data

- **Avoid relying solely on passwords.** Where possible, use passkeys. If you keep passwords, require two-factor authentication. For apps people stay logged in to, add Face ID, Optic ID or Touch ID (`LocalAuthentication`).
- **Store sensitive information in a keychain** (Keychain services).
- **Never store passwords or secure content in plain-text files**, even with restricted permissions.
- **Avoid inventing custom authentication schemes.** Prefer passkeys, Sign in with Apple or Password AutoFill.

## Platform considerations

No additional considerations for iOS, iPadOS, tvOS or watchOS.

### macOS

- **Sign your app with a valid Developer ID** when distributing outside the store.
- **Protect data with app sandboxing**; the Mac App Store requires it.
- **Avoid assuming who is signed in**; fast user switching allows multiple active users.

### visionOS

- ARKit algorithms (persistence, world mapping, segmentation, matting, environment lighting) always run, benefiting Shared Space apps automatically without sending them data. ARKit APIs require a Full Space; features like Plane Estimation, Scene Reconstruction, Image Anchoring and Hand Tracking also need permission.
- Input is private: the system automatically shows hover effects on SwiftUI and RealityKit interactive components without exposing where people look before they tap.
- The back camera provides blank input (compatibility only); the front camera feeds spatial Personas, only with permission. If an iOS or iPadOS app you bring over has a camera-dependent feature, remove it or replace it with content import.

## Resources

Source: [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy), captured 2026-09-12.
