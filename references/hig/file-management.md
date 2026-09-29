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

# File management

Document apps (Pages, Keynote, Photos, Preview) create, edit, save, and browse files. Outside an app, people use Finder on Mac or Files on iPhone, iPad, and Apple Vision Pro; watchOS/tvOS have no document browser.

## Create, open, and save

- In iPadOS/macOS, support familiar New/Open menus and commands (iPadOS shows them while Command is held on hardware keyboard; macOS puts them in File). Always include Add (+); on macOS put it in File.
- If a custom browser is necessary, follow Finder/Files’ file system. It may open at Documents, iCloud, or the last location, but must allow browsing the rest.
- In general, unless canceled or deleted, preserve work with periodic autosave while editing and when closing/switching apps. Hide extensions by default, allow revealing them, and honor the choice in every open/save interface.

## Quick Look

Quick Look can preview/interact with files (listen to audio, mark up photos, rotate/scale 3D). Use its viewer for attachments or files your app cannot open; consider a generator for custom types so Finder, Files, and Spotlight can preview them.

## iOS and iPadOS

Starting in iOS/iPadOS 18, a document app can use the full-screen document launcher via [DocumentGroupLaunchScene](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene), a SwiftUI launch scene for document-based apps. It has a title card (app title plus two app-specific buttons), background with optional *accessories*, and a sheet with file browser/optional app controls. Customize all three; the app name is automatic, while button text/functions, background, accessories, and browser-toolbar controls come from the app. No additional considerations apply to tvOS, visionOS, or watchOS.

- Assign the primary button to the key action (typically new document), secondary to more options.
- Distinguish background from card/accessories with solid color, gradient, or pattern; complex imagery can distract.
- Accessories may sit in front/behind for depth, but keep app name and both buttons visible. Avoid clutter; test supported sizes/orientations.
- Use motion sparingly; prefer gentle repeating breathing/swaying ([Motion](https://developer.apple.com/design/human-interface-guidelines/motion)).

If files are shared, a File Provider extension can import/export/open/move documents. An app extension is installable code extending a specific system area; [FileProvider](https://developer.apple.com/documentation/fileprovider) exposes files and folders managed by the app, including remote-synced storage. In context, list only appropriate documents (a PDF editor lists PDFs), optionally showing modification date, size, and local/remote status. Unless documents use one directory, let people choose an export/move destination in the hierarchy; optionally provide new subdirectories. Don’t add a top toolbar to the modal extension; it already has one. A document browser can give in-app access to local or remote documents from other apps ([Adding a document browser](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app)).

## macOS

Use the default Finder-like browser unless an important reason warrants custom. A custom open interface may add Open Recent, filtering, multiple selection, and task-specific button titles (for example, Insert). Save must allow name, format, and location; new documents start “Untitled,” and the browser can default to a logical location. If formats vary, provide format choice. A Save-dialog accessory can add settings (Mail’s includes attachments).

A Finder Sync extension expresses local/remote sync in Finder ([FinderSync](https://developer.apple.com/documentation/findersync)): status badges, contextual favorite/password-protect actions, and toolbar sync actions.

With autosave off via Desktop & Dock’s “Ask to keep changes when closing documents,” show unsaved state and a save dialog on close, quit, logout, or restart. Use a dot on the close button and beside the Window-menu name. With autosave on, omit dots; they imply required action. Regardless of autosave state, “Edited” may suffix the document title in the title bar; remove it as soon as autosave or explicit save occurs.

## Resources

- Related: [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu), [Printing](https://developer.apple.com/design/human-interface-guidelines/printing)
- APIs: [SwiftUI Documents](https://developer.apple.com/documentation/swiftui/documents); [Build document-based apps in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10039).

Source: [File management](https://developer.apple.com/design/human-interface-guidelines/file-management) (captured 2026-09-12).
