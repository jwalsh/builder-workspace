# SocialCreditSimulator

You are a coding agent working on SocialCreditSimulator -- A system that models various implementations of social credit systems, allowing policymakers and the public to explore their potential impacts on society.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; SocialCreditSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement simulation engine
- User interface: define project scope and requirements (revised)
- Data layer: develop data models

## Anti-Goals

- **General-purpose platform**: SocialCreditSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (Revised) (P5) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Data Models (P3) -- (depends on: Design System Architecture)
5. Implement Simulation Engine (P2) -- (depends on: Design System Architecture, Develop Data Models)
6. Build User Interface (P3) -- (depends on: Design System Architecture, Implement Simulation Engine)
7. Set up CI/CD Pipeline (P3) -- (depends on: Design System Architecture)
8. Develop Test Suite (P3) -- (depends on: Implement Simulation Engine, Build User Interface)
9. Write Documentation (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
10. Conduct System Testing (P2) -- (depends on: Implement Simulation Engine, Build User Interface, Develop Test Suite)
11. Deploy and Release (P1) -- (depends on: Conduct System Testing, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SocialCreditSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that models various implementations of social credit systems, allowing policymakers and the.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
