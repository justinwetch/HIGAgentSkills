---
topic: generative-ai
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "generative AI"
  - "AI"
  - "LLM"
  - "generated content"
  - "foundation model"
  - "Foundation Models"
  - "Core AI"
related:
  - machine-learning
  - inclusion
  - accessibility
  - privacy
  - loading
---
# Generative AI

Generative AI uses machine-learning models to create or transform text, images, and other content for creativity, communication, productivity, stories, image editing, and AI-driven game dialogue.

## Design responsibly

Design for direct and indirect effects on people, systems, and society. Small input changes (even repeating one) can produce different outcomes, and requests/responses are hard to anticipate. Make the experience inclusive, careful, and privacy-protective.

- Keep people in control: honor in-scope requests when output is clear, handle sensitive content carefully, let people dismiss/revert/retry, and identify where/when AI is used. Account for model bias/stereotypes: for people’s images/descriptions, ask for needed information rather than infer personal/cultural attributes, clarify before assuming gender or relationships, and test with diverse people. See [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) and [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- Offer generative features for clear value (time, communication, creativity). Preserve a good experience when AI is unavailable or declined. AI may be essential without a substitute; when complementary, consider a non-AI fallback (regular emoji beside Genmoji; notifications beside Apple Intelligence summaries).

## Transparency and privacy

Tell people where AI is used; never make AI interaction/content appear human-authored; align disclosure with regional regulations. Set capability/limit expectations (for example, a brief tutorial, curated starter prompts for open-ended inputs, upfront limits, good-result guidance, and explanations for inferior results). See [Limitations](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Limitations).

Choose model type for privacy, capability, and performance. On-device models keep information on-device, respond quickly, and work offline. Consider servers for more processing power/context; process locally as much as possible, minimize sharing, and explain what is sent, stored off-device, or used for training.

Ask permission before using personal/usage data (details, messages, photos, feature use); then use the minimum and provide a clear opt-out. Get explicit permission for sensitive data used for improvement/storage and handle it carefully. Understand third-party practices; outputs can also contain sensitive information. Apps for kids have stricter rules. Explain benefits and whether personal information trains/improves the model.

## Models, datasets, and inputs

Evaluate model types hands-on early: some are general, others specialized. Availability can depend on device, network, and battery; [Foundation Models](https://developer.apple.com/documentation/foundationmodels) requires a compatible device with Apple Intelligence turned on.

Choose/create datasets intentionally: use diverse subject representations, learn provenance, license data you don’t own, and offer choices when using people’s data. Test imperfect real-world datasets early to mitigate learned bias and misinformation.

Guide people toward good results; one technique to consider is offering diverse, predefined example inputs. Explain that hallucinations can sound factual while made up (including wrong dates or people). Scope generation; avoid factual requests unless you’re confident the model has access to verified, up-to-date information for the task, and avoid contexts where hallucinations could harm.

Before irreversible/problematic tasks, consider consequences and get permission. Avoid automating destructive actions (deleting photos) or hard-to-undo actions (purchases); generally confirm significant actions. Follow model-specific and local government/regulatory AI policies.

## Outputs

- To make refinement/reversion easy, for example surface Edit, Undo, Retry, or Adjust near generated content; acknowledge when a correction or personalization takes effect.
- When output is blocked or undesirable, coach people toward a better request and, when possible, show examples.
- Identify risks, make policies, and test accidental/purposeful misuse: out-of-scope, unrelated, poorly represented, vague, ambiguous, personal, sensitive, controversial, harmful, and incorrect requests. Use findings to improve the model, prevention, and responses; it may not be possible to mitigate every harmful scenario.
- Reduce copyright risk by building on models with protections, curating inputs, offering pre-approved prompts, and/or telling the model to avoid mimicking specified content or styles.
- Design for latency. Non-generative [ARKit body-position tracking](https://developer.apple.com/documentation/arkit/capturing-body-motion-in-3d) and [Vision](https://developer.apple.com/documentation/vision) typically suit real time; generative models take longer, so show loading or generate in the background. See [Loading](https://developer.apple.com/design/human-interface-guidelines/loading). Consider specific reassuring status (“Finding substitutions for ingredients,” “Summarizing key themes from your notes”) rather than “Processing…”; explain failures plainly and give a next step.
- Consider one result or multiple meaningfully different versions. Multiple choices can increase control and bridge the model’s interpretation with intent (Image Playground can generate multiple images); see [Multiple options](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Multiple-options).

## Continuous improvement

Consider updates for behavior, feedback, new data, and improved capabilities. Blocked-word lists can update independently; larger improvements can ship with app releases. For a newer base model, plan fine-tuning, retesting, and prompt engineering; retrain/fine-tune your own model as needed and test every update for unexpected behavior.

Let people voluntarily report output feedback in a clear, noninterruptive location; resolve issues quickly. Consider quick positive/negative feedback controls, and you might also offer detailed feedback for complex problems. See [Explicit feedback](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Explicit-feedback) and [Implicit feedback](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Implicit-feedback).

Design flexibly for changing models/resources; separating model from experience can permit replacement while preserving the user experience.

Platform considerations: no additional guidance for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Resources: [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning), [Foundation Models](https://developer.apple.com/documentation/foundationmodels), [Core AI](https://developer.apple.com/documentation/coreai), [Explore prompt design & safety for on-device foundation models](https://developer.apple.com/videos/play/wwdc2025/248), [Create UI prototypes using agents in Xcode](https://developer.apple.com/videos/play/wwdc2026/227), [What’s new in the Foundation Models framework](https://developer.apple.com/videos/play/wwdc2026/241), and [Acceptable Use Requirements for the Foundation Models Framework](https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework).

Source: [Apple Human Interface Guidelines — Generative AI](https://developer.apple.com/design/Human-Interface-Guidelines/generative-ai), captured 2026-09-12.
