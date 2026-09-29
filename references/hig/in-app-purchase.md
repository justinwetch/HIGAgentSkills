---
topic: in-app-purchase
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "in-app purchase"
  - "IAP"
  - "StoreKit"
  - "subscription"
  - "paywall"
  - "Advanced Commerce API"
  - "AdvancedCommerceAPI"
  - "canMakePayments"
  - "beginRefundRequest(for:in:)"
  - "presentOfferCodeRedeemSheet(in:)"
  - "offerCodeRedemption(isPresented:onCompletion:)"
  - "Product.SubscriptionInfo"
  - "showManageSubscriptions(in:)"
related:
  - apple-pay
---
# In-App Purchase

In-App Purchase lets people securely buy virtual goods in an app: premium content/features, digital items, and subscriptions. Use [Apple Pay](https://developer.apple.com/design/Human-Interface-Guidelines/apple-pay) for physical goods, real-world services (such as tickets, hotel reservations, or memberships), and donations. Developer starting point: [StoreKit In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase).

## Product types and general experience

| Type | Meaning |
|---|---|
| Consumable | Depletes with use (for example, lives or gems); may be bought again. |
| Non-consumable | Permanent purchase (for example, premium features); does not expire. |
| Auto-renewable subscription | Ongoing virtual content, services, or features; renews each period until canceled. |
| Non-renewing subscription | Time-limited content/service (for example, a battle pass); people repurchase to extend access. |

Let people experience the app before asking for payment; consider limited free access for subscriptions. Keep browsing, product presentation, and transactions integrated with the app’s visual style. Use short, plain names and descriptions that do not truncate or wrap. Display the total billing price for every purchase type. Show the store only when people can make payments; check [`canMakePayments`](https://developer.apple.com/documentation/storekit/appstore/canmakepayments), a Boolean indicating whether the person can make purchases. If restrictions such as parental controls prevent payment, consider hiding the store or displaying UI that explains why it is unavailable. Use the system confirmation sheet unchanged; do not reproduce or modify it.

You can promote and offer In-App Purchases directly through the App Store. For exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or subscriptions with optional add-ons sold as one purchase, the [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) (`AdvancedCommerceAPI`; [developer documentation](https://developer.apple.com/documentation/advancedcommerceapi)) lets you manage the In-App Purchase catalog directly.

## Family Sharing

Family Sharing can share eligible purchased content, including auto-renewable subscriptions and non-consumable purchases, with up to five additional family members across the purchaser’s Apple devices. Call out sharing where people learn about an item (for example, “Family” or “Shareable” in a name and on the sign-up screen). Explain the benefit and participation: when sharing is enabled, Apple may notify an existing subscriber whose sharing setting is off (the default) and may notify family members receiving shared content; notification behavior depends on current settings. Tailor in-app wording to both audiences, such as “Your family subscription includes…”. See [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/) for notification details.

## Purchase help and refunds

Offer a purchase-help screen before the refund flow. It can address missing purchases, FAQs, feedback, and direct support, while linking to the system refund flow. Label the action simply (“Refund” or “Request a Refund”); people request the refund from Apple, so the system flow needs no repeated explanation. Help people locate a purchase with contextual details such as product image, name, description, and original purchase date. Consider immediate fulfillment or a conciliatory item when content is missing, but keep the refund option clear. Put the refund action where it is visible without scrolling or another screen. Use [`beginRefundRequest(for:in:)`](<https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph>) to present the sheet for a specified transaction in a window scene.

Do not characterize or predict Apple’s refund policy. Link to [Request a refund for apps or content that you bought from Apple](https://support.apple.com/en-us/HT204084) for process information.

## Auto-renewable subscriptions

Call out benefits during onboarding with a strong call to action and a concise terms summary. Offer choices among content, service levels, and durations. Consider freemium access, a metered paywall, or a free trial, and prompt at relevant moments such as when people approach a free-content limit. Prompt for a new subscription only when someone is not already subscribed. If the same service is sold in multiple apps or on a website, offer sign-in so people do not think they must pay twice.

### Signup information

Make options distinguishable with short names, price, and duration. If an introductory price exists, show its amount, duration, and the standard price after it ends. Ask only for information needed to sign up; defer optional data. In tvOS, use another device and a code for sign-up/authentication instead of requiring data entry on Apple TV.

The in-app sign-up screen must include links to the app’s Terms of Service and Privacy Policy (also include them in App Store metadata), plus:

- subscription name, duration, and the content or services delivered in each period;
- the correctly localized total billing amount for each available territory and currency; and
- a sign-in or restore-purchases path for existing subscribers.

Explain a free trial’s duration and the amount automatically billed when it ends. Include a sign-up opportunity in app or account settings.

To help people compare value, give each option’s billing total the most prominent position and any per-period price breakdown a subordinate one.

## Offer codes

In iOS and iPadOS, offer codes can give new, existing, or lapsed subscribers free or discounted access through online or offline distribution.

| Code | Redemption and best fit |
|---|---|
| One-time-use | Unique code generated in App Store Connect; redeem through a shareable redemption URL, in-app if supported, or the App Store (which can prompt installation). Consider for small or restricted distributions. |
| Custom | Code you create (for example, `NEWYEAR` or `SPRINGSALE`); redeem through a redemption URL or in-app. Consider for large campaigns. Only alphanumeric ASCII characters; no special characters, including Chinese or Arabic characters. |

Explain offer terms plainly in marketing materials. Tell people how to redeem a custom code: it cannot be entered in App Store account settings, so provide a redemption URL or in-app path. If supporting in-app redemption, create only the initiating UI and let the system provide the redemption screens. The StoreKit `presentOfferCodeRedeemSheet(in:)` (presents the redemption sheet for an App Store Connect–configured offer code in a window scene) and SwiftUI `offerCodeRedemption(isPresented:onCompletion:)` are deprecated; verify the current replacement before implementation. Natural entry points include a paywall, onboarding, or settings screen.

Supply an engaging, informative promotional image when useful; without one, redemption screens use the app icon. After redemption, align the app with the new status: consider a welcome experience for new subscribers and, for an existing subscriber who unlocked additional functionality, a brief feature tour. Handle people who subscribed before opening the app, including a smooth required account/sign-in step. See [Promoting your in-app purchases](https://developer.apple.com/app-store/promoting-in-app-purchases/), [Offer codes](https://developer.apple.com/documentation/storekit/implementing-offer-codes-in-your-app), and [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

## Managing subscriptions

Provide a subscription summary, especially the upcoming renewal date. Consider placing it near subscription management in settings or an account screen. [`Product.SubscriptionInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo) describes subscription status, period, group, and offer details. Consider the system management sheet via [`showManageSubscriptions(in:)`](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)), which presents the App Store subscription-management sheet. Make upgrade, downgrade, and cancellation available without leaving the app, and keep cancellation easy to find; a deep or obscure action can feel obstructive.

When StoreKit reports cancellation, consider a personalized retention offer or an exit survey; feedback can inform retention and win-back messaging. A branded contextual layer may suggest a popular tier, alternative plan, promotional discount, or offer code, while complementing rather than obscuring the system management UI.

The system cancellation alert offers **Not Now** and **Confirm** and states the date through which access continues after canceling.

### watchOS

The watchOS sign-up screen needs the same subscription information required elsewhere. Clearly describe differences from iPhone and other devices. Consider a modal sheet: it can hold required information in one scrollable view and supplies a default Close action back to free content. If using a custom sign-up view, make the flow complete and efficient and include Close or Cancel back to free content. Make options easy to compare by compactly showing duration and discount; either use one button per option and keep each description associated with its button, or list one option per row followed by an action button whose title can update to the selected option.

## Resources

[In-App Purchase](https://developer.apple.com/in-app-purchase/) · [Offering Subscriptions](https://developer.apple.com/app-store/subscriptions/) · [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) · [StoreKit](https://developer.apple.com/documentation/storekit)

Source: [Apple Human Interface Guidelines — In-App Purchase](https://developer.apple.com/design/Human-Interface-Guidelines/in-app-purchase), captured 2026-09-12.
