---
topic: game-controls
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: patterns/interaction
triggers:
  - "game controller"
  - "MFi controller"
  - "gamepad"
  - "thumbstick"
  - "GCController"
  - "GCRequiresControllerUserInteraction"
  - "GCControllerElement"
related:
  - designing-for-games
  - gestures
  - keyboards
  - playing-haptics
---
# Game controls

Games can accept physical controllers alongside each platform’s familiar input—touch, remote, mouse/keyboard, or trackpad. Every platform except watchOS supports controllers, but not every player has or can use one.

## Touch controls (iOS, iPadOS)

You can use the [`TouchController`](https://developer.apple.com/documentation/touchcontroller) framework to add virtual controls to Metal-based games over game content, while allowing direct touch on game elements. Virtual controls generally help games with many actions or movement; when direct interaction is more immersive, reduce overlap by attaching actions to gestures (for example, tap an object to select it instead of adding a selection button).

- Account for device boundaries and safe areas; keep controls away from the Home indicator and Dynamic Island. Put frequent controls near the thumb but outside expected movement/camera regions; place secondary controls such as menus at the top.
- Make frequent controls at least **44x44 pt** and less important controls, including menus, at least **28x28 pt**.
- Always include visible and tactile press states; keep the visual state visible under the finger (for example, increased opacity and a glow), and pair it with sound and haptics.
- Use action-representing symbols (a weapon for attack), not abstract shapes or controller names such as A, X, or R1.
- Show or hide controls according to context. You can hide controls when an action is unavailable or irrelevant to reduce clutter; for example, consider hiding movement controls until the player touches the screen. A movement thumbstick can fade at rest and, while moving, become more visible with a highlight showing direction.
- When mechanics require multiple buttons at once or in sequence, consider redesigning them into one control. Use double-tap or touch-and-hold for variations such as a powered-up attack; for multiple actions such as walking and sprinting, consider combining them into one control.
- Make movement and camera behavior predictable: movement is typically left, camera right. Maximize both input areas; let a movement thumbstick appear where the thumb lands, and use direct touch to pan the camera.

## Physical controllers

- If supporting controllers, try to provide a fallback for the platform default: touchscreen on iPhone/iPad, keyboard plus trackpad or mouse on Mac, remote on Apple TV, and eye/hand gestures on Apple Vision Pro. See [Adding virtual controls to games that support game controllers in iOS](https://developer.apple.com/documentation/gamecontroller/adding-virtual-controls-to-games-that-support-game-controllers-in-ios).
- In tvOS and visionOS, a game may require a controller. The App Store then shows **Game Controller Required**; because the game can open without a connected controller, check presence and prompt gracefully. [`GCRequiresControllerUserInteraction`](https://developer.apple.com/documentation/bundleresources/information-property-list/gcrequirescontrolleruserinteraction) identifies platforms where the app requires or recommends a game controller.
- Detect pairing and obtain the controller profile automatically with the [`GameController`](https://developer.apple.com/documentation/gamecontroller) framework.
- The framework gives elements standard placement-based names, but real controllers can use different colors and symbols. Match the connected controller’s labeling scheme in onscreen content; [`GCControllerElement`](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement) is an input for a physical control such as a button or thumbstick.

Outside gameplay, use these UI conventions:

|Button|Expected UI behavior|
|---|---|
|A|Activates a control|
|B|Cancels an action or returns to the previous screen|
|X|—|
|Y|—|
|Left shoulder|Navigates left to another screen or section|
|Right shoulder|Navigates right to another screen or section|
|Left trigger|—|
|Right trigger|—|
|Left/right thumbstick|Moves selection|
|Directional pad|Moves selection|
|Home/logo|Reserved for system controls|
|Menu|Opens game settings or pauses gameplay|

With multiple controllers, use labels and glyphs for the active controller and, in multiplayer, the relevant player; if referring to more than one controller, consider listing their buttons together. Prefer SF Symbols from the Game Controller framework (SF Symbols Gaming category) for controller elements, especially for players unfamiliar with controller labels.

## Keyboards

Prefer single-key commands, which are fast while a mouse or trackpad is also in use (for example, I for Inventory, M for Map, or Space for the main action). Test comfort on an Apple keyboard: if a non-Apple binding uses Control (^), consider Command (⌘), which is next to Space and convenient during W-A-S-D play. Consider grouping related commands on nearby keys (common commands near W-A-S-D; inventory categories on number keys). Provide customizable bindings alongside reasonable defaults.

## visionOS spatial controllers

A visionOS game can also support spatial controllers such as PlayStation VR2 Sense. Match hand input: looking at an object plus the left or right trigger is indirect interaction; reaching toward it plus that trigger is direct interaction.

Source: [Game controls](https://developer.apple.com/design/Human-Interface-Guidelines/game-controls) (captured 2026-09-12).
