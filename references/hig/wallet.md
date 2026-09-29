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

Wallet securely stores cards, IDs, transit cards, tickets, keys and more on iPhone and Apple Watch.

## Passes

Passes digitally represent items like event tickets, boarding passes, reward cards and coupons.

- **Offer to add new passes to Wallet.** When an action creates a pass, you can present one-tap system UI. For frequent, predictable actions, you can add passes in the background after a one-time authorization. Wallet notifies people whenever a pass is added. To let people review a pass first, you can show a custom view with an Add to Apple Wallet button. APIs: `addPasses(_:withCompletionHandler:)`, `PKPassLibrary.Capability.backgroundAddPasses`, `PKAddPassesViewController`.
- **For a pass created on your website or another device, suggest adding it** at the next app launch. If people decline, don't ask again.
- **Add related passes as a group**, like multi-connection boarding passes; bundle a website's pass set for one download.
- **Show an Add to Apple Wallet button (`PKAddPassButton`) for an existing pass not in Wallet**, such as one people declined or removed. You can place it wherever that pass's information appears. Emails and webpages can use the Add to Apple Wallet badge.
- **Let people jump to their pass.** Wherever your app shows a pass that's in Wallet, you can link to it, labeled something like "View in Wallet."
- **Tell the system when passes expire:** set each pass's expiration date, relevant date and voided properties correctly (`Pass`). Wallet automatically hides expired passes, with a button to revisit them.
- **Always get permission before deleting passes from Wallet**, e.g. via an in-app setting for manual or automatic removal. If necessary, you can show an alert before deleting.
- **Help the system suggest a pass when relevant.** Given when and where it's relevant, the system can link to it on the Lock Screen and, for certain types like event tickets, start a Live Activity.
- **Keep passes up to date**, like showing flight delays and gate changes.
- **Use change messages only for updates to time-critical information.** Never use them for marketing or other noncritical communication. They're available per field.

## Pass anatomy

Pass fields define what appears and where. Semantic tags describe content to the system, enabling features like surfacing the pass when needed and featured actions (quick links like venue directions). Poster event and semantic boarding passes require semantic tags, which enable automatic layout; include pass fields too so they display correctly on older iOS versions. Supplemental information can sometimes go in sheets linked from the pass front.

|Field area|Shows|
|---|---|
|Logo, logo text|Brand icon and name; visible when the pass is collapsed|
|Header|Critical information; visible when collapsed|
|Primary|The most important information|
|Secondary, auxiliary|Useful, less critical information|
|Footer|Supplemental information, like pass category ("Family", "Annual")|
|Back|Rarely needed settings and information, like legal text; shown in pass details|

Layout varies by pass style.

## Designing passes

Design a clean, simple pass that feels at home in Wallet, not merely a replica of the physical one. Use Pass Designer to design and preview passes from templates or a blank pass.

- **Design for all devices.** Apple Watch shows less information and fewer images. Don't put essential information in elements that might be unavailable on some devices. Avoid padding images; watchOS crops white space from some.
- **Keep the pass front uncluttered.** Put essentials (event date, account balance) in the header; quick-access information on the rest of the front; rarely needed details on the additional pass information sheet.
- **Make your pass instantly identifiable** with brand colors, images, icons and full-art backgrounds.
- **Ensure sufficient contrast** between label colors and both solid backgrounds and background images.
- **Use language that works on any device**: "Slide to view" doesn't apply on Apple Watch.

## Pass styles

|Style|For|
|---|---|
|Boarding pass|Airline, train, bus and boat tickets, generic transit passes; typically one trip. Use semantic tags for airline passes, pass fields for other transit.|
|Coupon|Coupons, special offers, discounts|
|Event ticket|Events like concerts, sports, movies, plays; typically one event, but can cover several (season ticket). Supports a full-art background; non-poster tickets use standard pass fields and can use a background image and thumbnail.|
|Store card|Loyalty, discount, points and gift cards; usually shows any balance|
|Poster generic pass|Full background image, distinct field layout; not tied to a category, so you can use it whenever another style doesn't fit|
|Generic|Passes fitting no other category, like a gym card or coat-check ticket|

## Pass images

Use PNG at @2x and @3x.

