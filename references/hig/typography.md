---
topic: typography
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "font"
  - "type"
  - "text size"
  - "Dynamic Type"
  - "typeface"
  - "tracking"
  - "leading"
related:
  - sf-symbols
  - writing
  - accessibility
---

# Typography

Type choices that keep text legible, convey hierarchy and scale with people's text-size settings.

## Ensuring legibility

- **Use sizes most people can read easily.** Follow each platform's default and minimum sizes, for custom and system fonts alike. For a custom font with a thin weight, aim larger than recommended.

  |Platform|Default|Minimum|
  |---|---|---|
  |iOS, iPadOS|17 pt|11 pt|
  |macOS|13 pt|10 pt|
  |tvOS|29 pt|23 pt|
  |visionOS|17 pt|12 pt|
  |watchOS|16 pt|12 pt|

- **Test legibility in different contexts**, such as game text on each platform the game runs on. For hard-to-read text, consider a larger size, more contrast via text or background colors, or legibility-optimized typefaces like the system fonts. Visible background shapes behind text can help.
- **In general, avoid light weights.** With system fonts, prefer Regular, Medium, Semibold or Bold; avoid Ultralight, Thin and Light, especially at small sizes.

## Conveying hierarchy

- **Adjust weight, size and color as needed to emphasize important information and show hierarchy.** Be sure to maintain relative hierarchy and distinction when people adjust text size.
- **Minimize the number of typefaces, even in a highly customized interface.**
- **Prioritize important content when responding to text-size changes.** People typically want what they care about enlarged, not always every word (in a tabbed window, not tab titles; in games, often dialog over transient hit-damage values).

## Using system fonts

