---
topic: app-clips
tier: 3
platforms: [ios, ipados]
category: technologies
triggers:
  - "App Clip"
  - "mini app"
  - "NFC clip"
  - "QR clip"
  - "lightweight experience"
related:
  - launching
  - onboarding
  - nfc
---

# App Clips

An App Clip is a lightweight version of an app or game, usable without installing it, offering a fast task solution or a demo. It stays on the device for a limited time.

People launch App Clips by scanning an App Clip Code (usually best), NFC tag or QR code, from permitted location-based suggestions in Siri Suggestions and Maps, or from Smart App Banners, Safari App Clip cards and Messages links. Starting with iOS 17, apps can include links and previews that launch another app's App Clip.

Consider an App Clip for an in-the-moment task over a finite time, or as a demo; for demos, focus on letting people experience and understand the app or game before purchase or subscription.

## Designing your App Clip

- **Let people complete a task or demo in the App Clip.** Don't require the full app to finish the demo, a task or a game level.
- **Focus on essential features**; reserve advanced or complex ones for the app. For demos, show enough to convey the app's or game's functionality.
- **Don't use App Clips solely for marketing.** Don't advertise services or products, and don't display ads.
- **Avoid web views.** If only web components are available, offer a quick link to your website instead.
- **Design a linear, focused UI**; tab bars, complex navigation and settings aren't needed. Minimize screens and entry forms; remove extraneous information.
- **On launch, show the most relevant part** for people's context, skipping unnecessary steps.
- **Ensure immediate use.** Include all required assets, omit splash screens, never make people wait on launch.
- **Keep it small**, especially for limited bandwidth: reduce code and remove unused assets as much as possible; avoid downloading additional data.
- **Make it shareable.** Offer links to specific points (Messages recipients launch it in place), and encourage sharing.
- **Offer easy, secure, privacy-respecting payment**; consider Apple Pay for express checkout and shipping details without typing.
- **Avoid requiring an account before people benefit.** Consider not requiring one, or asking after a task. If required, limit requested information; consider offering Sign in with Apple, which keeps login information off the device.
- **Provide a familiar, focused experience in your app**, which replaces the App Clip once installed and receives its invocations. Don't add slowing steps, like logging in again.

### Preserving privacy

The system limits App Clips for privacy; for example, they can't perform background operations.

- **Limit data you store and handle yourself.** Store it securely, and login information securely off the device. Don't rely on previously stored data; the system may delete the App Clip and its data between launches.

### Showcasing your app

App Clips don't appear on the Home screen; the system removes them after inactivity. The App Clip card and a system banner on first launch link to the App Store.

- **Don't compromise the experience by asking people to install the full app.** For on-the-go App Clips, consider whether the card and banner are enough incentive; let people fully experience a demo before asking.
- **Pick the right time to recommend your app:** after a task or at a natural pause, display an `SKOverlay` for downloading it.
- **Recommend it politely.** Don't ask repeatedly or interrupt a task; push notifications aren't a good way to ask. Clearly communicate the app's additional features.

### Limiting notifications

App Clips can schedule and receive notifications for up to 8 hours after launch.

- **Only ask permission for extended notifications if really needed.** If functionality spans more than a day, explicitly request permission to schedule and receive notifications.
- **Keep notifications focused.** Don't send purely promotional ones; only use them in response to an explicit user action. If the task finishes inside the App Clip, you might not need any.
- **Use notifications to help complete the App Clip's task**, such as a scheduled delivery.

### Creating App Clips for businesses

A platform provider may power several App Clip experiences, configured in App Store Connect, with one App Clip that shows each business's or location's branding.

- **Use consistent branding.** Tone down your own; keep the business's clearly visible.
- **Consider multiple businesses.** The App Clip must handle use for several businesses or locations at once and update its UI; for example, consider switching between recent ones, and verify location at launch.

## Creating content for an App Clip card

- **Be informative.** Make sure the image clearly communicates features, tasks or content.
- **Prefer photography and graphics.** Avoid UI screenshots; show the App Clip's value or the business's location or point of interest.
- **Avoid text** in the header image; it isn't localizable.
- **Image:** 1800x1200 px PNG or JPEG, no transparency.
- **Use concise copy.** Title (max 30 characters) and subtitle (max 56 characters) are both required.
- **Action button verb:** *View* for media or informational or educational content, *Play* for games, *Open* for all others.

## App Clip Codes

App Clip Codes follow size, placement and printing guidelines. Use the badge design with the App Clip logo or, when space is at a premium, the design without it, in a default color pair or custom colors.

|Variant|Center icon|Launch by|
|---|---|---|
|Scan-only|Camera|Camera app or Code Scanner in Control Center|
|NFC-integrated|iPhone|Holding the device close or NFC Tag Reader in Control Center; also Camera or Code Scanner|

