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

A control is a button or toggle giving quick access to app features from Control Center, the Lock Screen or the Action button. Buttons perform an action, open a specific app area or launch a locked-device camera experience; toggles switch between two states. People add them via Control Center, Lock Screen customization or Action button settings.

## Anatomy

A symbol (SF Symbols or custom) shows what the control does, a title what it relates to, and an optional value its state. Control Center shows the symbol, plus title and value at larger sizes; the Lock Screen, the symbol; on iPhone, holding the Action button shows the symbol and any value in the Dynamic Island.

## Best practices

- **Offer controls for actions that benefit most from not launching your app**, like starting a Live Activity.
- **Update controls on interaction, on action completion or remotely via push notification**, showing current and in-progress state.
- **Choose a symbol that suggests the behavior**; some placements omit title and value. Give toggles on and off symbols.
- **Use symbol animations for state changes**: toggles between on and off; buttons whose actions have a duration, indefinitely until the action completes (`SymbolEffect`).
- **Select a tint that works with your brand.** The system applies it to a toggle's on-state symbol and to the Action button's Dynamic Island display.
- **Help people provide information the system needs**, like which light to control. Prompt for required configuration when people first add the control; they can reconfigure anytime (`promptsForUserConfiguration()`).
- **Provide Action button hint text using verbs** ("Hold for Silent"), shown on press (`controlWidgetActionHint(_:)`); press-and-hold performs the configured action.
- **If the title or value can vary, include a placeholder**, shown in the controls gallery and before Action button assignment.
- **Hide sensitive information when the device is locked.** Consider having the system redact the title and value to hide personal or security-related information; if you also specify symbol-state redaction, the symbol shows its off state.
- **Require authentication for actions that affect security**, like locking or unlocking a house door or starting a car (`IntentAuthenticationPolicy`).

## Camera experiences on a locked device

Starting with iOS 18, an app that supports camera capture can offer a control that launches directly to its camera experience on a locked device (`LockedCameraCapture`). Tasks beyond capture require authenticating and unlocking.

- **Use the same camera UI in your app and camera experience.**
- **Provide instructions for adding the control.**

## Platform considerations

No additional considerations for iOS, iPadOS or macOS.

Not supported in watchOS, tvOS or visionOS.

## Resources

Developer: `WidgetKit`, `Symbols`

Source: [Controls](https://developer.apple.com/design/human-interface-guidelines/controls), captured 2026-09-12.
