---
topic: disclosure-controls
tier: 3
platforms: [ios, ipados, macos]
category: components/controls
triggers:
  - "disclosure"
  - "expand collapse"
  - "accordion"
  - "DisclosureGroup"
  - "chevron"
related:
  - lists-and-tables
  - outline-views
---
# Disclosure Controls

> Disclosure controls reveal and hide information or functionality associated with a specific control or view.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

iOS/iPadOS/visionOS: via SwiftUI `DisclosureGroup`.

- **Show essential controls at top; hide advanced details by default** — keeps the interface from overwhelming users upfront.

## Disclosure Triangles

Show/hide information or a list associated with a *view or collection of items* (e.g., Finder folder hierarchy, Keynote advanced export options).

- **Points inward (leading)** when hidden → **points down** when visible. Clicking/tapping toggles.
- **Descriptive label required** — label indicates what's inside: "Advanced Options."

## Disclosure Buttons

Show/hide functionality associated with a *specific control* (e.g., macOS Save sheet: reveals full navigation panel when clicked).

- **Points down** when hidden → **points up** when visible. Clicking/tapping toggles.
- **Place near the content it controls** — users must clearly see the relationship between the button and the expanded content.
- **Max one per view** — multiple disclosure buttons add confusion.
