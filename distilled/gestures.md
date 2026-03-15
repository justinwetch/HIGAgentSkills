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
related:
  - drag-and-drop
  - motion
  - feedback
---
# Gestures

> A gesture is a physical motion used to directly affect an object in an app, whether on a touchscreen, in the air, or via an input device.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Standard Gestures (All Platforms)

| Gesture | Supported platforms | Common action |
|---|---|---|
| Tap | All | Activate a control; select an item |
| Swipe | All | Reveal actions/controls; dismiss views; scroll |
| Drag | All | Move a UI element |
| Touch/pinch and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality |
| Double tap | All | Zoom in/out; primary action on Apple Watch |
| Zoom (pinch) | iOS, iPadOS, macOS, tvOS, visionOS | Zoom or magnify content |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate selected item |

## Best Practices

- **Multiple input methods** — don't assume people can perform a specific gesture. Support voice, keyboard, Switch Control alternatives.
- **Consistent with expectations** — tap activates/selects, swipe scrolls. Don't repurpose familiar gestures for unique app actions, and don't require unique gestures for standard actions.
- **Responsive** — provide immediate feedback. As people gesture, show what will happen.
- **Communicate unavailability** — if a gesture doesn't work, indicate clearly why (locked object indicator, visibly disabled button state), or people will assume the app froze.

## Custom Gestures

Add only for specialized tasks not covered by standard gestures (e.g., games, drawing apps). If you define a custom gesture, it must be:
- Discoverable
- Straightforward to perform
- Distinct from other gestures
- Not the only way to do an important action

- **Teach custom gestures** — in-app moments with simple language and graphics. If it's hard to explain, it'll be hard to learn.
- **Custom gestures supplement, never replace standard gestures** — always provide a standard fallback (e.g., a Back button alongside a swipe-from-edge shortcut).
- **Avoid conflicting with system gestures** — e.g., edge swipes in watchOS, hand-roll to access system overlays in visionOS.

## Platform Considerations

### iOS, iPadOS — Additional Expected Gestures

| Gesture | Common action |
|---|---|
| Three-finger swipe left | Initiate undo |
| Three-finger swipe right | Initiate redo |
| Three-finger pinch in | Copy selected text |
| Three-finger pinch out | Paste copied text |
| Four-finger swipe (iPadOS only) | Switch between apps |
| Shake | Initiate undo/redo |

- **Simultaneous gestures**: consider allowing in games (e.g., joystick + fire button at same time). See apple-pencil-and-scribble for Pencil + touch coordination.

### macOS

Primary: keyboard + mouse. Standard gestures also work on Magic Trackpad, Magic Mouse, and game controllers with touch surfaces.

### tvOS

Standard gestures via Siri Remote, compatible remotes, or game controllers with touch surfaces. See remotes.

### visionOS

Two gesture categories:

**Indirect** — look at an object to target it, then manipulate from a distance (e.g., tap finger to thumb to select). Comfortable at any distance; quick to redirect focus. Preferred for UI and common components.

**Direct** — physically touch the interactive object (e.g., type on the virtual keyboard). Best for infrequent use; arm fatigue can result. visionOS supports direct versions of all standard gestures.

**Direct gesture reference:**

| Direct gesture | Common use |
|---|---|
| Touch | Select or activate |
| Touch and hold | Open contextual menu |
| Touch and drag | Move object |
| Double touch | Preview; select a word |
| Swipe | Reveal actions; dismiss; scroll |
| Two-hand pinch together/apart | Zoom in/out |
| Two-hand pinch in circular motion | Rotate |

Custom visionOS gestures:
- Requires Full Space + hand access permission.
- **Prioritize comfort** — avoid sustained raised arms; repetitive similar movements cause muscle fatigue.
- **Avoid hand-specific gestures** — don't require a specific hand; adds cognitive load and excludes users with limb differences.
- Careful with complex multi-finger/two-hand gestures — offer an alternative for single-hand users.
- **Reserve palm area for system overlays** — don't anchor content to hands/wrists. In Full Space, you may defer the Home indicator (require a tap instead).
- **Avoid rolling-hand motions** — reserved for system overlays (Home and Control Center in visionOS 2+).

### watchOS — Double Tap (watchOS 11+)

Scrolls lists/scroll views; advances vertical tab views; activates a designated primary action in a view/widget/Live Activity.

- **Don't set a primary action in views with lists, scroll views, or vertical tabs** — conflicts with default double-tap navigation.
- **Choose the most commonly used button as the primary action** — e.g., play/pause in a media controls view.
