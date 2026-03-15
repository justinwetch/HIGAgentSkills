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
  - live-activities
  - widgets
---
# Notifications

> A notification delivers timely, high-value information people can understand at a glance.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Requires user permission before sending. People control notification styles and delivery times in Settings.

**Styles:** banners/views (Lock Screen, Home Screen, Home View, desktop), app icon badges, Notification Center items. Communication notifications (calls, messages) feature prominent contact images/avatars.

## Best Practices

- **Concise and informative** — valuable info delivered succinctly.
- **Don't repeat-notify for the same thing** — multiple notifications for one unresolved event fill Notification Center and may cause people to disable all notifications from your app.
- **Don't tell people to do specific in-app tasks via notification** — they won't remember after dismissing. Use notification actions for simple tasks people can do without opening the app.
- **Errors use alerts, not notifications** — alerts and notifications have distinct purposes; mixing them causes confusion.
- **Handle foreground notifications gracefully** — notifications don't appear when your app is frontmost but your app still receives the data. Present it subtly (increment a badge, insert new data into the current view) without interruption.
- **Avoid sensitive, private, or confidential content** — notifications can be viewed by anyone nearby.

## Content

- **Title:** short, glanceable. Use when it adds context (headline, event name, email subject). If only "New Document" is possible, let the system display your app name instead. Title-style capitalization, no ending punctuation.
- **System shows app name and icon automatically** — don't repeat them in your content.
- **Complete sentences, sentence case, proper punctuation** — never truncate deliberately; the system handles truncation.
- **Hidden preview placeholder text:** when people hide notification previews in Settings, the system shows only your app icon + "Notification". Write body text for `hiddenPreviewsBodyPlaceholder` that provides minimal context without revealing private details: "Friend request", "New comment", "Shipment". Use sentence-style capitalization.
- **Sound:** custom sounds should be short, distinctive, and professionally produced. Don't rely on sound alone for critical information.

## Notification Actions

A notification can include up to 4 action buttons that let people act without opening the app.

- **Only beneficial, time-saving actions** — eliminate the need to open the app.
- **Short, title-case button labels** — clearly describe the result. No app name, no extraneous info. Account for localization.
- **Don't include "Open App" as an action** — tapping the notification already does this.
- **Prefer nondestructive actions** — if destructive, ensure sufficient context. The system visually differentiates destructive actions.
- **Provide an SF Symbols icon for each action** — reinforces meaning; system displays it on the trailing side.

## Badging

- **Badges = unread notification count only** — don't use for non-notification data (weather, dates, stock prices, scores).
- **Keep badges up to date** — refresh immediately when people open the corresponding notifications. Reducing to zero removes all related items from Notification Center.
- **Never mimic a badge with custom UI** — people can disable badges; a custom element that looks like a badge will frustrate those who have done so.

## Platform Considerations

### watchOS

Notifications occur in two stages: *short look* and *long look*. Notification Center also available. Double tap can respond to notifications on supported devices.

**Short looks** *(wrist raise → wrist lower = disappears)*
- Not suitable as the only delivery method for critical info — they're too brief.
- Keep privacy in mind — titles should not include sensitive info.

**Long looks** *(scrollable, dismissible by tap or wrist lower)*
- Can be **static** (message + static text/images) or **dynamic** (full content + more configurability; use SwiftUI animations, SpriteKit, or SceneKit).
- Always provide a static interface (fallback when network/iPhone is unreachable); also provide dynamic when possible.
- **Sash** (top): displays app icon + name. Customize with a color or blurred appearance (blurred looks good behind a photo at the top of the content area).
- **Content area background:** transparent by default. For system-matching look, use white at 18% opacity; otherwise use a brand color.
- **Up to 4 custom action buttons** (system always adds a Dismiss button below all custom buttons).

**Double tap responses**
- Double tap selects the **first nondestructive action** — order your actions with the most-used action first.
