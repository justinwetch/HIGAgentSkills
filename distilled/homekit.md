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

> HomeKit lets people control smart home accessories via Siri, the Home app, and third-party apps. Your app must follow HomeKit's object model and terminology exactly.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Object Model and Terminology

| Term | Meaning |
|---|---|
| Home | A physical home, office, or location. One person can have multiple homes. |
| Room | A named physical room. No size/location attributes - name only. |
| Accessory | A connected device (lamp, lock, fan). Assigned to a category (thermostat, fan, light). |
| Service | A controllable feature of an accessory. Never display "service" in UI; use descriptive names. |
| Characteristic | A controllable attribute of a service. Never use in UI; describe it (e.g. "brightness"). |
| Service group | A group of services to control as one unit. |
| Action | Changing a service's characteristic. |
| Scene | A group of actions across multiple services/accessories. Always use "scene" in UI, never "action set". |
| Automation | Triggers actions based on context: time, location, sensor, or other accessory state. |
| Zone | Optional area grouping multiple rooms. Enables commands like "turn off the lights upstairs." |

**Rules:**
- Reference the HomeKit hierarchy even if your app doesn't display it overtly; it matters for Siri voice commands.
- Don't duplicate home settings; defer to the Home app. Don't ask people to set up their home again.
- Recognize multiple homes per user; surface relevant home info in accessory detail views.
- Automatically reflect changes made in the Home app or other HomeKit apps.
- Ask permission before updating the HomeKit database; never overwrite settings without explicit direction.

## Setup

- **Use the system-provided setup flow** - it handles naming, pairing, network joining, room/category assignment, and favorites in one flow.
- **Purpose string**: explain why you need Home data access. Example: "Lets you control this accessory with the Apple Home app and Siri across your Apple devices."
- **Don't require account creation** before HomeKit setup. If cloud services need an account, offer it after setup.
- **Honor people's platform choice** - if they chose HomeKit, don't force cross-platform setup inside the same flow.
- **Present system setup first**, then offer a custom post-setup experience for unique features.

### Naming Rules

Service names must:
- Use only alphanumeric, space, and apostrophe characters.
- Start and end with alphanumeric characters.
- Contain no emoji.
- Never suggest company names or model numbers as service names.
- **Help people avoid or correct room/zone duplication in service names** - duplicated location info can cause voice command ambiguity. Assign accessories to rooms/zones instead.

## Siri Interactions

Siri understands home/room/zone/service/characteristic combinations:

| Example phrase | Siri resolves |
|---|---|
| "Turn on the floor lamp" | Service name |
| "Turn off the living room light" | Room + accessory category |
| "Make the living room a little bit brighter" | Room + brightness characteristic |
| "Turn off the lights upstairs" | Accessory category + zone |
| "Dim the lights in the bedroom and nursery" | Category + characteristic + two rooms |
| "Run Good night" | Scene name |
| "Is my security system tripped?" | Accessory category |
| "It's dark in here" | Current home/room via HomePod + implied category |

- **Demonstrate Siri commands immediately after setup** using the service name the person chose.
- **Teach more complex Siri commands later** - in scene detail views, etc.
- **Only offer shortcuts for functionality HomeKit doesn't already support.** Never offer shortcuts that duplicate what people can do with natural Siri commands.

## Cameras

- Don't block camera images with controls or overlays.
- Show a microphone button only when the camera supports bidirectional audio.

## HomeKit Icon Usage

- Use only Apple-provided HomeKit icon artwork - no custom designs.
- **Icon styles**: Black (on light backgrounds), White (on dark backgrounds), Custom color (match other technology icons).
- Position it consistently with other technology icons.
- **Non-interactive only** - don't use as a button. Use the Apple Home app icon to link to the App Store.
- Don't use inline in text or as a substitute for the word "HomeKit."

## Editorial Rules

- **"HomeKit"** - one word, capital H and K, lowercase letters after. Not possessive, not plural.
- **"Apple Home"** - two words, capital A and H.
- Terms: *works with*, *use*, *supports*, *compatible*, and category phrasing like "HomeKit-enabled thermostat" when appropriate.
- Don't suggest HomeKit is the actor: say "Back door is unlocked with HomeKit," not "HomeKit unlocked the back door."
- Refer to the Apple Home **app** specifically as "Apple Home app" on first mention, then "the Home app."
- Don't indicate Apple sponsorship, partnership, or endorsement.