### Displaying App Clip Codes

- Use NFC-integrated if people can physically reach the code (a tabletop); scan-only if it's inaccessible or digital (a poster).
- **Include the App Clip logo when space allows.** Omit it if you can't meet clear space requirements, on disposable paper or plastic items, or on items associated with gambling or drinking (bar coasters). The logo appears only in the badge design, below the code; never use it on its own.
- **Use only flat or cylindrical surfaces.** On a cylinder, make sure code width doesn't exceed one-sixth (60 degrees) of the circumference.
- **Keep the code as flat as possible.** Avoid deformable materials (fabric); on a bag or flexible box, attach a rigid card bearing it. Make stickers adhere well.
- **Place codes for reliable scanning**, for example with enough light for scan-only codes and no wide-angle scanning.
- **Keep the code unobstructed.** Don't overlay text, logos or images. Never animate or dim it.
- **Display it upright.** Don't rotate it or angle the center glyph.
- **Don't make codes too small.** Minimums:

|Type|Minimum size|
|---|---|
|Printed|3/4 in (1.9 cm) diameter|
|Digital|256x256 px; PNG or SVG|
|NFC-integrated|Embedded NFC tag at least 35 mm diameter or equivalent; with a 35 mm tag, code at least 1.37 in (3.48 cm) diameter|

- Consider a distance-to-size ratio of no more than 20:1; if possible, use 10:1. Scanned from 40 in (101 cm), a code needs at least 4 in (10.16 cm) diameter.
- Near a QR code or other scannable item, make the App Clip Code at least that size.
- **Leave clear space from adjacent codes, graphics or materials**, at minimum the gap between the center glyph and the circular code; beside other machine-readable codes, enough to scan each reliably.

### Using clear messaging

Add a call to action explaining how to launch the App Clip, especially without the logo. Use suggested or your own copy, always simple and clear.

- Either variant: "Scan to [what people can do]."
- Scan-only: "Scan using the camera on your iPhone or iPad to [...]."
- NFC-integrated: "Hold your iPhone near the [object name] to launch an App Clip that [...]."

### Customizing your App Clip Code

Create codes with App Store Connect or the App Clip Code Generator command-line tool.

- **Always use the generated code.** Don't design your own or modify it: no filters, color changes, glows, shadows, gradients or reflections. When scaling, keep the aspect ratio and scale all attributes, such as stroke widths.
- **Choose colors with enough contrast for accurate scanning.** A third color is generated from your foreground and background. The tools won't generate codes from poorly scanning custom colors, and can suggest a foreground for a custom background.

## Printing guidelines

Always test printed codes before distributing to be sure they scan from a variety of angles.

- **Use high-quality, non-textured materials.** Print on matte finishes, and use matte laminate if laminating. Avoid shine, gloss, reflective or holographic overlays, and thin laminates or materials. Outdoors, use UV-resistant materials or coatings. Use flexographic printing with a professional service, or inkjet on a desktop printer.
- **Use high resolution.** Rasterize SVGs at 600 ppi or more; print at 300 dpi or more. Consider leveling and calibrating the printer. On receipt printers, print as close to the paper's maximum bounds as possible.
- **Convert the generated sRGB SVG to CMYK correctly:** relative colorimetric (media-relative) intent, "Generic CMYK ICC profile" on CMYK printers or "Gracol 2013 ICC profile" on CMYKOV printers, CIELab Delta E tolerance 2.5.
- **On grayscale-only printers, only generate grayscale codes.** Color codes printed in grayscale may be less reliable.
- **For NFC-integrated codes, choose Type 5 NFC tags.**
- **For large batches, thoroughly test the workflow and verify printed codes.** Test with small runs; print each code's URL and filename beside it; keep an SVG-to-URL map.

### Verifying your printer's calibration

- **Verify your color pair's print quality with Apple's calibration test sheet showing each default color pair**, printed at the scale its instructions give.
- **Verify grayscale settings with the test sheet showing two grayscale bars.** Light or missing grays mean the printer may need calibration or may be unsuitable.

## Legal requirements

- Only codes that follow these guidelines are approved, to indicate an App Clip's availability.
- Stop displaying the code of an inactive App Clip.
- Don't use the code, Apple Logo or App Clip mark in a company or product name; seek copyright or trademark registration for them; add a symbol to generated codes; use codes in ways likely to damage Apple's or App Clips' reputation, infringe third-party rights or confuse the source of products or services; put Apple trademarks in your app name or images; or translate Apple trademarks (with Apple's approval, legal notices and credit lines can be translated outside the U.S.). Always title case App Clips and App Clip Code.

## Platform considerations

No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS or watchOS.

## Resources

Developer: `AppClip`, App Store Connect.

Source: [App Clips](https://developer.apple.com/design/human-interface-guidelines/app-clips), captured 2026-09-12.
