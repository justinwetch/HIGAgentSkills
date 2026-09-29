---
topic: keyboards
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: patterns/input
triggers:
  - "keyboard"
  - "keyboard shortcut"
  - "hardware keyboard"
  - "key command"
  - "isFullKeyboardAccessEnabled"
  - "Focus-based navigation"
  - "discoverabilityTitle"
  - "KeyboardShortcut"
  - "UIKeyCommand"
related:
  - text-fields
  - virtual-keyboards
  - entering-data
  - pointing-devices
  - focus-and-selection
---

# Keyboards

Connects to any device except Apple Watch. *Keyboard shortcut*: primary key plus modifiers; a game *key binding* is often one key.

## Best practices

- **Support Full Keyboard Access when possible** (iOS, iPadOS, macOS, visionOS): keyboard-only navigation and activation of windows, menus, controls, system features. Test via Settings > Accessibility. `isFullKeyboardAccessEnabled`.
- iPadOS navigates text fields, text views, sidebars (APIs extend this to collection and custom views), but **avoid keyboard navigation for controls** (buttons, segmented controls, switches); leave controls, all onscreen components and gestures like drag and drop to Full Keyboard Access. `Focus-based navigation`.
- **Respect standard keyboard shortcuts.** For a frequent unique action, prefer a custom shortcut to repurposing a standard. Games: people may expect standards (Command-Q quits) and remappable key bindings ([Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls#Keyboards)).

## Standard keyboard shortcuts

**In general, don't repurpose standard keyboard shortcuts for custom actions.** Only consider it when the standard action doesn't make sense in your experience (no text editing: Command-I could be Get Info).

|Key|Shortcut|Action|
|---|---|---|
|Space|Command-Space|Show/hide Spotlight search field|
||Shift-Command-Space|Varies|
||Option-Command-Space|Show Spotlight results window|
||Control-Command-Space|Show Special Characters window|
|Tab|Shift-Tab|Navigate controls in reverse|
||Command-Tab|Move forward to next most recently used open app|
||Shift-Command-Tab|Move backward through open apps (by recent use)|
||Control-Tab|Focus next control group in a dialog, or next table (when Tab moves to next cell)|
||Control-Shift-Tab|Focus previous control group|
|Esc|Esc|Cancel current action or process|
|Esc|Option-Command-Esc|Open Force Quit dialog|
|Eject|Control-Command-Eject|Quit all apps (after saving open documents) and restart|
||Control-Option-Command-Eject|Quit all apps (after saving open documents) and shut down|
|F1|Control-F1|Toggle full keyboard access|
|F2|Control-F2|Focus menu bar|
|F3|Control-F3|Focus Dock|
|F4|Control-F4|Focus active (or next) window|
||Control-Shift-F4|Focus previously active window|
|F5|Control-F5|Focus toolbar|
||Command-F5|Toggle VoiceOver|
|F6|Control-F6|Focus first (or next) panel|
||Control-Shift-F6|Focus previous panel|
|F7|Control-F7|Temporarily override keyboard access mode in windows and dialogs|
|F8||Varies|
|F9||Varies|
|F10||Varies|
|F11||Show desktop|
|F12||Hide/display Dashboard|
|Grave accent (`)|Command-Grave accent|Activate next open window in frontmost app|
||Shift-Command-Grave accent|Activate previous open window in frontmost app|
||Option-Command-Grave accent|Focus window drawer|
|Hyphen (-)|Command-Hyphen|Decrease selection size|
||Option-Command-Hyphen|Zoom out (screen zooming on)|
|Left bracket ({)|Command-Left bracket|Left-align selection|
|Right bracket (})|Command-Right bracket|Right-align selection|
|Pipe (\|)|Command-Pipe|Center-align selection|
|Colon (:)|Command-Colon|Display Spelling window|
|Semicolon (;)|Command-Semicolon|Find misspelled words|
|Comma (,)|Command-Comma|Open app settings window|
||Control-Option-Command-Comma|Decrease screen contrast|
|Period (.)|Command-Period|Cancel an operation|
||Control-Option-Command-Period|Increase screen contrast|
|Question mark (?)|Command-Question mark|Open app Help menu|
|Forward slash (/)|Option-Command-Forward slash|Toggle font smoothing|
|Equal sign (=)|Shift-Command-Equal sign|Increase selection size|
||Option-Command-Equal sign|Zoom in (screen zooming on)|
|3|Shift-Command-3|Capture screen to file|
||Control-Shift-Command-3|Capture screen to Clipboard|
|4|Shift-Command-4|Capture selection to file|
||Control-Shift-Command-4|Capture selection to Clipboard|
|8|Option-Command-8|Toggle screen zooming|
||Control-Option-Command-8|Invert screen colors|
|A|Command-A|Select all items in document or window, or all text-field characters|
||Shift-Command-A|Deselect all|
|B|Command-B|Bold selected text or toggle bold|
|C|Command-C|Copy selection to Clipboard|
||Shift-Command-C|Display Colors window|
||Option-Command-C|Copy style of selected text|
||Control-Command-C|Copy selection's formatting settings to Clipboard|
|D|Option-Command-D|Show/hide Dock|
||Control-Command-D|Show selected word's definition in Dictionary|
|E|Command-E|Use selection for find|
|F|Command-F|Open Find window|
||Option-Command-F|Jump to search field|
||Control-Command-F|Enter full screen|
|G|Command-G|Find next occurrence of selection|
||Shift-Command-G|Find previous occurrence|
|H|Command-H|Hide current app's windows|
||Option-Command-H|Hide all other apps' windows|
|I|Command-I|Italicize selected text or toggle italic|
||Command-I|Display Info window|
||Option-Command-I|Display inspector window|
|J|Command-J|Scroll to selection|
|M|Command-M|Minimize active window to Dock|
||Option-Command-M|Minimize all active-app windows to Dock|
|N|Command-N|New document|
|O|Command-O|Open-document dialog|
|P|Command-P|Print dialog|
||Shift-Command-P|Page Setup dialog|
|Q|Command-Q|Quit app|
||Shift-Command-Q|Log out current user|
||Option-Shift-Command-Q|Log out current user without confirmation|
|S|Command-S|Save new document or save a version|
||Shift-Command-S|Duplicate active document or Save As|
|T|Command-T|Display Fonts window|
||Option-Command-T|Show/hide toolbar|
|U|Command-U|Underline selected text or toggle underline|
|V|Command-V|Paste at insertion point|
||Shift-Command-V|Paste as (e.g., Paste as Quotation)|
||Option-Command-V|Apply one object's style to selection|
||Option-Shift-Command-V|Paste at insertion point, matching surrounding text style|
||Control-Command-V|Apply formatting settings to selection|
|W|Command-W|Close active window|
||Shift-Command-W|Close file and its windows|
||Option-Command-W|Close all app windows|
|X|Command-X|Cut selection to Clipboard|
|Z|Command-Z|Undo|
||Shift-Command-Z|Redo (when Undo and Redo are separate commands, not a Command-Z toggle)|
|Right arrow|Command-Right arrow|Switch to current Roman-script keyboard layout|
||Shift-Command-Right arrow|Extend selection to next semantic unit (typically line end)|
||Shift-Right arrow|Extend selection one character right|
||Option-Shift-Right arrow|Extend selection to end of current word, then next word|
||Control-Right arrow|Focus another value or cell in a view (e.g., table)|
|Left arrow|Command-Left arrow|Switch to current system-script keyboard layout|
||Shift-Command-Left arrow|Extend selection to previous semantic unit (typically line start)|
||Shift-Left arrow|Extend selection one character left|
||Option-Shift-Left arrow|Extend selection to start of current word, then previous word|
||Control-Left arrow|Focus another value or cell in a view (e.g., table)|
|Up arrow|Shift-Command-Up arrow|Extend selection upward to next semantic unit (typically document start)|
||Shift-Up arrow|Extend selection to line above, nearest character boundary at same horizontal position|
||Option-Shift-Up arrow|Extend selection to start of current paragraph, then next paragraph|
||Control-Up arrow|Focus another value or cell in a view (e.g., table)|
|Down arrow|Shift-Command-Down arrow|Extend selection downward to next semantic unit (typically document end)|
||Shift-Down arrow|Extend selection to line below, nearest character boundary at same horizontal position|
||Option-Shift-Down arrow|Extend selection to end of current paragraph, then next paragraph (includes the terminator, such as Return, in cut, copy and paste)|
||Control-Down arrow|Focus another value or cell in a view (e.g., table)|

Input-source shortcuts (not menu commands):

|Shortcut|Action|
|---|---|
|Control-Space|Toggle current and last input source|
|Control-Option-Space|Next input source in list|
|[Modifier key]-Command-Space|Varies|
|Command-Right arrow|Switch to current Roman-script layout|
|Command-Left arrow|Switch to current system-script layout|

## Custom keyboard shortcuts

- **Define custom keyboard shortcuts for only the most frequently used app-specific commands**; too many make an app hard to learn.
- **Use modifier keys in ways that people expect:** Command-drag moves items as a group; Shift-drag-resize keeps aspect ratio; holding an arrow key moves the selection by the smallest app-defined unit of distance until released.

|Modifier|Symbol|Recommended usage|
|---|---|---|
|Command|⌘|Prefer as main modifier|
|Shift|⇧|Prefer as secondary modifier complementing a related shortcut|
|Option|⌥|Use sparingly, for less-common commands or power features|
|Control|⌃|Avoid; the system uses it widely (focus, screenshots)|

- Command is usually safe; avoid additional modifiers with characters not on all keyboards (French Option-5 types "{"). If you must use a non-Command modifier, prefer alphabetic characters only.
- **List modifier keys in the correct order:** always Control, Option, Shift, Command.
- **Avoid adding Shift to a shortcut that uses the upper character of a two-character key:** Help is Command-Question mark, not Shift-Command-Slash.
- **Let the system localize and mirror your keyboard shortcuts as needed:** it localizes keys per connected keyboard and mirrors shortcuts in right-to-left layouts.
- **Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command** (Shift-Command-Z for a non-undo command).

## Platform considerations

No additional considerations for iOS, iPadOS, macOS or tvOS. Not supported in watchOS.

### visionOS

Holding Command on a connected keyboard shows one view of all menu-bar-style system categories (File, Edit, View), listing only available commands with shortcuts.

- **Write descriptive shortcut titles**; the flat list lacks submenu context. `discoverabilityTitle`.
- **Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game**: the system adds a virtual overlay with typing completion and controls.

## Resources

Developer: `KeyboardShortcut`, `UIKeyCommand`.

Source: [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), captured 2026-09-12.
