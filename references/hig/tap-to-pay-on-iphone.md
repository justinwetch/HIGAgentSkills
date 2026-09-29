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

Tap to Pay on iPhone lets merchants accept contactless payments in an iPhone app without external hardware. It works alongside payment-acceptance hardware/accessories. Integration requires a supported payment service provider (PSP), the Tap to Pay entitlement, and [ProximityReader](https://developer.apple.com/documentation/proximityreader) APIs through the PSP SDK or framework. If the PSP supplies UI (for example, tap-result screens), follow its documentation.

## Enable and educate

- Before enabling/configuring a merchant device, use ProximityReader to check the status of the **terms and conditions** and show acceptance only when needed. Help merchants accept them **before** customer-facing checkout; initial configuration requires acceptance. In-app messaging/onboarding can provide the action.
- Show terms only to an administrative user. Explain the administrator requirement to nonadministrators; where needed, let an administrator accept through a web interface or another app/device, following PSP implementation guidance. If the PSP requires a specific iOS version, update the device before presenting terms.
- Provide a quick tutorial covering every supported payment type: launch each checkout, help the customer position a contactless card or digital wallet near the merchant iPhone, and handle PIN entry including accessibility mode. Offer it through Learn More; automatically after terms acceptance or for new users; or in a stable help/settings location. Use Apple-approved [marketing assets](https://developer.apple.com/tap-to-pay/marketing-guidelines/) or [`ProximityReaderDiscovery`](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery), which provides a pre-built merchant-education experience Apple keeps up to date and localizes for the merchant’s region; finish with an opportunity to accept terms if still pending.

## Checkout

- Always expose Tap to Pay on iPhone as a checkout option, enabled or not. Tapping it can present terms, complete configuration, then automatically open the Tap to Pay screen without leaving checkout. Keep other payment options where necessary.
- Configure early: perform initial setup and call [`PaymentCardReader.prepare(using:)`](https://developer.apple.com/documentation/proximityreader/paymentcardreader/prepare(using:)) when the app starts and after every foreground transition. Keep the option selectable while background configuration continues. Usually show indeterminate progress; if ProximityReader reports progress, show determinate progress using [`PaymentCardReader.Event.updateProgress(_:)`](https://developer.apple.com/documentation/proximityreader/paymentcardreader/event/updateprogress(_:)) (integer **1–100**).
- Make the option easy to find without scrolling; if it is the only payment method, open it automatically at checkout. Let merchants switch between Tap to Pay and supported hardware without visiting Settings; setup for both can occur together.
- Label the payment button **Tap to Pay on iPhone**, or **Tap to Pay** when space is constrained. If it is the only acceptance method, existing **Charge** or **Checkout** labels may activate it. In multi-method button sets, use SF Symbol `wave.3.right.circle` or `wave.3.right.circle.fill` when using icons. Never include the Apple logo. Match the app’s other button color/shape. The “Tap to Pay on iPhone” label is for payment actions only.
- Determine the customer’s final amount before opening the Tap to Pay screen. Collect tips, other total-changing interactions, and any pre-payment choice (such as payment type) first; aim to show the final amount on the Tap to Pay screen.

## Results and recovery

Customers tap a contactless card or digital wallet near the in-app screen. After a successful tap and any required PIN, the system shows a checkmark and gives the app an object containing encrypted payment information for the PSP. A failed tap shows a system error screen; the app must show the transaction result after success and offer alternatives after failure.

- Start PSP processing as soon as possible: set `returnReadResultImmediately` so the framework can return a successful read before the system UI finishes its checkmark animation. [`returnReadResultImmediately`](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/returnreadresultimmediately) is a Boolean.
- After the Tap to Pay animation finishes, show an authorization progress indicator before the transaction-result screen. Authorization may take several seconds depending on PSP and merchant-device connectivity. Apple points to [`PaymentCardReader.Event.readyForTap`](https://developer.apple.com/documentation/proximityreader/paymentcardreader/event/readyfortap) for this step, but that event signals the reader is ready for a card within range, not that the animation finished.
- Clearly show success or decline (including insufficient funds, suspected fraud, or incorrect PIN) and, where possible, offer digital receipts such as QR code or text message.
- If the tap cannot complete because the card is unreadable, unsupported by the payment network, not valid for the amount, or lacks online PIN entry, let the merchant accept cash/another tender, use external hardware or a payment link, or relaunch Tap to Pay for another card.
- After card data is received, contact the PSP for regional cases: Strong Customer Authentication (SCA) may apply even when the tap did not require a PIN; the bank that issued the card can request a PIN after receiving the transaction-processing request, and the app may need to show PIN entry instead of the transaction-result screen. Offline PIN markets can impose requirements, and some PSPs provide PIN fallback that collects partial tap data so payment can continue via a payment link.
- For a system error the merchant must fix, explain the problem and recommend the resolution; for an unsupported iOS version, use an alert recommending the latest update. See [`PaymentCardReaderSession.ReadError`](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readerror). Provide in-app/web help and a support action for unresolved issues.

## Nonpayment and loyalty reads

Tap to Pay can read a payment card without a transaction amount for past-transaction lookup, retaining card information for future payment, refunds, or customer verification. Use a generic button label such as **Look Up**, **Store Card**, **Verify**, or **Refund**; do not call a nonpayment action “Tap to Pay” or “Tap to Pay on iPhone.”

It can also read NFC-compatible Apple Wallet items such as loyalty, discount, and points cards, simultaneously with or independently of payment. If supporting an independent loyalty transaction, give it a separate, clearly labeled button and omit “Tap to Pay,” “Tap to Pay on iPhone,” and other payment terms so merchants do not choose the payment flow by mistake.

Tap to Pay on iPhone is supported only on iOS; it has no additional iOS considerations and is not supported on iPadOS, macOS, tvOS, visionOS, or watchOS.

Resource: [Tap to Pay on iPhone](https://developer.apple.com/tap-to-pay/).

Source: [Tap to Pay on iPhone](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone) (captured 2026-09-12).
