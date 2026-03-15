# IdeaAnonymizer

You are a coding agent working on IdeaAnonymizer -- A system that allows employees to submit ideas anonymously, which are then vetted and presented to management without revealing the source.

## Foundational Axiom

The bottleneck in system is not compute or data but the feedback loop between intent and artifact; IdeaAnonymizer compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project requirements
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: IdeaAnonymizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Design Database Schema (P3) -- (depends on: Design System Architecture)
4. Implement Backend Services (P2) -- (depends on: Design System Architecture, Design Database Schema)
5. Implement Frontend User Interface (P2) -- (depends on: Design System Architecture)
6. Write User Documentation (P4) -- (depends on: Implement Backend Services, Implement Frontend User Interface)
7. Set up CI/CD Pipeline (P3) -- (depends on: Implement Backend Services, Implement Frontend User Interface)
8. Implement Security Measures (P2) -- (depends on: Design System Architecture)
9. Perform Quality Assurance Testing (P2) -- (depends on: Implement Backend Services, Implement Frontend User Interface, Implement Security Measures)
10. Deploy to Production (P1) -- (depends on: Set up CI/CD Pipeline, Perform Quality Assurance Testing, Write User Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: IdeaAnonymizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that allows employees to submit ideas anonymously, which are then vetted and presented to m.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
