# iPhone Duo redesign checklist

This is a paraphrased checklist for the [Duo mode](duo.md) Stage 2 match.

Tags:
- **[HIG]** is `references/hig/designing-for-iphone-duo.md`, Apple HIG captured 2026-09-12.
- **[T461]–[T466]** are Apple's iPhone Duo tech talks, listed under Sources.

Quote the HIG file for exact wording. Talk items are summaries, not quotes.

## 1. Build and resizability

- The full edge-to-edge experience with vertical bars needs a rebuild with Xcode 27.1 / the iOS 27.1 SDK. Nothing goes vertical before that. [T461, T462]
  - Built with an older SDK, the app uses only the space left of the status bar and camera when closed, and is iPhone-sized when open.
  - Built with the iOS 27 SDK, the app extends left of the status bar on the inner display. [T461]
- Size classes drive layout. [T461, HIG]
  - Outer portrait: compact width, regular height.
  - Outer landscape: compact, compact.
  - Inner: regular, regular.
- Design for those size classes, not for five poses. [T466]
- Avoid all of these [T461, T466, HIG]:
  - fixed widths;
  - width breakpoints;
  - metrics tied to a screen;
  - `UIScreen.main` (ambiguous, to be deprecated);
  - using idiom or orientation to decide layout.
- Use scene or window-scene bounds instead. [T461]
- `UIRequiresFullScreen` is honored, but the app still resizes. [T461]
- The inner display doesn't honor supported orientations. [T461] See Tensions §2.
- Landscape is worth supporting, e.g. for the tent stance. [T461]
- Games may lock portrait or landscape. When they do, fill the screen, keep text and control sizes consistent, and prefer changing the aspect ratio to letterboxing. [HIG]

## 2. Containers and bars

- Vertical bars need system-managed bars:
  - SwiftUI: `toolbar` in `NavigationStack`/`NavigationSplitView`.
  - UIKit: `UINavigationController`/`UITabBarController`.
- The system doesn't consider custom `UIToolbar`, `UINavigationBar` or `UITabBar` content. Move custom bars into managed bars. [T462]
- `NavigationSplitView`/`TabView` and `UISplitViewController`/`UITabBarController` adapt across the displays. On the inner display, a tab bar can be placed as a sidebar. [T461]

## 3. Bar audit

**Where items go**
- Bars are vertical on the outer display and in inner landscape. Inner portrait keeps horizontal bars. [HIG, T466]
- Only a container on the display edge goes vertical. [T462]
  - In split views, only the detail column does, and other columns stay horizontal.
  - An expanded inspector gets no vertical bar of its own.
- On the outer display, the order from the top is: Dynamic Island, status bar, toolbar, tab bar. [HIG]
- Top-bar items go to the top of the strip and bottom-bar items to the bottom. The tab bar stays at the bottom. [T466]
- In general, don't override the default placement. [HIG]

**Item order**
- Primary navigation (Back/Close) goes first, then the prominent action (Done), then the app's original groups. [HIG]
  - For a custom Back/Close [T462]: `cancellationAction` (SwiftUI), or a leading item with `leftItemSupplementsBackButton = false` (UIKit).
  - For the prominent action [T462]: `topBarPinnedTrailing` (SwiftUI) / `pinnedTrailingGroup` (UIKit).

**Item content**
- Give every item that isn't text-only a title and a symbol (`Label`, or a `UIBarButtonItem` with title + image), so the system picks the representation. [HIG, T462]
- Minimize text buttons, which stay horizontal. [HIG]
- Items too wide for the side should stay in the nav bar, like a text button or a segmented control. [T466]
- If an item's text carries information on its own, such as a cart price, it's better to keep that control in the horizontal bar. [T462]
- Replace inline counts with a badge. [T462]
- Items that switch between a symbol and text shouldn't go in a vertical bar. [T462]
  - The system Edit button stays horizontal automatically.
  - Give custom ones the horizontal-only `AxisBehavior`.