- **Reserve pass images for visual content.** Embedded text isn't accessible and may not show on all devices; use text fields and semantic tags. Add barcodes with Pass Designer or the APIs, not in images.
- **Keep image file sizes small**, the smallest that still look great; passes download via email or webpages.
- **Provide a pass icon** for the Lock Screen, Mail and passes in Wallet: your app icon or a separate design.

|Image|File|Pass styles|Width (pt)|Height (pt)|
|---|---|---|---|---|
|Logo|logo.png|Non-semantic airline boarding, non-airline boarding, coupon, non-poster event ticket, generic, store card|50-160|50|
|Primary logo|primaryLogo.png|Airline boarding, poster event ticket, poster generic|30-126|30|
|Secondary logo|secondaryLogo.png|Poster event ticket|12-135|12|
|Icon|icon.png|All|38|38|
|Strip|strip.png|Coupon, store card|375|144|
|Thumbnail|thumbnail.png|Event ticket, generic|60-90|90|
|Background, non-poster|background.png|Event ticket|343|503|
|Background, poster|artwork.png|Poster event ticket, poster generic|358|448|
|Footer|footer.png|Airline boarding only|268|15|

- **Logo:** top leading corner of passes with pass fields; typically a horizontal text logo, optionally with a graphic. **Avoid inner drop shadows**; they can reduce legibility.
- **Primary logo:** top leading corner; square with logo text, or rectangular without.
- **Secondary logo:** ticket issuer or event organizer, bottom trailing corner.
- **Icon:** square. The system rounds its corners, so you don't need to.
- **Strip:** reinforces brand or offer. Because text can overlay it, ensure sufficient contrast, keep areas behind text uncluttered, and place important elements toward the bottom or trailing edge. Avoid embedding text.
- **Thumbnail:** small square image like a movie poster, upper trailing. Round your artwork's corners; export as transparent PNG.
- **Background:** blurred behind content on older event tickets; unblurred on poster passes, where a material strip covers the bottom edge. Position content within the safe area (header at top, barcode or QR code and footer below) and account for any barcode; preview in Pass Designer. See `footerBackgroundColor` in `Pass`.

## Order tracking

With order tracking, Wallet can show orders placed through your app or website in a dashboard of active and completed orders, updating whenever status changes. Using the Wallet Orders schema, supply as much information as you can, with properties matching your order processes; Wallet displays it in system-defined interfaces.

- **Make adding an order easy.** For example, after an Apple Pay transaction, use `PKPaymentOrderDetails` (app) or `ApplePayPaymentOrderDetails` (web) to add it automatically. In iOS 17 and later, you can place the Track with Apple Wallet button (`AddOrderToWalletButton`) in relevant places like order confirmation, status or tracking pages, or in emails. Adding an order already in Wallet opens it there.
- **Make order information available immediately after purchase**, even with payment, processing and fulfillment pending. If details come later, provide what you have, with a status description like "Check back later for full order details."
- **Provide fulfillment information as soon as available, and keep status up to date.** The system updates the order and can automatically notify customers, mapping your status to values like Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, or, if something goes wrong, Issue or Canceled.
- **Supply a high-resolution logo (`logo` in `Merchant`) and distinct, high-resolution product images, all with nontransparent backgrounds**: PNG or JPEG, 300x300 px each. The logo appears in the dashboard and detail view; product images also appear in notifications. Depict products straightforwardly on a solid background.
- **In general, keep text brief**; the system can truncate it.
- **Use clear, approachable language, and localize your text.** Make sure the price matches the final price the customer confirmed.

### Displaying order and fulfillment details

- **Provide a link to where people manage their order** (`Order`); a universal link works without your app installed.
- **Clearly describe each item** so people can verify the order. You can use `LineItem` for price, name and image. An order lists every item; a fulfillment only its own. When appropriate, you can attach a PDF receipt to a transaction.
- **Supply a prioritized list of your apps that might be installed** (`Order`). Order details link to the highest-listed installed app, or the first listed if none is installed.
- **Avoid sending duplicate notifications**; for example, you can suppress Wallet order notifications when one of your associated apps is installed.
- **Make contacting the merchant easy** (`Merchant`). Provide multiple methods: at minimum a website or landing page link; optionally Messages for Business, phone, email and a support page. The Contact button shows them in a menu.
- **Help people track their order.** For every fulfillment (a multi-item order can have several, each shipping or pickup), you need to supply enough for people to know where items are and when they'll arrive. Beyond an estimated arrival, people particularly appreciate:
  - For shipping, a direct carrier link when possible, plus a tracking number; if necessary, show it on any intermediate tracking page you open.
  - A scannable barcode when pickup requires one.
  - Clear, detailed receiving or pickup instructions.
