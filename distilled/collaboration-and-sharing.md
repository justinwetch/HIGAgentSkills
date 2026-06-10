---
topic: collaboration-and-sharing
tier: 3
platforms: [ios, ipados, macos, visionos, watchos]
category: patterns/ux
triggers:
  - "share"
  - "collaboration"
  - "shared document"
  - "invite"
  - "ShareLink"
related:
  - shareplay
  - activity-views
---
# Collaboration and Sharing

> Great collaboration experiences are simple and responsive, letting people engage with content while communicating with others.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

Integration uses the system share sheet, Messages, and the Collaboration button. Works with CloudKit, iCloud Drive, or custom collaboration (custom requires universal links support).

## Best Practices

- **Place the Share button in a toolbar** for easy access. Use the system share sheet (iOS 16+) or sharing popover (iPadOS 16 / macOS 13) — they handle method selection and collaboration permissions.
- **Customize share sheet/popover** for your supported file sharing types if needed. CloudKit: pass both file and collaboration object to the sheet; iCloud Drive: "send copy" is built in; custom: include a file or plain text representation in the collaboration object.
- **Write succinct permission summaries**: "Only invited people can edit", "Everyone can make changes." System uses your text in a button that reveals sharing options.
- **Keep sharing options simple** — who can access, edit vs. read-only, whether collaborators can add others. Minimize choices; group logically.
- **Show the Collaboration button prominently as soon as collaboration starts** (next to the Share button). It reminds people the content is shared and shows who is sharing.
- **Only add essential custom items to the collaboration popover** — the popover has three sections: collaborators + communication (Messages/FaceTime), your custom items, and manage-file button. Don't overwhelm.
- **Customize the "Manage Shared File" button title** if a more specific label fits your app. CloudKit provides the management view; otherwise build your own.
- **Post collaboration event notifications to Messages** — include universal links so people can open the relevant view in your app.

## Platform Considerations

### visionOS

Screen sharing of Shared Space windows is supported by default (streams the current window to collaborators). If an app moves to a Full Space during sharing, the stream pauses for collaborators until it returns to the Shared Space.

### watchOS

Use `ShareLink` in SwiftUI to present the system share sheet.
