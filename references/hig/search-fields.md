---
topic: search-fields
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "search field"
  - "NSSearchField"
  - "SearchBar"
  - "searchable(text:placement:prompt:)"
  - "UISearchBar"
  - "UISearchTextField"
  - "search token"
  - "search suggestion"
related:
  - searching
  - text-fields
  - token-fields
---
# Search fields

A search field lets people search a collection for entered terms. It is an editable text field with a Search icon, Clear button, and placeholder. Scope bars and tokens can filter or refine it; choose the access pattern according to app goals, layout, content, and navigation. See [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) and [Searching](https://developer.apple.com/design/human-interface-guidelines/searching).

## Shared guidance

- Use placeholder text to state what is searchable, reinforcing scope or content type.
- If possible, search as someone types so results continuously refine and feel responsive.
- Consider recent searches before typing and predictive suggestions while typing; they speed search even when search does not start immediately.
- Put the most relevant results first; categorization can reduce scrolling. Consider a scope bar in the results area for quick filtering.

### Scope bars and tokens

A scope bar filters/adjusts search scope; a token visually encapsulates a selectable, editable search term and filters additional terms. Use scope bars before or after a search for defined categories, starting broad and letting people narrow (for example, Mail from all mailboxes to the current mailbox); the broad default provides context for the full result set. Use tokens for common terms/items (a contact token clarifies a Mail term; a Photos token filters an attribute in Messages). Pair tokens with suggestions when people may not know what tokens exist. See [Scoping a search operation](https://developer.apple.com/documentation/swiftui/scoping-a-search-operation) and [Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields).

## iOS

Search can be a tab-bar tab, a top/bottom-toolbar item, or an inline field. A standard tab matches other tabs and opens a landing page with the field at top; choose it for suggestions, discovery, and exploration, especially rich content (Apple TV uses genres/categories). A separate trailing button-appearance tab focuses the field and opens the keyboard immediately with the field above it; choose it for fast, transient search that returns to the previous tab on exit.

In a bottom toolbar, choose an expanded field or button according to available space; either animates above the keyboard when tapped. You can add it to an existing toolbar or create a search-only bottom toolbar. In a top toolbar/navigation bar, it is a button that animates above the keyboard or to the top when bottom space is unavailable. Place search at the bottom if there’s room; this keeps priority search easy to reach. Place it at the top when bottom content must remain visible or there is no bottom toolbar (Wallet keeps event passes at the bottom for access and glanceable viewing). Use an inline field when adjacency clarifies that it filters one view rather than searches globally—useful with multiple fields or location-dependent scope (Music has a global Search tab and inline library search). Put a top inline field above its list and consider pinning it to the top toolbar while scrolling.

## iPadOS and macOS

Keep placement and behavior consistent when supporting both. For many uses, put search at the trailing side of the toolbar, especially in split views where people search across columns while keeping the selected item visible in detail; also consider it when results appear in detail (Freeform filters boards there). Put search atop a sidebar when filtering navigation/content, exposing nested sections while preserving separation from a rich adjacent detail view (Settings). Use a sidebar/tab-bar search item for a dedicated discovery area with rich suggestions, categories, content, or recent searches (Music and TV), keeping search available across sections; on iPad, place a Search tab at the tab bar’s trailing edge with a distinct background.

In a dedicated area, consider focusing immediately so people find and use the field faster; on iPad with only a virtual keyboard, leave it unfocused to avoid unexpected keyboard coverage. Account for resizing: iPad fields resize fluidly with the window like Mac, while compact iPad views still need a useful entry point (Notes and Mail place search above the content-list column).

## tvOS and watchOS

A tvOS search screen is a specialized keyboard screen: it accepts text and displays results beneath the keyboard in a customizable view, optionally with a scope bar. Order it field and keyboard, then scope bar, then results. People generally want to type little, so provide popular, context-specific, and available recent suggestions. See [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller) and [Using suggested searches with a search controller](https://developer.apple.com/documentation/uikit/using-suggested-searches-with-a-search-controller). On watchOS, tapping the field opens a full-screen text-input control; return to the field only after Cancel or Search.

visionOS has no additional considerations.

Resources: [`searchable(text:placement:prompt:)`](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) marks a view searchable and configures its field; [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) receives search information; [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) displays/edits text and tokens; [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) is optimized for text searches. [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller) manages results from a search bar. Videos: [Design intuitive search experiences](https://developer.apple.com/videos/play/wwdc2026/292), [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356), [Discoverable design](https://developer.apple.com/videos/play/wwdc2021/10126).

Source: [Apple HIG — Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), captured 2026-09-12.
