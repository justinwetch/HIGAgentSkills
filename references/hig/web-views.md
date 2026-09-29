---
topic: web-views
tier: 4
platforms: [ios, ipados, macos, visionos]
category: components/content
triggers:
  - "web view"
  - "WebKit"
  - "WKWebView"
  - "embedded HTML"
  - "in-app browser"
related:
  []
---

# Web views

A web view loads and displays rich web content—such as embedded HTML and websites—directly within an app. For example, Mail uses one to show HTML message content.

## Best practices

- Forward/back navigation is supported but off by default; if people are likely to visit multiple pages, enable it and provide both controls.
- Brief in-app website access is fine; avoid replicating Safari, the primary web browser, because doing so is unnecessary and discouraged.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, or visionOS. Web views are not supported in tvOS or watchOS.

## Resources

- [Webkit.org](https://webkit.org/).
- [`WKWebView`](https://developer.apple.com/documentation/webkit/wkwebview) — WebKit object that displays interactive web content, such as for an in-app browser.
- [Explore WKWebView additions](https://developer.apple.com/videos/play/wwdc2021/10032).

Source: [Apple HIG — Web views](https://developer.apple.com/design/human-interface-guidelines/web-views), captured 2026-09-12.
