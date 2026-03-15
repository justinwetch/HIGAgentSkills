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
related:
  - apple-pay
  - ratings-and-reviews
---
# In-App Purchase

> In-App Purchase lets people buy virtual goods — premium content, digital items, and subscriptions — securely within your app.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

> **Distinction**: Use In-App Purchase for virtual goods (features, subscriptions, game content). Use Apple Pay for physical goods and real-world services (groceries, tickets, hotel, donations).

## IAP Types

| Type | Description |
|---|---|
| Consumable | Depletes with use (lives, gems); can repurchase |
| Non-consumable | Permanent upgrade (premium features); never expires |
| Auto-renewable subscription | Renews automatically each period until canceled |
| Non-renewing subscription | Fixed-duration access (e.g., battle pass); must repurchase |

## Best Practices

- **Let people try your app before buying** — free access increases likelihood of purchase.
- **Integrated shopping experience** — match the style of your app; don't make it feel like a different app.
- **Simple, succinct names and descriptions** — titles that don't truncate; plain, direct language.
- **Always display total billing price** for every purchase type.
- **Only show the store when payments are possible** — if payments are restricted (e.g., parental controls), hide or explain.
- **Use the default confirmation sheet** — don't modify or replicate it.

## Family Sharing

- Prominently mention Family Sharing where people learn about content — e.g., include "Family" or "Shareable" in names.
- Customize in-app messaging for both purchasers and family members (e.g., "Your family subscription includes…").

## Refunds and Purchase Help

- **Provide pre-refund help** — resolve missing purchases, FAQ, direct support options.
- **Simple refund action label** — "Refund" or "Request a Refund." Don't reiterate that it goes to Apple.
- **Help people identify the problematic purchase** — show image, name, description, purchase date.
- **Offer alternative solutions** — immediate fulfillment, conciliatory item — but always also offer the refund path.
- **Don't bury the refund button** — it must be prominent; don't require scrolling to reveal it.
- **Don't characterize Apple's refund policies** — you can link to Apple's support page (HT204084).

## Auto-Renewable Subscriptions

- **Call out subscription benefits during onboarding** — educate people early; strong call to action; clear summary of terms.
- **Offer tiers** — multiple content levels, service tiers, or duration options.
- **Consider free trials or freemium access** — metered paywall or limited free tier.
- **Prompt to subscribe at relevant moments** — e.g., when approaching the free content limit.
- **Don't prompt existing subscribers** — they may think their subscription lapsed.

### Sign-Up Screen (required content)

- Subscription name, duration, and what's included per period.
- Billing amount, correctly localized.
- A way to sign in or restore purchases for existing subscribers.
- Free trial: clearly state duration and what's billed after it ends.

**tvOS sign-up**: send a code to another device for authentication — don't ask people to type in the tvOS app.

### Offer Codes

- **One-time use code** — unique code generated in App Store Connect. Redeem via URL, in-app, or App Store. Best for small or restricted distributions.
- **Custom code** — e.g., `NEWYEAR`. Alphanumeric ASCII only (no special characters). Redeem via URL or in-app. Best for mass campaigns.
- Tell people how to redeem custom codes — they can't redeem in App Store account settings.
- Consider supporting in-app redemption with StoreKit (system provides all screens automatically).

### Subscription Management

- **Show renewal date** in settings or account screen.
- **Use system-provided sub-management UI** (via StoreKit) for a consistent experience.
- Make it **easy to cancel** — don't bury the manage-subscription option.
- On cancellation: consider a personalized retention offer or exit survey.

## Platform Considerations

### watchOS

Sign-up screen must display all required subscription info (same items as other platforms). Design guidance:
- **Clarify differences** between the watchOS and other-device versions of your app.
- **Use a modal sheet** to display required info — default Close button makes it easy to return to free content.
- **Make subscription options easy to scan** — display duration and discount info compactly. Either:
  - One button per option (locked-up with its description), or
  - A list of options followed by a single action button (button title updates with selected option).
