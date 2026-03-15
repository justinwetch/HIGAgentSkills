---
topic: printing
tier: 4
platforms: [ios, ipados, macos]
category: patterns/system
triggers:
  - "print"
  - "UIPrintInteractionController"
  - "print panel"
  - "NSPrintPanel"
  - "page setup"
related:
  - the-menu-bar
  - file-management
---
# Printing

> Apps can integrate system print functionality, presenting standard or custom print panels when printing makes sense for the content.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS, watchOS)*

## Best Practices

- **Make printing discoverable** — macOS: File menu > Print. iOS/iPadOS: toolbar button opening action sheet. (macOS toolbar print button is optional/customizable.)
- **Show print option only when possible** — if nothing is printable or no printers available: dim the item in macOS menus; remove from iOS action sheet; dim/hide custom print buttons.
- **Show only relevant print options** — page range, copies, duplex (when printer supports them). Use system-provided print view.

## macOS-Specific

- **Custom print categories**: if you have app-specific options the system doesn't provide, create a custom category (named after your app) in the print panel. (e.g., Keynote's presentation notes, backgrounds, skipped slides.)
- **Page setup dialog**: for doc-specific page size/orientation/scaling. Don't duplicate system-provided options (reverse order, orientation changes).
- **Clarify interdependencies** — e.g., if double-sided printing is selected, transparency option becomes unavailable.
- **Separate advanced from common options** — use a disclosure control; label section "Advanced Options."
- **Live previews** — consider updating a thumbnail to show the impact of changed settings.
- **Persist settings with the document** — at minimum, until the document is closed.
