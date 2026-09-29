---
topic: pointing-devices
tier: 3
platforms: [ios, ipados, macos, visionos]
category: patterns/interaction
triggers:
  - "pointer"
  - "mouse"
  - "trackpad"
  - "cursor"
  - "hover"
  - "pointer interaction"
  - "iPadOS pointer"
  - "UIBandSelectionInteraction"
  - "UIPointerAccessory"
  - "UIPointerShape.roundedRect(_:radius:)"
related:
  - gestures
  - focus-and-selection
  - drag-and-drop
---

# Pointing devices

People can use a pointing device like a trackpad or mouse to navigate and initiate actions. Mac users typically expect to pair it with a keyboard; on iPad and Apple Vision Pro it supplements touch, eyes and gestures.

## Best practices

- **Respond to mouse and trackpad gestures consistently, and provide a consistent experience across gestures, eyes, a pointing device and a keyboard**; people expect most gestures to work the same systemwide, in any app or game.
- **Avoid redefining systemwide trackpad gestures**, like revealing the Dock or Mission Control in macOS, even in a game with custom gestures. Mac users can customize them.
- **Let the pointer reveal and hide controls that automatically minimize or fade out**, like the minimized Safari toolbar in iPadOS or full-screen video playback controls.
- **Keep modifier-key interactions consistent**: if Option-drag duplicates an object, ensure the result is the same by touch or pointer.

## Platform considerations

No additional considerations for iOS. Not supported in tvOS or watchOS.

### iPadOS

- **Allow multiple selection in custom views when necessary.** In iPadOS 15 and later, click-dragging the pointer draws a rectangle that selects the items it encompasses. Standard nonlist collection views support this by default; custom views need you to implement it (`UIBandSelectionInteraction`).
- **Distinguish between pointer and finger input only if it provides value**, like clicking a precise seek destination on a video scrubber.

#### Pointer shape and content effects

The pointer is a circle by default but can take a system-defined or custom shape over specific elements or regions (automatically an I-beam over text entry). With a *content effect*, the element beneath also changes; depending on the effect, the pointer keeps its shape or morphs to integrate with it.

|Effect|Behavior|Default for|
|---|---|---|
|Highlight|Pointer becomes a translucent rounded-rectangle background with gentle parallax|Bar buttons, tab bars, segmented controls, edit menus|
|Lift|Pointer fades beneath; element scales up with shadow, specular highlight and parallax|App icons, Control Center buttons|
|Hover|Your custom scale, tint or shadow; default pointer shape unchanged||

#### Pointer accessories

Accessories are small secondary indicators, combinable with any pointer, that show how to interact with an element, like resize arrows (`UIPointerAccessory`).

- **Use clear, simple images for custom accessories.**
- **Consider using the accessory transition to signal a change in an element's state or behavior**, like `plus` to `circle.slash` when adding becomes unavailable. The system animates accessory appearance, disappearance, shape and position.

#### Pointer magnetism

The pointer starts transforming on entering an element's hit region (typically beyond its visible bounds); flicks pull it toward the center of the likely target in its path. By default, magnetism applies to lift and highlight elements and text-entry areas (preventing line skips while selecting text), not hover elements.

#### Standard pointers and effects

- **When possible, support the system-provided content effects**, matching their intent: highlight for small elements with transparent backgrounds, lift for small opaque ones, hover for large ones (customize scale, tint and shadow as needed).
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas.**
- **Add padding around interactive elements for comfortable hit regions.** In general, about 12 pt works well around bezeled elements, about 24 pt around the visible edges of unbezeled ones, such as symbols.
- **Create contiguous hit regions for custom bar buttons**, so the pointer doesn't briefly revert to its default shape between them.
- **Specify the corner radius of a nonstandard element that receives the lift effect**, like a circle (`UIPointerShape.roundedRect(_:radius:)`), so the pointer morphs seamlessly instead of using the system radius.

#### Customizing pointers

