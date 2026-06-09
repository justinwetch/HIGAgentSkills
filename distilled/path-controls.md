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
# Path Controls

> A path control shows the file system path of a selected file or folder.

**Platforms:** macOS only

Finder example: View > Show Path Bar shows the path of the selected item (or the window folder if nothing is selected).

## Two Styles

**Standard** — linear list with root disk, parent folders, and selected item. Each item shows icon + name. If the list is too long, names in the middle are hidden. If editable: people can drag an item onto the control to select it and display its path.

**Pop up** — similar to a pop-up button showing the selected item's icon and name. Clicking opens a menu with the full path. If editable: menu includes an additional Choose command; dragging an item also updates the control.

## Best Practices

- **Place in the window body, not the window frame** — path controls are not intended for toolbars or status bars. Finder's path bar is in the window body (bottom), not the status bar.
