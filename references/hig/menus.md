---
topic: menus
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/presentation
triggers:
  - "menu"
  - "menu item"
  - "pull-down menu"
  - "submenu"
  - "NSMenu"
  - "preferredElementSize"
  - "BreakthroughEffect.automatic"
  - "BreakthroughEffect.subtle"
  - "BreakthroughEffect.prominent"
  - "BreakthroughEffect.none"
related:
  - context-menus
  - pop-up-buttons
  - pull-down-buttons
  - the-menu-bar
---

# Menus

A menu reveals its items (commands, options or states for the current selection or context) when people interact with it. Label and organization guidance applies to all menu types; macOS and iPadOS menu bar menus hold all app commands.

## Labels

- App items can show keyboard commands; game items rarely do.
- **Write clear, succinct labels**, in general a verb or verb phrase for an action (View, Close), in your communication style.
- **Use title-style capitalization**; a game might differ, but generally prefer it.
- **Remove articles (a, an, the).**
- **Show when an item is unavailable**, often dimmed and unresponsive. A menu needs to remain available even if none of its items are.
- **Append an ellipsis (…) when an action needs more input or choices to complete**, typically in another view.

## Icons

- **Represent common actions consistently** with [standard icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons) like Share, Print and Search.
- **Use icons sparingly and with purpose**: for the most common actions and key features, file system locations, connected devices, visual concepts like rotating an image, and user-generated content like folders. Don't display an icon unless one clearly represents the item.
- **Treat items in the same group uniformly:** icons for all or none.

## Organization

- **Prefer listing important or frequently used items first.**
- **Consider grouping logically related items** (Copy, Cut, Paste). Use a separator between groups: a line or gap, depending on platform and menu type.
- **Prefer keeping all related commands in one group, even less important ones** (Paste and Match Style with Paste).
- **Be mindful of menu length**; consider splitting a too-long menu, or you might use a submenu. User-defined or dynamic content (Safari History) can be long and scroll.

## Submenus

A submenu item shows a symbol like a chevron after its label.

- **Use submenus sparingly**; they add complexity and hide items. You might consider one when a term appears in more than two items in a group (Sort by > Date, Score, Time); generally, label it with that term.
- **Limit depth and length**: generally one level; if a submenu has more than about five items, consider a new menu.
- **Make sure a submenu remains available even when its items are unavailable.**
- **Prefer a submenu to indenting items.**

## Toggled items

- **Consider a changeable label describing the current state** (Show Map/Hide Map).
- **Include a verb if a changeable label isn't clear enough**: Turn HDR On, since HDR On could read as a state.
- **If necessary, display both items instead**, with only the applicable one available.
- **Consider a checkmark to show an attribute is in effect.**
- **Consider an item that removes multiple toggled attributes at once**, like Plain.

## In-game menus

- **Let players navigate with the platform's default interaction method** (touch in iOS and iPadOS; direct and indirect gestures in visionOS).
- **Make sure menus remain easy to open and read on all platforms you support.** If scaling to another screen, especially mobile, makes them too small, modify tap target sizes and consider other ways to communicate the content.

## Platform considerations

No additional considerations for macOS, tvOS or watchOS.

### iOS, iPadOS

Layouts (`UIMenu.preferredElementSize`):

|Layout|Top row, above a list|
|---|---|
|Small|4 items, symbol or icon only|
|Medium|3 items, symbol or icon over short label|
|Large (default)|None|

**Choose small or medium when it can help streamline choices.** Consider medium for three important, frequent actions. Use small only for closely related actions that typically appear as a group (Bold, Italic, Underline, Strikethrough), each with a symbol recognizable without a label.

### visionOS

Menus can use the small or large layout, present from 3D content via a SwiftUI view, and extend outside their window.

- **Prefer displaying a menu near the content it controls**; people might miss an item's effect on distant content.
- To keep a menu visible when content occludes it, you can apply `presentationBreakthroughEffect(_:)`. **Prefer `subtle` in most cases**. `automatic` applies `subtle` to a menu overlapping 3D content. You can use `prominent` if showing a menu over the entire scene is important, but it can disrupt the experience and potentially cause discomfort. `none` fully occludes the menu behind 3D content (like in a puzzle game) but may make it hard to see and access.

## Resources

Developer: `Menu` (SwiftUI).

Source: [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), captured 2026-09-12.
