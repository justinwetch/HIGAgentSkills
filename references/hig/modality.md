---
topic: modality
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/interaction
triggers:
  - "modal"
  - "presented view"
  - "dismissal"
  - "swipe to dismiss"
  - "UIModalPresentationStyle"
related:
  - sheets
  - alerts
  - action-sheets
  - popovers
  - activity-views
---
# Modality

Modality presents content in a dedicated mode that blocks the parent view until explicit dismissal. Use it for critical information, confirming/modifying a recent action, a narrowly scoped task, or focus on immersive/complex work. All platforms can present an alert; other context-option components depend on platform. For distinct tasks, iOS/iPadOS/macOS tend to use sheets or popovers; iPadOS/macOS/visionOS may also use a separate window. Other components include activity views and confirmation dialogs/action sheets. Full-screen modals suit temporary media and multistep work such as photo editing or document markup; distinguish them from [nonmodal full-screen experiences](https://developer.apple.com/design/human-interface-guidelines/going-full-screen). In visionOS, a full-screen modal fills the window in Shared Space and can become more immersive in Full Space; see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

## Best practices

- Use modality only when it helps people focus or make choices affecting content/device. Keep modal tasks simple, short, and streamlined.
- Avoid an “app within the app.” If subviews are necessary, provide one path through the hierarchy and avoid buttons that could be mistaken for the modal dismissal control.
- Always provide an obvious, platform-conventional dismissal: iOS/iPadOS/watchOS commonly use a top-toolbar button or swipe down; macOS/tvOS use a button in the main content view.
- If either a dismiss gesture or button could lose user-generated content, get confirmation before closing, explain the risk, and offer resolution (for example, an iOS action sheet with Save).
- Identify the task with a title or explanatory/guidance text so people can regain their place after switching context.
- Let people dismiss a modal before presenting another. Multiple modals add clutter and cognitive load; an alert may appear above other content/modals, but never show more than one alert at once.

Related: [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers), [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets), [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views). APIs: [SwiftUI presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation), [`UIModalPresentationStyle`](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle), [AppKit modal windows/panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels).

Source: [Apple HIG — Modality](https://developer.apple.com/design/human-interface-guidelines/modality), captured 2026-09-12.
