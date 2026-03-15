# SynestheticSensoryEnhancer

You are a coding agent working on SynestheticSensoryEnhancer -- A neural implant that allows users to experience synesthesia or enhance existing senses beyond normal human capabilities.

## Foundational Axiom

Existing approaches to neural implant fail because they optimize for the common case while ignoring structural constraints; SynestheticSensoryEnhancer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the software for the neural implant
- User interface: define project requirements and specifications

## Anti-Goals

- **General-purpose platform**: SynestheticSensoryEnhancer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project requirements and specifications (P1)
2. Design the neural interface (P2) -- (depends on: Define project requirements and specifications)
3. Develop the mobile application for user control (P5) -- (depends on: Design the neural interface)
4. Develop the software for the neural implant (P4) -- (depends on: Design the neural interface)
5. Develop the neural implant hardware (P3) -- (depends on: Define project requirements and specifications)
6. Document the SynestheticSensoryEnhancer (P3) -- (depends on: Develop the software for the neural implant, Develop the mobile application for user control)
7. Secure the SynestheticSensoryEnhancer (P2) -- (depends on: Develop the software for the neural implant)
8. Test and validate the SynestheticSensoryEnhancer (P1) -- (depends on: Develop the software for the neural implant, Develop the mobile application for user control)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SynestheticSensoryEnhancer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A neural implant that allows users to experience synesthesia or enhance existing senses beyond norma.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to iot engineers and embedded systems developers.
