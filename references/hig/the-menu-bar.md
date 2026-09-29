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

# The menu bar

On Mac and iPad, the menu bar at the top of the screen shows the top-level menus of your app or game. iPad menus follow the Mac order with similar item sets; iPadOS keyboard shortcuts follow macOS patterns.

## Anatomy

Order, when present: *YourAppName* (a short version of the app name), File, Edit, Format, View, app-specific menus, Window, Help. macOS adds the Apple menu (leading side) and menu bar extras (trailing side).

## Best practices

- **Support the standard menus and their order.** The system implements many standard items (e.g., Edit > Copy for text selected in a standard text field).
- **Disable, don't hide, unavailable items**; always show the same set.
- **Use the system's icons** for actions like Copy, Share and Delete, everywhere ([Standard icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons)).
- **Support standard shortcuts for the standard items you include**; define custom ones only when necessary.
- **Prefer short, one-word menu titles.** Use title-style capitalization for multiword titles.

## App menu

Items for the app or game as a whole; the app name shows in bold. Tables list each menu's typical items in order; "Option -> X": pressing Option changes the item to X.

|Item|Action|Guidance|
|---|---|---|
|About *YourAppName*|Opens the About window (copyright, version)|Prefer a name of 16 characters or fewer; reuse it for Hide and Quit. Don't include a version number.|
|Settings...|Opens your settings window, or your app's page in iPadOS Settings|Only app-level settings; document-specific settings go in the File menu.|
|Optional app-specific items|Custom app-level configuration actions|List after Settings, in the same group.|
|Services (macOS only)|Submenu of system and other-app services for the current context||
|Hide *YourAppName* (macOS only)|Hides the app and its windows, then activates the most recently used app||
|Hide Others (macOS only)|Hides other apps||
|Show All (macOS only)|Shows other apps' windows behind yours||
|Quit *YourAppName*|Option -> Quit and Keep Windows||

**Display the About menu item first**, followed by a separator so it's alone in its group.

## File menu

Manages the app's files or documents. If the app handles no file types, you can rename or eliminate it.

|Item|Action|Guidance|
|---|---|---|
|New *Item*|Creates a document, file or window|Name *Item* for the type created (Calendar: *Event*, *Calendar*).|
|Open|Can open the selected item or present a chooser|Add an ellipsis when people choose in a separate interface.|
|Open Recent|Submenu of recent documents and files, typically with *Clear Menu*|Show recognizable names, not file paths; most recently opened first.|
|Close|Closes the current window or document; Option -> Close All. Close Tab replaces it in tab-based windows.|In tab-based windows, consider adding Close Window.|
|Close Tab|Closes the current tab; Option -> Close Other Tabs||
|Close File|Closes the file and all its windows|Consider it if the app can open multiple views of one file.|
|Save|Saves the current document or file|Autosave periodically as people work. For a new document, prompt for name and location. For multiple formats, prefer a format pop-up menu in the Save sheet.|
|Save All|||
|Duplicate|Duplicates the document, leaving both open; Option -> Save As|Prefer it to Save As, Export, Copy To and Save To.|
|Rename...|||
|Move To...|Prompts for a new document location||
|Export As...|Prompts for name, location and format; the document stays open, the export doesn't open|Reserve for formats your app doesn't typically handle.|
|Revert To|With autosave on, submenu of recent versions and the version browser; the chosen version replaces the document||
|Page Setup...|Panel for printing parameters (paper size, orientation) a document can save|Include for document-specific printing parameters. Global ones (printer name) and frequently changed ones (copies) belong in the Print panel.|
|Print...|Standard Print panel: print, fax, save as PDF||

## Edit menu

Edits content in the current document or text container and handles the Clipboard; useful even in non-document apps.

**Determine whether Find menu items belong in the Edit menu.** For searching files or other objects, the File menu might fit better.

|Item|Action|Guidance|
|---|---|---|
|Undo|Reverses the previous operation|Clarify the target: after a menu command, you can append its title (Undo Paste and Match Style); for text entry, you might append *Typing* (Undo Typing).|
|Redo|Reverses the previous Undo|Clarify the target likewise (Redo Typing).|
|Cut|Moves the selection to the Clipboard, replacing its contents||
|Copy|To the Clipboard||
|Paste|Inserts the Clipboard at the insertion point; contents stay for repeat pastes||
|Paste and Match Style|Pastes, matching surrounding text style||
|Delete|Removes the selection without using the Clipboard|Use Delete, not Erase or Clear.|
|Select All|Highlights all selectable content in the document or text container||
|Find|Submenu: Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection||
|Spelling and Grammar|Submenu: Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically||
|Substitutions|Submenu toggling automatic substitutions while typing: Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement||
|Transformations|Submenu for selected text: Make Uppercase, Make Lowercase, Capitalize||
|Speech|Submenu: Start Speaking, Stop Speaking (reads selected text aloud)||
|Start Dictation|Opens the dictation window; speech becomes text at the insertion point||
|Emoji & Symbols|Opens the Character Viewer to insert emoji, symbols and other characters||

The system automatically adds Start Dictation and Emoji & Symbols at the bottom of the menu.

## Format menu

Adjusts text formatting. You can exclude it if the app doesn't support formatted text editing.

|Item|Submenu for selected text|
|---|---|
|Font|Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style|
|Text|Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler|

## View menu

Customizes the appearance of all app windows; navigating or managing specific windows belongs in the Window menu.

