---
topic: icloud
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "iCloud"
  - "CloudKit"
  - "sync"
  - "cross-device"
  - "document sync"
  - "ubiquity"
related:
  - file-management
  - settings
---

# iCloud

iCloud lets people access their content, like photos, videos and documents, from any device without explicit syncing.

## Best practices

- **Make it easy to use your app with iCloud:** people turn it on in Settings and expect apps to work with it automatically. If people might want a choice, offer a simple first-launch option: iCloud for all data or none.
- **Avoid asking which documents to keep in iCloud;** try to automate more file management.
- **Keep content current when possible,** within storage and bandwidth limits. For very large documents, it may be better to let people control downloads and to show when newer versions exist in iCloud. Give subtle feedback for downloads over a few seconds.
- **Respect iCloud storage.** Store information people create and understand; avoid app resources or content you can regenerate. iCloud backups include every app's Documents folder, even if your app doesn't implement iCloud support, so be picky about its contents.
- **Handle iCloud being unavailable** (e.g., turned off, Airplane Mode). You don't need an alert, but unobtrusively noting that changes won't reach other devices until iCloud access is restored may help.
- **Keep app state in iCloud,** like the last page viewed. Make sure synced settings are ones people want on all devices.
- **Show a warning and ask for confirmation before deleting a document:** it's removed from iCloud and all other devices.
- **Make conflict resolution prompt and easy,** ideally as early as possible. To the extent possible, try to resolve conflicts automatically; otherwise, use an unobtrusive notification to differentiate and choose versions.
- **Include iCloud content in search results.**
- **For games, consider saving player progress in iCloud,** such as with `GameSave`, which syncs saves and offers built-in alerts for offline or conflict issues; or use GameSave data in custom UI to resolve them.

## Platform considerations

No additional considerations for any platform.

## Resources

Developer: `CloudKit`

Source: [iCloud](https://developer.apple.com/design/human-interface-guidelines/icloud), captured 2026-09-12.
