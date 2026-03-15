---
topic: keyboards
tier: 3
platforms: [ios, ipados, macos, tvos]
category: patterns/input
triggers:
  - "keyboard"
  - "keyboard shortcut"
  - "hardware keyboard"
  - "key command"
related:
  - text-fields
  - virtual-keyboards
  - focus-and-selection
---
# Keyboards

> Physical keyboards are essential on Mac and commonly used on iPad; they enable text entry, app control, game play, and keyboard shortcuts.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

## Best Practices

- **Support Full Keyboard Access** (iOS, iPadOS, macOS, visionOS) — lets people navigate and activate all UI using only keyboard. Test by enabling it in Settings > Accessibility.
  - iPadOS: support keyboard navigation in text fields, text views, and sidebars. Do NOT support keyboard navigation for controls (buttons, segmented controls, switches) — use Full Keyboard Access for those.
- **Respect standard keyboard shortcuts** — don't repurpose them for custom actions. Only redefine if the action doesn't exist in your app (e.g., a non-text app can reuse ⌘I for Get Info).

## Standard Keyboard Shortcuts (Partial Reference — High-Value Map)

| Shortcut | Action |
|---|---|
| ⌘A | Select all |
| ⌘C | Copy |
| ⌘X | Cut |
| ⌘V | Paste |
| ⌘Z | Undo |
| ⇧⌘Z | Redo |
| ⌘N | New document |
| ⌘O | Open |
| ⌘S | Save |
| ⇧⌘S | Save As / Duplicate |
| ⌘P | Print |
| ⌘W | Close window |
| ⌘Q | Quit app |
| ⌘F | Find |
| ⌘G | Find next |
| ⇧⌘G | Find previous |
| ⌘H | Hide app windows |
| ⌘M | Minimize window |
| ⌘B | Bold |
| ⌘I | Italic |
| ⌘U | Underline |
| ⌘, | App settings/preferences |
| ⌘? | Help menu |
| ⌘Space | Spotlight |
| ⌘Tab | Switch to next recently used app |
| ⌘` | Next open window in frontmost app |
| ⌘= / ⇧⌘= | Increase selection size |
| ⌘- | Decrease selection size |
| Esc | Cancel |
| ⌥⌘Esc | Force Quit dialog |
| ⇧⌘3 | Capture screen to file |
| ⇧⌘4 | Capture selection to file |

## Custom Keyboard Shortcuts

- **Only for the most frequently performed app-specific commands** — too many new shortcuts make an app feel hard to learn.
- **Modifier key conventions:**

| Modifier | Symbol | Usage |
|---|---|---|
| Command | ⌘ | Primary modifier; prefer for custom shortcuts |
| Shift | ⇧ | Secondary; complements a related shortcut |
| Option | ⌥ | Sparingly; for less-common or power features |
| Control | ^ | Avoid — system uses widely for focus, screenshots, etc. |

- **Modifier key order when listing:** Control, Option, Shift, Command.
- **Don't add Shift to indicate the upper character of a two-character key** — just list the character (e.g., ⌘? not ⇧⌘/).
- **Don't extend an existing shortcut for an unrelated command** — e.g., don't use ⇧⌘Z for something other than Redo.
- **Let the system localize and mirror shortcuts** — the system handles keyboard localization and RTL mirroring automatically.
- **TIP:** Some languages use modifier keys to generate characters (e.g., French: ⌥5 = `{`). Safe to use ⌘ as modifier. Avoid additional modifiers with characters not available on all keyboards.

## Platform Considerations

### visionOS

- Keyboard shortcuts appear in a shortcut interface (shown when holding ⌘ on a connected keyboard). Organized like menu bar menus (File, Edit, View, etc.) but flat — no submenus.
- **Write self-descriptive shortcut titles** — without submenu context, each title must convey its action standalone.
- **Connected physical keyboard shows a virtual overlay** — provides typing completion and other controls; the overlay is system-managed.
