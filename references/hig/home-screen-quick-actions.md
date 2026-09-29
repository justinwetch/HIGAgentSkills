---
topic: home-screen-quick-actions
tier: 3
platforms: [ios, ipados]
category: patterns/system
triggers:
  - "quick action"
  - "3D Touch"
  - "long press icon"
  - "UIApplicationShortcutItem"
related:
  - app-icons
  - app-shortcuts
  - menus
---

# Home Screen quick actions

Touching and holding an app icon (or a harder 3D Touch press) shows app-specific actions plus items for removing the app and editing the Home Screen. Each has a title, optional subtitle and an icon placed left or right by the app's Home Screen position; text stays left-aligned in left-to-right languages.

## Best practices

- **Offer compelling, high-value tasks.** People tend to expect every app to offer at least one useful quick action; you can provide four total.
- **Avoid unpredictable changes.** Updating for factors like location, recent activity, time of day or settings may make sense; make sure changes are predictable.
- **Use a short title that states the result**; add a subtitle if you need more context. Keep both short, don't include your app name or extraneous text, and plan for localization.
- **Provide a familiar interface icon, preferably an SF Symbol.** For a custom icon, use the Quick Action Icon Template in Apple Design Resources for iOS and iPadOS.
- **Don't substitute emoji for symbols or icons**; quick action symbols are monochromatic and adapt to Dark Mode.

## Platform considerations

No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS or watchOS.

## Resources

Developer: UIKit, [Add Home Screen quick actions](https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions).

Source: [Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions), captured 2026-09-12.
