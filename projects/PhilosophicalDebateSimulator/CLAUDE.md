# PhilosophicalDebateSimulator

You are a coding agent working on PhilosophicalDebateSimulator -- An AI-powered platform that simulates debates between historical philosophers on contemporary issues, using natural language processing and vast philosophical knowledge bases.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; PhilosophicalDebateSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop natural language processing components
- User interface: define project scope and requirements (revised)

## Anti-Goals

- **General-purpose platform**: PhilosophicalDebateSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Natural Language Processing Components (P3) -- (depends on: Design System Architecture)
4. Build Philosophical Knowledge Bases (P3) -- (depends on: Define Project Scope and Requirements)
5. Develop Debate Simulation Engine (P3) -- (depends on: Design System Architecture, Develop Natural Language Processing Components, Build Philosophical Knowledge Bases)
6. Implement Security and Access Controls (P3) -- (depends on: Design System Architecture)
7. Develop Testing Strategy and Test Cases (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
8. Design and Implement User Interface (P2) -- (depends on: Design System Architecture)
9. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
10. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PhilosophicalDebateSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered platform that simulates debates between historical philosophers on contemporary issues.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