- **Prefer system-provided pointer effects for custom elements that behave like standard ones.**
- **Use pointer effects consistently throughout your app.**
- **Avoid gratuitous pointer and content effects.**
- **Keep custom pointer shapes simple**, ideally signaling the available action without drawing attention.
- **Consider custom annotations with useful information**, like X and Y values over a graph.
- **Avoid displaying instructional text with a pointer**; instead, prioritize a clear, simple interface.
- **Consider the interplay of shadow, scale and spacing in custom hover effects.** In general, reserve scaling for elements that can grow without crowding neighbors (not table rows); with little surrounding space, consider tint without scale and shadow. Shadow without scale doesn't work well.

### macOS

People can customize many mouse and trackpad interactions (often toggling non-primary clicks and gestures, secondary-click regions, gesture finger combinations and movements).

|Mouse and trackpad|Expected behavior|
|---|---|
|Primary click|Select or activate an item, such as a file or button|
|Secondary click|Reveal contextual menus|
|Scrolling|Move content up, down, left or right within a view|
|Smart zoom|Zoom in or out on content, such as a webpage or PDF|
|Swipe between pages|Go forward or backward between individually displayed pages|
|Swipe between full-screen apps|Same, between full-screen apps and spaces|
|Mission Control (mouse: two-finger double-tap; trackpad: three- or four-finger swipe up)||

|Trackpad only|Expected behavior|
|---|---|
|Lookup and data detectors (one-finger force click or three-finger tap)|Lookup window above selected content|
|Tap to click|Primary click by tapping|
|Force click|Click then press firmly for a Quick Look or lookup window above selected content; variable pressure affects pressure-sensitive controls, such as variable speed media controls|
|Zoom in or out (two-finger pinch)||
|Rotate (two fingers in a circular motion)|Rotate content, such as an image|
|Notification Center (swipe from the trackpad edge)||
|App Exposé (three- or four-finger swipe down)|Current app's windows|
|Launchpad (thumb and three fingers pinch)||
|Show Desktop (thumb and three fingers spread)|Slide all windows aside to reveal the desktop|

#### Pointers

Your app can use standard pointer styles (`NSCursor`) to communicate an element's interactive state or a drag's result.

|Pointer (API)|Meaning|
|---|---|
|Arrow (`arrow`)|Standard; selecting and interacting with content and elements|
|Closed hand (`closedHand`)|Dragging to reposition content's display within a view, like a map in Maps|
|Contextual menu (`contextualMenu`)|Content below has a contextual menu; generally shown only while Control is pressed|
|Crosshair (`crosshair`)|Precise rectangular selection is possible, like in an image in Preview|
|Disappearing item (`disappearingItem`)|Dragged item disappears when dropped; any original it references is unaffected (like a mailbox dragged out of Mail's favorites bar)|
|Drag copy (`dragCopy`)|Dropping duplicates rather than moves the item; appears when pressing Option during a drag|
|Drag link (`dragLink`)|Dropping creates an alias of the file, leaving the original unmoved; appears when pressing Option-Command during a drag|
|Horizontal I beam (`iBeam`)|Text selection and insertion possible in a horizontal layout, like a TextEdit or Pages document|
|Open hand (`openHand`)|Dragging to reposition content within a view is possible|
|Operation not allowed (`operationNotAllowed`)|Dragged item can't be dropped here|
|Pointing hand (`pointingHand`)|Content beneath is a URL link to a webpage, document or other item|
|Resize down (`resizeDown`)|Resize or move a window, view or element downward|
|Resize left (`resizeLeft`)|Same, left|
|Resize left/right (`resizeLeftRight`)|Same, left or right|
|Resize right (`resizeRight`)|Same, right|
|Resize up (`resizeUp`)|Same, upward|
|Resize up/down (`resizeUpDown`)|Same, upward or downward|
|Vertical I beam (`iBeamCursorForVerticalLayout`)|Text selection and insertion possible in a vertical layout|

The resize APIs are deprecated.

### visionOS

- People can use an attached pointing device or keyboard alongside eyes and hands. If people look at an element, then move the pointer, the system focuses the element under the pointer automatically, with no app work.
- With a pointing device attached, where people look sets the pointer's context, following their eyes between windows.
- With a gesture-capable device like a trackpad or mouse, the pointer hides during gestures until people move it, reappearing where they look.

## Resources

Developer: Input events (SwiftUI), Pointer interactions (UIKit), Mouse, Keyboard, and Trackpad (AppKit).

Source: [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices), captured 2026-09-12.
