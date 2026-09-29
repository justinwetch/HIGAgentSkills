---
topic: lists-and-tables
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "list"
  - "table"
  - "UITableView"
  - "row"
  - "grouped list"
related:
  - outline-views
  - collections
  - layout
---

# Lists and tables

Lists and tables present data in one or more columns of rows, optionally hierarchical.

## Best practices

- **Prefer text in lists and tables.** For items that vary widely in size, or many images, consider a collection.
- **Let people edit a table when it makes sense**, even just to reorder. In iOS and iPadOS, people must enter edit mode to select table items.
- **Provide appropriate selection feedback.** In general, hierarchy-navigation tables persistently highlight the selected row; option tables often highlight briefly, then add an image like a checkmark.

## Content

- **Keep item text succinct.** For long item text, consider alternatives to over-large rows, like titles only, with content in a detail view.
- **Consider ways to keep clipped text readable in narrow tables**; sometimes a middle ellipsis distinguishes items better.
- **Use descriptive column headings in multicolumn tables**: nouns or short noun phrases, title-style capitalization, no ending punctuation. Give a heading-less single-column table a label or header for context.

## Style

- **Choose a table or list style (`ListStyle`) that coordinates with your data and platform**, like grouped (iOS, iPadOS: headers, footers, extra space between groups), elliptical (watchOS: rows seem to roll off a rounded surface while scrolling) or bordered (macOS: alternating row backgrounds for large tables).
- **Choose a row style that fits the information.** Built-in row styles include `UIListContentConfiguration` for rows, headers and footers in iOS, iPadOS and tvOS.

## Platform considerations

### iOS, iPadOS, visionOS

- **Use an info button (detail disclosure button) only to show more about a row's content**; for drill-down, use a disclosure indicator (`UITableViewCell.AccessoryType.disclosureIndicator`).
- **Avoid a trailing section index** (typically a vertical alphabet) **in a table with trailing controls like disclosure indicators**; people can activate one while using the other.

### macOS

- **When it provides value, let people click a column heading to sort by it**; if the column is already sorted, re-sort in the opposite direction.
- **Let people resize columns.**
- **Consider alternating row colors in a multicolumn table** to help people track values across columns, especially in wide tables.
- **Use an outline view instead of a table view for hierarchical data.**

### tvOS

**Confirm images near a table still look good as a focused row highlights, grows slightly and may round its corners.** Don't add your own masks to round corners.

### watchOS

- **When possible, limit the number of rows.** When people expect a long list, you can show the most relevant items and a way to view more.
- **Constrain detail view length if you want to support vertical page-based navigation** (swiping among rows' detail views); it doesn't work when detail views scroll.

## Resources

Developer: `List`, Tables (SwiftUI), `UITableView`, `NSTableView`.

Source: [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), captured 2026-09-12.
