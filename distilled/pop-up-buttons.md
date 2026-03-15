---
topic: pop-up-buttons
tier: 3
platforms: [ios, ipados, macos]
category: components/controls
triggers:
  - "pop-up button"
  - "drop-down selection"
  - "NSPopUpButton"
  - "menu selection button"
related:
  - pickers
  - menus
  - pull-down-buttons
---
# Pop-Up Buttons

> A pop-up button displays a menu of mutually exclusive options; after selection, the button updates to show the chosen item.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

**Pop-up vs. pull-down:** use pop-up for *selecting a state from mutually exclusive options*. Use pull-down-buttons for performing *actions*, allowing *multi-select*, or including *submenus*.

## Best Practices

- **Flat list of mutually exclusive options** — not for actions or multi-select.
- **Provide a useful default** — the default shows before any selection is made; choose what most people are likely to want.
- **Help people predict the options without opening** — use an introductory label or button label that describes the button's effect.
- **Space-efficient for wide arrays of choices** — good when space is limited and showing all options simultaneously is impractical.
- **Custom option** — include if some users occasionally need items not in the standard list. Offer explanatory text below the list to clarify options.

## Platform Considerations

### iPadOS

- **Use a pop-up button instead of a disclosure indicator** inside a popover or modal view when presenting multiple options for a list item — lets people choose from a menu without navigating to a detail view. Best for small, well-defined option sets.
