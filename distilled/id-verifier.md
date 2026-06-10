---
topic: id-verifier
tier: 4
platforms: [ios]
category: technologies
triggers:
  - "ID verification"
  - "identity document"
  - "driver license"
  - "mobile ID"
  - "MobileDriversLicenseDisplayRequest"
  - "MobileDriversLicenseDataRequest"
  - "MobileDriversLicenseRawDataRequest"
  - "ageAtLeast(_:)"
  - "ProximityReader"
related:
  - wallet
---
# ID Verifier

> ID Verifier lets your iPhone app read ISO 18013-5 compliant mobile IDs in person, without external hardware. Available in iOS 17+.

**Platforms:** iOS only

## Request Types

| Type | How it works | Transmits data to app? |
|---|---|---|
| Display Only | Shows name, age threshold result, or portrait in system-provided UI on the requester's iPhone | No — data stays within system UI |
| Data Transfer | Transfers data (address, date of birth) to your app | Yes — requires additional entitlement |

Use Data Transfer only if you have a legal verification requirement to store or process that data.

## Best Practices

- **Ask only for the data you need.** For age verification, use a age-threshold request — not birth date or current age.
- **Register with Apple Business Register if your app qualifies** to display your official organization name and logo to customers during the verification UI.
- **Provide a clearly labeled button** to initiate the verification process. Use "Verify Age" or "Verify Identity." Don't include NFC/QR symbols. Never include the Apple logo.

### Button Labels

| Button | Use when |
|---|---|
| Verify Age | Checking minimum age for an event or venue |
| Verify Identity | Verifying specific identity info (e.g., name + birth date for car rental pickup) |

- **Display Only**: provide `Matches Person` / `Doesn't Match Person` buttons so your app can record the reviewer's visual confirmation result.
