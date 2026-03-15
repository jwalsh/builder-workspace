# EmotionalAIForCustomerService

You are a coding agent working on EmotionalAIForCustomerService -- An AI platform that detects emotional states and tailors customer service responses.

## Foundational Axiom

Existing approaches to ai platform fail because they optimize for the common case while ignoring structural constraints; EmotionalAIForCustomerService makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: requirements gathering and analysis for emotionalaiforcustomerservice
- User interface: requirements gathering and analysis for emotionalaiforcustomerservice

## Anti-Goals

- **General-purpose platform**: EmotionalAIForCustomerService solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis for EmotionalAIForCustomerService (P1)
2. Design AI Model Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
3. Develop AI Model for Emotion Detection (P3) -- (depends on: Design AI Model Architecture)
4. Develop Tailored Customer Service Responses for EmotionalAIForCustomerService Project (P4) -- (depends on: AI Model for Emotion Detection)
5. Integrate AI into Customer Service Platform (P5) -- (depends on: Develop AI Model for Emotion Detection, Develop Tailored Customer Service Responses)
6. Perform Unit and Integration Testing (P1) -- (depends on: Develop AI Model for Emotion Detection, Develop Tailored Customer Service Responses, Integrate AI into Customer Service Platform)
7. Deploy the EmotionalAIForCustomerService to Production (P5) -- (depends on: Perform Unit and Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmotionalAIForCustomerService can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI platform that detects emotional states and tailors customer service responses..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to marketing professionals and campaign managers.
