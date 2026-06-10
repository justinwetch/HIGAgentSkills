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

> Be transparent about privacy-related data and resources, and protect the data people allow the app to access.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Apps must provide privacy-practice and collected-data details for App Store product pages. People use those details before downloading.

## Best Practices

- **Request only data actually needed.** Asking for excess data, or asking before people show interest in a feature, reduces trust. Make permission requests specific.
- **Be transparent about data collection and use.** Explain exactly how the app uses data. Respect system privacy features like Hide My Email and Mail Privacy Protection. Understand app-tracking obligations.
- **Process data on device where possible.** On iOS, use Apple Neural Engine and Create ML models to avoid remote-server round trips when feasible.
- **Use system privacy protections and security best practices.** Example: iOS 15+ CloudKit encryption/key management for data types like strings, numbers, and dates.

## Permission Requests

Request permission for access to:

- Personal data: location, health, financial, contact, and other identifying information.
- User-generated content: emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, audio, video, and photos.
- Protected resources: Bluetooth peripherals, home automation, Wi-Fi connections, local networks.
- Device capabilities: camera, microphone.
- visionOS Full Space ARKit data: hand tracking, plane estimation, image anchoring, world tracking.
- Device advertising identifier for app tracking.

System permission alerts display app-provided copy explaining why access is needed. People can review and change choices in Settings > Privacy.

- **Request permission only when access is clearly needed.** Ideally wait until people use a feature that requires the data/resource.
- **Avoid launch-time permission requests** unless the app cannot function without the data/resource and the reason is obvious.
- **Write a clear purpose string / usage description string.** Use a brief, complete, specific sentence in sentence case. Avoid passive voice. End with a period.

Purpose-string examples:

| Quality | Example | Reason |
|---|---|---|
| Good | "The app records during the night to detect snoring sounds." | Active sentence; explains how and why data is collected. |
| Bad | "Microphone access is needed for a better experience." | Passive and vague. |
| Bad | "Turn on microphone access." | Imperative; no justification. |

Standard alert examples include location, photos, and contacts requests. Button sets vary by resource, e.g. location can include "Allow Once", "Allow While Using App", and "Don't Allow"; Photos can include "Select Photos", "Allow Access to All Photos", and "Don't Allow."

## Pre-Alert Screens

Use a pre-alert screen/window only when current context cannot sufficiently explain why permission is needed. Applies to protected data/resources including camera, microphone, location, contacts, calendar, and tracking.

- **Include only one button** and make clear it opens the system alert.
- Prefer button labels like "Continue" or "Next".
- **Do not use "Allow" or similar terms** for the pre-alert button; it can manipulate people into also choosing Allow in the system alert.
- **Do not include additional actions** such as close or cancel that let people leave without seeing the system alert.

## Tracking Requests

If app tracking begins at launch, display the system-provided alert before collecting tracking data.

- **Never precede the system tracking alert with custom UI that could confuse or mislead people.** Manipulative pre-alerts can cause App Store rejection.
- Prohibited custom-screen designs include:
  - Offering incentives or compensation for granting tracking permission.
  - Withholding functionality/content or making the app unusable until people allow tracking.
  - Mirroring the system alert or using button titles like "Allow" on a pre-alert screen.
  - Showing an image of the standard alert and modifying it.
  - Adding visual cues that draw attention to the system alert's Allow buttons.

## Location Button

iOS, iPadOS, watchOS: Core Location provides a location button that grants temporary location authorization at the moment a task needs it.

- First tap shows a standard alert explaining limited location access and the location indicator.
- After people confirm, tapping the button grants one-time location permission.
- One-time authorization expires when people stop using the app.
- If the app has no authorization status, tapping the button acts like choosing **Allow Once**.
- If people previously chose **While Using the App**, tapping does not change authorization status.

Use the location button for lightweight, specific location sharing, especially when people often choose Allow Once.

Customizable:

- System-provided title, e.g. "Current Location" or "Share My Current Location".
- Filled or outlined location glyph.
- Background color and title/glyph color.
- Corner radius.

Not customizable: other visual attributes. System warns about low contrast or excessive translucency. App remains responsible for fitting text at all accessibility sizes and localizations.

If the system identifies consistent customized-button problems, tapping the button will not grant location access.

Developer guidance: `LocationButton`, `CLLocationButton`.

## Protecting Data

- **Avoid relying solely on passwords.** Prefer passkeys. If passwords remain, require two-factor authentication where possible. Use Face ID, Optic ID, or Touch ID for apps that keep people logged in.
- **Store sensitive information in a keychain.**
- **Never store passwords or secure content in plain-text files**, even with restricted file permissions.
- **Avoid custom authentication schemes.** Prefer passkeys, Sign in with Apple, or Password AutoFill.

## Platform Considerations

### macOS

- Sign apps distributed outside the store with a valid Developer ID.
- Use app sandboxing to protect user data and system resources. Mac App Store apps require sandboxing.
- Do not assume who is signed in; fast user switching means multiple people may be active on the same system.

### visionOS

- Shared Space: ARKit algorithms handle persistence, world mapping, segmentation, matting, and environment lighting by default; ARKit does not send this data to apps in Shared Space.
- To access ARKit APIs, open a Full Space.
- Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require permission.
- User input is private by design. System hover effects for SwiftUI/RealityKit interactive components do not expose where people look before they tap.
- Camera access differs from other platforms: back camera provides blank input and exists only for compatibility; front camera input is available only after permission. Remove or replace iOS/iPadOS camera-dependent features when bringing them to visionOS.

## Developer References

- App privacy details on the App Store
- User privacy and data use
- Requesting access to protected resources
- App Tracking Transparency
- Core Location authorization
- Security / Keychain services
- Local Authentication
- CoreLocationUI `LocationButton` / `CLLocationButton`