**Custom views**
- Custom views stay horizontal unless opted in. [T462]
- Opted-in views must fit a fixed-width bar, or re-layout by reading `toolbarVerticalEdge`. [T462]
- Vertical bars get a background under Reduce Transparency, so custom content must stay legible there. [T462]

**Grouping and spacing**
- Group related items with `ToolbarItemGroup`/`UIBarButtonItemGroup`, and don't add fixed spacing. [HIG]
- Keep controls near the content they affect. Controls for a pane other than the edge pane stay with that pane. [HIG]

**Compression and overflow**
- When space runs out [HIG, T462]:
  - navigation-focused views keep the tab bar and overflow toolbar items (the default);
  - task-focused views minimize the tab bar.
- Set this per view with `toolbarCompressionBehavior`. [T462]
- Overflow happens most in outer landscape, and also with the keyboard up or with Picture in Picture in open portrait. [T462]
- Set visibility priority by group, then by item, so frequent actions (Compose, New Note) and badged items overflow last. [HIG, T462]
  - SwiftUI: `ToolbarItemVisibilityPriority`. UIKit: `UIBarButtonItemVisibilityPriority`.
- Use one system overflow: `ToolbarOverflowMenu` / `additionalOverflowItems`. [HIG, T462]
  - Reserve the ellipsis for overflow; use another symbol for other menus. [HIG]

**Opting out**
- Consider disabling vertical bars for these, with `toolbarVerticalBehavior` / `preferredVerticalBarBehavior` [T462]:
  - single-page, bottom-heavy layouts like Calculator, which then reflows across the full width (four columns of five become five of four) [HIG, T462];
  - control-heavy sheets with a single item, like Close.

## 4. Outer display

- Safe areas and layout margins are asymmetric. Controls can sit on the left in landscape and in Split View, so handle each side independently. [T461, HIG]
- Keep foreground content inside the safe area. Backgrounds may extend behind bars. [T461]
- **Inset** is the usual choice. Aligning to the horizontal safe-area insets gives the offset automatically. [T466]
- **Full display width** suits visual, immersive, non-scrolling interfaces where bars aren't necessary and nothing conflicts with the Dynamic Island or status bar. [HIG, T466]
- **Mixed** means a full-width background or header over inset scrolling content, with every interactive element inset. [HIG, T466]
- Outer-display sheets get side controls by default. With the vertical bar disabled, the sheet stops short of the camera. [T466, T461]

## 5. Inner display

- Don't ship a stretched iPhone app. [T466]
- Expand the existing layout, and show another level only if it suits the content, like Mail's list and message. [HIG]
- Keep the same hierarchy inside and out. [T466]
- The options are [T466]:
  - a split view;
  - a width reflow (Music goes from stacked to two columns);
  - a tab bar as sidebar, which suits information-dense apps (Health) but isn't for every app.
- Split views show one pane on the outer display and multiple panes inside, in the same way as compact vs regular iPhone environments. [HIG]
- Inner sheets are centered with horizontal bars by default. [T462, T466]
  - A sheet placed on the right with `preferredPlacement` gets a vertical bar; one placed on the left doesn't. [T462]

## 6. Fold and reserved regions

- Alerts, context menus, sheets, standard split views and toolbar buttons avoid the fold automatically. Rely on them. [HIG, T466]
- Scrolling content need not avoid the fold. [T466, T463] See Tensions §4.
- **Audit centered layouts and custom splits.** [HIG, T463]
  - Consider `ArrangementView` / `UIArrangementViewController` (iOS 27.1) where a custom layout already resembles one. Side-by-side or stacked (`HStack`/`VStack`) maps to a split arrangement; layered (`ZStack`) maps to an overlay.
  - Prefer even grid column counts.
- **Split vs overlay.** [T463]
  - Split is for main-detail content where neither view may be obscured.
  - Overlay is for foreground over background where partial obscuring is fine. It prefers content above or below, goes side by side when folded, and can collapse. React to its fold layering with `overlayArrangementZIndex`.
  - Don't nest navigation containers inside arrangements, or arrangements inside `List`/`ScrollView`.
