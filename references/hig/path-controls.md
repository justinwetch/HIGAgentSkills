---
topic: path-controls
tier: 4
platforms: [macos]
category: components/controls
triggers:
  - "path control"
  - "NSPathControl"
  - "breadcrumb"
  - "file path"
related:
  - file-management
---
# Path controls

A path control shows a selected file or folder’s file-system path. In Finder, View > Show Path Bar displays one, showing the selected item—or the window folder when nothing is selected. There are two styles.

- **Standard:** A linear list of root disk → parent folders → selected item, each with an icon and name. If too long, it hides names between the first and last items. The Finder example shows four locations.
- **Pop up:** Like a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), it shows the selected icon and name; clicking it opens a menu of root disk, parent folders, and selected item. When editable, its menu adds **Choose**, which selects and displays an item.
- When editable, dragging an item onto either style selects it and displays its path.

Use a path control in the window body, rather than the window frame. It isn’t intended for toolbars or status bars; Finder’s is at the body’s bottom, not in the status bar.

**Platform:** supported in macOS; not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

**Resources:** [File management](https://developer.apple.com/design/human-interface-guidelines/file-management). [`NSPathControl`](https://developer.apple.com/documentation/appkit/nspathcontrol) is an AppKit display of file-system or virtual path information.

Source: [Apple HIG — Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls), captured 2026-09-12.
