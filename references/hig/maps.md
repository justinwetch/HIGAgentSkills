---
topic: maps
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "map"
  - "MapKit"
  - "location"
  - "annotation"
  - "overlay"
  - "geocoding"
  - "MKStandardMapConfiguration.EmphasisStyle"
  - "MKMapFeatureOptions"
  - "mapItemDetailSelectionAccessory(_:)"
  - "mapFeatureSelectionAccessory(_:)"
  - "mapView(_:selectionAccessoryFor:)"
  - "selectionAccessory"
  - "selectableMapFeatureSelectionAccessory"
  - "MapItemDetailSelectionAccessoryStyle"
  - "MKSelectionAccessory.MapItemDetailPresentationStyle"
  - "PlaceSelectionAccessoryStyle"
  - "mapItemDetailSheet(item:displaysMap:)"
  - "init(mapItem:displaysMap:)"
  - "WKInterfaceMap"
related:
  - layout
---

# Maps

A map shows outdoor or indoor geographic data in an app or website, with Maps-style zooming, panning, rotation, annotations, overlays and routing, in standard, satellite or hybrid views.

## Best practices

- **In general, make your map interactive.**
- **Pick a map emphasis style that suits your app** (`MKStandardMapConfiguration.EmphasisStyle`): *default* (fully saturated) suits most maps without many custom elements and matches the Maps app when people might switch between them; *muted* (desaturated) makes information-rich content stand out.
- **Help people find places in your map.** Consider search combined with category filters.
- **Clearly identify elements that people select** with distinct styling, like an outline and color variation.
- **Cluster overlapping points of interest.** One pin represents nearby points; clusters expand as people zoom in.
- **Help people see the Apple logo and legal link.** Covering them temporarily is fine; don't cover them all the time.
  - Pad them from map edges and custom controls; 7 pt at the sides and 10 pt above and below works well.
  - Avoid making them move with your interface; it's best when they appear fixed to the map.
  - If custom interface can move relative to the map, place them by its lowest position, e.g., 10 pt above a pull-up card's lowest resting position.
  - They aren't shown on maps smaller than 200x100 px.

## Custom information

- **Use annotations that match the visual style of your app** (`MKAnnotationView`). The default marker is red with a white pin icon. You can change the tint, and replace the icon with a string or image; a string can use any characters, including Unicode, but keep it to two to three characters.
- **To display custom information related to standard map features, consider making them independently selectable** (`MKMapFeatureOptions`): the system treats Apple-provided features (points of interest, territories, physical features) separately from your annotations, and you can customize what they show on selection.
- **Use overlays to define map areas with a specific relationship to your content** (`MKOverlayLevel`):
  - *Above roads* (default): below buildings, trees and other features.
  - *Above labels*: hides everything beneath; for content abstracted from map features, or hiding irrelevant areas.
- **Make sure there's enough contrast between custom controls and the map.** Consider a thin stroke or light drop shadow on controls, or blend modes on the map.

## Place cards

Place cards show structured, up-to-date information for places you specify.

### Displaying place cards in a map

You can present a place card when someone selects one of your places (`mapItemDetailSelectionAccessory(_:)`, `mapView(_:selectionAccessoryFor:)`, `selectionAccessory`) or another place, like a point of interest, territory or physical feature (`mapFeatureSelectionAccessory(_:)`, `selectableMapFeatureSelectionAccessory`). On websites, an embedded map can show a place card by default for one specified place ([Maps Embed API](https://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api)).

Styles (`MapItemDetailSelectionAccessoryStyle`, `MKSelectionAccessory.MapItemDetailPresentationStyle`, `PlaceSelectionAccessoryStyle`): *automatic* (chosen from map view size); *callout*, a popover beside the place, either *full* (large, detailed) or *compact* (concise), defaulting to *automatic* callout, chosen from map view size, if unspecified; *caption*, an "Open in Apple Maps" link; *sheet*. A full callout appears as a popover in iPadOS and macOS and as a sheet in iOS.

- **Consider your map presentation when choosing a style.** For a small map with many annotations, consider compact callout.
- **Make sure your place card looks great on different devices and window sizes.** If you specify a style, keep content viewable as sizes change; for full callouts, you can set a minimum width to prevent text overflow.
- **Avoid duplicating information.** Consider what you already show when choosing a style; if a full callout repeats it, compact callout or caption might complement better.
- **Keep the location on your map visible when displaying a place card.** You can offset the card and point it at the location (`offset(_:)`, `accessoryOffset`, `selectionAccessoryOffset`).

### Adding place cards outside of a map

You can also present place cards outside a map in an app or website, e.g., from a list like search results or a store locator (`mapItemDetailSelectionAccessory(_:)`, `mapItemDetail(_:)`, `PlaceDetail`).

- Important: Outside a map view, you must include a map in the place card (`mapItemDetailSheet(item:displaysMap:)`, `init(mapItem:displaysMap:)`).
- **Use location-related cues in surrounding content to communicate that people can open a place card**, like a place name and address beside a details button, or, compactly, a map pin icon with a place name.

## Indoor maps

Venue apps can design custom interactive indoor maps with area overlays, labels, icons and routes.

- **Adjust map detail based on the zoom level.** Show large areas like rooms and buildings at all zoom levels; progressively add detailed features and labels when zoomed in.
- **Use distinctive styling to differentiate the features of your map**, like color with icons.
- **Offer a floor picker if your venue includes multiple levels.** Keep floor numbers concise; in most cases, numbers rather than names suffice.
- **Include surrounding areas to provide context.** If they're noninteractive, dim them and use a distinct color.
- **Consider supporting navigation between your venue and nearby transit points** like bus stops, stations and parking. You might offer a quick switch to Apple Maps.
- **Limit scrolling outside of your venue.** When possible, keep part of the indoor map onscreen at all times; you may need to vary allowed scrolling by zoom level.
- **Design an indoor map that feels like a natural extension of your app.** Don't try to replicate Apple Maps; match overlays, icons and text to your app's style ([IMDF](https://register.apple.com/resources/imdf/)).

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS or visionOS.

### watchOS

Maps are noninteractive static snapshots (`WKInterfaceMap`): place the map at design time and set the region at runtime; tapping opens Maps. You can add up to five annotations.

- **Fit the map interface element to the screen**, entirely visible without scrolling.
- **Show the smallest region that encompasses the points of interest.** Map content doesn't scroll, so all key content must be visible in the region.

## Resources

Developer: MapKit, MapKit JS.

Source: [Maps](https://developer.apple.com/design/human-interface-guidelines/maps), captured 2026-09-12.
