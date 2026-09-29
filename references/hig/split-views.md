---
topic: split-views
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/navigation
triggers:
  - "split view"
  - "UISplitViewController"
  - "NavigationSplitView"
  - "master detail"
related:
  - sidebars
  - tab-bars
  - layout
---
# Split views

A split view presents adjacent panes, often several hierarchy levels: selecting an item in the primary pane shows its contents in the secondary, with an optional tertiary pane for further detail. A leading sidebar commonly supplies top-level navigation; rarely, panes supplement a primary view, as in Keynote’s macOS navigator, presenter notes, and inspector around the slide canvas.

## Best practices

- Persistently highlight the current selection in each pane leading to a detail view; the selected appearance explains relationships and preserves orientation.
- Consider [drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop) between panes for moving content.

## Platform considerations

**iOS:** Prefer split views in a regular environment. In compact space, such as iPhone portrait, multiple panes can wrap or truncate content and reduce legibility/interactivity.

**iPadOS:** A split view can have two vertical panes (Mail) or three (Keynote); design for narrow, compact, and intermediate fluid widths so navigation among panes remains logical. [`NavigationSplitView`](https://developer.apple.com/documentation/swiftui/navigationsplitview), [`UISplitViewController`](https://developer.apple.com/documentation/uikit/uisplitviewcontroller).

**macOS:** Panes can be vertical (stacked), horizontal (side by side), or combined; draggable dividers resize them. If panes are resizable, set reasonable minimum/maximum defaults so the divider stays visible. Consider hiding panes when useful for more room or fewer distractions (editing is an example), and provide multiple reveal paths (toolbar button or menu command, including keyboard shortcut). Prefer the **1 pt thin divider**; thicker styles need a specific reason, such as strong linear table rows on both sides making a thin divider hard to distinguish. [`VSplitView`](https://developer.apple.com/documentation/swiftui/vsplitview), [`HSplitView`](https://developer.apple.com/documentation/swiftui/hsplitview), [`NSSplitView.DividerStyle`](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle-swift.enum).

**tvOS:** Choose a balanced split view to filter content: select a category in the primary pane and show results in the secondary. The default width is one-third primary/two-thirds secondary; half-and-half is also available. Use one title above the split view. Consider centering it in the window when the secondary pane is a collection; when it is one important main view, consider placing the title above the primary view to give that content more room.

**visionOS:** Prefer a split view for supplementary information so people stay in context; a new window can confuse navigation/repositioning and complicate view relationships. Use a [sheet](https://developer.apple.com/design/human-interface-guidelines/sheets) for a small information request or simple task that must finish before returning.

**watchOS:** The list or detail view occupies the full screen. On launch, show the most pertinent detail (for example, based on location, time, or recent actions). With multiple detail pages, use a vertical tab view navigated by the Digital Crown; watchOS shows a page indicator beside it with the tab count and current selection.

Source: [Apple HIG — Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), captured 2026-09-12.
