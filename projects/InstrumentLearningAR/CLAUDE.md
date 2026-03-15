# InstrumentLearningAR

You are a coding agent working on InstrumentLearningAR -- An augmented reality system for learning musical instruments through interactive, real-time guidance.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; InstrumentLearningAR closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An augmented reality system for learning musical instruments through interactive, real-time guidance
- User interface: requirements gathering and analysis
- Data layer: database design and development

## Anti-Goals

- **General-purpose platform**: InstrumentLearningAR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation and Planning (P1)
2. Requirements Gathering and Analysis (P2) -- (depends on: Project Initiation and Planning)
3. User Interface Design (P3) -- (depends on: Requirements Gathering and Analysis)
4. Augmented Reality Modeling and Implementation (P4) -- (depends on: Requirements Gathering and Analysis, User Interface Design)
5. Database Design and Development (P4) -- (depends on: Requirements Gathering and Analysis)
6. Testing and Quality Assurance (P5) -- (depends on: Augmented Reality Modeling and Implementation, Database Design and Development)
7. Deployment and Release Management (P5) -- (depends on: Testing and Quality Assurance)
8. Documentation and Knowledge Base Creation (P3) -- (depends on: Project Initiation and Planning)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InstrumentLearningAR can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An augmented reality system for learning musical instruments through interactive, real-time guidance.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
