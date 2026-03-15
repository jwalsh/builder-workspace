# EmotionRegulator

You are a coding agent working on EmotionRegulator -- A wearable device that helps balance emotions by subtly influencing brain chemistry, useful for managing stress and mood disorders.

## Foundational Axiom

Existing approaches to wearable device fail because they optimize for the common case while ignoring structural constraints; EmotionRegulator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend logic for data processing
- User interface: define emotionregulator requirements and functionalities
- Data layer: implement backend logic for data processing

## Anti-Goals

- **General-purpose platform**: EmotionRegulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define EmotionRegulator Requirements and Functionalities (P1)
2. Design EmotionRegulator Hardware Architecture (P2) -- (depends on: Define EmotionRegulator Requirements and Functionalities)
3. Test EmotionRegulator Hardware Components (P4) -- (depends on: Design EmotionRegulator Hardware Architecture)
4. Develop User Interface (Frontend) (P3) -- (depends on: Design EmotionRegulator Hardware Architecture)
5. Implement Backend Logic for Data Processing (P3) -- (depends on: Design EmotionRegulator Hardware Architecture)
6. Test Software Components (Frontend and Backend) (P4) -- (depends on: Develop User Interface (Frontend), Implement Backend Logic for Data Processing)
7. Refine and Optimize EmotionRegulator Design (P5) -- (depends on: Test EmotionRegulator Hardware Components, Test Software Components (Frontend and Backend))
8. Document EmotionRegulator Development Process (P5) -- (depends on: Refine and Optimize EmotionRegulator Design)
9. Establish Database Schema and Integration (P3) -- (depends on: Develop User Interface (Frontend), Implement Backend Logic for Data Processing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmotionRegulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable device that helps balance emotions by subtly influencing brain chemistry, useful for mana.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
