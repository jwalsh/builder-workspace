# AITutoringCompanion

You are a coding agent working on AITutoringCompanion -- An AI-powered tutoring system that provides personalized support for employees engaged in skill-building programs.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; AITutoringCompanion closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-powered tutoring system that provides personalized support for employees engaged in skill-buil
- User interface: define project scope and requirements: ai tutoring companion
- Data layer: implement data storage and integration

## Anti-Goals

- **General-purpose platform**: AITutoringCompanion solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: AI Tutoring Companion (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Create User Documentation and Training Materials (P5) -- (depends on: Design System Architecture)
4. Implement Data Storage and Integration (P4) -- (depends on: Design System Architecture)
5. Develop Testing and Quality Assurance Plan (P4) -- (depends on: Design System Architecture)
6. Implement Security and Compliance Measures (P4) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P4) -- (depends on: Design System Architecture)
8. Implement AI Tutoring Model (P3) -- (depends on: Design System Architecture)
9. Design and Develop User Interface (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AITutoringCompanion can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered tutoring system that provides personalized support for employees engaged in skill-buil.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
