---
topic: managing-accounts
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns
triggers:
  - "account"
  - "account creation"
  - "sign in"
  - "login"
  - "authentication"
  - "passkey"
  - "biometric authentication"
  - "Face ID sign in"
  - "delete account"
  - "account deletion"
  - "TV provider account"
related:
  - in-app-purchase
  - onboarding
  - privacy
  - settings
  - sign-in-with-apple
---

# Managing accounts

**Ask people to create an account only if your core functionality requires it**; if you do, consider Sign in with Apple.

## Best practices

- **Explain why an account is required, its benefits and how to sign up** in a brief, friendly sign-in view message.
- **Delay sign-in as long as possible**; a shopping app might wait until purchase.
- **Without Sign in with Apple, prefer passkeys** in iOS, iPadOS, macOS and visionOS apps (Supporting passkeys). If you keep passwords, require two-factor authentication.
- **Always identify the authentication method**: "Sign In with Face ID", not "Sign In".
- **Refer only to methods available in the current context** (`LABiometryType`).
- **In general, avoid an in-app biometric opt-in setting**; people enable it system-wide.
- **Avoid calling account authentication a *passcode***; people may think you want their device passcode.

## Deleting accounts

If people can create an account in your app or game, you must let them delete it, not just deactivate it. Comply with regional deletion law, including the right to be forgotten; if law compels you to retain accounts or data (like health records) or follow a specific process, clearly describe what you retain and the process.

- **Provide a clear way to initiate deletion in-app.** If people can't delete in-app, you must link directly to the deletion webpage; make the link easy to discover, not buried in Privacy Policy or Terms of Service pages.
- If the account used Sign in with Apple, revoke its tokens on deletion (Revoke tokens REST API).
- **Provide consistent in-app and website deletion**; avoid making either flow longer or more complicated.
- **Consider allowing scheduled deletion**; if you do, also offer immediate deletion.
- **Tell people when deletion will complete, and notify them when it's done.**
- **If you support in-app purchases, explain billing and cancellation on deletion**, such as that Apple keeps billing auto-renewable subscriptions until people cancel, regardless of deletion, and that people then need to cancel or request a refund; describe how to cancel subscriptions and manage purchases. Support deletion even for subscriptions bought outside your app.

## TV provider accounts

If your TV provider app requires sign-in, use TV Provider Authentication.

- **Avoid a sign-out option when people are signed in at the system level.** If you must include one, it needs to prompt people to go to Settings > TV Provider to sign out.
- **Never direct sign-out to privacy controls**; the TV provider controls in Settings > Privacy manage which apps can access the account.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS or visionOS.

### tvOS

- **Prefer sign-up and authentication on another device.** With associated domains configured, Apple TV can work with other devices to suggest credentials, including Sign in with Apple.
- **On a shared account, avoid asking people to pick their profile each time they become the current user.** tvOS 16 and later: share credentials across users, keep profiles separate, use the current profile automatically (`kSecUseUserIndependentKeychain`, `com.apple.developer.user-management` entitlement).
- **Minimize data entry**, since most people use a remote. For more than a little information, send people to a website on another device; for email, show the email keyboard screen, which lists recent addresses.

### watchOS

Use iCloud synchronization for Keychain access, enabling credential autofill and preserved app settings.

## Resources

Source: [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts), captured 2026-09-12.
