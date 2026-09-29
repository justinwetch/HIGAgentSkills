---
topic: settings
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "settings"
  - "preferences"
  - "configuration"
  - "in-app settings"
  - "Settings app"
related:
  - onboarding
---

# Settings

System Settings handles global appearance, network, accounts, accessibility, language, and region; on some platforms it also handles app/game access to location, microphone, camera, notifications, Siri, and Search. When necessary, add custom settings for general experience options (interface style, game-saving); when possible, keep task-specific options in the affected task.

## Best practices

- Choose defaults that serve most people; for example, optimize a game for its device rather than ask after launch ([Metal guidance](https://developer.apple.com/documentation/metal/improving-your-games-graphics-performance-and-settings)).
- Minimize settings so the app remains approachable and options findable.
- Expose settings where expected: Command–Comma (,) with a physical keyboard; Esc in games.
- Detect setup information when possible (connected controller/accessory, current Dark Mode) instead of asking.
- Honor systemwide settings. Don’t duplicate global accessibility, scrolling, or authentication options; duplicates imply system choices may not apply or the custom change affects other apps.

## Placement

Put general, infrequently changed options in custom settings (window configuration, game-saving, keyboard mappings, accounts), because opening settings suspends the task. Put view visibility, item order, and list filtering on the affected screens for discoverability and context. In games, adapting to a task is usually gameplay. Add only the rarest options to system Settings; consider a button that opens it directly.

There are no additional iOS, iPadOS, tvOS, or visionOS considerations.

### macOS

Choosing Settings from the App menu opens a window, typically a toolbar of related panes. Put Settings in the [App menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu), not a window toolbar; put document options in the [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu). Dim minimize/maximize (Command–Comma opens settings quickly and panes fit their content). Use a visible, noncustomizable toolbar that marks the active button; title the window for its pane, or *App Name Settings* with one pane; restore the last pane.

### watchOS

Apps and games don’t add custom settings to system Settings. Consider a few essential options at the main view’s bottom or in a More menu for reconfiguring objects.

## Resources

- Related: [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- APIs: [SwiftUI Settings](https://developer.apple.com/documentation/swiftui/settings) (scene for viewing/modifying app settings); [UserDefaults / NSUserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) (systemwide and app-specific defaults database); [Preference Panes](https://developer.apple.com/documentation/preferencepanes) (integrate custom preferences into System Preferences).

Source: [Settings](https://developer.apple.com/design/human-interface-guidelines/settings) (captured 2026-09-12).
