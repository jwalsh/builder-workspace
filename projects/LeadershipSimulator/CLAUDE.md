# LeadershipSimulator

You are a coding agent working on LeadershipSimulator -- A VR-based leadership training platform that simulates various management scenarios for skill development.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; LeadershipSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A VR-based leadership training platform that simulates various management scenarios for skill develo
- User interface: gather requirements - revised
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: LeadershipSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Gather Requirements)
3. Design Database Schema (P4) -- (depends on: Design System Architecture)
4. Develop VR Environment (P3) -- (depends on: Design System Architecture)
5. Implement Scenario Logic (P3) -- (depends on: Design System Architecture)
6. Implement User Management (P3) -- (depends on: Design Database Schema)
7. Design User Interface (P3) -- (depends on: Gather Requirements)
8. Set up CI/CD Pipeline (P3)
9. Conduct Security Audits (P3) -- (depends on: Implement User Management)
10. Implement User Interface (P2) -- (depends on: Design User Interface)
11. Write User Documentation (P2) -- (depends on: Implement User Interface)
12. Perform Testing (P2) -- (depends on: Develop VR Environment, Implement Scenario Logic, Implement User Management, Implement User Interface)
13. Deploy to Production (P1) -- (depends on: Perform Testing, Conduct Security Audits, Write User Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LeadershipSimulator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A VR-based leadership training platform that simulates various management scenarios for skill develo.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
