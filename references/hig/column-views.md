---
topic: column-views
tier: 4
platforms: [macos]
category: components/content
triggers:
  - "column view"
  - "NSBrowser"
  - "Miller columns"
  - "hierarchical browser"
related:
  - lists-and-tables
  - outline-views
  - split-views
---

# Column views

A column view, or *browser*, navigates a data hierarchy through vertical columns: each column is one level of horizontal rows; a parent with children has a triangle, and selecting it opens its children in the next column. People can continue to a childless leaf and move back up to explore other branches. For hierarchical content in iPadOS or visionOS, consider a [split view](https://developer.apple.com/design/human-interface-guidelines/split-views).

## Best practices

Consider a column view for a deep hierarchy that people frequently navigate between levels, when list/table sorting isn’t needed. Finder offers it alongside icon, list, and gallery views for directories.

- Show the root in the first column so people can quickly return to the top.
- When a selected item has no nested items, consider showing a preview and details such as creation date, modification date, file type, and size (as Finder does).
- Let people resize columns, especially when names exceed the default width.

## Platform considerations

Column views aren’t supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

## Resources

- Related: [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views).
- [`NSBrowser`](https://developer.apple.com/documentation/appkit/nsbrowser) (AppKit).

Source: [Apple Human Interface Guidelines — Column views](https://developer.apple.com/design/human-interface-guidelines/column-views) (captured 2026-09-12).
