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
# Collaboration and sharing

Effective collaboration and sharing are simple and responsive, letting people work with content while communicating. System interfaces and Messages provide familiar entry points: people can drop a document into a Messages conversation or choose a destination in the share sheet.

These features work with CloudKit, iCloud Drive, or custom infrastructure. A custom solution must also support universal links. SharePlay supports real-time activities from each person’s device; see [SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay).

## Best practices

- Put the **Share button** somewhere convenient, such as a toolbar (the Notes example places it beside More). iOS 16’s share sheet lets people choose a file-sharing method and permissions for a new collaboration; iPadOS 16 and macOS 13 provide similar sharing popovers. SwiftUI’s [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink) presents the system share sheet.
- Customize the share sheet or popover only as needed for supported file-sharing types. CloudKit can enable “send copy” by passing both file and collaboration object; iCloud Drive collaboration objects support it by default; custom infrastructure can include a file or plain-text representation in the collaboration object.
- Write short permission summaries such as “Only invited people can edit” or “Everyone can make changes.” The summary button opens customizable sharing options; keep choices few and grouped for quick comprehension. They can specify who has access, whether people edit or read, and whether collaborators can add participants.
- Display the **Collaboration button** as soon as collaboration starts, typically next to Share. It signals that content is shared and identifies who shares it.
- Add custom items to the collaboration popover only when needed. Its top section lists collaborators and communication buttons (Messages or FaceTime), the middle contains custom items, and the bottom has the shared-file management button. Keep custom items essential; Notes, for example, summarizes recent updates and offers buttons for more update information or more activities.
- If useful, rename the modal management button (default: “Manage Shared File”). CloudKit supplies the management view; otherwise create one for changing settings and adding or removing collaborators.
- Consider Messages collaboration event notifications for content or membership changes and participant mentions; include a universal link to the relevant app view via [`SWHighlightEvent`](https://developer.apple.com/documentation/sharedwithyou/swhighlightevent).

## Platform considerations

No additional considerations for iOS, iPadOS, or macOS. Collaboration and sharing aren’t available in tvOS.

### visionOS

In the Shared Space, the system streams the current app window to collaborators by default. If someone moves the app to a Full Space during sharing, the system pauses that stream until the app returns to the Shared Space.

### watchOS

In SwiftUI, use [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink) to present the system share sheet.

## Resources and provenance

- [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views), [Shared with You](https://developer.apple.com/documentation/sharedwithyou), and [Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)
- [Design for Collaboration with Messages](https://developer.apple.com/videos/play/wwdc2022/10015), [Enhance collaboration experiences with Messages](https://developer.apple.com/videos/play/wwdc2022/10095), and [Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093)

Source: [Collaboration and sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing) (captured 2026-09-12).
