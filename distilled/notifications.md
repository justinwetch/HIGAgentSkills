---
topic: notifications
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/system
triggers:
  - "notification"
  - "push notification"
  - "banner"
  - "badge"
  - "UNNotification"
related:
  - alerts
  - live-activities
  - privacy
  - settings
  - widgets
---
# Notifications

> A notification gives people timely, high-value information they can understand at a glance.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Requires user permission before sending. People control notification styles, badges, previews, and related settings.

## Anatomy

Depending on platform, notifications can appear as:

- Banner/view on Lock Screen, Home Screen, Home View, or desktop.
- App icon badge.
- Notification Center item.

Direct communication notifications, such as calls and messages, can use a distinct interface with prominent contact images/avatars and group names instead of the app icon.

## Best Practices

- **Be concise and informative.** People enable notifications for quick, valuable updates.
- **Avoid multiple notifications for the same unresolved event.** Repetition fills Notification Center and can make people disable all notifications from the app.
- **Avoid notifications that tell people to perform specific in-app tasks.** If the task can happen without opening the app, use notification actions.
- **Use alerts, not notifications, for errors.**
- **Handle foreground notifications gracefully.** Notifications do not appear when the app is frontmost, but the app still receives the data. Present it subtly, e.g. increment a badge or insert new data in the current view.
- **Avoid sensitive, personal, or confidential content.** Notifications may be visible to others.
- **Represent urgency accurately.** People can turn notifications off; do not use high urgency for low-priority information.

## Content

- **Title:** short and glanceable. Use when it adds context (headline, event name, email subject). Direct communication notifications automatically show the sender name in the title area. For noncommunication notifications, system shows the app name if no title is provided; if only a generic title like "New Document" is possible, let system show app name instead.
- Use title-style capitalization for titles; no ending punctuation.
- Write body content as complete sentences in sentence case with proper punctuation.
- Do not deliberately truncate; system truncates as needed.
- **Do not include app name or icon.** System displays them automatically.
- **Hidden preview placeholder:** when previews are hidden, system shows only the app icon and default title `Notification`. Use `hiddenPreviewsBodyPlaceholder` for minimal body context without private details, e.g. "Friend request", "New comment", "Reminder", "Shipment". Use sentence-style capitalization.
- **Sound:** can supplement notifications. Custom sounds should be short, distinctive, and professionally produced. Do not rely on sound for important information; people may not hear it. Apps cannot programmatically add vibration to alert sounds.

## Notification Actions

Notification detail views can include up to four custom action buttons for tasks people can perform without opening the app.

- Provide beneficial, time-saving actions that make sense in context.
- Use short, title-case labels that describe the result.
- Do not include app name or extraneous information; account for localization.
- Do not provide an action that merely opens the app; tapping the notification already opens related content.
- Prefer nondestructive actions. If destructive, provide enough context and mark destructive so system differentiates it.
- Provide a simple, recognizable SF Symbols icon for each action; system shows it trailing the action title.

## Badging

- Use badges only for unread notification count.
- Do not use badges for unrelated numbers like weather, dates, stock prices, or scores.
- Do not rely on badges as the only way to communicate essential information; people can disable badges.
- Keep badges up to date. Updating count to zero removes related notifications from Notification Center.
- Never mimic a badge with custom UI.

## Platform Considerations

### watchOS

Notification settings from iPhone apply to the same apps on Apple Watch by default. People can manage settings in the Apple Watch app on iPhone or use per-notification options by swiping left on a notification.

Apple Watch notifications have two stages: short look and long look. Notification Center is also available. Supported devices can use double tap to respond.

If the watchOS app has an iPhone companion that supports notifications, watchOS can automatically provide default short-look and long-look interfaces when needed.

**Short looks** appear on wrist raise and disappear on wrist lower.

- Do not use a short look as the only delivery method for critical information.
- Keep privacy in mind; avoid sensitive information in titles.

**Long looks** are scrollable and dismissible by tap or wrist lower.

- Can be static (message + static text/images) or dynamic (full content + more configurable UI).
- At minimum, provide a static interface; prefer dynamic too. Static is fallback when dynamic is unavailable, e.g. no network or iPhone companion unreachable.
- Structure includes sash at top and Dismiss button below all custom buttons.
- Sash displays app icon/name; customize color or use blurred appearance.
- Content background is transparent by default. For system-like look, use white at 18% opacity; otherwise use a brand color.
- Provide up to four custom action buttons below content. System always adds Dismiss.

**Double tap** selects the first nondestructive action. Put the most-used nondestructive action first.

## Developer References

- User Notifications
- User Notifications UI
- `UNNotification`
- `INSendMessageIntent`
- `UNNotificationContentProviding`
- `UNNotificationSound`
- `hiddenPreviewsBodyPlaceholder`
