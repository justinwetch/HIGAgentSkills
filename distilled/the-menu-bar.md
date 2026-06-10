---
topic: the-menu-bar
tier: 3
platforms: [ipados, macos]
category: components/navigation
triggers:
  - "menu bar"
  - "File menu"
  - "Edit menu"
  - "View menu"
  - "Window menu"
  - "Help menu"
  - "CommandMenu"
  - "MenuBarExtra"
  - "NSStatusBar"
  - "dynamic menu items"
  - "standard keyboard shortcuts"
  - "iPadOS menu bar"
related:
  - menus
  - dock-menus
  - toolbars
  - windows
  - keyboards
---
# The Menu Bar

> The macOS and iPadOS menu bar at the screen top displays top-level app menus. Mac users expect a consistent, discoverable menu structure — it's how they learn what an app can do.

**Platforms:** iPadOS, macOS *(not iOS, tvOS, visionOS, watchOS)*

## Menu Bar Anatomy (order matters)

1. *YourAppName*
2. File
3. Edit
4. Format
5. View
6. App-specific menus (custom, if any)
7. Window
8. Help

macOS also has the Apple menu (leading) and menu bar extras (trailing).

## Best Practices

- **Support all standard menus in standard order.** System often implements functionality for you (e.g., Edit > Copy for text selection).
- **Always show the same menu items** — disable, don't hide. Hidden items are invisible to people learning your app.
- **Use standard system icons** for common actions (Copy, Share, Delete, etc.) — see [icons.md](icons.md).
- **Support standard keyboard shortcuts** for all included menu items.
- **One-word menu titles preferred** — title-style caps if multi-word.

## App Menu

Items apply to the app as a whole, not to any specific document.

| Item | Action | Notes |
|---|---|---|
| About *YourAppName* | Opens About window | ≤16 char name, no version number |
| Settings… | Opens settings | App-level only; doc settings go in File menu |
| *(Custom app-config items)* | Custom actions | After Settings, in same group |
| Services *(macOS only)* | System/other-app services submenu | — |
| Hide *YourAppName* *(macOS only)* | Hides app + windows | Same short name as About |
| Hide Others *(macOS only)* | Hides all other apps | — |
| Show All *(macOS only)* | Shows all other apps | — |
| Quit *YourAppName* | Quits app; Option → Quit and Keep Windows | Same short name as About |

**About** must be first, separated by a divider.

## File Menu

Manage files/documents. Rename or remove if app doesn't handle files.

| Item | Notes |
|---|---|
| New *Item* | Name for the item type (e.g., Event, Calendar) |
| Open | Ellipsis if opens picker |
| Open Recent | Recent files by last-opened order, most recent first; "Clear Menu" at bottom |
| Close | Option → Close All; tab-based → Close Tab |
| Close Tab | Current tab in a tab-based window; Option → Close Other Tabs |
| Close File | Current file and all associated windows |
| Save | Auto-save periodically; no need for constant manual saves |
| Save All | Saves all open documents |
| Duplicate | Prefer over Save As, Export, Copy To — more explicit about file relationship |
| Rename… | — |
| Move To… | — |
| Export As… | For formats your app doesn't natively use; original stays open |
| Revert To | Version browser when autosave is on |
| Page Setup… | Doc-specific print params |
| Print… | Standard Print panel |

## Edit Menu

Content and clipboard operations. Useful even in non-document apps.

| Item | Notes |
|---|---|
| Undo | Append action name (e.g., "Undo Paste and Match Style", "Undo Typing") |
| Redo | Append action name |
| Cut / Copy / Paste | Standard clipboard ops |
| Paste and Match Style | Matches surrounding text style |
| Delete | Not "Erase" or "Clear" — consistent with Delete key |
| Select All | — |
| Find | Submenu: Find, Find and Replace, Find Next/Previous, Use Selection for Find, Jump to Selection |
| Spelling and Grammar | Submenu: Show, Check Now, Check While Typing, Grammar, Correct Automatically |
| Substitutions | Submenu: Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement |
| Transformations | Submenu: Make Uppercase, Make Lowercase, Capitalize |
| Speech | Submenu: Start Speaking, Stop Speaking |
| Start Dictation | *(System adds automatically at bottom)* |
| Emoji & Symbols | *(System adds automatically at bottom)* |

