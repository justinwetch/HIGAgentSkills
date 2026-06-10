---
topic: tap-to-pay-on-iphone
tier: 3
platforms: [ios]
category: technologies
triggers:
  - "Tap to Pay"
  - "Tap to Pay on iPhone"
  - "contactless payment"
  - "merchant payment"
  - "NFC payment"
  - "point of sale"
  - "ProximityReader"
  - "ProximityReaderDiscovery"
  - "PaymentCardReader.prepare(using:)"
  - "PaymentCardReader.Event.updateProgress(_:)"
  - "returnReadResultImmediately"
  - "readyForTap"
  - "PaymentCardReaderSession.ReadError"
related:
  - apple-pay
  - nfc
---
# Tap to Pay on iPhone

> Tap to Pay on iPhone lets merchants accept contactless payments using an iPhone app, without external payment hardware.

**Platforms:** iOS only

Requires a supported payment service provider, entitlement, ProximityReader APIs, and the provider SDK where applicable.

## Enabling And Onboarding

- **Accept terms before initial device configuration** - present terms before customer-facing checkout, not mid-payment.
- **Only admins see terms** - non-admins get an error; admins can accept elsewhere if needed.
- **Check iOS support before setup.**
- **Use `ProximityReaderDiscovery` when appropriate** for prebuilt localized merchant education.

## Merchant Education

- Launch checkout for each payment type.
- Help customers position card/device for tap.
- Handle PIN entry, including accessibility mode.
- Recover from tap failures and switch payment methods.

Offer education through Learn More, after terms acceptance, for new users, or in help/settings.

## Checkout Flow

- **Always show Tap to Pay on iPhone as a checkout option** - if not enabled, tapping can start setup then continue.
- **Prepare early and often** - call prepare when the app starts and returns to foreground; keep the option available during background configuration.
- **Show setup progress** - usually indeterminate; use determinate progress if ProximityReader reports it.
- **Make it easy to find** - don't require scrolling; if it is the only method, open it automatically.
- **Let merchants switch payment methods** without visiting settings.
- **Finalize amount before opening Tap to Pay** - collect tip, adjustments, and payment type first.
- **Start result processing as soon as possible** - request the read result before/while the checkmark animation completes when the API supports it.

## Labels

- Payment button: **Tap to Pay on iPhone** or **Tap to Pay** in constrained space.
- If it is the only payment method, existing **Charge** or **Checkout** labels can work.
- Multiple-method contexts: use `wave.3.right.circle` or `wave.3.right.circle.fill`.
- Never include the Apple logo in Tap to Pay buttons.
- Non-payment actions (look up, refund, store card, verify): use generic labels, never "Tap to Pay."
- Loyalty/discount cards need separate, clearly labeled actions.

## Results And Errors

- **Display authorization progress after tap completion.**
- **Show clear success/decline results** and offer receipts.
- **Handle failed taps gracefully** - offer another card, alternate tender, payment link, or relaunch Tap to Pay.
- **Surface merchant-actionable errors** - use alerts/support paths for setup, entitlement, PSP, region, account, or reader-session failures.
- Be aware of regional requirements like SCA PIN entry or Offline PIN fallback.
