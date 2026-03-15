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
related:
  - machine-learning
  - writing
---
# Generative AI

> Generative AI uses ML models to create and transform text, images, and other content. Use it where it provides clear value; design responsibly.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Core Principles

- **Responsible design**: AI outcomes vary with the same input; you can't predict all requests. Design for inclusion, privacy, and care.
- **Keep people in control**: let people dismiss, revert, or retry AI outputs. Always let them know when AI is being used.
- **Inclusive experiences**: AI models favor common training data — watch for biases. Ask people for info rather than inferring sensitive attributes (gender, culture, relationships). Test with diverse groups.
- **Offer generative features only where they add clear, specific value** (time savings, better communication, enhanced creativity).
- **Ensure a great experience even when AI is unavailable or declined.** Offer a non-AI fallback whenever possible.

## Transparency

- **Disclose AI use** — set expectations; never trick people into thinking they're interacting with human-authored content.
- **Clarify capabilities and limitations** — brief tutorial on introduction; example prompts for open-ended features. For limitations, see [machine-learning#Limitations].
- Align disclosure approach with local regulations.

## Privacy

- **Prefer on-device processing** when capable models are available (e.g., Apple Foundation Models framework). On-device is faster, works offline, and doesn't send data off the device.
- **Server-based models**: process as much as possible locally first; minimize what's shared. Tell people if info may be sent to a server; explain what's stored or used for training.
- **Ask permission before using personal information** (messages, photos, usage data). Use the minimum data needed; always offer opt-out.
- **Disclose clearly**: how data is used, stored, shared with third parties. Get explicit permission if storing for model improvement.
- Health apps and minors have stricter requirements.

## Models and Datasets

- **Evaluate model capabilities hands-on early.** Know what it can and can't do. Note: some model types (e.g., FoundationModels) require a compatible device with Apple Intelligence on.
- **Choose datasets intentionally**: diverse, representatively sourced, properly licensed. Test and mitigate bias proactively.

## Inputs

- **Guide people** toward producing great results — offer example prompts.
- **Address hallucinations proactively**: AI may produce plausible but false content. Communicate that outputs may contain errors. Don't use AI for facts unless the model has verified, up-to-date data. Never use AI output in situations where hallucinations could cause harm.
- **Get confirmation before destructive or hard-to-undo actions** (deleting photos, making purchases). Avoid automating such actions.
- **Review model usage policies and regional AI regulations** before deployment.

## Outputs

- **Help people improve blocked/poor requests** — coach them; offer example prompts that would succeed.
- **Reduce harmful outcomes**: test for out-of-scope requests, poorly phrased inputs, sensitive topics, misuse scenarios. Use results to improve the model and policies.
- **Avoid replicating copyrighted content**: use models that guard against this; curate approved prompts; explicitly tell the model to avoid certain styles.
- **Factor in latency**: generative models take time. Design a loading state or generate in the background. Show a progress indicator or interim content.
- **Offer alternate result versions** when multiple meaningfully different outputs are possible — gives people control.

## Continuous Improvement

- **Plan for model iteration**: update to adapt to behavior, incorporate feedback, and leverage new capabilities. Some updates (e.g., blocked words) can happen frequently; major features around app updates.
- **Let people voluntarily share feedback** on outputs — thumbs up/down for quick feedback, detailed report for complex issues. Take feedback seriously and resolve issues quickly. Feedback mechanism must not interrupt the experience.
- **Design adaptable features**: separate model from UX so you can swap models over time.
