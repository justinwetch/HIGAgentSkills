---
topic: activity-views
tier: 3
platforms: [ios, ipados, tvos]
category: components/presentation
triggers:
  - "activity view"
  - "share sheet"
  - "UIActivityViewController"
  - "AirDrop share"
related:
  - collaboration-and-sharing
  - action-sheets
---
# Activity Views (Share Sheet)

> An activity view (share sheet) presents sharing and action tasks people can perform in the current context.

**Platforms:** iOS, iPadOS, visionOS *(not macOS native UI, tvOS, or watchOS)*

Triggered by the Share button while viewing content or after selecting something. Appears as a sheet or popover depending on device and orientation. Displays sharing activities (messaging, AirDrop), system actions (Copy, Print), and app-specific actions. People can customize/reorder which actions appear.

## Best Practices

- **No duplicate system actions** — if the activity view already has Print, don't add your own. If your print action differs (e.g., custom formatting), give it a distinctive title like "Print Transaction."
- **SF Symbols for custom activity icons** — if you create a custom icon, center it in ~70×70px. See icons.
- **Succinct descriptive action title** — verb or brief verb phrase; no company or product name. (Exception: share activity titles show a company name below the icon, which is different from action titles.)
- **Show only contextually appropriate activities** — exclude inapplicable system actions; control which custom actions appear per context.
- **Always use the Share button** — people expect the system share sheet from that button; don't create an alternative entry point.

## Share and Action Extensions

Share and action extensions add custom behaviors visible in other apps:
- **iOS/iPadOS:** appear in the share sheet.
- **macOS:** share via Share button/context menu → Share; actions via pointer hover on embedded content, toolbar buttons, or Finder quick actions.

Extension guidelines:
- **Custom interface should feel familiar** — prefer system composition view for share extensions. For action extensions, include your app name; use UI elements from your app to signal the relationship.
- **Streamline interaction** — complete the task in as few steps as possible (ideally one tap/click).
- **No modal views above your extension** — extension itself is already modal; adding another modal is disruptive.
- **Icon:** share extensions automatically use your app icon. Action extensions need an SF Symbol or interface icon matching the task.
- **Long operations: continue in the background** — activity view dismisses immediately after the task is initiated. Provide status in the main app. Don't send completion notifications; do notify about errors.
