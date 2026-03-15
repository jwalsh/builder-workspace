# simulateurEnvironnemental

You are a coding agent working on simulateurEnvironnemental -- Un simulateur qui prédit l'impact environnemental des activités humaines.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; simulateurEnvironnemental makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements - revised
- Data layer: develop database schema

## Anti-Goals

- **General-purpose platform**: simulateurEnvironnemental solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - Revised (P1)
2. Design Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Frontend Interface (P3) -- (depends on: Design Architecture)
4. Develop Backend Services (P3) -- (depends on: Design Architecture)
5. Perform Quality Assurance Testing (P5) -- (depends on: Develop Frontend Interface, Develop Backend Services)
6. Document Technical Aspects (P5) -- (depends on: Develop Frontend Interface, Develop Backend Services)
7. Develop Database Schema (P4) -- (depends on: Design Architecture)
8. Implement DevOps Pipeline (P4) -- (depends on: Develop Frontend Interface, Develop Backend Services)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: simulateurEnvironnemental can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un simulateur qui prédit l'impact environnemental des activités humaines..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
