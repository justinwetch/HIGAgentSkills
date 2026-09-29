---
topic: toolbars
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/navigation
triggers:
  - "toolbar"
  - "UIToolbar"
  - "NSToolbar"
  - "toolbar item"
  - "toolbar button"
  - "navigation bar"
related:
  - sidebars
  - tab-bars
  - layout
  - buttons
  - search-fields
  - icons
---
# Toolbars

A toolbar gives access to frequent commands, controls, navigation, and search in logical groups along a view’s top or bottom edge. It can contain the view title, navigation/search controls, and button/menu actions; in iOS, a navigation-specific toolbar is sometimes called a navigation bar. A [tab bar](https://developer.apple.com/design/human-interface-guidelines/tab-bars) navigates app areas; a toolbar acts on content.

## Best practices

- Keep items distinguishable and activatable; define what moves to overflow as width narrows. macOS/iPadOS add system overflow when items no longer fit—don’t add one manually or design for default overflow. Add **More** only when needed, putting less important actions there.
- In iPadOS/macOS, consider customization for many, advanced, or long-session actions. Reduce backgrounds/tints that interfere with system effects; let content set appearance and use [`ScrollEdgeEffectStyle`](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) when needed. Prefer monochrome labels against colorful content. Prefer standard buttons, text fields, headers, and footers; custom radii should be concentric with bar corners.
- Consider temporarily hiding toolbars contextually for distraction-free work; if supported, provide a reliable restore path.

## Titles and navigation

Give each window a useful title to confirm location and distinguish windows; you can omit it when content supplies context (Notes omits a single-window note title but titles separate note windows with their first content line). Never use the app name; keep a short title under **15 characters**. The standard Back button retraces an information hierarchy and Close dismisses a modal; prefer their standard symbols without text labels. A custom version should retain the standard appearance, expected behavior, fit with the interface, and consistent implementation throughout the app.

Prioritize commands supporting main tasks—usually those people use most, though some apps may prioritize commands for the highest-level or most important objects. Prefer simple, recognizable symbols except where a symbol is poor (for example, Edit). Prefer system symbols without borders: the section supplies the boundary and system supplies hover/selection states. Use `.prominent` for a key action such as Done/Submit; specify one primary action at the trailing edge.

## Item groupings

Toolbar locations are leading, center, and trailing:

- **Leading:** back/previous-document and sidebar controls, then the view title; a document menu may follow for whole-document commands (Duplicate, Rename, Move, Export). Leading items remain available and aren’t customizable.
- **Center:** common controls, or the title when not leading. On macOS/iPadOS, customizable items can be added, removed, or reordered and collapse into system overflow as the window shrinks.
- **Trailing:** important always-available items, nearby inspectors, optional search, More/customization, and a primary action such as Done. Trailing items remain visible at every window size.

Apple’s own Mac Notes example, however, moves several items—including the trailing More menu—into system overflow when the window is narrow.

Group by function/frequency and consistently across platforms; dedicate distinct groups to navigation/critical actions (Done, Close, Save); generally use no more than **three groups**. Separate text from symbol actions so they don’t appear as one control, and separate multiple text buttons with fixed space via [`UIBarButtonItem.SystemItem.fixedSpace`](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem/fixedspace).

## Platform considerations

**tvOS:** No additional considerations.

**iOS:** Put only essential actions in the main area; use More for the rest. Use a large title to help people stay oriented; by default it becomes standard while scrolling and returns to large at the top. [`prefersLargeTitles`](https://developer.apple.com/documentation/uikit/uinavigationbar/preferslargetitles) controls it.

**iPadOS:** A toolbar and tab bar can share top horizontal space, navigating a few main areas while preserving full window width.

**macOS:** The toolbar sits in the top frame, below or integrated with the title bar; titles can be inline and items have no bezel. Every toolbar item must also be a menu-bar command because people can customize or hide the toolbar; the reverse is unnecessary.

**visionOS:** The system toolbar is along the bottom, above window controls and slightly forward on the z-axis. Variable blur preserves legibility over scrolling content and uniform glass. Supply a symbol or text; looking at a symbol reveals its label. Prefer the system toolbar for familiar eye/hand input and correct placement. Avoid creating a vertical toolbar (tab bars are vertical); try to prevent resizing below toolbar width because visionOS has no app menu bar. Modal states may need contextual controls; reinstate standard controls on exit. Avoid pull-down menus, which can be undiscoverable and obscure controls below the window.

**watchOS:** Buttons may sit in top corners or at the bottom and stay visible above scrolling content. A scrolling-view button is hidden until people scroll up; use it for an important related action that isn’t the app’s primary function (Mail’s New Message in Inbox). SwiftUI: [`topBarLeading`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarleading), [`topBarTrailing`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbartrailing), [`bottomBar`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/bottombar), [`primaryAction`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction).

## Resources

Developer references: [`Toolbars`](https://developer.apple.com/documentation/swiftui/toolbars), [`UIToolbar`](https://developer.apple.com/documentation/uikit/uitoolbar), [`NSToolbar`](https://developer.apple.com/documentation/appkit/nstoolbar), [Apple Design Resources](https://developer.apple.com/design/resources/), [WWDC 2025 design system](https://developer.apple.com/videos/play/wwdc2025/356). Source: [Apple HIG — Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), captured 2026-09-12.
