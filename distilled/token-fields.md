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
# Token Fields

> A token field converts text into selectable, manipulable tokens.

**Platform:** macOS. Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

Token fields are text fields that transform entered text into tokens. Example: Mail address fields convert recipient names into tokens that people can select, reorder, or move to another field.

## Behavior

- Token fields can show suggestions as people type.
- Selecting a suggestion inserts it as a token.
- Individual tokens can include contextual menus with information or editing options.
- Tokens can represent search terms in some contexts; see Search fields.

## Best Practices

- **Add value with a context menu.** People often benefit from token-specific options or information.
- **Consider additional tokenization shortcuts.** By default, entered text becomes a token after a comma. You can add shortcuts such as Return.
- **Consider customizing suggestion delay.** Default suggestions appear immediately; if that distracts while typing, adjust delay to a comfortable level.

## Developer Reference

- `NSTokenField`
