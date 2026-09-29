---
topic: live-activities
tier: 3
platforms: [ios, ipados, macos, watchos]
category: components/system
triggers:
  - "live activity"
  - "Dynamic Island"
  - "ActivityKit"
  - "realtime update"
  - "ActivityFamily.small"
  - "activitySystemActionForegroundColor(_:)"
  - "ContainerRelativeShape"
related:
  - notifications
  - widgets
---

# Live Activities

A Live Activity tracks a task or event at a glance with frequent, interactive updates over a few hours. It starts on iPhone or iPad and automatically appears on the Lock Screen, Home Screen, Dynamic Island and StandBy (iPhone), Mac menu bar, Apple Watch Smart Stack and CarPlay Dashboard.

## Anatomy

The system picks presentations per location, so you must support **compact, minimal, expanded and Lock Screen**.

- **Compact:** Dynamic Island with one active Live Activity; leading and trailing elements around the TrueDepth camera.
- **Minimal:** with multiple active, two show in the Dynamic Island, one attached and one detached (circular or oval by content size).
- **Expanded:** on touch and hold of compact or minimal (a tap opens the app).
- **Lock Screen:** bottom banner; use a layout similar to expanded. Without a Dynamic Island, alerts briefly show it over other content.
- **StandBy:** minimal; a tap shows Lock Screen scaled 2x, with any custom background extended full screen.

## Best practices

- **Offer Live Activities for tasks and events with a defined beginning and end**, ideally no longer than eight hours.
- **Focus on important information people need at a glance.**
- **Don't use a Live Activity to display ads or promotions.**
- **Avoid displaying sensitive information.** Show an innocuous summary with details in the app, or redact and let people choose whether it shows.
- **Match your app's aesthetic in both dark and light appearances.**
- **If you include a logo mark, display it without a container.** Don't use the entire app icon.
- **Don't add elements to your app that draw attention to the Dynamic Island.**
- **Ensure text is easy to read**: large, medium weight or heavier; use small text sparingly.

### Creating layouts

- **Adapt to different screen sizes and presentations**, using only the space content needs. Provide assets for multiple scale factors; actual size may vary.
- **Use familiar layouts for custom views** (Apple Design Resources templates).
- **Use consistent margins and concentric placement.** Keep even margins to the edges and corners so nothing pokes into the rounded shape; a nested corner radius is the outer radius minus the margin (`ContainerRelativeShape`).
- **When separating a block of content, place it in an inset container shape or use a thick line.** Don't draw content to the edge of the Dynamic Island.
- **Dynamically change height on the Lock Screen and in expanded** to fit the available information.

### Choosing colors

- **Carefully consider a custom background color and opacity.** Only Lock Screen allows one; with a custom color or image, ensure contrast, especially tints on reduced-luminance Always-On displays.
- **Use color to express identity.** On the opaque black Dynamic Island, consider bold text and object colors.
- **Tint the key line** (shown around the Dynamic Island on dark backgrounds) **to match your content.**

### Animation

Animations, system or custom, last at most 2 seconds; the system doesn't animate on Always-On displays with reduced luminance.

- **Use animations to reinforce information and highlight updates**: movement, the default content-replace transition, or custom scale, opacity and movement transitions.
- **Animate layout changes**, moving existing elements to new positions rather than removing and re-adding them.
- **Try to avoid overlapping elements.** In lists, animate only the moving item and fade the others.

### Interactivity

- **Make sure a tap opens your app at the related details.**
- **Focus on simple, direct actions.** Only include controls for essential, related functions people activate once or pause and resume (playback, workouts, live audio recording). Prefer a single interactive element.
- **Consider letting people respond to updates** with a button or toggle (contact the driver).

### Starting, updating and ending

- **Start Live Activities at appropriate times, and make it easy to turn them off in your app.** Unexpected ones can be unwanted. Consider an off control in the corresponding app view, or people may disable Live Activities in Settings.
- **Offer an App Shortcut that starts your Live Activity** (such as from the Action button).
- **Update only when new content is available.**
- **Alert only for essential updates.** Alerts light the screen, play the notification sound by default, and show expanded in the Dynamic Island (a banner without one). Avoid alerting too often; don't also send push notifications for the same updates.
- **Prefer a single Live Activity that rotates through multiple events** over separate ones.
- **Always end a Live Activity immediately when the task or event ends, and consider a custom dismissal time.** The system removes it immediately from the Dynamic Island and CarPlay; on the Lock Screen, Mac menu bar and Smart Stack it stays up to four hours. Consider a dismissal time proportional to duration; in most cases 15-30 minutes is adequate.