- **Provide a View menu even if it holds only Enter/Exit Full Screen.**
- **Ensure show/hide titles reflect current state**: Show Toolbar while hidden, Hide Toolbar while visible.

|Item|Action|
|---|---|
|Show/Hide Tab Bar|Toggles the tab bar above the body area (tab-based windows)|
|Show All Tabs/Exit Tab Overview|Enters/exits an overview of all open tabs, like Mission Control (tab-based windows)|
|Show/Hide Toolbar|Toggles the toolbar (windows with one)|
|Customize Toolbar|Opens toolbar customization (windows with a toolbar)|
|Show/Hide Sidebar|Toggles the sidebar (windows with one)|
|Enter/Exit Full Screen|Opens the window full screen in a new space (apps with a full-screen experience)|

## App-specific menus

Custom menus go between View and Window.

- **Provide app-specific menus for custom commands**, even ones available elsewhere, infrequent or advanced; the menu bar enables keyboard shortcuts and Full Keyboard Access.
- **Reflect your app's hierarchy as much as possible** (Mail: Mailbox, Message, Format).
- **Aim to order them from most to least general or commonly used.** People tend to expect leading menus to be more specialized.

## Window menu

Navigates, organizes and manages windows; customizing is in View, closing in File.

- **Provide a Window menu even if your app has only one window**, with Minimize and Zoom for Full Keyboard Access.
- **Consider including menu items for showing and hiding panels**; the font and text color panels don't need them, since the Format menu lists them.

|Item|Action|Guidance|
|---|---|---|
|Minimize|Minimizes the active window to the Dock; Option -> Minimize All||
|Zoom|Toggles between a predefined content-fit size and the size people set; Option -> Zoom All|Avoid using Zoom for full screen.|
|Show Previous Tab|Shows the previous tab (tab-based windows)||
|Show Next Tab|Shows the next tab (tab-based windows)||
|Move Tab to New Window|||
|Merge All Windows|Into one tabbed window||
|Enter/Exit Full Screen|Same as View menu|Include here only if the app has no View menu; still provide separate Minimize and Zoom.|
|Bring All to Front|Brings all app windows forward, keeping location, size and layering (like clicking the Dock icon); Option -> Arrange in Front, which tiles them||
|*Name of an open app-specific window*|Brings that window to the front|List open windows alphabetically. Avoid listing panels or other modal views.|

## Help menu

At the trailing end of the menu bar. With the Help Book format, macOS automatically adds a search field at the top. See [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) and `NSHelpManager`.

|Item|Action|Guidance|
|---|---|---|
|Send *YourAppName* Feedback to Apple|Opens Feedback Assistant||
|*YourAppName* Help|Opens Help Book content in the built-in Help Viewer||
|*Additional Item*||Separate from primary help (e.g., registration, release notes) with a separator. Keep the total small; alternatively, consider linking these from your help.|

## Dynamic menu items

A dynamic menu item changes behavior when chosen with a modifier key (Control, Option, Shift or Command). In rare cases, one can make sense.

- **Avoid making one the only way to do a task**; they're hidden by default, so they're best suited as shortcuts to advanced actions.
- **Use them primarily in menu bar menus**; in contextual or Dock menus they're even harder to discover.
- **Require only a single modifier key to reveal one** (`isAlternate`).
- macOS automatically sizes a menu to its widest item, including dynamic items.

## Platform considerations

Not supported in iOS, tvOS, visionOS or watchOS.

### iPadOS

People reveal the menu bar by moving the pointer to, or swiping down from, the top edge; it then occupies the status bar's space.

||iPadOS|macOS|
|---|---|---|
|Visibility|Hidden until revealed|Visible by default|
|Alignment|Centered|Leading side|
|Menu bar extras|Not available|System default and custom|
|Window controls|In the menu bar when the app is full screen|Never in the menu bar|
|Apple menu|Not available|Always available|
|App menu|No About, Services or app-visibility items|Always available|

- **Ensure every function is reachable in your UI**; the menu bar is often hidden in full screen. Always offer alternatives to dynamic menu items, which require a hardware keyboard. Avoid using the menu bar as a catch-all.
- **Reserve Settings for opening your app's page in iPadOS Settings**; put internal-preferences and other custom configuration items beneath it, in the same group.
- **Tab-style navigation: consider a View menu item per tab**, and key bindings for each.
- **Consider grouping items into submenus to save vertical space**, more often than on Mac.

### macOS

You can't modify or remove the Apple menu. When space is constrained, the system prioritizes menus and essential extras and may reduce title spacing, truncating if necessary. In full screen, the menu bar typically hides until people move the pointer to the top.

#### Menu bar extras

A menu bar extra (`MenuBarExtra`) is an icon, opposite the app menus, exposing app functionality while your app runs, even when not frontmost. The system hides extras as needed to make room for app menus, and may hide some if there are too many.

- **Consider a symbol** (custom icon or SF Symbol), in black and clear so the system can tint it for light and dark menu bars and selection. Menu bar height: 24 pt.
- **Display a menu - not a popover - when people click it**, unless the functionality is too complex for a menu.
- **Let people - not your app - decide whether to show it**, typically in settings; consider offering it during setup.
- **Avoid relying on extras being present**; the system hides and shows them regularly, and their location is unpredictable.
- **Consider other access too**, e.g., an always-available Dock menu.

## Resources

Developer: `CommandMenu` (SwiftUI), `NSStatusBar` (AppKit).

Source: [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar), captured 2026-09-12.
