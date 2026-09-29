---
topic: gestures
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/interaction
triggers:
  - "gesture"
  - "tap"
  - "swipe"
  - "pinch"
  - "zoom"
  - "long press"
  - "pan"
  - "rotate"
  - "multi-touch"
  - "persistentSystemOverlays(_:)"
  - "handGestureShortcut(_:isEnabled:)"
  - "HandGestureShortcut.primaryAction"
related:
  - drag-and-drop
  - motion
  - feedback
---

# Gestures

A gesture is a physical motion that directly affects an object, on a touchscreen, in the air or on an input device. People expect standard gestures everywhere.

## Best practices

- **Give people more than one way to interact** (voice, keyboard, Switch Control); don't assume people can use a specific gesture.
- **In general, respond to gestures as people expect** (tap activates or selects). Avoid familiar gestures (tap, swipe) for app-unique actions, and unique gestures for standard actions like activating a button or scrolling.
- **Handle gestures as responsively as possible**, with immediate feedback that predicts the result and, if necessary, shows the extent and type of movement needed.
- **Indicate when a gesture isn't available**, and why; make locked or unavailable states clearly distinct.

## Custom gestures

- **Add custom gestures only when necessary**, for frequent specialized tasks no existing gesture covers (games, drawing). Make them discoverable, easy, distinct, and not the only way to perform an important action.
- **Make custom gestures easy to learn**: teach them in context and test in real use. One that's hard to describe simply may be hard to learn.
- **Supplement standard gestures, don't replace them**: a swipe-back shortcut still keeps the Back button.
- **Avoid conflicting with gestures for system UI**, like watchOS edge swipes or the visionOS hand roll (in specific cases, games and immersive experiences can defer them; see visionOS).

## Platform considerations

### iOS, iPadOS

|Additional gesture|Common action|
|---|---|
|Three-finger swipe|Undo (left); redo (right)|
|Three-finger pinch|Copy selected text (in); paste (out)|
|Four-finger swipe (iPadOS only)|Switch apps|
|Shake|Undo; redo|

- **Consider simultaneous recognition of multiple gestures if it enhances the experience**, e.g. a game's joystick plus fire buttons; unlikely useful in nongame apps.

### macOS

Primarily keyboard and mouse; standard gestures also work on Magic Trackpad, Magic Mouse and touch-surface game controllers.

### tvOS

People expect standard gestures on a compatible remote, Siri Remote or touch-surface game controller.

### visionOS

*Indirect* gestures: look to target, then act from a distance (tap finger and thumb to select); comfortable at any distance. *Direct* gestures: touch the object, like virtual keys; best within reach and for infrequent use. Every standard gesture has a direct version.

|Direct gesture|Common use|
|---|---|
|Touch|Select or activate an object|
|Touch and hold|Open a contextual menu|
|Touch and drag|Move an object|
|Double touch|Preview an object or file; select a word when editing|
|Swipe|Same as standard Swipe|
|Two hands pinch and drag together or apart|Zoom in or out|
|Two hands pinch and drag in a circle|Rotate an object|

- **Support standard gestures everywhere you can**, even alongside custom ones.
- **Offer both indirect and direct interactions when possible.** Prefer indirect for UI and common components like buttons; reserve direct and custom gestures for objects inviting close-up interaction or specific motions in a game or interactive experience.
- **Avoid requiring specific body movements or positions.** If movement is required, consider alternative inputs.

Custom gestures require a Full Space and hand-data permission ([ARKit data access](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data)).

- **Prioritize comfort.** Continually test ergonomics: raised arms tire, and repeated similar movements can strain muscles and joints.
- **Carefully consider gestures needing multiple fingers or both hands.** If you require one, consider a lower-movement alternative.
- **Avoid custom gestures that require a specific hand.**

#### System overlays

In visionOS 2 and later, systemwide palm gestures are reserved solely for overlays: palm up shows the Home indicator; hand turned over shows the status bar, and a tap opens Control Center. visionOS 1's look-up Control Center access remains an accessibility setting.

- **Reserve the area around a person's hand for system overlays.** If possible, don't anchor content to hands or wrists; place a game's hand-anchored content outside the hand's immediate area, to avoid the Home indicator.
- **Consider deferring overlays in immersive apps or games**, like ones with virtual gloves: in a Full Space, `persistentSystemOverlays(_:)` can require a tap before the Home indicator appears. Apps built for visionOS 1 defer by default.
- **Use caution with custom gestures that roll the hand, wrist and forearm**; that motion is reserved for overlays, which draw over your content without notifying your app. Test for conflicts.

### watchOS

In watchOS 11 and later, double tap scrolls lists and scroll views and advances vertical tabs. It highlights, then performs, the toggle or button you set as a view's primary action (in an app, or a widget or Live Activity in the Smart Stack). In notifications, it performs the first nondestructive custom action.

- **Avoid setting a primary action in views with lists, scroll views or vertical tabs.**
- **Choose the most commonly used button as a nonscrolling view's primary action**, e.g. play/pause. Use `handGestureShortcut(_:isEnabled:)` with `primaryAction`.

## Specifications

System APIs support these on touchscreens, trackpads, mice, remotes, game controllers and as visionOS indirect gestures.

|Standard gesture|Supported in|Common action|
|---|---|---|
|Tap|All platforms|Activate a control; select an item|
|Swipe|All platforms|Reveal actions and controls; dismiss views; scroll|
|Drag|All platforms|Move a UI element|
|Touch (or pinch) and hold|All except macOS|Reveal additional controls or functionality|
|Double tap|All platforms|Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2|
|Zoom|All except watchOS|Zoom a view; magnify content|
|Rotate|All except watchOS|Rotate a selected item|

## Resources

Developer: Gestures (SwiftUI), `UITouch`.

Source: [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), captured 2026-09-12.
