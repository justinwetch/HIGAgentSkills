---
topic: file-management
tier: 3
platforms: [ios, ipados, macos, visionos]
category: patterns/data
triggers:
  - "file"
  - "document"
  - "Files app"
  - "DocumentBrowser"
  - "DocumentGroupLaunchScene"
  - "File Provider"
  - "Finder Sync"
  - "Documents"
  - "iCloud Drive"
  - "file picker"
related:
  - icloud
  - drag-and-drop
  - undo-and-redo
---
# File Management

> Document-based apps help people create, edit, and manage files across the system.

**Platforms:** iOS, iPadOS, macOS, visionOS *(tvOS/watchOS: no additional considerations; document browsing is limited or not a typical interface pattern)*

## Creating and Opening Files

- Provide **New** and **Open** menu commands with keyboard shortcuts (iPadOS: shown in Command key shortcut overlay; macOS: in File menu). Always include an Add (+) button.
- Custom file browsers should reflect the familiar platform layout (Finder/Files app conventions). Default to a sensible starting location (Documents, iCloud, last-selected) but allow navigation to the full file system.

## Saving Work

- **Autosave by default** — never require an explicit save action. Save periodically during editing and when closing/switching apps.
- **Hide file extensions by default** — let people show them if desired. Reflect the current choice consistently in all open/save interfaces.

## Quick Look

- Use a **Quick Look viewer** to let people preview files your app can't directly open (attach/interact flows, multi-format apps).
- Implement a **Quick Look generator** for custom file types so Finder, Files app, and Spotlight can show document previews — makes files discoverable system-wide.

## Platform Considerations

### iOS, iPadOS

**Document launcher** (iOS 18 / iPadOS 18+): system-provided full-screen document browser UI with:
- **Title card** — displays app name + 2 app-specific buttons (primary: usually "New Document"; secondary: additional options)
- **Background** — solid color, gradient, or pattern. Avoid complex images that distract from foreground. Accessories (images around title card) can float in front of or behind the card for depth.
- **File browser sheet** — standard Files-style browser + optional custom toolbar controls.

Document launcher guidelines:
- **Assign buttons to most important functions** (e.g., Numbers: "Start Writing" primary, "Choose a Template" secondary).
- **Background must be clearly distinct from accessories and title card** — test across all supported screen sizes and orientations.
- **Accessories must not obscure the app name or either button.**
- **Animate accessories sparingly** — gentle, repeating motions (breathe, sway). No disorienting rapid animations.

**File provider app extension** (for apps that share files with other apps):
- Filter displayed documents to only those appropriate for the importing context (e.g., show only PDFs in a PDF editor).
- Show relevant metadata: modification date, size, local vs. remote.
- Let people pick a destination when exporting or moving (unless single-directory structure).
- **No custom top toolbar** — the hosting modal view already has one; a second toolbar is confusing and wastes space.

### macOS

**Custom file browsers:** only deviate from system open/save dialogs when there's a strong reason. Make custom open dialogs convenient: "open recent", multi-select, filter criteria. Customize the Open button label to match the task (e.g., "Insert").

**Save dialog:** default title is "Untitled"; let people set name, format, and location. Support format selection if the app handles multiple formats. Extend the Save dialog with a custom accessory view for relevant options (e.g., Mail: "Include Attachments" checkbox).

**Finder Sync extension** (for apps syncing local + remote files): display sync-status badges in Finder, provide contextual menu actions (favorite, protect), and custom toolbar buttons (initiate sync).

**Autosave state indicators:**
- When **autosave is OFF** (user preference): show a dot on the window close button and in the Window menu next to the document name when there are unsaved changes. Show a save dialog on close/quit/logout/restart. Append "Edited" to the title bar; remove it as soon as autosave occurs or the user saves.
- When **autosave is ON**: don't show the dot (it implies action is needed). May still append "Edited" to title bar — remove on save.
