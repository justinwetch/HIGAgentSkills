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

> Most people appreciate apps that just work, but also want the ability to customize the experience.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Settings can live in three places: the system Settings app, your app's custom settings area, or inline within the task itself.

## Best Practices

- **Choose great defaults** — the best setting is one people never need to change. Auto-detect device capabilities, current appearance mode, and connected accessories.
- **Minimize settings count** — too many settings make the experience feel unapproachable and make individual settings hard to find.
- **Use expected access patterns:**
  - Physical keyboard connected: Command-Comma (,) to open app settings
  - Games: Esc key for settings
- **Don't ask for information you can detect** — controller presence, Dark Mode state, display resolution.
- **Respect systemwide settings** — don't duplicate global options (accessibility, scroll behavior, auth methods) in your own settings. Doing so implies your app might not honor system settings, or that changing yours affects other apps.

## Where to Place Settings

| Type | Where |
|---|---|
| **Rarely changed, general options** | Custom settings area in your app (window config, game-save behavior, keyboard mappings, account options) |
| **Task-specific options** (show/hide view elements, reorder, filter) | Inline within the affected screen — don't make people leave context to adjust |
| **Extremely rarely changed** | System Settings app — provide a direct-link button from within your app |

## Platform Considerations

### macOS

Settings window opened via App menu → Settings item (or Command-Comma):
- Use a **toolbar-based multi-pane layout** — toolbar buttons switch between setting panes.
- **Don't add Settings buttons to the main toolbar** — wastes space for frequently-used commands.
- For document-level options, use the File menu instead.
- **Dim minimize and maximize buttons** in the settings window — it's opened/closed quickly via keyboard; no need to dock or resize it.
- **Non-customizable toolbar, always visible** — settings navigation must be stable and predictable.
- **Window title = active pane name** — if single-pane, title = "App Name Settings".
- **Restore the last-viewed pane** on next open — people frequently return to the same pane.

### watchOS

Apps don't add to the system Settings app on watchOS. Instead, make a small number of essential options available at the **bottom of the main view** or in a **More menu** to reconfigure objects.
