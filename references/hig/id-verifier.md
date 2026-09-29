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

ID Verifier (iOS 17+) lets an iPhone app read ISO18013-5 compliant mobile IDs in person without external hardware.

## Request types

- **Display Only** (`MobileDriversLicenseDisplayRequest`): system UI on the requester's iPhone shows data like name or age with the portrait for visual confirmation; the customer's data isn't sent to your app.
- **Data Transfer** (`MobileDriversLicenseDataRequest`, `MobileDriversLicenseRawDataRequest`): use only when you have a legal verification requirement and need to store or process data like address or birth date. Requires an additional [entitlement](https://developer.apple.com/wallet/id-verifier/).

## Best practices

- **Ask only for the data the current verification needs.** For a minimum age, request an age threshold (`ageAtLeast(_:)`); avoid requesting current age or birth date.
- **If your app qualifies for [Apple Business Register](https://register.apple.com/services/login?returnTo=/signin/tap-to-present-id-on-iphone), register for ID Verifier** so customers' devices show your official organization name and logo.
- **Provide a button that starts verification**, labeled like Verify Age for a simple age check or Verify Identity for a more detailed identity request. Avoid NFC, QR or other communication-type symbols. Never include the Apple logo in any button label.
- **In a Display Only request, help your app's user give feedback on their visual confirmation**; you might offer Matches Person and Doesn't Match Person buttons that return an approved or rejected value.

## Platform considerations

No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS or watchOS.

## Resources

Developer: `ProximityReader`

Source: [ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier), captured 2026-09-12.
