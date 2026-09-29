---
topic: searching
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/interaction
triggers:
  - "search"
  - "search bar"
  - "UISearchController"
  - "search results"
  - "filter"
  - "searchSuggestions(_:)"
  - "CSImportExtension"
  - "Core Spotlight"
  - "Quick Look"
related:
  - search-fields
  - tab-bars
  - sidebars
---
# Searching

Search spans devices, apps, and documents/files. In apps, people generally expect a [search field](https://developer.apple.com/design/human-interface-guidelines/search-fields). When it makes sense, personalize with knowledge of app interaction, such as recent terms, suggestions, completions, or corrections based on earlier searches. In some cases, consider scoping/filtering by example attributes such as creation date, file size, or type; you can also provide in-document find in an iOS/iPadOS/macOS window or page.

## Best practices

- Give important search a primary position (Notes’ bottom toolbar; Photos/Apple TV’s dedicated tab).
- Aim for one app-wide location; distinct sections may also need local search (iOS Music filters current songs/albums).
- Show current scope with descriptive placeholder, [scope bar](https://developer.apple.com/design/human-interface-guidelines/search-fields#Scope-bars-and-tokens), or title (Mail keeps the mailbox visible).
- Offer recents before typing or predictive suggestions while typing; [`searchSuggestions(_:)`](https://developer.apple.com/documentation/swiftui/view/searchsuggestions(_:)) configures a view’s suggestions. If showing history, consider privacy and provide a clear-history action.

## Systemwide search

On iOS, iPadOS, and macOS, [Spotlight](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) searches across apps and the web. Index app content with descriptive metadata; Spotlight extracts, stores, and organizes it for fast, comprehensive search without opening the app.

- For custom file types, supply a Spotlight File Importer plug-in describing their metadata; [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension) provides searchable attributes for supported types.
- Use Spotlight for advanced in-app file search: a button might search from the current selection, then show custom results or a filtered subset.
- Prefer system open/save views, which generally include a field to search/filter the entire system; see [File management](https://developer.apple.com/design/human-interface-guidelines/file-management).
- If producing custom file types, implement a [Quick Look](https://developer.apple.com/documentation/quicklook) generator so Spotlight and other apps can preview documents. The Quick Look framework can also create in-app previews or perform simple preview edits.

Platform: no additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Source: [Apple HIG — Searching](https://developer.apple.com/design/human-interface-guidelines/searching), captured 2026-09-12.