## Presentation

**Start with the iPhone design**, standard for each presentation, then add custom layouts for StandBy, CarPlay or Apple Watch as warranted.

### Compact

- **Focus on the most important information**: dynamic, essential and easy to understand.
- **Unify leading and trailing elements** into one piece of information with consistent color and typography.
- **Keep content narrow and snug against the TrueDepth camera.** Try not to obscure status bar information; don't pad around the camera. Balance both sides' widths, using shortened units or less precise data.
- **Link both elements to the same related screen.**

### Minimal

- **Keep it recognizable.** If possible, show updated information rather than just a logo (Timer shows remaining time).

### Expanded

- **Maintain elements' relative placement** so layouts expand predictably from compact or minimal.
- **Wrap content tightly around the TrueDepth camera.**

### Lock Screen

- **Don't replicate notification layouts.**
- **Use custom background or tint colors and opacity sparingly** to suit personalized Lock Screens.
- **Ensure contrast in Dark Mode and on Always-On displays.** The default background follows appearance; a custom one must suit both or vary per appearance. Verify on a reduced-luminance Always-On device, where the system adapts colors.
- **Verify the generated dismiss button color**; adjust with `activitySystemActionForegroundColor(_:)` if needed.
- **Use the standard 14 pt margin** (`padding(_:_:)`) to align with notifications. Tighter margins may suit graphics or buttons; avoid crowding edges.

### StandBy

- **Update your layout for StandBy**: assets must look great scaled; consider a custom layout using the extra space.
- **Consider the default background**; it blends with the bezel and lets the system scale slightly larger.
- **Use standard margins and avoid extending graphics to the screen edge**, or content gets cut off.
- **Verify contrast in Night Mode**, where the system applies a red tint.

## CarPlay

By default the system combines the compact elements on CarPlay Dashboard. Your design applies to CarPlay and Apple Watch; CarPlay deactivates interactive elements.

- **Consider a custom layout for larger text or more information** by declaring the `ActivityFamily.small` supplemental activity family.
- **Carefully consider buttons or toggles.** If people likely start or observe the Live Activity while driving, prefer timely content.

## Platform considerations

No additional considerations for iOS or iPadOS. Not supported in tvOS or visionOS.

### macOS

Live Activities appear in a paired Mac's menu bar using compact, minimal and expanded. Clicking launches iPhone Mirroring.

### watchOS

Live Activities top the paired Watch's Smart Stack, by default combining the compact elements. A tap opens your watchOS app or, without one, a view offering to open the iPhone app.

- **Consider a custom watchOS layout** to show more information or add a button or toggle.
- **Carefully consider buttons or toggles.** The custom layout also applies in CarPlay; if people likely start or observe it while driving, don't include them.
- **Focus on essential information**: progress, interactive controls (timer), significant updates (scores).

## Specifications

All values in points.

**CarPlay:** the system may scale to fit. Verify at 240x78, 240x100 and 170x78; test Smart Display Zoom (Settings > Display in CarPlay) Widescreen 1920x720, Portrait 900x1200, Standard 800x480.

**iOS:**

|Screen (portrait)|Compact leading / trailing (each)|Minimal|Expanded|Lock Screen|
|---|---|---|---|---|
|430x932|62.33x36.67|36.67-45x36.67|408x84-160|408x84-160|
|393x852|52.33x36.67|36.67-45x36.67|371x84-160|371x84-160|

Dynamic Island corner radius: 44 pt, matching the TrueDepth camera.

|Dynamic Island width|Compact or minimal|Expanded|
|---|---|---|
|iPhone 17 Pro Max, Air, 16 Pro Max, 16 Plus, 15 Pro Max, 15 Plus, 14 Pro Max|250|408|
|iPhone 17 Pro, 17, 16 Pro, 16, 15 Pro, 15, 14 Pro|230|371|

**iPadOS Lock Screen** (portrait screen): 1366x1024: 500x84-160; 1194x834, 1012x834, 1080x810, 1024x768: 425x84-160.

**macOS:** use iOS dimensions.

**watchOS** (same as widgets): 40mm 152x69.5; 41mm 165x72.5; 44mm 173x76.5; 45mm 184x80.5; 49mm 191x81.5.

## Resources

Developer: `ActivityKit`, `WidgetKit`, `SwiftUI`.

Source: [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities), captured 2026-09-12.
