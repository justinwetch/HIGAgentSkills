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
# Managing Accounts

> Require accounts only when core functionality depends on them.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Accounts can help people access content and track personal details, but they also create commitment and friction. Let people use the app or game without an account unless core functionality requires one.

## Best Practices

- **Explain required accounts.** In the sign-in view, briefly and warmly explain why an account is required, what benefits it provides, and how to sign up.
- **Delay sign-in as long as possible.** Let people understand the app before commitment. Example: shopping app allows browsing; requires sign-in at purchase.
- **Use Sign in with Apple when appropriate** for a consistent, trusted sign-in experience.
- **If not using Sign in with Apple in iOS, iPadOS, macOS, or visionOS, prefer passkeys.** Passkeys simplify account creation/authentication and avoid passwords.
- **If passwords remain, augment security by requiring two-factor authentication.**
- **Identify the authentication method.** Use labels like "Sign In with Face ID", not generic "Sign In".
- **Mention only available authentication methods.** Do not reference Face ID on devices that do not support it. Check capabilities; developer guidance: `LABiometryType`.
- **Avoid app-specific biometric opt-in settings.** People enable biometric authentication at system level; an in-app setting is redundant/confusing.
- **Avoid using "passcode" for account authentication.** Passcode means device unlock or Apple-service authentication; people may think the app asks them to reuse it.

## Account Deletion

If people can create an account in the app/game, the app must help them delete it, not only deactivate it. Follow regional legal requirements, including right-to-be-forgotten rules.

- If legal requirements compel retaining accounts/data or following a specific process, clearly explain what must be maintained and why.
- Provide a clear in-app way to start deletion. If deletion cannot happen in-app, provide a direct, easy-to-discover webpage link; do not bury it in Privacy Policy or Terms.
- If the account was created with Sign in with Apple, revoke associated tokens when deleting the account.
- Keep account-deletion experience consistent across app/game and website. Do not make one flow longer or harder.
- If offering scheduled deletion, also offer immediate deletion.
- Tell people when deletion will complete; notify them when finished.
- If supporting in-app purchases, explain billing/cancellation effects:
  - Auto-renewable subscription billing continues through Apple until canceled, regardless of account deletion.
  - After account deletion, people may still need to cancel the subscription or request a refund.
- Provide information for canceling subscriptions and managing purchases.
- Support account deletion even if people did not use the app to purchase the subscription.

## TV Provider Accounts

Many TV providers support system-level sign-in. If a TV provider app requires sign-in, use TV Provider Authentication for efficient onboarding.

- Avoid showing sign-out when people are signed in at system level.
- If sign-out must appear, invoking it should prompt people to go to Settings > TV Provider.
- Never instruct people to sign out by changing Settings > Privacy TV provider controls; those manage which apps can access the TV provider account, not sign-out.

## Platform Considerations

### tvOS

- Ask for the minimum information; most people use a remote, not a keyboard.
- Prefer sign-up/authentication on another device. Associated domains let Apple TV safely suggest credentials, including Sign in with Apple.
- For shared accounts, avoid asking people to choose a profile every time they become current user.
- tvOS 16+: apps can share credentials with all users while storing individual profiles/user data separately; use the current user's profile automatically.
- Minimize data entry. For more than small amounts of information, ask people to visit a website on another device.
- For email entry, show the email keyboard screen with recently entered addresses.

### watchOS

Use iCloud synchronization to provide Keychain access, autofill user names/passwords, and preserve app settings.

## Developer References

- Authentication Services passkeys
- iCloud Keychain Verification Codes
- Local Authentication / `LABiometryType`
- Sign in with Apple token revocation
- Associated domains
- `kSecUseUserIndependentKeychain`
- User Management Entitlement
