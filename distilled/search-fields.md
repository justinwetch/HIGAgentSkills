---
topic: search-fields
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "search field"
  - "NSSearchField"
  - "SearchBar"
  - "search token"
  - "search suggestion"
related:
  - searching
  - text-fields
---
# Search Fields

> A search field lets people search a collection of content by entering search terms, with optional scope controls and tokens for refining results.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Components: Search icon, Clear button, placeholder text. Optional: scope control (segmented filter), tokens (selectable/editable filter terms).

## Best Practices

- **Descriptive placeholder text** — e.g., "Shows, Movies, and More." Never just "Search."
- **Start searching on each keystroke** — continuous refinement feels more responsive.
- **Suggestions before or during typing** — speeds up search; surface common queries early.
- **Most relevant results first** — minimize scroll to find the right item. Consider categorizing results.
- **Let people filter results** — scope control in the results area.

## Scope Controls and Tokens

- **Scope control** — acts like a segmented control for category filtering. Default to a broader scope; let people narrow it.
- **Token** — visual bubble representing a search term people can select and edit as a unit (e.g., filtering by a specific contact in Mail, filtering by photo type in Messages).
- **Pair tokens with search suggestions** — people may not know which tokens are available.

## Platform Considerations

### iOS

Three entry-point locations:

**Search in a tab bar (trailing tab):**
- **Focused field** — keyboard appears immediately. Best for fast, transient search that returns people to their prior tab after exiting.
- **Unfocused field** — expands the screen for discovery before search begins. Best for content-rich apps (Music, TV) where browsing before searching is valuable.

**Search in a toolbar:**
- **Bottom toolbar** — as an expanded field or a toolbar button (expanded on tap). Best when search is a priority (Settings, Mail, Notes).
- **Top toolbar (navigation bar)** — as a toolbar button that expands into a field. Use when bottom is occupied by a tab bar or when covering bottom content conflicts with primary functionality (e.g., Wallet with pass stack at bottom).

**Search as an inline field:**
- Use when the search's relationship to adjacent content should be visually explicit (filtering within a single view, e.g., Music library).
- Even then, prefer bottom placement. If the bottom is occupied, place inline at the top, above the list it searches, pinned when scrolling.

### iPadOS, macOS

- **Trailing side of toolbar** — global search for most apps with split views or multi-source navigation (Mail, Notes, Voice Memos).
- **Top of sidebar** — for filtering sidebar content/navigation (Settings-style, exposing nested sections).
- **Dedicated search item in sidebar or tab bar** — for apps where browsing and search are tightly coupled (Music, TV): shows suggestions, categories, recent searches all in one area.
  - In dedicated areas: auto-focus the field on navigation. Exception: iPad-only virtual keyboard — leave unfocused to avoid covering the view.
- **Account for window resizing** — search field resizes fluidly on iPad like on Mac. In compact views, ensure search is available where most contextually useful (Notes/Mail: above the content list column).

### tvOS

- Search screen = specialized keyboard + results area below. **Provide suggestions** — people dislike typing on tvOS; recent and popular suggestions minimize keystrokes.

### watchOS

- Tapping the search field shows a full-screen text-input control. App returns to search only after Cancel or Search is tapped.