- **Keep the fulfillment screen centered on order tracking**, prioritized over any recommendations for your app or services.
- **Choose shipping-fulfillment values that match what you know** (`ShippingFulfillment`). Enter a known carrier in `carrier`; otherwise keep the default "Track Shipment". With interim carrier steps, use statuses like `onTheWay`, `outForDelivery` or `delivered`; without, use `shipped`. Either way, provide a tracking link when available.
- **Keep customers informed with relevant status descriptions**: approachable, accurate, clearly tied to the status; they can carry your brand's voice. **Be direct and thorough about Issue or Canceled statuses**; people generally need to know why and what they can do.

## Identity verification

On iPhone with iOS 16 and later, people can let an app or App Clip read an ID stored in Wallet to verify identity in context. Apple doesn't create or see these IDs; your app receives only encrypted data that isn't readable on the device. The Verify with Wallet button opens a sheet describing your request, where people share or cancel. For in-person verification, see ID Verifier.

- **Offer Wallet verification only when the device supports it.** If the device can't return the requested information, don't show a Verify with Apple Wallet button. Be prepared with a fallback view offering another method if it isn't available (`VerifyIdentityWithWalletButton`).
- **Ask for identity information only at the precise moment you need it**, as people complete the process that requires it; not before they're ready to start or when they're simply creating an account.
- **Clearly and succinctly explain why.** You must write a purpose string, shown in the sheet. Aim for one brief, complete, direct, specific sentence everyone understands; sentence case; active voice; end with a period.

|To verify|To support|Example purpose string|
|---|---|---|
|Identity|Account opening where proof of identity is legally required|Federal law requires this information to verify your identity and also to help [App Name] prevent fraud.|
|Driving privilege|Vehicle rental|Applicable state law requires [App Name] to verify your driving privileges.|

- **Ask only for the data you actually need.** To confirm a minimum age, request an age threshold (`age(atLeast:)`); avoid requesting current age or birth date.
- **Clearly indicate whether you'll keep the data and, if so, how long.** When you specify a duration (a period, indefinitely, or this verification only) with `PKIdentityIntentToStore`, the sheet explains it automatically.
- **Choose the system button that fits your use case and visual design.**

|Button label|Consider when|
|---|---|
|Verify Age with Apple Wallet|Age check completes the transaction (making a car available to lease)|
|Verify Identity with Apple Wallet|Identity check completes the transaction (car rental)|
|Continue with Apple Wallet|Process also needs data Wallet doesn't provide, like a Social Security or phone number (financial account, background check)|
|Verify with Apple Wallet|No further steps, but other labels don't fit (government service sign-up)|

Every label has a multiline variant the system uses automatically when horizontal space is constrained (`PKIdentityButton.Label`). The button always has white letters on black; you can choose a light outline (`PKIdentityButton.Style.blackOutline`) for contrast on dark backgrounds and use `cornerRadius` to match related buttons.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS or visionOS. Not supported in tvOS.

### watchOS

Passes appear in a scrolling card carousel; people can add your pass to Apple Watch even without a watch app. Tapping a pass opens a scrolling details screen, which also holds information that doesn't fit the layout; sometimes people can tap a transaction for more. **Important:** In every style, watchOS crops the strip image to the card's aspect ratio and may crop white space from other images.

|Style|Beside logo (essential)|Row 2 (primary)|Row 3 (secondary, auxiliary)|
|---|---|---|---|
|Boarding|Departure or boarding time|Origin, destination|Passenger name, seat|
|Coupon|Expiration date|Strip image|Unused|
|Store|Unused|Strip image|Member name, number|
|Event|Start date|Event information|Attendee name, seat|
|Generic|Expiration date|Strip image|Name, number|

## Resources

Developer: `PassKit`, `WalletPasses`, `WalletOrders`, `FinanceKit`, `FinanceKitUI`.

Source: [Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet), captured 2026-09-12.
