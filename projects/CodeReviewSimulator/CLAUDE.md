# CodeReviewSimulator

You are a coding agent working on CodeReviewSimulator -- A platform that simulates real-world code review scenarios, teaching users how to give and receive constructive feedback on code.

## Foundational Axiom

The bottleneck in platform is not compute or data but the feedback loop between intent and artifact; CodeReviewSimulator compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend functionality
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: CodeReviewSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and requirements (P5)
2. Design system architecture (P4) -- (depends on: Define project scope and requirements)
3. Set up development environment (P4)
4. Implement security measures (P4) -- (depends on: Design system architecture)
5. Design user interface (P3) -- (depends on: Define project scope and requirements)
6. Set up testing framework (P3) -- (depends on: Set up development environment)
7. Write documentation (P3) -- (depends on: Define project scope and requirements)
8. Implement backend functionality (P2) -- (depends on: Design system architecture, Set up development environment)
9. Implement frontend functionality (P2) -- (depends on: Design user interface, Set up development environment)
10. Perform code reviews (P3) -- (depends on: Implement backend functionality, Implement frontend functionality)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeReviewSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that simulates real-world code review scenarios, teaching users how to give and receive c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
