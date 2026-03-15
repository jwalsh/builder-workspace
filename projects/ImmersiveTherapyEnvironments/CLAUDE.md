# ImmersiveTherapyEnvironments

You are a coding agent working on ImmersiveTherapyEnvironments -- Customizable immersive environments for various therapeutic applications, including phobia treatment and stress reduction.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; ImmersiveTherapyEnvironments embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for environment management
- User interface: implement customization interface

## Anti-Goals

- **General-purpose platform**: ImmersiveTherapyEnvironments solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Immersive Therapy Environments (P2) -- (depends on: Define Project Requirements)
2. Implement Customization Interface (P3) -- (depends on: Design Immersive Therapy Environments)
3. Develop Backend for Environment Management (P4) -- (depends on: Define Project Requirements)
4. Integrate Environment Management with Frontend (P5) -- (depends on: Implement Customization Interface, Develop Backend for Environment Management)
5. Write Documentation for Immersive Therapy Environments (P4) -- (depends on: Implement Customization Interface)
6. Test Immersive Therapy Environments (P2) -- (depends on: Implement Customization Interface)
7. Refine and Iterate Based on Test Feedback (P3) -- (depends on: Test Immersive Therapy Environments)
8. Define Comprehensive Project Requirements for ImmersiveTherapyEnvironments (Revised) (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ImmersiveTherapyEnvironments can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Customizable immersive environments for various therapeutic applications, including phobia treatment.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
