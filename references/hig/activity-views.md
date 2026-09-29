---
topic: activity-views
tier: 3
platforms: [ios, ipados, visionos]
category: components/presentation
triggers:
  - "activity view"
  - "share sheet"
  - "UIActivityViewController"
related:
  - sheets
  - popovers
---

# Activity views

An activity view (share sheet, `UIActivityViewController`) offers sharing and actions like Copy and Print. People typically open it with an Action button; it appears as a sheet or popover, depending on device and orientation.

By default, app-specific actions list first; people can edit the list.

## Best practices

- **Avoid duplicating built-in actions**; give similar app-specific ones a custom title ("Print Transaction").
- **Consider a symbol for a custom activity**; center a custom interface icon in about 70x70 px.
- **Keep custom action titles succinct and descriptive**: prefer a single verb or brief verb phrase; avoid company or product names. Long titles wrap and may truncate. Share activity titles (typically company names) appear below the icon.
- **Fit activities to the current context**: you can exclude inapplicable tasks and choose which custom tasks show, but can't reorder system tasks.
- **Use the Share button to display an activity view**; avoid alternative ways to open it.

## Share and action extensions

Extensions work in other apps (share extensions send content to apps and services; action extensions do content-specific tasks in place) and appear in the share sheet in iOS and iPadOS; macOS has no activity view but supports them, showing share extensions via Share buttons and context menus and action extensions via hover over embedded content, toolbar buttons and Finder quick actions.

- **If necessary, create a familiar custom interface**: for share extensions, prefer the system composition view; for action extensions, include your app name. If you need to present an interface, include elements of your app's.
- **Streamline and limit interaction**: aim for a few steps, e.g. posting with a single tap or click.
- **Avoid placing modal views above your extension** (already modal by default); an alert might be necessary.
- **If necessary, provide an image conveying the extension's purpose.** Share extensions automatically use your app icon; for action extensions, prefer a symbol or icon identifying the task.
- **Show long-task progress in your main app**; continue in the background (the view dismisses immediately). You can notify about problems; don't notify just for completion.

## Platform considerations

No additional considerations for iOS, iPadOS or visionOS. Not supported in macOS, tvOS or watchOS.

## Resources

Developer: `UIActivity` (UIKit); App Extension Support (Foundation).

Source: [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views), captured 2026-09-12.
