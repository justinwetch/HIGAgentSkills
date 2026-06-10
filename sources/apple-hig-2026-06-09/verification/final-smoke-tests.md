# Final Smoke Tests

Source corpus: `sources/apple-hig-2026-06-09`

Smoke tests were checked against `SKILL.md` and regenerated `routing-index.md`.

| Query | Expected loaded files | Result |
|---|---|---|
| What principles should guide a new iOS app design? | Tier 1 including `design-principles`; platform match `designing-for-ios` | Pass |
| Review this interface using Apple design principles. | Tier 1 including `design-principles`, `accessibility`, `layout`, `privacy`, `writing` | Pass |
| What are the HIG rules for Liquid Glass color? | Tier 1 `materials` and `color`; related `dark-mode` from materials/color context | Pass |
| How should token fields work? | Tier 4 direct match `token-fields`; related `search-fields` when expanded from the file | Pass |
| What are the privacy permission request guidelines? | Tier 1 `privacy`; trigger match `onboarding` for permissions request | Pass |
| What changed for sidebars/search fields/menus? | Tier 3 matches `sidebars`, `search-fields`, and `menus` | Pass |
| How should Sign in with Apple be displayed? | Tier 3 match `sign-in-with-apple` | Pass |
| What are the rules for widgets in StandBy? | Tier 3 match `widgets`; related platform/foundation files already available through tier 1 | Pass |

Acceptance: broad design judgment routes through always-loaded `design-principles`; component/API queries route through generated trigger entries; tier-4 token fields load only on direct match.
