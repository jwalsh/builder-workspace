# EmotionRegulationWearable

You are a coding agent working on EmotionRegulationWearable -- A wearable device that detects emotional states and provides gentle neurostimulation to help regulate mood.

## Foundational Axiom

Existing approaches to wearable device fail because they optimize for the common case while ignoring structural constraints; EmotionRegulationWearable makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integration of hardware and software components
- User interface: requirements gathering for emotion regulation wearable

## Anti-Goals

- **General-purpose platform**: EmotionRegulationWearable solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for Emotion Regulation Wearable (P1)
2. Design the Emotion Detection System (P2) -- (depends on: Requirements Gathering)
3. Design the Neurostimulation System (P2) -- (depends on: Requirements Gathering)
4. Develop the Wearable Hardware Prototype (P3) -- (depends on: Design the Emotion Detection System, Design the Neurostimulation System)
5. Integration of Hardware and Software Components (P3) -- (depends on: Design the Emotion Detection System, Design the Neurostimulation System, Develop the Wearable Hardware Prototype)
6. Documentation and User Manual (P5) -- (depends on: Integration of Hardware and Software Components)
7. Thorough Testing of the Wearable Device (P4) -- (depends on: Integration of Hardware and Software Components)
8. Device Certification and Regulatory Compliance (P4) -- (depends on: Testing of the Wearable Device)
9. Deployment of the EmotionRegulationWearable (P5) -- (depends on: Device Certification and Regulatory Compliance)
10. Design the User Interface (P2) -- (depends on: Requirements Gathering)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmotionRegulationWearable can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable device that detects emotional states and provides gentle neurostimulation to help regulat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to iot engineers and embedded systems developers.
