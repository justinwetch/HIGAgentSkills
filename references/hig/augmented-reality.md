---
topic: augmented-reality
tier: 3
platforms: [ios, ipados, visionos]
category: technologies
triggers:
  - "AR"
  - "augmented reality"
  - "ARKit"
  - "3D object"
  - "world tracking"
related:
  - playing-audio
  - playing-haptics
  - gestures
---

# Augmented reality

AR superimposes 3D virtual objects on a live camera view of the physical world.

**Offer AR features only on capable devices.** If AR is the app's primary purpose, make it available only on ARKit-capable devices. For optional AR features or ones needing specific capabilities, don't show an error on unsupported devices; just don't offer them.

Guidance below covers iOS and iPadOS.

## Best practices

- **Let people use the entire display**; avoid cluttering it with controls and information.
- **Strive for convincing illusions when placing realistic objects**, with detailed, lifelike assets. ARKit supports proper scale, surface placement, environmental lighting, camera grain, top-down diffuse shadows on real surfaces, and camera-driven updates. Make sure scenes update 60 times per second so objects don't jump or flicker.
- **Consider how reflective surfaces show the environment.** ARKit reflections are approximations; prefer small or coarse reflective surfaces.
- **Use audio and haptics to enhance immersion**, e.g. to confirm contact.
- **Minimize text in the environment.**
- **If additional information or controls are necessary, consider screen space**: fixed to a consistent location in the virtual world or, less commonly, on the device screen.
- **Consider indirect controls (2D, in screen space) for persistent controls**, placed so people needn't change their grip; consider translucency so they don't block the scene.
- **Anticipate varied environments**, like cramped spaces without large flat surfaces. Communicate requirements up front; consider environment-specific feature sets.
- **Be mindful of comfort.** Consider placing objects so people needn't move the device closer; in games, consider short levels with brief downtime.
- **If your app encourages movement, introduce motion gradually.**
- **Be mindful of safety**; immersed people may not notice their surroundings. Consider ways to make the app safe, like a game not encouraging large or sudden movements.

## Providing coaching

Consider the built-in coaching view (`ARCoachingOverlayView`, deprecated) to guide the device movement ARKit needs to detect surfaces, at initialization and during *relocalization* after an interruption.

- **Hide unnecessary app UI while people use a coaching view.** By default it appears automatically when initialization or relocalization starts.
- **If necessary, offer a custom coaching experience** when configuring the system view (e.g. for horizontal or vertical planes) isn't enough or you want a different style. Use the system view for reference.

## Helping people place objects

- **Show people when to locate a surface and place an object.** Consider the coaching view to help find a horizontal or vertical surface. After ARKit detects a surface, your app can show a custom placement indicator aligned with the detected plane.
- **When people place an object, immediately integrate it.** It's best not to wait for more accurate surface data; subtly refine position once detection completes, such as nudging an object placed off the surface back onto it (`ARTrackedRaycast`).
- **Consider guiding people toward offscreen objects** with visual or audible cues.
- **Avoid trying to precisely align objects with detected surface edges**; boundaries are approximations that may change.
- **Use plane classification to inform placement**, like furniture only on "floor", a game board only on "table".

## Designing object interactions

- **Let people use direct manipulation when possible.** If people move around while using the app, indirect controls can work better.
- **Use standard, familiar gestures**; consider single-finger drag to move, two-finger rotation to spin.
- **In general, keep interactions simple.** Consider limiting movement to the object's resting surface and rotation to one axis.
- **Respond to gestures within reasonable proximity of interactive objects**; it's usually best to assume a gesture near one targets it.
- **Let people initiate object scaling when it makes sense**, as in an imaginary environment, not for a chair in a furniture-shopping app.
- **Regardless of purpose, don't use scaling to adjust an object's distance**; an enlarged distant object still looks far away.
- **Be wary of conflicting gestures**, like two-finger pinch and rotation; test that similar gestures are interpreted properly.
- **Strive for object movement consistent with your AR environment's physics.** People expect moving objects to stay visible, not necessarily smooth over rough surfaces; aim to keep them attached to real surfaces, avoiding jumps or vanishing and reappearing during resize, rotate or move.
- **Explore interaction beyond gestures**, such as motion and proximity.

## Offering a multiuser experience

