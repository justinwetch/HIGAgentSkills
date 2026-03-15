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
related:
  - search-fields
  - tab-bars
  - sidebars
---
# Searching

> People use search to find content on their device, within an app, or within a document.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Use a search field for in-app search. Personalize results with recent searches, suggestions, completions, and corrections. Allow scope filtering and attribute-based filtering where appropriate (see search-fields for scope controls).

iOS, iPadOS, and macOS: support Find-in-window/page for locating content in open documents.

## Best Practices

- **Make search a primary action if it's important** — give it a dedicated tab bar entry (TV, Photos, Phone apps) or a persistent toolbar search field (Notes). Don't bury it.
- **One search location** — provide a single clearly identified place to find anything in the app. For distinct sections, a local search within a section is acceptable.
- **Use meaningful placeholder text** — indicate what's being searched (e.g., "Shows, Movies, and More").
- **Clearly communicate search scope** — use descriptive placeholder text, scope controls, or a title (e.g., Mail always shows which mailbox is being searched).
- **Provide search suggestions** — show recent searches and suggestions before and during typing to reduce typing effort.
- **Handle privacy for search history** — consider whether others might see it; provide a way to clear it, or offer scope controls instead.

## Systemwide Search (iOS, iPadOS, macOS — Spotlight)

- **Index your content for Spotlight** — make app content findable without opening the app. Provide metadata (descriptive attributes) for indexed content.
- **Define metadata for custom file types** — supply a Spotlight File Importer plug-in describing your file format's metadata.
- **Offer Spotlight-powered in-app file search** — use Spotlight to power advanced file search within your app (e.g., button that initiates Spotlight search based on current selection, displayed in a custom result view).
- **Use system-provided open/save views** — they include a built-in search field covering the whole system.
- **Implement a Quick Look generator** for custom file types — enables Spotlight and other apps to show document previews.

## Platform Considerations

*No additional considerations for any platform.*
