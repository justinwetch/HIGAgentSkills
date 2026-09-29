---
topic: tab-views
tier: 4
platforms: [macos, watchos]
category: components/macos
triggers:
  - "tab view"
  - "TabView"
  - "NSTabView"
  - "macOS tab view"
  - "tabbed pane"
  - "watchOS page control"
related:
  - tab-bars
  - segmented-controls
---

# Tab views

A tab view presents closely related content in mutually exclusive panes in one area. Its visual enclosure signals that tabs contain similar or related content. People switch with a tabbed control; controls in each pane must affect only that pane.

## Best practices

- **Label every tab by its pane’s contents.** Prefer nouns or short noun phrases (verbs can fit some contexts), use title-style capitalization, and make contents predictable.
- **Use a tabbed control instead of a pop-up button when feasible.** One click/tap selects and keeps all choices visible; a pop-up takes two actions. It is reasonable when too many panes cannot fit as tabs.
- **Avoid more than six tabs.** More can overwhelm and create layout problems; for six or more, consider a pop-up menu of view options.

## Anatomy

The tabbed control appears centered on the content area’s top edge and may be hidden for programmatic switching. With the tabbed control hidden, the content area can be borderless (solid or transparent), bezeled, or line-bordered. In general, inset it with a window-body margin on all sides for unrelated controls; extending to window edges is unusual.

## Platform considerations

Tab views aren’t supported in iOS, iPadOS, tvOS, or visionOS. On iOS/iPadOS, consider a segmented control for similar functionality.

watchOS presents tab views as pages using [page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls). The indicator beside the Digital Crown enlarges the current dot to signal scrolling within current content and between pages. Use [`TabView`](https://developer.apple.com/documentation/swiftui/tabview).

## Resources

Related: [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls).

API: [`NSTabView`](https://developer.apple.com/documentation/appkit/nstabview) (AppKit tab view).

Source: [Apple Human Interface Guidelines — Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views), captured 2026-09-12.
