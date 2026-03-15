---
topic: wallet
tier: 3
platforms: [ios, ipados, macos, visionos]
category: technologies
triggers:
  - "Wallet"
  - "pass"
  - "boarding pass"
  - "loyalty card"
  - "PKPass"
  - "PassKit"
related:
  - apple-pay
  - in-app-purchase
---
# Wallet

> Wallet securely stores credit/debit cards, driver's licenses, transit cards, event tickets, keys, and more, presenting them when most needed.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

## Passes

- **Offer to add new passes immediately** after they're created (check-in, ticket purchase, rewards sign-up). Use system-provided UI; one tap to add.
- **Add related passes as a group** (e.g., multi-leg boarding passes) — don't ask people to add each one individually.
- **Display an "Add to Apple Wallet" button** wherever pass info appears for passes not yet in Wallet.
- **Offer "View in Wallet"** wherever you display info about a pass already in Wallet.
- **Set expiration, relevantDate, and voided** on each pass so Wallet hides expired passes correctly.
- **Always get permission before deleting a pass** from Wallet.
- **Supply relevancy context** (location, time) so passes surface automatically on the Lock Screen at the right moment.
- **Update passes for time-critical info** (gate changes, delays). Use change messages only for updates people need immediately — not marketing or phone number changes.

## Designing Passes

- **Great on all devices** — essential info must not be in elements unavailable on some devices (e.g., Apple Watch omits some images). No device-specific language ("slide to view").
- **Instantly identifiable** — use brand color; ensure content is readable against the background.
- **Front: only essential info.** Top-right area stays visible when collapsed. Use the back (iOS) or details screen (watchOS) for extra info.
- **Prefer NFC.** If you support both NFC and barcode, barcode goes on the back (or watchOS details screen). QR/barcode can appear on the front if necessary for your design.
- **No text embedded in images** — not accessible and not shown on all devices.
- **Reduce image file sizes** for fast delivery via email/web.
- **No custom fonts** if they impair readability.

### Pass Styles

| Style | Use for | Images supported | Fields |
|---|---|---|---|
| Boarding pass | Train/airline tickets, transit passes | Logo, footer | Up to 2 primary, 5 auxiliary |
| Coupon | Coupons, offers, discounts | Logo, strip | 4 secondary/auxiliary on one row |
| Store card | Loyalty, discount, points, gift cards | Logo, strip | 4 secondary/auxiliary on one row |
| Event ticket | Concerts, sports, movies; seasonal | Logo + strip OR background + thumbnail (not both) | Primary, secondary, auxiliary + extra row of 4 auxiliary |
| Generic | Gym memberships, coat-check, etc. | Logo, thumbnail | 4 secondary/auxiliary on one row |

**Pass field areas:**

| Field | Area | Use for |
|---|---|---|
| Header | Essential (stays visible when collapsed) | Critical info |
| Primary | Primary | Important usage info |
| Secondary / Auxiliary | Secondary / Auxiliary | Useful but not every-use info |
| Back | Not on pass front | Supplemental details |

Up to 3 header fields, 1 primary, 4 secondary, 4 auxiliary (some may be hidden based on content length).

#### Poster Event Tickets (iOS 18+)

- Contactless only — **not compatible with QR code / barcode entry**.
- Displays event logo + background image; optional issuer/event company logo.
- System generates Maps shortcut to venue, event guide (weather, venue map, quick actions, food ordering), and additional ticket info (e.g., pre-paid parking).
- **Background image**: the centerpiece. Limit text in artwork. Easy-to-identify imagery.
- **Safe area**: position content away from header and footer overlaps. System applies gradient (header) + blur (footer) for contrast — adjust if needed. System auto-selects text color; if you override, check contrast.
- Consider setting footer background color to blend background image with footer.
- **Continue to support legacy event ticket fields** — the system auto-generates the right style per device version.

### Passes on Apple Watch

Wallet shows a scrolling carousel of cards on Apple Watch. Details screen shows additional info. watchOS crops strip image to card aspect ratio, and may crop white space from other images. Put essential info on the front regardless of device.

## Order Tracking

Wallet can display real-time order status and fulfillment details, updated via the WalletOrders schema.

- **Add order automatically** via PKPaymentOrderDetails (app) or ApplePayPaymentOrderDetails (web) at Apple Pay transaction completion.
- **Display Track with Apple Wallet button** (AddOrderToWalletButton) in order confirmation, status/tracking pages, and emails.
- **Make info available immediately** after order placement — even if payment is pending.
- **Logo image**: 300×300 px, PNG or JPEG, non-transparent background.
- **Product images**: 300×300 px, PNG or JPEG, non-transparent solid background (no lifestyle shots).
- Keep all text brief; use clear, approachable language; localize; match final confirmed price.
- **Fulfillment**: supply carrier name, use specific status values (`onTheWay`, `outForDelivery`, `delivered`) when you have interim shipping steps; use `shipped` when you don't. Always provide a tracking link when available.
- **Issue or Canceled status**: be direct about reason and recommended action.
- **Avoid sending duplicate notifications** — suppress Wallet notifications when your app is installed and handles its own.

## Identity Verification (Wallet)

Apps can request identity verification via Wallet using a "Verify with Wallet" button (iOS 16+).

- **Show only if the device supports it.** Provide a fallback for unsupported devices.
- **Ask only at the precise moment verification is needed** — not before people start the process or during account creation.
- **Purpose strings**: brief, complete sentence, direct, specific, sentence-case, include a period. E.g., "Federal law requires this information to verify your identity and also to help [App Name] prevent fraud."
- **Ask only for the data you actually need.** For age checks, use an age threshold — not birth date.
- **Disclose data retention clearly** — specify whether you keep it and for how long.

**Verify with Wallet button labels:**

| Label | Use when |
|---|---|
| Verify Age | Completing a transaction requiring age verification (e.g., leasing a car) |
| Verify Identity | Completing a transaction requiring identity verification (e.g., car rental) |
| Continue | Verification is one part of a larger flow (e.g., also requires SSN or phone number) |
| [Unlabeled/Other] | No other label applies (e.g., government service sign-up) |

All labels available in multiline for constrained widths. Always white text on black background; optional light outline for dark backgrounds. Adjust `cornerRadius` to match other buttons.

## Specifications — Pass Image Dimensions

| Image | Supported styles | Filename | Max dimensions (pt) |
|---|---|---|---|
| Logo | Boarding, coupon, store card, event ticket, generic | `logo.png` | 160×50 |
| Primary logo | Poster event ticket | `primaryLogo.png` | 126×30 |
| Secondary logo | Poster event ticket | `secondaryLogo.png` | 135×12 |
| Icon | All | `icon.png` | 38×38 (exact) |
| Background | Event ticket | `background.png` | 180×220 |
| Artwork | Poster event ticket | `artwork.png` | 358×448 |
| Strip | Coupon, store card | `strip.png` | 375×144 |
| Strip | Event ticket | `strip.png` | 375×98 |
| Footer | Boarding pass | `footer.png` | 286×15 |
| Thumbnail | Event ticket, generic | `thumbnail.png` | 90×90 |

Logo, primary logo, secondary logo dimensions are **maximum** values — don't add padding to reach them.
