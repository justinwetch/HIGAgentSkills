---
topic: mac-catalyst
tier: 3
platforms: [ipados, macos]
category: platforms
triggers:
  - "Mac Catalyst"
  - "Catalyst"
  - "iPad app on Mac"
  - "scaled idiom"
  - "Mac idiom"
related:
  - designing-for-macos
---

# Mac Catalyst

Mac Catalyst creates a Mac version of an iPad app.

## Before you start

Good candidates already work well on iPad and support features such as drag and drop and multiple scenes (these carry over, the latter as multiple windows), keyboard navigation and shortcuts (Mac users expect both), and Split View, Slide Over and Picture in Picture (groundwork for extensive Mac window resizing).

An app might not suit the Mac if its essential features require capabilities like gyroscope, accelerometer or rear camera, frameworks like HealthKit or ARKit, or its primary function is something like marking, handwriting or navigation.

Automatic macOS support includes features such as pointer and keyboard focus and navigation, window management, toolbars, rich text copy, paste and contextual editing menus, file management, menu bar menus and Settings app settings. System elements such as split view, file browser, activity view, form sheet, contextual actions and color picker look more Mac-like.

## Choose an idiom

- **iPad idiom** ("Scale Interface to Match iPad", the Xcode default) fits macOS without significant layout changes but scales views and text to 77% (17 pt becomes 13 pt), so they may look slightly less detailed.
- **Mac idiom** renders at 100%: more detailed text and artwork, some elements more Mac-like, and possibly better performance and lower power use for graphics-intensive apps.

**Once your app feels at home in the iPad idiom, consider the Mac idiom**, most likely to benefit apps with a lot of text, detailed artwork or animations. When you adopt it:

- **Thoroughly audit your layout and plan to change it**; unscaled elements report different metrics, often meaning significant extra work. Consider a separate Mac asset catalog.
- **Adjust font sizes as needed**; 100% text can look too large. When possible, use text styles. Avoid fixed font, view or layout sizes.
- **Make sure views and images look good.**

**Limit appearance customizations to standard macOS ones similar to iPadOS ones**; not all iPadOS control customizations exist in macOS.

## Integrate the Mac experience

Regardless of idiom, it's essential to go beyond showing your iPadOS layout in a macOS window.

### Navigation

- **If your iPad app uses a tab bar, consider a split view with a sidebar or a segmented control.** In general, a split view works better; a sidebar lists top-level items that can disclose children and holds each tab's contents, and a sidebar on iPad too keeps layouts consistent. A segmented control can work well on the Mac if the app uses a flat navigation hierarchy.
- **Make sure people retain access to important tab-bar items**: either way, list top-level items in the View menu.
- **Offer multiple ways to move between pages**, such as Next and Previous buttons in addition to swipe gestures, especially for pointer-only or keyboard-only users.

### Inputs

Most iPadOS gestures convert automatically, for example:

|iPadOS gesture|Mouse|Trackpad|
|---|---|---|
|Tap|Left or right click|Click|
|Touch and hold|Click and hold|Click and hold|
|Pan|Left click and drag|Click and drag|
|Pinch||Pinch|
|Rotate||Rotate|

Both pinch and rotate touches go to the view under the pointer, not the view under each touch.

### App icons

**Create a macOS version of your app icon** in the lifelike macOS style.

### Layout

- Consider: split a single column into multiple columns; use regular-width and regular-height size classes, reflowing content side by side as the window resizes; show an inspector beside content instead of a popover.
- **Consider moving controls from the iPad main UI to the toolbar**, and be sure to list their commands in menu bar menus.
- **As much as possible, adopt a top-down flow**, with the most important actions and content near the top. Put iPad toolbar controls in the window toolbar.
- **Relocate buttons from the side and bottom screen edges** (iPad reachability doesn't apply); you may want to use the toolbar.

### Menus

Mac users expect all of an app's commands in the menu bar.

- Support menu command shortcuts with `UIKeyCommand`. Add and remove custom app menus with `UIMenuBuilder`, with iPad commands as `UICommand` items.
- Pop-up and pull-down button menus automatically look like macOS menus.
- Context menus convert automatically. Consider adding more; Mac users tend to expect every object to offer one with relevant actions. On Mac they're sometimes called contextual menus.

## Platform considerations

No additional considerations for iPadOS or macOS. Not supported in iOS, tvOS, visionOS or watchOS.

## Resources

Source: [Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst), captured 2026-09-12.