Each participant maps the environment independently; ARKit merges the maps automatically (`isCollaborationEnabled`).

- **Consider allowing people occlusion** of virtual objects behind people in the camera feed.
- **When possible, let new participants join.** Unless all must join before the experience begins, consider implicit map merging.

## Reacting to real-world objects

ARKit reports when and where it detects your app's 2D reference images or 3D reference objects, so virtual content can appear.

- **When a detected image first disappears, consider delaying removal of attached objects.** ARKit doesn't track detected images' position or orientation changes; consider waiting up to one second before fading out or removing them.
- **Limit reference images in use at one time.** Detection works best with 100 or fewer distinct images; for more, swap the active set by context, such as location.
- **Limit reference images requiring an accurate position**, which costs more resources. Use a tracked image when the image may move, or when an attached animation or object is small relative to it.

## Communicating with people

- **If you must display instructional text, use approachable terminology.** Avoid terms like ARKit, world detection and tracking; use friendly, conversational terms.

|Do|Don't|
|---|---|
|Unable to find a surface. Try moving to the side or repositioning your phone.|Unable to find a plane. Adjust tracking.|
|Tap a location to place the *[name of object to be placed]*.|Tap a plane to anchor an object.|
|Try turning on more lights and moving around.|Insufficient features.|
|Try moving your phone more slowly.|Excessive motion detected.|

- **In a 3D context, prefer 3D hints**, like a rotation indicator around an object. Avoid textual 2D overlay hints unless people aren't responding to contextual hints.
- **Make important text readable.** Put critical labels, annotations and instructions in screen space. Make text in 3D space face people and keep one type size regardless of distance from the labeled object.
- **If necessary, provide a way to get more information**, with a fitting visual indicator that people can tap.

## Handling interruptions

During interruptions, such as app switches or calls, ARKit can't track the device, so placed objects likely appear misplaced afterward. With relocalization support, ARKit attempts to restore their original positions.

- **Consider using the system-provided coaching view to help people relocalize** by returning the device to its previous position and orientation.
- **Consider hiding placed objects during relocalization**, redisplaying them in their new positions.
- **Minimize interruptions if your app supports both AR and non-AR experiences**, e.g. embed non-AR tasks within AR.
- **Allow people to cancel relocalization**, which never ends if the device isn't returned near its prior pose; if coaching fails, consider a reset button or other restart.
- **Indicate when the front-facing camera can't track a face for more than about half a second**, with a visual indicator; keep any text instructions minimal.

## Suggesting problem resolutions

- **Let people reset the experience if it doesn't meet their expectations**; don't force them to wait for better conditions or struggle with placement.
- **Suggest possible fixes if problems occur** and your app is notified of them, in straightforward, friendly language. Causes include insufficient light, reflective or featureless surfaces, and too much camera motion.

|Problem|Possible suggestion|
|---|---|
|Insufficient features detected.|Try turning on more lights and moving around.|
|Excessive motion detected.|Try moving your phone slower.|
|Surface detection takes too long.|Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface.|

## Icons and badges

Controls that launch ARKit-based experiences can show the AR glyph, and apps can badge items viewable in AR using ARKit; get both from [Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps).

- **Use the AR glyph and badges as intended.** Use the glyph strictly to initiate an ARKit-based experience; never alter it other than its size and color. Use the badges (collapsed and expanded) exclusively for items viewable in AR using ARKit; never alter them or change their color. Never use either for other purposes or with non-ARKit AR experiences.
- **Maintain minimum clear space** around the glyph or a badge of 10% of its height; don't let other elements infringe on it or occlude the glyph or badge.
- **Prefer the AR badge (glyph plus "AR") to the glyph-only badge**, which in general is for constrained spaces. Both work well at default size.
- **Use badging only when your app mixes objects that can and can't be viewed in AR.**
- **Keep badge placement consistent and clear**: always the same corner of the photo, clearly visible without occluding important detail.

## Platform considerations

No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS or watchOS.

### visionOS

With the wearer's permission, ARKit can detect surfaces, use hand and finger positions to inform custom gestures, incorporate nearby physical objects into immersive experiences, and more.

## Resources

Developer: `ARKit`.

Source: [Augmented reality](https://developer.apple.com/design/human-interface-guidelines/augmented-reality), captured 2026-09-12.
