---
topic: controls
tier: 3
platforms: [ios, ipados, macos]
category: components/system-experiences
triggers:
  - "Control Center control"
  - "Lock Screen control"
  - "Action button control"
  - "control widget"
  - "control toggle"
  - "control button"
  - "LockedCameraCapture"
  - "ControlWidgetConfiguration"
related:
  - action-button
  - branding
  - live-activities
  - sf-symbols
  - widgets
---
# Controls

> A control provides quick access to an app feature from Control Center, the Lock Screen, or the Action button.

**Platforms:** iOS, iPadOS, macOS. Not supported in watchOS, tvOS, or visionOS.

A control is a **button** or **toggle**. Control buttons perform an action, link to a specific app area, or launch a locked-device camera experience. Control toggles switch between two states.

People can add controls to Control Center, the Lock Screen, and the Action button.

## Anatomy

Controls contain:

- **Symbol image**: visually represents the control; use SF Symbols or a custom symbol.
- **Title**: describes what the control relates to.
- **Value**: optional state text.

Display varies by location:

| Location | Display |
|---|---|
| Control Center | Symbol; at larger sizes, title and value |
| Lock Screen | Symbol |
| Action button / Dynamic Island | Symbol and value, if present |

## Best Practices

- **Offer controls for high-benefit actions that avoid launching the app.** Example: starting a Live Activity.
- **Update controls** when a person interacts, when an action completes, or remotely through push notification. Contents must reflect current state and in-progress action.
- **Choose a descriptive symbol.** A control may appear without title/value, so the symbol must communicate the action. For toggles, provide both on/off symbols, e.g. `door.garage.open` and `door.garage.closed`.
- **Use symbol animations for state changes.** Toggle: animate between on/off. Button with duration: animate indefinitely while action performs; stop when complete. Developer guidance: Symbols, `SymbolEffect`.
- **Choose a tint color that works with app branding.** System applies tint to toggle symbol in on state and to Action button value/symbol in Dynamic Island.
- **Prompt for required configuration** when people first add a control. People can reconfigure later. Developer guidance: `promptsForUserConfiguration()`.
- **Provide Action button hint text.** System shows hint text when someone presses the Action button; use verbs. Developer guidance: `controlWidgetActionHint(_:)`.
- **Include placeholders** when title/value vary. System displays placeholder in controls gallery and before Action button assignment.
- **Hide sensitive information on locked devices.** Let system redact title/value. If needed, also redact symbol state; system displays the symbol in off state.
- **Require authentication for security-affecting actions.** Example: locking/unlocking a home door or starting a car. Developer guidance: `IntentAuthenticationPolicy`.

## Camera Experiences On Locked Devices

iOS 18+: apps that support camera capture can create a control that launches directly into the app's camera experience while the device is locked.

- For any task beyond capture, require authentication and unlock before completion in the app.
- Use the same camera UI in the app and locked-device camera experience; shared UI makes transition back into the app seamless after capture.
- Provide instructions for adding the control.

Developer guidance: `LockedCameraCapture`.

## Developer APIs

- `ControlWidgetConfiguration`
- `promptsForUserConfiguration()`
- `controlWidgetActionHint(_:)`
- `IntentAuthenticationPolicy`
- `LockedCameraCapture`
- WidgetKit
