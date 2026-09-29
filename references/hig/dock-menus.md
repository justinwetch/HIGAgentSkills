---
topic: dock-menus
tier: 4
platforms: [macos]
category: components/macos
triggers:
  - "Dock menu"
  - "right-click Dock"
  - "Dock context menu"
  - "applicationDockMenu(_:)"
related:
  - menus
  - home-screen-quick-actions
---
# Dock menus

On macOS, secondary-clicking an app or game icon in the Dock reveals system-provided and custom items. System items vary with whether the app is open; Safari, for example, offers viewing a current window or creating a new window.

## Best practices

- Apply general [menu](https://developer.apple.com/design/human-interface-guidelines/menus) rules: succinct labels and logical organization.
- Offer custom Dock commands elsewhere too (menu-bar menus or main interface), because not everyone uses Dock menus.
- Prefer high-value custom items: list all currently or recently open windows for quick switching; also consider a few actions useful when the app isn’t frontmost or has no open windows, as Mail does with Get New Mail and Compose New Message alongside all open windows.

Dock menus are unsupported in iOS, iPadOS, tvOS, visionOS, and watchOS. iOS/iPadOS instead provide similar system and custom actions through [Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions), revealed by long-pressing an app icon on the Home Screen or in the Dock.

Developer documentation: on `NSApplicationDelegate`, Swift [`applicationDockMenu(_: NSApplication) -> NSMenu?`](<https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:)>); Objective-C `applicationDockMenu:`. It returns the app’s Dock menu.

Source: [Apple HIG — Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus), captured 2026-09-12.
