---
topic: homekit
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "HomeKit"
  - "Home app"
  - "smart home"
  - "accessory"
  - "scene"
  - "automation"
  - "performAccessorySetup(using:completionHandler:)"
related:
  - siri
  - app-shortcuts
---

# HomeKit

HomeKit lets people securely control connected home accessories with Siri or the Home app on iPhone, iPad, Apple Watch and Mac; in iOS, the Home app also manages and configures them. iOS, tvOS and watchOS apps can integrate with it. MFi licensees: see the [MFi portal](https://mfi.apple.com) for packaging naming and messaging.

## Terminology and layout

It's crucial to use HomeKit's terms and object model: each home (home, office or other relevant location) roots a hierarchy of all other objects, such as rooms, accessories and zones.

- **Acknowledge the hierarchy**, even if your UI doesn't organize by rooms and zones; people need accessory locations for voice control.
- **Make related HomeKit details easy to find, and recognize that people can have multiple homes.** In an accessory-based app, don't hide an accessory's zone, room or other HomeKit details in a hard-to-discover settings screen. Consider showing them, and the relevant home even if your app doesn't support multiple homes, in an accessory detail view.
- **Don't present duplicate home settings** or ask people to set up all or part of their homes again, even if your app organizes homes differently. Always defer to Home app settings and present them intuitively.

|Term|Meaning|
|---|---|
|Room|Just a name; no size or location|
|Category|Accessory type, typically manufacturer-assigned; your app can help if necessary (a switch must share its controlled accessory's category)|
|Service|Controllable feature; an accessory can have several. Siri users say its name, not the accessory's|
|Characteristic|Controllable service attribute (speed, brightness)|
|Service group|Services controlled as a unit|
|Action|Characteristic change, by people or automation|
|Scene|Actions across one or more services and accessories; API: *action set*, but always say *scene* in UI|
|Automation|Accessory reactions to situations like location, time, other accessories or sensors|
|Zone|Optional multiroom area (upstairs) for controlling many accessories at once|

UI uses descriptive names (*ceiling fan light*, *brightness*), not *service* or *characteristic*.

## Setup

- **Use the system-provided setup flow** (`performAccessorySetup(using:completionHandler:)`).
- **Explain why you need Home data** in a purpose string ("Lets you control this accessory with the Apple Home app and Siri across your Apple devices.").
- **Don't require an account or personal information**; defer to HomeKit. Make any account for extra services like cloud optional, offered only after initial HomeKit setup.
- **Honor setup choices**: don't force people choosing HomeKit setup to set up other platforms during it.
- **Carefully consider custom setup.** Always begin with the system flow; offer a custom post-setup experience for unique features once basic functionality is available.

### Help people choose useful names

- **Suggest suitable service names**, recommending alternatives that work well for most people when you detect one that's suboptimal for Siri. Never suggest company names or model numbers.
- **If people can rename services in your app, make sure names follow HomeKit rules** (the system flow checks originals): only alphanumeric, space and apostrophe characters; alphanumeric first and last characters ("2nd garage door", not "#2 garage door"); no emojis. Briefly explain violations and suggest alternatives.
- **Help people avoid location in names**: "kitchen light" can make voice control unpredictable. Your app can detect this and, for example post-setup, remove the room or zone from the name and encourage assigning the accessory to it.

## Siri interactions

- **Present example voice commands during setup**: as soon as it completes, consider a few Siri phrases using the chosen service name, and encourage people to try them.
- **After setup, consider teaching more complex Siri commands** in useful places (in a scene detail view, "You can say 'Hey Siri, set Movie Time'").

Siri recognizes home, room, zone, service, service group and scene names, alone or combined, and can identify an unnamed service by category and characteristic ("dim" means brightness). It also answers status questions, even when category and characteristic are only implied ("Is someone in the living room?"). "Here" means the current home and, via HomePod, the current room.

- **Recommend zones and service groups if they make sense for your accessory**, and help people set them up ("upstairs", "media center").
- **Offer shortcuts only for accessory-specific functionality HomeKit doesn't support** ("Order AC filters"); shortcuts duplicating HomeKit's configuration-free natural language confuse people.
- **If you support both HomeKit and shortcuts, help people understand the difference.** Be sure to clearly indicate what shortcuts can do; never encourage a shortcut for a scene or action HomeKit already supports.

## Custom functionality

- **Be clear about what people can do in your app and when they might want the Home app.** For example, a lights-only app can guide people to create a scene with only its actions, then suggest adding shades and a TV to it in the Home app.
- **Defer to HomeKit when your database differs**, automatically reflecting changes from the Home app or other third-party HomeKit apps. If you must ask people to manage conflicts, present them visually (old and new names side by side).
- **Ask permission, or an indication of intent, before writing your app's changes to the HomeKit database.** Never overwrite its settings without a person's explicit direction.

### Cameras

- **Don't block camera images.** Supplementary features like activity alerts are fine; avoid covering portions of the images.
- **Show a microphone button only if the camera supports bidirectional audio.**

## Using HomeKit icons

Use the HomeKit icon in HomeKit setup or instructional communications. You can use the Apple Home app icon to reference the app or in a button opening its App Store [product page](https://itunes.apple.com/us/app/home/id1110145103?mt=8).

- **Use only [Apple-provided icons](https://developer.apple.com/design/resources/)**; don't create or mimic HomeKit or Home app icons.
- Use the black icon on white or light backgrounds when other technology icons are black, the white icon on black or dark backgrounds when they're white, and a custom color when they share it.
- **Position it consistently with other technology icons**, within shapes if they use them.
- **Use it noninteractively**: neither the icon nor the name *HomeKit* in custom interactive elements or buttons.
- **Don't use it within text or in place of the word HomeKit**; it can lead a line.
- **Pair it with the name *HomeKit* correctly**: you can place the name below or beside it if other technologies appear that way; use your layout's font.

## Referring to HomeKit

- **Emphasize your app over HomeKit**: make HomeKit or Apple Home references less prominent than your app name or identity.
- **Adhere to Apple's trademark guidelines.** Apple trademarks can't appear in your app name or images. In text, use Apple product names exactly as on the [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html), and:
  - Singular only, never possessive.
  - Don't translate Apple, Apple Home, HomeKit or any Apple trademark.
  - No category descriptors (iPad, not tablet).
  - Don't imply sponsorship, partnership or endorsement from Apple.
  - Attribute all Apple trademarks with correct credit lines wherever your app shows legal information.
  - Mention Apple devices and operating systems only in technical specifications or compatibility descriptions ("iPhone or iPad", not "iOS devices").

### Referencing HomeKit and the Home app

- **Capitalize correctly**: *HomeKit*, *Apple Home*. If your layout displays only all-uppercase designations, they can be all uppercase.
- **Don't use *HomeKit* as a descriptor**; use terms like *works with*, *use*, *supports* or *compatible*. "HomeKit-enabled thermostat" is fine; "HomeKit lightbulbs" isn't.
- **Don't suggest that HomeKit performs an action or function**: "Back door is unlocked with HomeKit", not "HomeKit unlocked the back door".
- If desired, say "Apple HomeKit" and use *HomeKit* in setup, configuration and instructions ("Open HomeKit settings").
- **Use *Apple Home* whenever referring specifically to the app**, in full on first body-copy mention; later mentions can say "the Home app". Not "Open Home".

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

## Resources

Developer: `HomeKit`.

Source: [HomeKit](https://developer.apple.com/design/human-interface-guidelines/homekit), captured 2026-09-12.
