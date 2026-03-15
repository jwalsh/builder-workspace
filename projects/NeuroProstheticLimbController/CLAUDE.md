# NeuroProstheticLimbController

You are a coding agent working on NeuroProstheticLimbController -- An advanced BCI system for controlling prosthetic limbs with natural, thought-driven movements.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroProstheticLimbController models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend processing logic
- User interface: develop frontend for bci interface

## Anti-Goals

- **General-purpose platform**: NeuroProstheticLimbController solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design BCI System Architecture (P2) -- (depends on: Define Project Requirements)
2. Develop Frontend for BCI Interface (P3) -- (depends on: Design BCI System Architecture)
3. Implement Backend Processing Logic (P3) -- (depends on: Design BCI System Architecture)
4. Integrate Hardware Components (P4) -- (depends on: Design BCI System Architecture)
5. Test and Validate BCI System (P4) -- (depends on: Develop Frontend for BCI Interface, Implement Backend Processing Logic, Integrate Hardware Components)
6. Document System Design and Implementation (P5) -- (depends on: Design BCI System Architecture, Develop Frontend for BCI Interface, Implement Backend Processing Logic, Integrate Hardware Components, Test and Validate BCI System)
7. Define Comprehensive Project Requirements for NeuroProstheticLimbController - Revised (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroProstheticLimbController can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced BCI system for controlling prosthetic limbs with natural, thought-driven movements..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
