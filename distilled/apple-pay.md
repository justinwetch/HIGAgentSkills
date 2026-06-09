---
topic: apple-pay
tier: 3
platforms: [ios, ipados, macos, visionos, watchos]
category: technologies
triggers:
  - "Apple Pay"
  - "payment"
  - "checkout"
  - "PKPaymentButton"
  - "Apple Pay wallet"
related:
  - in-app-purchase
  - wallet
---
# Apple Pay

> Apple Pay lets people pay for physical goods and services, donations, and subscriptions securely across iOS, iPadOS, macOS, visionOS, and watchOS.

> **Apple Pay vs. In-App Purchase**: Use Apple Pay for physical goods, services, donations. Use In-App Purchase for virtual goods and digital subscriptions.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

## Offering Apple Pay

- Apple Pay works in apps and any browser. People can authorize with a nearby iPhone or Apple Watch, scan a code, or use device authentication including `Optic ID` where available.
- Web: use `applePayCapabilities`, semantic markup that search engines can index, a privacy statement, and Apple's acceptable-use requirements.
- **Offer on all supported devices.** Use Apple Pay APIs to detect support — don't show the option if the device can't use it.
- **If you use APIs to check for an active card, Apple Pay must be the primary payment option** everywhere you use those APIs.
- **Feature Apple Pay at least as prominently as other payment options** on every page that offers payment methods.
- **Use the Apple-provided API to display the button** — it's always correct and auto-localizes.
- **Custom buttons must not display "Apple Pay" or the Apple Pay logo.** Instead, show the Apple Pay mark or reference Apple Pay in text on that page.
- **Apple Pay buttons: use only to start payment or set-up.** Don't hide or gray the button — if pre-conditions aren't met, reveal the issue after the tap.
- **Apple Pay mark: use only to communicate acceptance**, not as a button.

## Streamlining Checkout

- Keep checkout cohesive; don't open new windows or send people to a separate checkout flow.
- **Present Apple Pay first** — preselect it or display it larger; visually separate it from other options.
- **Add Apple Pay buttons on product detail pages** for single-item quick purchase (exclude cart contents).
- **Express checkout** — immediately display the payment sheet for multi-item purchases.
- **Collect required info (size, color, etc.) before people reach the button.** Gracefully point to missing info after tap.
- **Collect optional info (gift messages, delivery instructions) before or after** checkout — not on the payment sheet.
- **Single shipping method per order.** For multi-destination orders, collect details before checkout begins.
- **In-store pickup**: select location before the payment sheet; display as read-only on the sheet.
- **Prefer info from Apple Pay** as more up-to-date over stored app data.
- **Avoid requiring account creation before purchase.** Offer sign-up on the order confirmation page; pre-fill from payment sheet data.
- **Always display an order confirmation** page after success.

### Payment Sheet Customization

- **Request only essential information.**
- **Display or allow entry of coupon/promo codes** on the sheet.
- **Line items** — explain additional charges, discounts, pending costs, subscriptions, donations. Not an itemized product list. Keep short; fit on one line.
- **Business name after "Pay"** — use the exact name on the bank statement. E.g., *Pay [Business_Name]*.
- **If you're a marketplace/intermediary** — name both businesses: *Pay [End_Merchant] (via [Your_Business])*.
- **Pending amounts** — clearly disclose; use Amount Pending.
- **Shipping methods** — show description, cost, and estimated delivery date; use shipping method's calendar/timezone support (iOS 15+).

### Error Handling

- Validate data at sheet-appear time and on field changes.
- **Error messages**: specific, field-referencing, ≤128 characters. Noun phrases, sentence-case, no punctuation. E.g., "Zip code doesn't match city."
- **Don't force compliance with business logic that can be inferred** — accept Zip+4 if you need 5-digit, accept multiple phone formats.
- **Handle interruptions (cancel, timeout) by cancelling in-progress payment.**

## Subscriptions and Donations

- For trials, use line items to show free trial period, discount duration, and first paid renewal. Avoid billing-agreement fields that contradict the sheet's line items.
- **Subscriptions**: clarify billing frequency before the payment sheet. Line items reiterating frequency, discounts, and upfront fees. Show payment amount clearly in the total.
- **Only show the payment sheet when a subscription change adds fees.**
- **Donations**: use a line item to label the donation (e.g., *Donation $50.00*). Offer predefined amount buttons + Other Amount.

## Apple Pay Buttons

### Button Types

| Button type | Use when |
|---|---|
| Apple Pay | General purchase |
| Buy with Apple Pay | Product purchase |
| Pay with Apple Pay | Bill or invoice payment |
| Check Out with Apple Pay | Cart with "Check Out"-labeled buttons |
| Continue with Apple Pay | Cart with "Continue with"-labeled buttons |
| Book with Apple Pay | Travel/experiences booking |
| Donate with Apple Pay | Approved nonprofit donations |
| Subscribe with Apple Pay | Subscriptions |
| Reload with Apple Pay | Adding money ("reload" terminology) |
| Add Money with Apple Pay | Adding money ("add money" terminology) |
| Top Up with Apple Pay | Adding money ("top up" terminology) |
| Order with Apple Pay | Placing orders (meals, flowers, etc.) |
| Rent with Apple Pay | Rentals (cars, scooters, etc.) |
| Support with Apple Pay | Giving to projects/causes |
| Contribute with Apple Pay | Contributing to projects/causes |
| Tip with Apple Pay | Tipping |
| Apple Pay (plain) | Style-constrained contexts; fallback for unsupported types |

**Set up Apple Pay button** — display on Settings, profile, or interstitial pages when the device supports Apple Pay but hasn't been set up.

API style names include `PKPaymentButtonStyle.automatic` and `ApplePayButtonStyle`.

### Button Styles

| Style | Use on |
|---|---|
| Black | White or light backgrounds with sufficient contrast |
| White with outline | White or light backgrounds without sufficient contrast |
| White | Dark backgrounds with sufficient contrast |

### Button Sizing

| Button | Min width | Min height | Min margin |
|---|---|---|---|
| Apple Pay | 100 pt (100 px @1x, 200 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 button height |
| Book with Apple Pay | 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 button height |
| Buy with Apple Pay |  |  |  |
| Check Out with Apple Pay |  |  |  |
| Donate with Apple Pay |  |  |  |
| Set Up Apple Pay |  |  |  |
| Subscribe with Apple Pay |  |  |  |

- **Side-by-side**: Apple Pay button to the right of Add to Cart.
- **Stacked**: Apple Pay button above Add to Cart.
- Adjust corner radius to match other buttons (default: rounded; supports square and capsule).
- If translated title won't fit the specified size, system falls back to plain Apple Pay button.

## Apple Pay Mark

- **Use only for indicating acceptance, not as a payment button.**
- Use only Apple-provided artwork — no alterations except height.
- Height must be ≥ other payment brand marks.
- Don't adjust width/corner radius/aspect ratio; don't add trademark symbol; don't remove border; no effects (shadows, glows, reflections); don't flip, rotate, or animate.
- **Minimum clear space**: 1/10 of its height; don't share border with other graphics.

## Website Icon

Provide these sizes for the summary view and authorizing-device payment sheet:

| Scale | Size |
|---|---|
| @2x | 60×60 pt (120×120 px) |
| @3x | 60×60 pt (180×180 px) |

## Editorial Rules

- Always "Apple Pay" (title case, two words). Never plural or possessive.
- In body text (US): include ® on first appearance.
- Don't translate "Apple Pay." Always English.
- Don't use the Apple logo to represent "Apple" in text.
- APPLE PAY (all caps) only when your UI capitalizes all text.
