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

> iCloud gives people seamless access to their content across all devices, without explicit syncing. Your app should treat iCloud as transparent and always available.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Opt-in, not opt-out.** Show a simple iCloud on/off choice at first launch if you think people may want to choose — don't prompt again after.
- **Don't ask which documents to keep in iCloud.** Default to syncing everything; automate file management.
- **Keep content up to date.** Always provide the most recent version. For very large documents, indicate when a newer version is available in iCloud and provide subtle download progress feedback after a few seconds.
- **Respect iCloud storage.** Use it only for user-created content — not app resources or regenerable data. Avoid bloating the Documents folder (iCloud backs it up).
- **Handle iCloud unavailability gracefully.** No alert when someone manually disables it or uses Airplane Mode. Unobtrusively note that changes won't appear on other devices until iCloud is restored.
- **Sync app state, not just files.** Use iCloud to remember last-viewed position, preferences that apply across all devices (be selective — some settings are device-specific).
- **Warn before deleting.** iCloud deletion removes the document from all devices — always confirm.
- **Resolve conflicts promptly.** Auto-resolve when possible. If not, show an unobtrusive diff of conflicting versions; resolve early so no time is wasted in the wrong version.
- **Include iCloud content in search results.**
- **Games: save progress to iCloud.** Use the GameSave framework for sync, offline handling, and conflict alerts.
