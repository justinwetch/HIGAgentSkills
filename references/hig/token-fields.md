---
topic: token-fields
tier: 4
platforms: [macos]
category: components/controls
triggers:
  - "token field"
  - "NSTokenField"
  - "recipient token"
  - "address token"
  - "search token"
  - "token suggestions"
related:
  - context-menus
  - search-fields
  - searching
  - text-fields
---
# Token fields

A token field converts text into easily selected and manipulated tokens.

Mail uses token fields in compose-window address fields: entered recipient names become tokens that people can select and drag to reorder or move to another field. A token field can show suggestions while typing; selecting a suggested Mail recipient inserts it as a token.

Tokens can also represent search terms in some situations; see [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

- Add value with a [context menu](https://developer.apple.com/design/human-interface-guidelines/context-menus) offering token information or editing options; in Mail, a recipient-token menu can edit the name, mark it as a VIP, view its contact card, and more.
- **Consider** additional conversion triggers. By default, text becomes a token when people type a comma; you can specify shortcuts such as Return.
- Suggestions appear immediately by default and can distract while typing; if your app suggests tokens, consider a more comfortable delay.

**Platform:** supported in macOS; not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

**Resources:** [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields), [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), and [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus). [`NSTokenField`](https://developer.apple.com/documentation/appkit/nstokenfield) is an AppKit text field converting text into visually distinct tokens.

Source: [Apple HIG — Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields), captured 2026-09-12.
