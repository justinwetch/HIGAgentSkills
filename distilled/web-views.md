---
topic: web-views
tier: 4
platforms: [ios, ipados, macos]
category: components/content
triggers:
  - "web view"
  - "WKWebView"
  - "embedded HTML"
  - "in-app browser"
related:
  []
---
# Web Views

> A web view loads and displays rich web content (HTML, websites) inline within your app.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS, watchOS)*

## Best Practices

- **Support forward/back navigation when people will visit multiple pages.** This behavior isn't on by default — enable it explicitly and provide corresponding UI controls.
- **Don't build a web browser.** Brief, in-context web access is fine. Don't replicate Safari's functionality.
