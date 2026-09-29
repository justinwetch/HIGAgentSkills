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

Apple Pay handles payment for physical goods, services, donations and subscriptions in apps and any browser; its button opens a payment sheet where people review details and authorize. For virtual goods and digital-content subscriptions, use in-app purchase.

## Offering Apple Pay

- **Offer Apple Pay on all devices and browsers that support it**; don't present it on unsupported devices (`PKPaymentAuthorizationController` in iOS and watchOS; web `applePayCapabilities`).
- **Make Apple Pay the primary option when credentials are available.** If you use Apple Pay APIs to detect an active Wallet card, you must make it primary (not necessarily sole) everywhere you use them, e.g. preselected. Don't separate it into a different step or flow.
- **Use Apple Pay buttons only to initiate payment or, when appropriate, setup** (offered if Apple Pay isn't set up); never otherwise.
- **A custom button that starts Apple Pay payment must not show "Apple Pay" or its logo**; you must then show the Apple Pay mark or mention Apple Pay in text on the same page.
- **Use the Apple Pay mark only to communicate acceptance**, such as wherever you highlight payment options; never use or position it as a button. With it showing Apple Pay selected, a separate custom button can start payment.
- **Don't hide an Apple Pay button or make it appear unavailable**; if it can't be used yet (no size chosen), gracefully explain after it's tapped or clicked.
- **Inform search engines**: list Apple Pay as a payment option in your website's semantic product markup.
- Websites offering Apple Pay must include a privacy statement and follow the [Acceptable use guidelines for Apple Pay on the web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).

## Streamlining checkout

- **Provide a cohesive, branded checkout**; avoid opening different pages or windows, which on websites can suggest a handoff to another site.
- **If Apple Pay is available, assume people want it.** Consider showing its button first, larger, or separated by a line.
- **Consider Apple Pay buttons on product detail pages** for quick single-item purchases, besides the cart. Such a purchase must cover only that item; if the cart contains it, remove it after purchase.
- **Accelerate multi-item purchases with express checkout**: the sheet appears immediately for the whole cart, with one shipping method and destination.
- **If you offer coupons or promotional codes, support entry in the payment sheet**, not a separate step, especially in express checkout.
- **Collect necessary options (color, size) before people reach the Apple Pay button**; if one is missing, highlight it or show warning text and automatically navigate to the field.
- **Collect optional information (gift messages, delivery instructions) before checkout** or after purchase; the sheet can't accept it.
- **Gather multiple shipping methods and destinations before showing the sheet**, which allows one of each per order.
- **For in-store pickup, help people choose a location before showing the sheet**, then show its address on it (Displaying a Read-Only Pickup Address).
- **Prefer checkout information from Apple Pay**; assume it's complete and current, and consider fetching it even if you store details.
- **Avoid requiring account creation before purchase.** Invite registration on the order confirmation page, prefilled from checkout.
- **Report transaction results in the payment sheet**, with error messages for failures like a bad address.
- **Display an order confirmation or thank-you page** with shipping timing and how to check status. Listing Apple Pay isn't necessary; if you do, put it after the last four digits ("1234 (Apple Pay)") or in a separate note ("Paid with Apple Pay").

### Customizing the payment sheet

- **Only present and request essential information.** For an electronically delivered gift card, request an email, not a shipping address.
- **Display the active coupon or promotional code**, including one entered before the sheet.
- **Let people choose the shipping method in the sheet.** Space permitting, give each a description, cost and, optionally, estimated delivery or pickup date or range, using the method's calendar and time-zone support (`PKDateComponentsRange`).
- **For in-store pickup, consider letting people choose a pickup window**, supplied as date and time ranges through the shipping method.
- **Use line items for additional charges, discounts, pending costs, add-on donations, recurring and future payments** (`paymentSummaryItems`). Each has a label and cost, plus frequency if recurring. Don't use line items to itemize products.
- **Keep line items short and specific**, on one line whenever possible.
- **Provide a business name after *Pay* on the total line** ("Pay [Business_Name]"), matching people's bank or card statement.
- **If your app, App Clip or website is an intermediary (e.g. a marketplace) rather than the end merchant, identify both businesses**: "Pay [End_Merchant_Business_Name (via Your_Business_Name)]".
- **Clearly disclose possible costs after authorization.** When local regulations allow, you can explain this in the sheet with a subtotal marked Amount Pending. Make any preauthorized amount accurate in the sheet.
- **Defer to the payment sheet for progress information**; extra spinners or progress indicators can confuse the transaction state.

## Displaying a website icon

If your website supports Apple Pay, provide a website icon at 60x60 pt (120x120 px @2x, 180x180 px @3x). It can appear above the payment details during authorization, notably during Handoff to a connected device, and in Wallet for subscription flows.

## Handling problems

**Handle data entry and payment errors gracefully**, with clear, actionable guidance so people can complete the transaction.

- **Handle interruptions correctly.** When a cancellation or timeout dismisses the sheet, you must cancel any in-progress payment; people restart with the Apple Pay button (`PKPaymentAuthorizationViewControllerDelegate`; web `oncancel`).

### Data validation errors

Check input when the sheet appears, when people change certain fields and after they authenticate. System messages highlight invalid fields; provide custom messages for the detail view a field opens. Before authorization, only the card type and a redacted shipping address are available. It's critical to show errors when authorization fails, but to the extent possible also validate and report problems before authorization.

- **Avoid forcing compliance with your business logic.** Ignore irrelevant and infer missing data whenever possible: drop Zip+4's extra digits when you need five; accept phone numbers with or without dashes or country code.
- **Accurately report problems to the system** with a custom message and the correct status code (`PKPaymentError` in iOS and watchOS; web Apple Pay Status Codes).
- **Explain invalid or badly formatted data clearly and succinctly**, naming the field and what's expected: "Zip code doesn't match city", not "Address is invalid"; "Shipping not available for this state". Use noun phrases, sentence-style capitalization and no ending punctuation; aim for 128 characters or fewer to avoid truncation.

## Supporting subscriptions

Recurring payments can be fixed or, when local regulations allow, variable (shown as Amount Pending); the initial authorization can include discounts and fees.

- **Clarify billing frequency and other terms before showing the payment sheet**, and **include line items that reiterate billing frequency, discounts and upfront fees**.
- **Clarify in the total line the amount billed at authorization**; if it's $0, clearly disclose when billing occurs.
- **Clearly communicate trial terms** with line items for the trial amount (including $0 if free), the regular amount after it and the date regular billing begins.
- **Only show the payment sheet when a subscription change adds fees**; authorization isn't needed if the cost falls or stays the same.
- Treat the billing agreement field as a plain-language summary, not formal terms. If you use it, be concise and avoid duplicating info shown elsewhere in your app, website or line items; when in doubt, leave it blank.

## Supporting donations

For [approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/).

- **Use a line item to identify a donation** (*Donation $50.00*).
- **Offer predefined donation amounts** ($25, $50, $100) plus an Other Amount option.

## Using Apple Pay buttons

**Always use the Apple-provided API to display Apple Pay buttons** (`PKPaymentButtonType`, `PKPaymentButtonStyle` in iOS and macOS; `WKInterfacePaymentButton` in watchOS; Apple Pay on the Web). Localization and VoiceOver alternative text are automatic. Don't create custom Apple Pay button designs or replicate Apple's.

### Button types

Choose the type that fits your flow's terminology. In some contexts, the system shows the default card's image on payment buttons, signaling Apple Pay is ready.

|Button ("... with Apple Pay")|Use for|
|---|---|
|Buy|Purchase areas, like product detail or cart pages|
|Pay|Bills or invoices for utilities or services|
|Check Out, Continue|Flows whose other payment buttons start with the same words|
|Book|Flights, trips, other experiences|
|Donate|Approved nonprofits|
|Subscribe|Subscriptions, like gym memberships or meal kits|
|Reload, Add Money, Top Up|Adding money to a service's card, account or payment system (transit, prepaid phone); match the term you use|
|Order|Orders, like meals or flowers|
|Rent|Rentals, like cars or scooters|
|Support, Contribute|Giving money to projects, causes, organizations and other entities; match the term you use|
|Tip|Tips for goods or services|
|Apple Pay (no "with")|Stylistic need for a smaller minimum width or no call to action. The system may substitute it for a type the running OS version doesn't support.|

You can offer **Set Up Apple Pay** when a device supports Apple Pay but it isn't set up; place it in Settings, a user profile or an interstitial page.

### Button styles

Use the *automatic* style to follow system appearance (`PKPaymentButtonStyle.automatic`; web `ApplePayButtonStyle`), or choose:

|Style|Background|Don't use on|
|---|---|---|
|Black|Light, with sufficient contrast|Black or dark|
|White with outline|Light, without sufficient contrast|Dark or saturated|
|White|Dark, with sufficient contrast|Light|

### Button size and position

- **Prominently display the Apple Pay button**: no smaller than other payment buttons; avoid making people scroll to it.
- **Place it right of an Add to Cart button side by side, above it when stacked.**
- **Adjust the corner radius to match other buttons**, from square through the rounded default to capsule (`cornerRadius`).
- **Maintain the minimum button size and margins**; titles vary by locale. If the size can't fit the translated title, the system automatically substitutes the plain Apple Pay button. Set Up Apple Pay has no automatic replacement.

|Button|Min width|Min height|Min margins|
|---|---|---|---|
|Apple Pay|100 pt (200 px @2x)|30 pt (60 px @2x)|1/10 of button height|
|Book, Buy, Check Out, Donate, Subscribe with Apple Pay; Set Up Apple Pay|140 pt (280 px @2x)|30 pt (60 px @2x)|1/10 of button height|

### Apple Pay mark

- **Use only Apple's artwork, altering nothing but height**, which must equal or exceed other payment brand marks in the flow. Don't adjust width, corner radius or aspect ratio; add a trademark symbol or other content; remove the border; add effects like shadows, glows or reflections; or flip, rotate or animate it.
- **Maintain minimum clear space of 1/10 of the mark's height.** Don't let it share its surrounding border with another graphic or button.
- Get the mark and full usage rules from the [Apple Pay Marketing Guidelines](https://developer.apple.com/apple-pay/marketing/).

## Referring to Apple Pay

You can use plain text to promote Apple Pay or indicate it's a payment option.

- **Use Apple Pay exactly as in the [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)**: two words, uppercase *A* and *P*, the rest lowercase, never plural or possessive; all caps only to conform to an established all-caps typographic style. Follow the [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).
- **Never use the Apple logo to represent *Apple* in text.** In the United States, use ® the first time Apple Pay appears in body text, but not when it's a checkout selection option.
- **Coordinate font face and size with your app or website**; don't mimic Apple typography.
- **Don't translate *Apple Pay* or any Apple trademark**; always use English, even in non-English text.
- **In a payment selection context, use a text-only Apple Pay description only if all options are text-only.** If any has an icon or logo, you must use the Apple Pay mark.
- **When promoting Apple Pay in an app, follow the [App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/).**

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, visionOS or watchOS. Not supported in tvOS.

## Resources

Source: [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay), captured 2026-09-12.
