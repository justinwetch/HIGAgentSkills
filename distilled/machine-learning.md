---
topic: machine-learning
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "machine learning"
  - "ML"
  - "Core ML"
  - "model"
  - "prediction"
  - "classifier"
related:
  - generative-ai
---
# Machine Learning

> Machine learning enables apps to learn from data and patterns, improving experiences and enabling intelligent behaviors.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## ML Role Dimensions (Design Framework)

Evaluating your ML feature across these dimensions guides your design decisions:

| Dimension | Examples |
|---|---|
| **Critical vs. Complementary** | Critical: Face ID fails without ML. Complementary: QuickType still works without suggestions. |
| **Private vs. Public data** | Health misreads → anxiety/lost trust; music misreads → inconsequential. Higher sensitivity = must prioritize accuracy. |
| **Proactive vs. Reactive** | Proactive: Siri Suggestions based on routine. Reactive: QuickType responds to current input. Proactive requires higher accuracy — users didn't ask for it. |
| **Visible vs. Invisible** | Visible: word completion list. Invisible: keyboard tap-area optimization. Visibility affects how people perceive reliability. |
| **Dynamic vs. Static** | Dynamic: Face ID adapts to changing faces. Static: Photos improves object recognition per iOS release. |

## Explicit Feedback

Explicit feedback = information people provide in response to a specific app request.
*(Favoriting and social feedback are implicit, not explicit — people use them for their own goals.)*

- **Request only when necessary.** Prefer implicit feedback — no extra user effort.
- **Always voluntary** — never mandatory.
- **Direct, specific language**: "Suggest less pop music" > "Dislike." Describe the consequence.
- Add icons to descriptions where helpful — never icon alone.
- **Offer multiple options** getting progressively more specific.
- **React immediately and persist** — if people say to remove content, it disappears instantly and stays removed.

## Implicit Feedback

Implicit feedback = behavioral data gathered from how people use your app.

- **Secure all data** — implicit feedback often captures sensitive info.
- **Give people control** — explain how data is collected/shared; let them restrict it.
- **Don't reinforce too narrowly** — implicit feedback amplifies current behavior; allow room for discovery.
- **Use multiple signals** — a single action (e.g., viewing a photo) is ambiguous. Combine signals to understand intent.
- **Withhold sensitive suggestions** when devices are shared.
- **Prioritize recent feedback** — people's preferences change. Fall back to historical if recent unavailable.
- **Match update cadence to user mental model** — typing suggestions: instant; music recommendations: not continuous.
- **Watch for UI change effects** — moving a button changes interaction data even without changing the button's value.
- **Beware confirmation bias** — implicit feedback reflects what's already visible; doesn't reveal new interests.

## Calibration

Calibration = initial data collection before a feature can work.

- **Only use calibration when the feature can't function without it.** Otherwise collect via implicit/explicit feedback.
- **Be clear why you need the information.** Focus on the benefit, not the mechanism.
- **Collect only essential information.**
- **One-time per person** (exception: calibrating with an object each time, e.g., a new baseball field).
- **Make it quick** — prioritize a few key data points; infer the rest.
- **Show goal and progress** — like Face ID's face-scan progress ring.
- **Assist if progress stalls** — never imply fault; always give a clear next step.
- **Confirm success** — reward with a clear path into the feature.
- **Allow cancel at any time.** No judgment, no special messaging.
- **Let people update or remove calibration data** outside the calibration flow.

## Corrections

Corrections = how people fix your app's ML mistakes.

- **Familiar, easy-to-discover correction paths** — show the controls used in automation so people can adjust them.
- **Immediate value + persistence** — show corrected content instantly; save the change.
- **Let people correct their corrections** — respond immediately; persist.
- **Balance feature value vs. correction effort** — if corrections are too burdensome, people stop using the feature.
- **Never rely on corrections for low-quality results** — it erodes trust.
- **Learn from corrections when appropriate** — only when it will genuinely improve results.
- **Prefer guided corrections** (specific alternatives) over freeform when possible.

## Mistakes

- Anticipate, mitigate, and learn from mistakes.
- **Match corrective tools to seriousness of consequence** (missed Siri word vs. missed flight).
- **Easy corrections for predictable mistakes.**
- **Update continuously** via implicit feedback, domain-specific data, and app updates.
- **Don't complicate the UI** to handle mistakes — lightweight patterns work best.
- **Proactive features must be especially accurate** — unsolicited results have zero tolerance.
- **Optimizing one area can degrade another** — watch for this as models evolve.

## Multiple Options

Multiple results give people control and align model predictions with actual desires.

- **Prefer diverse options** (e.g., Maps showing toll-free, scenic, and highway routes).
- **Don't offer too many** — cognitive overload. List on one screen, no scrolling.
- **Most likely option first** — use confidence + contextual signals (time of day, location). Consider pre-selecting it.
- **Make options easy to distinguish** — brief description; highlight differences. Group if many.
- **Learn from selections** — use as implicit feedback to improve future ordering.

## Confidence

Confidence = certainty measure for a result. Not all models produce it by default.

- **Verify what your confidence values actually mean** before using them. High confidence ≠ high quality unless you verify the correlation.
- **Translate to human concepts** rather than displaying raw numbers — "Because you listen to pop music" > "97% match."
- **Order results by implied confidence** if labeling isn't appropriate.
- **Use semantic categories** when you must display confidence — "high chance" / "low chance" vs. raw percentages.
- **Display numerical confidence only when statistical values are expected** (weather, sports, polls).
- **Actionable suggestions** > percentages — e.g., "This is a good time to buy."
- **Adapt presentation at different thresholds** — e.g., Photos shows photos confidently matched; asks to confirm low-confidence matches.
- **Don't show proactive suggestions when confidence is low** — set a floor threshold.

## Attribution

Attribution = explaining what drove a result, without revealing model internals.

- Use to: encourage behavior change, minimize impact of mistakes, help people build a mental model, promote trust.
- **Helps distinguish among multiple options** — "New books by authors you've read."
- **Balance specificity** — too specific feels intrusive; too general feels impersonal.
- **Factual and objective** — no implied judgment of emotions/beliefs. "Because you've read nonfiction" > "Because you love nonfiction."
- **No technical jargon** in most cases. Exception: when the result itself is statistical (weather, sports, poll).

## Limitations

Every ML feature has limits — manage user expectations proactively.

- **Set expectations before use** — mention limitations in marketing/onboarding if the impact is serious.
- **Show how to get the best results** — placeholder text, in-context feedback, alternative suggestions.
- **Explain when limitations cause poor results** — e.g., Animoji warns that it doesn't work well in the dark.
- **Notify people when a limitation is resolved** — so they return to interactions they'd previously stopped attempting.