- **Displacement** is for the rest: move remaining high-priority custom controls clear of the fold. [HIG, T463]
  - Read regions with the `reservedRegion` method on `GeometryProxy` (SwiftUI) or `UIView` (UIKit), using its `frame` and `includeInactive`. [T463] The types are `ReservedRegion` / `UIViewReservedRegion`. [T461]
  - Move only what's necessary, and prefer small adjustments. Avoid moving elements far from their source or making them disappear. [HIG, T463]
  - Move independent elements alone and related elements together. [T463]
  - Continuous scrolling content doesn't displace. [T463]
- **Destination follows purpose.** [T463]
  - Book pose: alerts go trailing.
  - Table pose: at-a-distance content goes up top, and tappable controls go at the bottom.
- **Region types.** [T463]
  - A division (the fold) is active only when folded.
  - An occlusion (the inner camera) is active while the camera runs.
  - Use inactive regions for high-level choices, like even columns even when flat.
- When the inner camera activates, UI moves aside. [HIG]
- If a viewfinder is central to the UI, keep important content and controls clear of the camera. [T463]

## 7. Split View and Picture in Picture (all apps)

- All apps participate in side-by-side multitasking. [T464]
- Each app's controls go on its outer edge. [HIG]
- A pinned Picture in Picture window sits at the top, and the app resizes vertically. [T466]

## 8. Optional table-pose layout

- A pose-specific layout is optional. It puts media on top and controls on a stable bottom base, with the same controls and hierarchy. [T466] See Tensions §3.
- Never tie functionality to a pose. [T466]

## 9. Extras (only if relevant)

**Multiwindow** [T464]
- New windows open only on the inner display. Handle errors from scene requests.

**Hinge** [T464]
- `onHingeChange` / `UIHingeInteraction` report status and angle.
- Use them for interactions and effects only, never for layout.

**Scene accessories** [T464]
- `sceneAccessory` shows extra UI on the other display.
- The system can toggle it, so observe availability.
- `CameraCaptureAccessory` needs the app full screen on the inner display and an active camera session.

**Camera** [T465]
- There are two front cameras, one per display.
- The Virtual Front Camera auto-switches between them, but is capped at 1080p60.
- Use `AVCaptureDeviceDirectionCoordinator` to learn which camera faces the user.
- Mirror the preview when a rear camera faces the user.
- Offset or fill the inner preview.
- Adopt the rotation coordinator so the preview and photos stay upright as the app moves displays. Then disable camera-sensor-orientation compensation.

## Testing [T461]

- Run the app in the Device Hub iPhone Duo simulator (Xcode 27.1): open, close, rotate and fold. Try Split View on one side, then the other.
- Test safe-area and layout-margin handling in different configurations.
- Run the App Resizability skill in Xcode.
- Check camera preview quality on a device. [T465]

## Continuity checks

Check each of these in every pose [HIG, T466]:
- The same features and state.
- Controls in the same relative place.
- The hierarchy stays stable across frequent opening and closing.
- Nothing interactive sits in the fold or under the bars.
- Related elements move together. [T463]

## Tensions (mark as Decision, state both sides)

1. **Which side the bars are on.**
   - HIG: bars are on the outer display's trailing edge.
   - T466: they're on the right side.
   - HIG and T462: bars stay on the same side in right-to-left languages.
   - T461: controls can appear on the left in landscape.
2. **Orientation.**
   - HIG: games may lock orientation.
   - T461: the inner display doesn't honor supported orientations, but also that orientations are respected with scaling.
3. **Per-pose layout.**
   - HIG: no custom layout per pose.
   - T466: an optional table-pose layout is fine.
4. **Fold scope.**
   - HIG: keep important elements clear of the center.
   - T463/T466: scrolling content need not avoid the fold.

## Sources

Apple Developer tech talks, retrieved 2026-09-24:
- [T461] [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/)
- [T462] [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/)
- [T463] [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/)
- [T464] [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/)
- [T465] [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/)
- [T466] [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/)
