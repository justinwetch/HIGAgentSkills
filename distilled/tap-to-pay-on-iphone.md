---
topic: tap-to-pay-on-iphone
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Tap to Pay"
  - "contactless payment"
  - "merchant payment"
  - "NFC payment"
  - "point of sale"
related:
  - apple-pay
  - nfc
---
# Tap to Pay on iPhone

> Tap to Pay on iPhone lets merchants accept contactless payments — credit/debit cards, Apple Pay, NFC passes — using just an iPhone app, no external hardware.

**Platforms:** iOS only

## Enabling & Onboarding

- **Terms and conditions must be accepted before initial device configuration.** Present the acceptance flow before customer-facing activity starts — not mid-checkout.
- **Only show terms to administrative users.** Non-admins get an error message; admins can accept via a web interface or separate app if needed.
- **Ensure device is on the required iOS version** before presenting terms.

### Educating Merchants

Provide a tutorial showing:
- Launching a checkout flow for each payment type.
- Helping customers position their card/wallet for payment.
- Handling PIN entry (including accessibility mode).

Offer the tutorial via: a Learn More option, automatically after terms acceptance, automatically for new users, or in the help/settings area.

Can use ProximityReaderDiscovery API for a pre-built, localized merchant education experience instead of building your own.

## Checkout Flow

- **Always show Tap to Pay on iPhone as a checkout option**, whether or not the feature is enabled. If it's not enabled, tapping the button presents terms then proceeds.
- **Minimize wait times.** Prepare (configure) the feature as soon as the app starts and after every return to foreground.
- **Make the Tap to Pay option available even during background configuration.** Show a progress indicator (indeterminate usually; determinate if ProximityReader API indicates ongoing config).
- **Easy to find** — don't make merchants scroll. If it's the only payment method, open it automatically when checkout begins.
- **Let merchants switch between Tap to Pay and hardware accessories** without visiting settings.
- **Determine final amount before opening the Tap to Pay screen.** Collect tipping and other adjustments beforehand.
- **Pre-payment selections** (payment type, etc.) are shown in your checkout screen between the tap of the Tap to Pay button and the opening of the Tap to Pay screen.

### Button Labels

- **Payment button**: "Tap to Pay on iPhone" (full) or "Tap to Pay" (constrained space).
- **If it's your only method**, you may reuse existing "Charge" or "Checkout" buttons.
- **Icon for multiple-method contexts**: use `wave.3.right.circle` or `wave.3.right.circle.fill` SF Symbols.
- **Never include the Apple logo** in Tap to Pay on iPhone buttons.
- **Non-payment actions** (look up, refund, store card): use generic labels — "Look Up," "Store Card," "Verify," "Refund." **Never** use "Tap to Pay on iPhone" or "Tap to Pay" for non-payment actions.
- **Loyalty card transactions**: use a separate, clearly labeled button. Avoid payment-related terms.

## Displaying Results

- **Start processing immediately** — use the API to request the result before the checkmark animation finishes.
- **Display a progress indicator during authorization** — begins after the Tap to Pay checkmark animation finishes.
- **Clearly display the result** — success or decline (with reason). Offer digital receipt options (QR, text).
- **Handle failed taps gracefully** — offer alternate payment (cash, hardware, payment link) or relaunch Tap to Pay for another card.
- Be aware of regional requirements: SCA may require PIN entry after initial tap; Offline PIN markets may require PIN fallback.

## Additional Interactions

When reading a payment card with no transaction amount (look up, refund, store card):
- Use generic button labels only — never "Tap to Pay on iPhone" / "Tap to Pay."

For loyalty/discount/points cards in Wallet: Tap to Pay can read them alongside or independently of payment.
