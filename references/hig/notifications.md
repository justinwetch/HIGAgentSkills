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

A notification gives timely, high-value information understood at a glance. You need permission before sending any; people can revoke it and silence all notifications (except government alerts in some locales).

## Anatomy

By platform: banner or view (Lock Screen, Home Screen, Home View, desktop), app-icon badge, Notification Center item. Communication notifications (calls, messages) can show avatars and group names instead of the app icon.

## Best practices

- **Provide concise, informative notifications.**
- **Avoid sending multiple notifications for the same thing, even if someone hasn't responded.**
- **Avoid telling people to perform specific tasks in your app.** You can offer notification actions for simple tasks instead.
- **Use an alert, not a notification, for errors.**
- **Handle notifications gracefully in the foreground**, where they don't appear but your app gets the data: surface it discoverably but unobtrusively (increment a badge, subtly insert data).
- **Avoid sensitive, personal or confidential information.**

## Content

The title shows at the top: the sender's name for communication notifications, or your app name for an untitled noncommunication notification.

- **Create a short title if it adds context** (headline, event name, email subject), especially for Apple Watch. Rather than a generic title (New Document), it can be better to show the app name. Title-style capitalization, no ending punctuation.
- **Write succinct content**: complete sentences, sentence case, proper punctuation. Don't truncate; the system does.
- **Provide generic text for hidden previews**, when the system shows only your icon and the title *Notification*: sentence-case body text that describes without revealing details ("Friend request") via `hiddenPreviewsBodyPlaceholder`.
- **Avoid including your app name or icon.** The system shows a large app icon at the leading edge, or the sender's contact image badged with your small icon.
- **Consider a sound**, custom or system; a custom one must be short, distinctive and professionally produced. Don't rely on sound for important information. You can't add vibration programmatically (`UNNotificationSound`).

## Notification actions

A customizable detail view holds up to four buttons that act without opening your app (Calendar's Snooze).

- **Provide beneficial, contextual actions**, preferring common time-saving tasks. Labels: short, title case, describing the result, localizable, without app name or extraneous text.
- **Avoid an action that merely opens your app.**
- **Prefer nondestructive actions.** If you must offer a destructive one, give enough context; the system styles actions marked destructive distinctly.
- **Provide a simple, recognizable interface icon for each action**, shown trailing the title; if you use SF Symbols, choose or edit a related symbol.

## Badging

A badge shows the unread-notification count on an app icon, clearing once they're addressed. People can turn badges off.

- **Use a badge only for the unread-notification count**, not other numbers (weather, dates, prices, scores).
- **Don't make badging the only way to communicate essential information.** Always make it easy to find on opening your app.
- **Keep badges up to date** as soon as people open notifications. A zero count removes all related notifications from Notification Center.
- **Avoid custom images or components that mimic a badge.**

## Focus and interruption levels

A Focus filters notifications during an activity; delivery scheduling sends alerts immediately or in scheduled summaries. People choose which contacts, apps and, optionally, all Time Sensitive alerts break through a Focus. A delayed alert's notification is still available on arrival.

Direct communications use *communication* notifications, which require SiriKit intents (`INSendMessageIntent`, `UNNotificationContentProviding`); people can then customize their behavior via Siri. Delivery timing follows the sender. Every other (*noncommunication*) notification needs a system-defined interruption level (`UNNotificationInterruptionLevel`), which helps determine timing.

|Level|Use for|Overrides scheduled delivery|Breaks through Focus|Overrides Ring/Silent (iPhone, iPad)|
|---|---|---|---|---|
|Passive|View at leisure (restaurant recommendation)|No|No|No|
|Active (default)|Worth knowing on arrival (sports score)|No|No|No|
|Time Sensitive|Directly impacts the person, needs immediate attention (account security, package delivery)|Yes|Yes|No|
|Critical|Urgent health and safety; extremely rare, typically governmental and public agencies or health or home apps; requires an entitlement|Yes|Yes|Yes|

- **Represent each notification's urgency accurately**; don't interrupt with low-priority information at high urgency.
- **Use Time Sensitive only for things happening now or within an hour.** The system explains your app's first one, offers to turn it off, and periodically asks people to reevaluate.

## Marketing notifications

- **Don't send marketing or promotional notifications without explicit permission**, requested via an interface describing what you'll send, with clear opt-in or opt-out.
- **Never use Time Sensitive for marketing**; it must never break through Focus or scheduled delivery.
- **You must provide an in-app settings screen** for changing informational and marketing notification choices.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS or visionOS.

### watchOS

Notifications have *short look* and *long look* stages. Design Watch-relevant assets and actions. If the iPhone companion supports notifications, watchOS can provide default looks. iPhone notification settings apply by default; people change them in the Apple Watch app or by swiping left (Mute 1 Hour, Turn off Time Sensitive).

**Short looks** show only while the wrist is raised: a large primary image, title and preview.
- **Avoid using a short look as the only way to communicate important information.**
- **Keep privacy in mind**: basic information only, nothing sensitive in the title.

**Long looks** add detail, scroll by swipe or Digital Crown, and dismiss on tap or wrist lowering. *Static* long looks show the message plus static text and images; *dynamic* ones access full content with more appearance options. You customize the content area; the structure is fixed: a *sash* on top and a Dismiss button at the bottom, below custom buttons.
- **Consider a rich custom long look** so people needn't open your app; you can use SwiftUI Animations, SpriteKit or SceneKit (deprecated).
- **At minimum, provide a static interface; prefer adding a dynamic one.** Static is the fallback (no network, iPhone app unreachable); bundle its resources in advance.
- **Choose a sash background** (the sash shows your icon and name): custom color, or blurred for a photo at the top.
- **Choose a content background color.** Default is transparent; to match system notifications use white at 18% opacity, or a brand color.
- **Provide up to four custom actions below the content.** The notification's type picks which appear. A notification-supporting iPhone companion's registered actionable types configure them.

**Double tap**, on supported devices, runs the first nondestructive action.
- **Keep double tap in mind when ordering actions**; consider putting the most frequent first.

## Resources

Developer: `UserNotifications`, `UserNotificationsUI`.

Source: [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications), [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications), captured 2026-09-12.