## Format Menu

Exclude if app doesn't support formatted text editing.

| Item | Submenu contents |
|---|---|
| Font | Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy/Paste Style |
| Text | Align Left/Center/Right/Justify, Writing Direction, Show Ruler, Copy/Paste Ruler |

## View Menu

Customizes window appearance. Include even if only supporting full-screen.

- **Show/hide item titles must reflect current state** (if toolbar is hidden → "Show Toolbar"; if visible → "Hide Toolbar").
- Does NOT include window navigation/close commands (those are in Window menu).

| Item | Action |
|---|---|
| Show/Hide Tab Bar | Toggle tab bar |
| Show All Tabs / Exit Tab Overview | Mission Control-like tab overview |
| Show/Hide Toolbar | Toggle toolbar |
| Customize Toolbar | Toolbar item customization |
| Show/Hide Sidebar | Toggle sidebar |
| Enter/Exit Full Screen | Full-screen mode |

## App-Specific Menus

Custom menus go between View and Window. Reflect app hierarchy (e.g., Mail: Mailbox → Message → Format). Order from most to least general.

**Always list commands here** — even if accessible elsewhere. Menu bar = discoverability + keyboard shortcuts + Full Keyboard Access.

## Window Menu

Navigation and management of windows. Provide even with just one window.

| Item | Notes |
|---|---|
| Minimize | Option → Minimize All |
| Zoom | Toggle content-sized vs user-sized. Option → Zoom All. **Not for full-screen** |
| Show Previous / Next Tab | Tab-based navigation |
| Move Tab to New Window | — |
| Merge All Windows | All in one tabbed window |
| Enter/Exit Full Screen | Only if no View menu |
| Bring All to Front | Option → Arrange in Front |
| *(Open windows list)* | Alphabetical, windows only — no panels |

## Help Menu

At trailing end of menu bar. macOS auto-adds search field when using Help Book format.

| Item | Notes |
|---|---|
| Send *YourAppName* Feedback to Apple | Opens Feedback Assistant |
| *YourAppName* Help | Opens Help Viewer (Help Book format) |
| *(Additional items)* | Separate with divider; keep total count small |

## Dynamic Menu Items

Items that change behavior when a modifier key is held (e.g., Minimize → Minimize All with Option).

- Not the **only** way to accomplish the task — they're hidden by default.
- Best in menu bar menus only (not contextual or Dock menus).
- **Single modifier key only** — multi-key combos are awkward and undiscoverable.

## iPadOS vs macOS Differences

| | iPadOS | macOS |
|---|---|---|
| Menu bar visibility | Hidden until revealed (swipe from top or move pointer to top edge) | Always visible |
| Horizontal alignment | Centered | Leading |
| Menu bar extras | Not available | Yes |
| Window controls | In menu bar when full screen | Never in menu bar |
| Apple menu | Not available | Always available |
| App menu | No About, Services, or visibility items | Full |

**iPadOS-specific rules:**
- **All functions must also exist in your app's UI** — menu bar is hidden often.
- Settings menu item → iPadOS Settings page only. Internal preferences = separate item in the same group.
- Tab navigation: consider adding each tab as a View menu item with a key binding.
- Use submenus more liberally — iPad rows are taller, screen is smaller.

## macOS Menu Bar Extras

An icon in the trailing end of the menu bar that persists even when your app isn't frontmost.

- **Use a symbol** (SF Symbol or custom icon) — black + clear shapes, system handles dark/light.
- **Display a menu, not a popover**, when clicked. Exception: complex functionality.
- **Let people decide** whether to show your extra — don't add it automatically.
- **Don't rely on extras being visible** — system hides them when space is tight.
- **Provide alternate access** (e.g., Dock menu) since the extra can always be hidden.
- Menu bar height: **24 pt.**
