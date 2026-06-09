---
topic: wallet
tier: 3
platforms: [ios, ipados, macos, visionos, watchos]
category: technologies
triggers:
  - "Wallet"
  - "pass"
  - "boarding pass"
  - "poster generic pass"
  - "poster event ticket"
  - "semantic tags"
  - "Pass Designer"
  - "PKPass"
  - "PassKit"
  - "WalletOrders"
  - "FinanceKit"
  - "FinanceKitUI"
  - "VerifyIdentityWithWalletButton"
  - "PKIdentityButton"
related:
  - apple-pay
  - in-app-purchase
  - id-verifier
---
# Wallet

> Wallet stores passes, payment cards, IDs, keys, orders, and tickets, presenting them when people need them.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

## Passes

- **Offer to add new passes immediately** after creation. Use system UI for one-tap add; background-add only after one-time authorization for frequent predictable passes.
- **Add related passes as a group** - e.g., multi-leg boarding passes or a set of event tickets.
- **Display Add to Apple Wallet / View in Wallet** wherever pass info appears.
- **Supply relevance context** (time/location) so passes surface on the Lock Screen; event tickets can also start a Live Activity.
- **Keep passes up to date** for time-critical info like gate, delay, venue, or balance changes.
- **Always get permission before deleting a pass** from Wallet.

## Designing Passes

Use **Pass Designer** to design and preview passes from Apple templates or a blank pass. It supports boarding passes, coupons, event tickets, store cards, generic passes, and poster generic passes.

- **Use semantic tags where required** - poster event and semantic boarding passes require semantic tags for automatic layout; include pass fields too for older iOS versions.
- **Keep the front uncluttered** - put essential, glanceable information in header/primary areas; move rarely used details to the additional information sheet.
- **Reserve images for visual content** - don't embed text or barcodes in images; text belongs in fields/semantic tags, barcodes in pass APIs.
- **Design for every device** - essential information must survive watchOS cropping and omitted image areas.
- **Use brand color and readable contrast**; avoid custom fonts that reduce legibility.

### Pass Styles

| Style | Use |
|---|---|
| Boarding pass | Travel/transit tickets. Use semantic tags for airline boarding passes |
| Coupon | Offers, discounts, redeemable promotions |
| Store card | Loyalty, points, rewards, gift cards |
| Event ticket | Concerts, sports, movies, plays; poster event style supports full-art backgrounds |
| Generic | Memberships, coat check, or flexible non-category passes |
| Poster generic | Full-art generic pass for cases that don't fit other styles |

### Poster Styles

- **Poster event tickets** use full-art backgrounds, semantic tags, and optional issuer/event logos.
- **Poster generic passes** use a full background image with a distinct layout for flexible use cases.
- Keep artwork text-light and account for safe areas; material strips and barcodes can cover bottom areas.
- Use Pass Designer to verify layout and image placement.

## Order Tracking

Wallet displays active/completed orders using the `WalletOrders` schema.

- Add orders via `PKPaymentOrderDetails` / `ApplePayPaymentOrderDetails` after Apple Pay checkout, or show `AddOrderToWalletButton`.
- Provide order data immediately after purchase, even if some details are pending.
- Keep fulfillment status current and use precise shipping values when known (`onTheWay`, `outForDelivery`, `delivered`; use `shipped` when details are limited).
- Use 300x300 px nontransparent merchant logos and product images.
- Provide order-management links, contact methods, tracking links, pickup barcodes, and clear status descriptions.
- Avoid duplicate notifications when your own app already notifies about the same order.

## Identity Verification

Use Wallet identity verification only at the moment a transaction or process actually requires it.

- Show Wallet verification only on supported devices; provide fallback verification.
- Explain why data is needed with a direct, complete purpose string.
- Request only necessary data; for age checks, prefer an age threshold over birth date.
- Disclose retention clearly.
- Use the system Verify with Wallet button (`VerifyIdentityWithWalletButton`, `PKIdentityButton`) and appropriate labels: Verify Age, Verify Identity, Continue, or unlabeled/other.

## Specifications - Pass Images

| Image | Supported styles | Filename | Max dimensions (pt) |
|---|---|---|---|
| Logo | Non-semantic airline boarding, non-airline boarding, coupons, non-poster event, generic, store card | `logo.png` | 160x50 |
| Primary logo | Airline boarding, poster event, poster generic | `primaryLogo.png` | 126x30 |
| Secondary logo | Poster event | `secondaryLogo.png` | 135x12 |
| Icon | All | `icon.png` | 38x38 exact |
| Strip | Coupon, store card | `strip.png` | 375x144 |
| Thumbnail | Event ticket, generic | `thumbnail.png` | 60-90x90 |
| Background | Non-poster event ticket | `background.png` | 343x503 |
| Poster artwork | Poster event, poster generic | `artwork.png` | 358x448 |
| Footer | Airline boarding | `footer.png` | 268x15 |

Logo-style dimensions are maximums; don't add padding just to reach them.
