# UrbanDevelopmentSimulator

You are a coding agent working on UrbanDevelopmentSimulator -- A comprehensive simulation platform for modeling and analyzing urban development scenarios.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; UrbanDevelopmentSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement the simulation backend
- User interface: define project requirements and goals
- Data layer: integrate database systems

## Anti-Goals

- **General-purpose platform**: UrbanDevelopmentSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project requirements and goals (P1)
2. Develop simulation algorithms (P2) -- (depends on: Define project requirements and goals)
3. Implement the simulation backend (P2) -- (depends on: Develop simulation algorithms)
4. Design the user interface (P3) -- (depends on: Define project requirements and goals)
5. Perform unit tests and code reviews (P5) -- (depends on: Implement the simulation backend, Design the user interface)
6. Create Technical Documentation for Urban Development Simulator (P5) -- (depends on: Implement the simulation backend, Design the user interface)
7. Establish DevOps workflows and infrastructure (P4) -- (depends on: Implement the simulation backend)
8. Integrate database systems (P3) -- (depends on: Implement the simulation backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: UrbanDevelopmentSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive simulation platform for modeling and analyzing urban development scenarios..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
