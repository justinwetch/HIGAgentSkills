---
topic: nfc
tier: 4
platforms: [ios, ipados]
category: technologies
triggers:
  - "NFC"
  - "near field communication"
  - "Core NFC"
  - "tag reading"
related: []
---
# NFC

Near-field communication lets devices within a few centimeters exchange information wirelessly. On supported devices, iOS apps can read electronic tags attached to real objects—for example, scanning a toy to connect it to a game, a store sign for coupons, or products for inventory.

## In-app tag reading

When active, an app can scan one or multiple objects and show a scanning sheet before each scan. A device only needs to be close to the tag; it needn’t touch it. Use terms like *scan* and *hold near* instead of *tap* and *touch* when instructing people. Prefer approachable object-based language over technical terms such as *NFC*, *Core NFC*, *near-field communication*, and *tag*:

| Use | Don’t use |
|---|---|
| “Scan the [object name].” | “Scan the NFC tag.” |
| “Hold your iPhone near the [object name] to learn more about it.” | “To use NFC scanning, tap your phone to the [object].” |

Scanning-sheet instructions should be a short, complete, sentence-case sentence with ending punctuation, identify the object, and avoid truncation. Revise for repeat scans:

| First scan | Subsequent scans |
|---|---|
| “Hold your iPhone near the [object name] to learn more about it.” | “Now hold your iPhone near another [object name].” |

## Background tag reading

On supporting devices, background reading looks for compatible tags whenever the screen is illuminated, without opening the app. After matching a tag to an app, the system shows a notification that the person can tap to send tag data to that app. It is unavailable while an NFC scanning sheet is visible, Wallet or Apple Pay is in use, cameras are in use, Airplane Mode is enabled, or the device is locked after a restart. Provide in-app scanning too, because some devices don’t support background reading.

No additional considerations apply to iOS or iPadOS; NFC is unsupported in macOS, tvOS, visionOS, and watchOS.

Source: [Apple Human Interface Guidelines — NFC](https://developer.apple.com/design/Human-Interface-Guidelines/nfc), captured 2026-09-12.
