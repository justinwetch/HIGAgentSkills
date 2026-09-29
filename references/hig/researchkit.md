---
topic: researchkit
tier: 4
platforms: [ios, ipados]
category: technologies
triggers:
  - "ResearchKit"
  - "clinical study"
  - "research app"
  - "consent"
  - "survey"
  - "active task"
related:
  - healthkit
  - carekit
---
# ResearchKit

ResearchKit provides predesigned screens and transitions for custom research apps, enabling people to participate in medical studies.

> These guidelines are informational and don’t constitute legal advice. Contact an attorney about developing a research app and applicable laws.

## Onboarding order

Always present these screens in order; people generally don’t revisit them after completion, so make each clear:

1. **Introduction:** Describe the study’s subject and purpose, provide a call to action, and let existing participants log in and resume an in-progress study.
2. **Eligibility:** Determine eligibility as soon as possible, before consent; ineligible people need not proceed to consent. Ask only necessary requirements, use simple language, and make entry easy.
3. **Informed consent:** Ensure participants understand the study before seeking consent, including how it works and their responsibilities. Consent can incorporate legal requirements and institutional or ethics-review-board requirements; comply with applicable App Store Guidelines, including consent requirements. Break a long form into digestible sections (data gathering/use, benefits, risks, time commitment, withdrawal). Give a high-level explanation with **Learn More** detail where needed, and let participants view the entire form before agreeing. Consider a comprehension quiz where appropriate. After agreement, show confirmation, collect a signature and (if appropriate) contact details. Most research apps email a PDF consent copy for the participant’s records.
4. **Permission to access data:** When appropriate, request permission to access the participant’s device or data. Also request notification permission if the app requires it. Explain why the study needs each requested type (location, Health, and so on), and don’t request data that isn’t critical. Participants may choose to share data for future research or only this study where the design offers that choice.

## Conducting research

Studies may combine surveys and active tasks; depending on the architecture, participants may use a section multiple times or only once.

### Surveys

ResearchKit supports true/false, multiple-choice, date/time, sliding-scale, and open-ended text answers. Keep participants oriented: state question count and approximate duration, use one screen per question, show progress, keep each survey short (several short surveys generally work better than one long survey), use standard type for a question and slightly smaller type for explanatory text, and announce completion.

### Active tasks

Active tasks require participation—such as speaking into a microphone, tapping fingers, walking, or taking a memory test. Give clear, simple instructions, state requirements such as time or circumstances, and make completion obvious.

## Profile and dashboard

ResearchKit offers a profile screen; consider a custom screen to motivate participation and track study progress. Ideally keep both accessible at all times. A profile lets participants edit changing study data (such as weight or sleep habits), see upcoming activities, leave the study, and access the consent document and privacy policy. A dashboard can motivate continuation with daily progress, weekly assessments, activity-specific results, and, when appropriate, comparison with aggregated results from other participants.

**Platforms:** iOS, iPadOS. No additional considerations; not supported in macOS, tvOS, visionOS, or watchOS.

Resources: [Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/) · [Research & Care > Developers](https://www.researchandcare.org/developers/) · [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)

Source: [Apple Human Interface Guidelines — ResearchKit](https://developer.apple.com/design/Human-Interface-Guidelines/researchkit), captured 2026-09-12.
