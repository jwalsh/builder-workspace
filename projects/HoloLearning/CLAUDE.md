# HoloLearning

You are a coding agent working on HoloLearning -- A holographic learning platform that creates immersive educational experiences across various subjects.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; HoloLearning closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate hardware and software components for hololens
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: HoloLearning solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Develop Core Learning Content Management System (P3) -- (depends on: Define Project Scope and Requirements)
3. Integrate Hardware and Software Components for HoloLens (P5) -- (depends on: Develop Core Learning Content Management System)
4. Design Holographic Interface and User Experience (P2) -- (depends on: Define Project Scope and Requirements)
5. Implement Interactive Learning Experiences (P4) -- (depends on: Design Holographic Interface and User Experience, Develop Core Learning Content Management System)
6. Prepare Documentation and User Guides (RFC#7694) (P3) -- (depends on: Implement Interactive Learning Experiences, Integrate Hardware and Software Components for HoloLens)
7. Conduct Security Audit and Risk Assessment (P2) -- (depends on: Develop Core Learning Content Management System)
8. Perform Functional and Accessibility Testing (P1) -- (depends on: Implement Interactive Learning Experiences, Integrate Hardware and Software Components for HoloLens)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HoloLearning can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A holographic learning platform that creates immersive educational experiences across various subjec.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
