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

> NFC (Near-Field Communication) lets iOS apps read data from electronic tags on real-world objects within a few centimeters.

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

## In-App Tag Reading

- Supports single- or multiple-object scanning while the app is active.
- **Don't encourage contact.** Proximity is enough — no touching required. Use *scan* and *hold near*, not *tap* and *touch*.
- **Use approachable terminology** — avoid technical terms in UI:

| ✅ Use | ❌ Don't use |
|---|---|
| "Scan the [object name]." | "Scan the NFC tag." |
| "Hold your iPhone near the [object] to learn more about it." | "To use NFC scanning, tap your phone to the [object]." |

- **Scanning sheet instructional text**: complete sentence, sentence case, ending punctuation. Identify the object. Update text for subsequent scans:

| First scan | Subsequent scan |
|---|---|
| "Hold your iPhone near the [object name] to learn more about it." | "Now hold your iPhone near another [object name]." |

## Background Tag Reading

- Background reading scans when the screen is illuminated.
Background tag reading notifies users when a tag is detected without opening your app — they tap the notification to pass data to your app.

**Not available when**: NFC scanning sheet is visible; Wallet/Apple Pay in use; camera in use; Airplane Mode; device locked after restart.

- **Always provide in-app scanning too** — not all devices support background reading.