- **San Francisco (SF)**, sans serif: SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, SF Mono. All but SF Mono have rounded variants you can use to match soft or rounded UI elements or for an alternative voice.
- **New York (NY)**, serif, works alone and alongside SF. [Download SF and NY](https://developer.apple.com/fonts/).
- Both are variable fonts with *dynamic optical sizes* on all platforms (optical sizes and weights merge into one continuous design); you don't need discrete optical sizes (like Text and Display) unless your design tool lacks full variable-font support.
- Weights run Ultralight to Black; SF also has widths including Condensed and Expanded. SF Symbols use equivalent weights, precisely matching adjacent text at any size or style, and align automatically with text; consider symbols to convey a concept or depict an object, especially within text.
- A *text style* sets weight, point size and leading for each text size and scales proportionately when people change text size or turn on accessibility adjustments like Larger Text.
- **Consider using the built-in text styles.** With system fonts, they ensure support for Dynamic Type and larger accessibility sizes (where available).
- **Modify the built-in text styles if necessary** with *symbolic traits*, such as bold for another hierarchy level. Loose leading can help wide columns and long passages; tight leading can fit multiple lines in constrained height, like a list row, but avoid it for three or more lines even there (`leading(_:)`).
- Access system fonts through `Font.Design` (`.default` for the system font on all platforms, `.serif` for New York); don't embed system fonts in your app or game.
- **If necessary, adjust tracking in interface mockups.** Running apps adjust system-font tracking at every point size automatically; mockups might need tracking from [Tracking values](#tracking-values).

## Using custom fonts

- **Make sure custom fonts are legible**, guided by the minimum sizes for styles and weights in [Specifications](#specifications).
- **Implement accessibility features for custom fonts.** System fonts automatically support Dynamic Type (where available) and accessibility features such as Bold Text; make sure a custom font implements the same behaviors ([Applying custom fonts to text](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text)).

## Supporting Dynamic Type

Dynamic Type lets people adjust text size system-wide in iOS, iPadOS, tvOS, visionOS and watchOS. Size tables are in [Specifications](#specifications) and the [Apple Design Resources](https://developer.apple.com/design/resources/). In Unity-based games, use [Apple's Unity plug-ins](https://github.com/apple/unityplugins); if a plug-in isn't appropriate, be sure to let players adjust text size in other ways.

- **Make sure your layout adapts to all font sizes**, keeping text and glyphs legible. On iPhone or iPad, turn on Settings > Accessibility > Display & Text Size > Larger Text > Larger Accessibility Text Sizes and confirm the app stays comfortably readable.
- **Increase the size of meaningful interface icons as font size increases.** SF Symbols scale automatically.
- **Keep text truncation to a minimum as font size increases.** In general, aim to show as much useful text at the largest accessibility size as at the largest standard size. Avoid truncating text in scrollable regions unless people can open a separate view for the rest. You can prevent label truncation by allowing as many lines as needed (`numberOfLines`).
- **Consider adjusting your layout at large font sizes.** Where width is constrained, inline items (like glyphs and timestamps) and container edges can crowd text into truncation or overlap; consider stacking text above secondary items. Reduce the number of text columns as size increases (`isAccessibilityCategory`).
- **Maintain a consistent information hierarchy at any font size**, such as keeping primary elements toward the top.

## Platform considerations

|Platform|System font|New York|
|---|---|---|
|iOS, iPadOS, tvOS|SF Pro|Available|
|macOS|SF Pro|Mac Catalyst apps|
|visionOS|SF Pro|If used, specify the type styles you want|
|watchOS|SF Compact; SF Compact Rounded in complications|Available|

### macOS

macOS doesn't support Dynamic Type.

**When necessary, use dynamic system font variants to match text in standard controls**, via these `(ofSize:)` methods: `controlContentFont`, `labelFont`, `menuFont`, `menuBarFont`, `messageFont`, `paletteFont`, `titleBarFont`, `toolTipsFont`, `userFont` (document text), `userFixedPitchFont` (monospaced document text), `boldSystemFont`, `systemFont`.

### visionOS

Body and title Dynamic Type styles are bolder; Extra Large Title 1 and 2 serve wide, editorial-style layouts. For vibrancy as hierarchy, see [Materials > visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS).

- **In general, prefer 2D text.** A little 3D text can draw attention, but for content people need to read and understand, prefer little or no depth.
- **Make sure text looks good and remains legible when people scale it.** Pick a text style that looks good at full scale, then test other scales.
- **Maximize contrast between text and its container's background.** Text is white by default, contrasting with the default system background material; be sure to test any other color in a variety of contexts.
- **For text not on a background, consider bold.** Generally avoid shadows for contrast.
- **Keep text facing people as much as possible.** For text tied to a point in space, like a 3D object's label, you generally want *billboarding*: the text faces the wearer however they or the object move; otherwise, oblique views can make it unreadable. For example, a lamp's label rotates around the y-axis so its baseline stays perpendicular to the viewer's line of sight.

## Specifications

Get emphasized variants with symbolic traits: `bold()` in SwiftUI, `traitBold` in `UIFontDescriptor`. Emphasized weights can be medium, semibold, bold or heavy (Emph. columns).

### iOS, iPadOS Dynamic Type sizes

Size/leading in pt; **L** is the default. Point sizes based on 144 ppi @2x, 216 ppi @3x.

|Style|Weight|Emph.|xS|S|M|**L**|xL|xxL|xxxL|
|---|---|---|---|---|---|---|---|---|---|
|Large Title|Regular|Bold|31/38|32/39|33/40|34/41|36/43|38/46|40/48|
|Title 1|Regular|Bold|25/31|26/32|27/33|28/34|30/37|32/39|34/41|
|Title 2|Regular|Bold|19/24|20/25|21/26|22/28|24/30|26/32|28/34|
|Title 3|Regular|Semibold|17/22|18/23|19/24|20/25|22/28|24/30|26/32|
|Headline|Semibold|Semibold|14/19|15/20|16/21|17/22|19/24|21/26|23/29|
|Body|Regular|Semibold|14/19|15/20|16/21|17/22|19/24|21/26|23/29|
|Callout|Regular|Semibold|13/18|14/19|15/20|16/21|18/23|20/25|22/28|
|Subhead|Regular|Semibold|12/16|13/18|14/19|15/20|17/22|19/24|21/28|
|Footnote|Regular|Semibold|12/16|12/16|12/16|13/18|15/20|17/22|19/24|
|Caption 1|Regular|Semibold|11/13|11/13|11/13|12/16|14/19|16/21|18/23|
|Caption 2|Regular|Semibold|11/13|11/13|11/13|11/13|13/18|15/20|17/22|

Larger accessibility sizes:

|Style|Weight|Emph.|AX1|AX2|AX3|AX4|AX5|
|---|---|---|---|---|---|---|---|
|Large Title|Regular|Bold|44/52|48/57|52/61|56/66|60/70|
|Title 1|Regular|Bold|38/46|43/51|48/57|53/62|58/68|
|Title 2|Regular|Bold|34/41|39/47|44/52|50/59|56/66|
|Title 3|Regular|Semibold|31/38|37/44|43/51|49/58|55/65|
|Headline|Semibold|Semibold|28/34|33/40|40/48|47/56|53/62|
|Body|Regular|Semibold|28/34|33/40|40/48|47/56|53/62|
|Callout|Regular|Semibold|26/32|32/39|38/46|44/52|51/60|
|Subhead|Regular|Semibold|25/31|30/37|36/43|42/50|49/58|
|Footnote|Regular|Semibold|23/29|27/33|33/40|38/46|44/52|
|Caption 1|Regular|Semibold|22/28|26/32|32/39|37/44|43/51|
|Caption 2|Regular|Semibold|20/25|24/30|29/35|34/41|40/48|

### macOS built-in text styles

Values in pt; point sizes based on 144 ppi @2x.

|Style|Weight|Size|Line height|Emph.|
|---|---|---|---|---|
|Large Title|Regular|26|32|Bold|
|Title 1|Regular|22|26|Bold|
|Title 2|Regular|17|22|Bold|
|Title 3|Regular|15|20|Semibold|
|Headline|Bold|13|16|Heavy|
|Body|Regular|13|16|Semibold|
|Callout|Regular|12|15|Semibold|
|Subheadline|Regular|11|14|Semibold|
|Footnote|Regular|10|13|Semibold|
|Caption 1|Regular|10|13|Medium|
|Caption 2|Medium|10|13|Semibold|

### tvOS built-in text styles

Values in pt; point sizes based on 72 ppi @1x, 144 ppi @2x.

|Style|Weight|Size|Leading|Emph.|
|---|---|---|---|---|
|Title 1|Medium|76|96|Bold|
|Title 2|Medium|57|66|Bold|
|Title 3|Medium|48|56|Bold|
|Headline|Medium|38|46|Bold|
|Subtitle 1|Regular|38|46|Medium|
|Callout|Medium|31|38|Bold|
|Body|Medium|29|36|Bold|
|Caption 1|Medium|25|32|Bold|
|Caption 2|Medium|23|30|Bold|

### watchOS Dynamic Type sizes

Size/leading in pt. Defaults: S on 38mm, L on 40/41/42mm, xL on 44/45/49mm.

|Style|Weight|Emph.|xS|S|L|xL|xxL|xxxL|AX1|AX2|AX3|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Large Title|Regular|Bold|30/32.5|32/34.5|36/38.5|40/42.5|41/43.5|42/44.5|44/46.5|45/47.5|46/48.5|
|Title 1|Regular|Semibold|28/30.5|30/32.5|34/36.5|38/40.5|39/41.5|40/42.5|42/44.5|43/46|44/47|
|Title 2|Regular|Semibold|24/26.5|26/28.5|28/30.5|30/32.5|31/33.5|32/34.5|34/41|35/37.5|36/38.5|
|Title 3|Regular|Semibold|17/19.5|18/20.5|19/21.5|20/22.5|21/23.5|22/24.5|24/26.5|25/27.5|26/28.5|
|Headline|Semibold|Semibold|14/16.5|15/17.5|16/18.5|17/19.5|18/20.5|19/21.5|21/23.5|22/24.5|23/25.5|
|Body|Regular|Semibold|14/16.5|15/17.5|16/18.5|17/19.5|18/20.5|19/21.5|21/23.5|22/24.5|23/25.5|
|Caption 1|Regular|Semibold|13/15.5|14/16.5|15/17.5|16/18.5|17/19.5|18/20.5|18/20.5|19/21.5|20/22.5|
|Caption 2|Regular|Semibold|12/14.5|13/15.5|14/16.5|15/17.5|16/18.5|17/19.5|17/19.5|18/20.5|19/21.5|
|Footnote 1|Regular|Semibold|11/13.5|12/14.5|13/15.5|14/16.5|15/17.5|16/18.5|16/18.5|17/19.5|18/20.5|
|Footnote 2|Regular|Semibold|10/12.5|11/13.5|12/14.5|13/15.5|14/16.5|15/17.5|15/17.5|16/17.5|17/19.5|

### Tracking values

Cells: 1/1000 em, pt (not all apps use 1/1000 em); blank = not listed. iOS, iPadOS and visionOS use SF Pro, SF Pro Rounded and New York. macOS and tvOS use SF Pro, except 52 pt = +0.31 pt and 53 pt = +0.33 pt (1/1000 em unchanged). watchOS uses SF Compact and SF Compact Rounded; "=" marks SF Compact Rounded cells that match SF Compact (20 pt and up). Point sizes based on 144 ppi @2x and 216 ppi @3x; watchOS, 144 ppi @2x.

|pt|SF Pro|SF Pro Rounded|New York|SF Compact|SF Compact Rounded|
|---|---|---|---|---|---|
|6|+41, +0.24|+87, +0.51|+40, +0.23|+50, +0.29|+28, +0.16|
|7|+34, +0.23|+80, +0.54|+32, +0.22|+30, +0.21|+26, +0.18|
|8|+26, +0.21|+72, +0.57|+25, +0.20|+30, +0.23|+24, +0.19|
|9|+19, +0.17|+65, +0.57|+20, +0.18|+30, +0.26|+22, +0.19|
|10|+12, +0.12|+58, +0.57|+16, +0.15|+30, +0.29|+20, +0.20|
|11|+6, +0.06|+52, +0.56|+11, +0.12|+24, +0.26|+18, +0.19|
|12|0|+46, +0.54|+6, +0.07|+20, +0.23|+16, +0.19|
|13|-6, -0.08|+40, +0.51|+4, +0.05|+16, +0.20|+14, +0.18|
|14|-11, -0.15|+35, +0.48|+2, +0.03|+14, +0.19|+12, +0.16|
|15|-16, -0.23|+30, +0.44|0|+4, +0.06|+10, +0.15|
|16|-20, -0.31|+26, +0.41|-2, -0.03|0|+8, +0.12|
|17|-26, -0.43|+22, +0.37|-4, -0.07|-4, -0.07|+6, +0.10|
|18|-25, -0.44|+21, +0.37|-6, -0.11|-8, -0.14|+4, +0.07|
|19|-24, -0.45|+20, +0.37|-8, -0.15|-12, -0.22|+2, +0.04|
|20|-23, -0.45|+18, +0.36|-10, -0.20|0|=|
|21|-18, -0.36|+17, +0.35|-10, -0.21|-2, -0.04|=|
|22|-12, -0.26|+16, +0.34|-10, -0.23|-4, -0.09|=|
|23|-4, -0.10|+16, +0.35|-11, -0.25|-6, -0.13|=|
|24|+3, +0.07|+15, +0.35|-11, -0.26|-8, -0.19|=|
|25|+6, +0.15|+14, +0.35|-11, -0.27|-10, -0.24|=|
|26|+8, +0.22|+14, +0.36|-12, -0.29|-11, -0.28|=|
|27|+11, +0.29|+14, +0.36|-12, -0.32|-12, -0.30|=|
|28|+14, +0.38|+13, +0.36|-12, -0.33|-12, -0.34|=|
|29|+14, +0.40|+13, +0.37|-12, -0.34|-14, -0.38|=|
|30|+14, +0.40|+12, +0.37|-12, -0.37|-14, -0.42|=|
|31|+13, +0.39|+12, +0.36|-13, -0.39|-15, -0.45|=|
|32|+13, +0.41|+12, +0.38|-13, -0.41|-16, -0.50|=|
|33|+12, +0.40|+12, +0.39|-13, -0.42|-17, -0.55|=|
|34|+12, +0.40|+12, +0.38|-14, -0.45|-18, -0.60|=|
|35|+11, +0.38|+11, +0.38|-14, -0.48|-18, -0.63|=|
|36|+10, +0.37|+11, +0.39|-14, -0.49|-20, -0.69|=|
|37|+10, +0.36|+10, +0.38||-20, -0.72|=|
|38|+10, +0.37|+10, +0.39|-14, -0.52|-20, -0.74|=|
|39|+10, +0.38|+10, +0.38||-20, -0.76|=|
|40|+10, +0.37|+10, +0.39|-14, -0.55|-20, -0.78|=|
|41|+9, +0.36|+10, +0.38||-20, -0.80|=|
|42|+9, +0.37|+10, +0.39|-14, -0.57|-20, -0.82|=|
|43|+9, +0.38|+9, +0.38||-20, -0.84|=|
|44|+8, +0.37|+8, +0.37|-14, -0.62|-20, -0.86|=|
|45|+8, +0.35|+8, +0.37||-20, -0.88|=|
|46|+8, +0.36|+8, +0.36|-14, -0.65|-20, -0.92|=|
|47|+8, +0.37|+8, +0.37||-20, -0.94|=|
|48|+8, +0.35|+8, +0.35|-14, -0.68|-20, -0.96|=|
|49|+7, +0.33|+8, +0.36||-21, -1.00|=|
|50|+7, +0.34|+7, +0.34|-14, -0.71|-21, -1.03|=|
|51|+7, +0.35|+6, +0.32||-21, -1.05|=|
|52|+6, +0.33|+6, +0.33|-14, -0.74|-21, -1.07|=|
|53|+6, +0.31|+6, +0.31||-22, -1.11|=|
|54|+6, +0.32|+6, +0.32|-15, -0.79|-22, -1.13|=|
|56|+6, +0.30|+6, +0.30||-22, -1.20|=|
|58|+5, +0.28|+4, +0.25|-15, -0.85|-22, -1.25|=|
|60|+4, +0.26|+4, +0.23||-22, -1.32|=|
|62|+4, +0.24|+4, +0.21|-15, -0.91|-22, -1.36|=|
|64|+4, +0.22|+3, +0.19||-23, -1.44|=|
|66|+3, +0.19|+2, +0.16|-15, -0.97|-24, -1.51|=|
|68|+2, +0.17|+2, +0.13||-24, -1.56|=|
|70|+2, +0.14|+2, +0.14|-16, -1.06|-24, -1.64|=|
|72|+2, +0.14|+2, +0.11|-16, -1.09|-24, -1.69|=|
|76|+1, +0.07|+1, +0.07||-25, -1.86|=|
|80|0|0|-16, -1.21|-26, -1.99|=|
|84|0|0||-26, -2.13|=|
|88|0|0|-16, -1.33|-26, -2.28|=|
|92|0|0||-28, -2.47|=|
|96|0|0|-16, -1.50|-28, -2.62|=|
|100|||-16, -1.56|||
|120|||-16, -1.88|||
|140|||-16, -2.26|||
|160|||-16, -2.58|||
|180|||-17, -2.99|||
|200|||-17, -3.32|||
|220|||-18, -3.76|||
|240|||-18, -4.22|||
|260|||-18, -4.57|||

## Resources

Developer: [Text input and output](https://developer.apple.com/documentation/SwiftUI/Text-input-and-output) (SwiftUI), [Text display and fonts](https://developer.apple.com/documentation/UIKit/text-display-and-fonts) (UIKit), [Fonts](https://developer.apple.com/documentation/AppKit/fonts) (AppKit).

Source: [Typography](https://developer.apple.com/design/human-interface-guidelines/typography), captured 2026-09-12.
