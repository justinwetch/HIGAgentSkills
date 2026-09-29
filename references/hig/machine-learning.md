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
  - "Apple Intelligence and machine learning"
  - "Create ML"
related:
  - generative-ai
---
# Machine learning

Machine learning lets apps and games learn from data and usage patterns. Models can provide familiar capabilities such as image recognition and recommendations, or more individualized feeds, itineraries, and search suggestions. Design the model and the UI/experience together. Model behavior may take a long time to adjust; change the data and metrics you use when the intended app experience changes. Because behavior responds to changing inputs and conditions, teach the app how to interpret data and react rather than designing only for a fixed set of scenarios. First identify the feature’s role, then use the input/output patterns below to plan data, results, feedback, mistakes, and corrections. For model-design guidance, see [Create ML](https://developer.apple.com/documentation/createml).

## Define the feature’s role

Consider each feature along these dimensions:

| Dimension | Distinction and design consequence |
|---|---|
| Critical / complementary | If the app works without the ML-supported feature, ML is complementary; otherwise it is a critical dependency. QuickType suggestions are complementary because the keyboard still works; Face ID’s accurate face recognition is critical. The more central the feature (for example, a personalized news feed), the more people expect reliable results; people are often more forgiving of secondary-feature errors. |
| Private / public | Know what data the feature needs. The more sensitive the data, the more serious inaccurate results can be: a health recommendation may cause anxiety and lost trust, while an unwanted music recommendation is usually inconsequential. Sensitive-data features must prioritize accuracy and reliability; every app must protect privacy at all times. |
| Proactive / reactive | Proactive features provide unrequested results (Siri Suggestions can propose a shortcut from recent routines); reactive features respond to a request or action (QuickType responds as people type). People generally tolerate less low-quality information from proactive features, so additional data may be needed to avoid intrusive or irrelevant results. |
| Visible / invisible | Visible suggestions or choices let people judge reliability and provide feedback (Image Playground lets people describe, adjust, and remix images). Invisible results are less obvious (News can suggest topics from prior engagement), making reliability and feedback harder to communicate. |
| Dynamic / static | Dynamic models improve as people interact; static models improve offline and change when the app updates. Dynamic features often include calibration and implicit or explicit feedback; static ones might not. |

## Explicit feedback

Explicit feedback is information people provide in response to an app-specific request; implicit feedback is inferred from actions. Favoriting and social feedback are implicit because people use them for their own goals, even though an app can learn from them.

- Request explicit feedback **only when necessary**; prefer learning from implicit behavior when possible. Always make it voluntary and explain that it can improve the experience without implying an obligation.
- Describe each option and its consequence in simple, direct, translatable language (for example, “Suggest less pop music,” “Suggest more thrillers,” or “Mute politics for a week”), rather than an imprecise “dislike.” Add an icon when it clarifies the description, but don’t use an icon alone when granularity or consequence would be unclear.
- Consider multiple options, progressively more specific, so people can clarify unwanted suggestions and feel in control.
- Act immediately on feedback and persist the change across the app: hide unwanted content everywhere it would otherwise appear. Consider asking when and where people want results, not only whether they like them.

## Implicit feedback

Implicit feedback is optional for a great ML app, but can improve the experience without extra user work.

- Always secure people’s information. Explain how the app gets and shares it, and provide ways to restrict its flow, especially when activity in one app affects another or could make people think private data was shared.
- Don’t let reinforcement reduce exploration. When possible, combine signals because one action can be ambiguous: viewing, messaging, and adding a photo to a shared album does not necessarily indicate liking it.
- Consider withholding recommendations based on private or sensitive topics when accounts/devices may be shared. Prioritize recent feedback because tastes change; fall back to historical feedback only when recent data is unavailable.
- Update predictions at a cadence matching the person’s mental model: typing suggestions should update immediately, while continuously changing song recommendations can rush or overwhelm people. Reassess feedback when UI changes alter what people see or do, even if the action’s benefit is unchanged. Beware confirmation bias: observed behavior is constrained by available choices and rarely reveals what people might newly want, so don’t rely on implicit feedback alone.

## Calibration

Calibration collects information a feature cannot function without (Face ID’s initial face scan). In general, use it only in that case; if the feature can work without it, consider implicit or possibly explicit feedback instead.

Secure calibration data, explain briefly why it is valuable by describing what the feature does rather than how it works, and collect only essentials. Avoid asking people to calibrate more than once; do it early when possible, then learn from feedback. An object-based feature may need calibration for each new object (for example, a baseball-swing app for each field).

Make calibration quick and easy without compromising information quality: collect a few important pieces and infer the rest, avoid information people must look up or actions that are difficult, give a clear goal and progress, and immediately provide actionable help if progress stalls. Never imply blame or leave people without a next step. Confirm success with a clear path into the feature; let people cancel at any time without judgment or cancellation messaging. Give people a way to update or remove calibration information; the calibration flow can help edit responses, and consider also allowing edits outside it so people can change them at any time.

## Mistakes and corrections

Expect mistakes. Anticipate and mitigate them, give people tools appropriate to their consequences, and learn from them when doing so improves the app; learning can be undesirable if it makes behavior unpredictable. Use limitations to set expectations, corrections to restore success, attributions to show a result’s basis, confidence to gauge result quality, and explicit/implicit feedback to expose mistakes.

- Match empathy, corrective actions, and tools to significance: a wrong keyboard suggestion is annoying; a route that causes a missed flight is serious. Make frequent or predictable mistakes easy to correct, and continuously update features for changing interests, habits, and domain information so people benefit without extra work.
- Keep mistake-handling from complicating the UI when possible. A wrong attribution can magnify the original mistake. Be especially careful with proactive features, whose unrequested errors reduce control and patience. Improving one area can harm another (better dog recognition may reduce cat recognition); assess overall accuracy as models evolve and use people’s preferences to choose which areas to improve.
- Give familiar, easy correction paths and show the automated steps so people can refine or undo them (Photos highlights its auto-crop controls). Show corrected content immediately and persist it; let people correct a correction. Balance automation’s benefit against correction effort, and **never** use corrections to excuse low-quality results. A correction is implicit feedback; learn from it only when it should improve quality. Prefer guided alternatives when possible (speech-to-text completions) over more effortful freeform correction (Photos cropping), or combine both.

## Multiple options

Present one result or several according to the feature. Multiple options increase control and set realistic expectations. They may be proactive suggestions (Apple Music For You), reactive requested options (QuickType), or corrections (Photos Auto-Crop).

- Prefer diverse options that balance accuracy with meaningful differences (Maps can offer no-toll, scenic, or highway routes). Generally avoid too many: people must evaluate each; list them on one screen when possible. Put the most likely first, using validated confidence and context such as time or location; select it by default when appropriate.
- Make choices easy to distinguish with brief descriptions and highlighted differences. Group options that cannot fit in one view, such as recommendations, into rapidly scannable categories. Selections are implicit feedback; learn from them when doing so does not harm the experience. Repeatedly showing incorrect results reduces trust.

## Confidence

Confidence measures certainty, but models do not always provide it. Compute it only when it can improve the experience, and verify that values correlate with result quality; for example, review multiple confidence thresholds or compare app versions. If that relationship is uncertain, don’t show confidence.

Know what a value means before presenting it. People may forgive low-quality results from critical or complementary features, especially with attribution or context, but presenting them prominently erodes trust. Usually translate confidence into familiar concepts: “Because you listen to pop music” is more actionable than “97% match.” When attributions aren’t helpful, consider ranking or ordering results to imply confidence; if you must display confidence directly, consider semantic categories such as “high chance” and “low chance.” Use numerical values when the result is inherently statistical or technical (weather, sports, polling, scientific data), and whenever possible turn them into action (“This is a good time to buy” or “Consider waiting”).

Consider changing presentation at meaningful thresholds, when high or low confidence materially affects the experience (Photos shows high-confidence recognized photos, but asks for confirmation at lower confidence). When validated confidence corresponds to quality, generally suppress low-confidence results, especially unrequested proactive suggestions.

## Attribution

An attribution states the factual basis or rationale for a result without explaining the model. Consider it to help people change behavior, reduce the impact of mistakes, build a mental model, and develop trust. It can distinguish multiple results (for example, “New books by authors you’ve read”). Balance specificity: overly specific text demands interpretation and can feel watchful; overly general text is unhelpful or impersonal. Keep attributions objective and factual, without claiming to understand or judge emotions, preferences, or beliefs (“Because you’ve read nonfiction,” not “Because you love nonfiction”). Avoid technical/statistical jargon except when the result itself is technical or statistical.

## Limitations

Every feature has limits: it may perform some tasks poorly or be unable to perform others. A mismatch between expectation and capability can look like a defect. Identify impactful scenarios and:

- set expectations before use, especially for rare limitations with serious effects (in marketing or feature context); for less serious effects, attributions may suffice;
- demonstrate good inputs and interactions, using placeholder text (Photos: “Photos, People, Places…”) plus its description of scanning the library for suggestions, contextual feedback (Memoji can suggest more light or moving closer), and sensible alternatives instead of no results;
- explain the cause of poor results in plain language (Memoji says it doesn’t work well in the dark), and consider telling frequent users when an update resolves a limitation so they can revisit interactions they had avoided.

## Resources

- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai)
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning)
- [Create ML](https://developer.apple.com/documentation/createml)
- [Core ML](https://developer.apple.com/documentation/coreml)
- [Explore prompt design & safety for on-device foundation models](https://developer.apple.com/videos/play/wwdc2025/248)
- [Discover machine learning & AI frameworks on Apple platforms](https://developer.apple.com/videos/play/wwdc2025/360)

Platform considerations: no additional guidance for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Source: [Apple Human Interface Guidelines — Machine learning](https://developer.apple.com/design/Human-Interface-Guidelines/machine-learning), captured 2026-09-12.
