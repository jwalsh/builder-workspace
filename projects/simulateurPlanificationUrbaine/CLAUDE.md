# simulateurPlanificationUrbaine

You are a coding agent working on simulateurPlanificationUrbaine -- Un simulateur qui optimise la planification urbaine pour des villes plus durables et intelligentes.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; simulateurPlanificationUrbaine makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for urban simulation logic
- User interface: define urban simulation requirements
- Data layer: implement database integration for urban simulation data

## Anti-Goals

- **General-purpose platform**: simulateurPlanificationUrbaine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Urban Simulation Requirements (P1)
2. Design Urban Simulation Architecture (P2) -- (depends on: Define Urban Simulation Requirements)
3. Implement Database Integration for Urban Simulation Data (P5) -- (depends on: Design Urban Simulation Architecture)
4. Develop Frontend for Urban Simulation Interface (P3) -- (depends on: Design Urban Simulation Architecture)
5. Develop Backend for Urban Simulation Logic (P4) -- (depends on: Design Urban Simulation Architecture)
6. Detailed Documentation for Urban Simulation Component (P5) -- (depends on: Develop Frontend for Urban Simulation Interface, Develop Backend for Urban Simulation Logic)
7. Review and Approve Urban Simulation Component Code (P3) -- (depends on: Develop Frontend for Urban Simulation Interface, Develop Backend for Urban Simulation Logic)
8. Test and Debug Urban Simulation Component (P2) -- (depends on: Develop Frontend for Urban Simulation Interface, Develop Backend for Urban Simulation Logic)
9. Review and Approve Urban Simulation Component Design (P1) -- (depends on: Design Urban Simulation Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: simulateurPlanificationUrbaine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un simulateur qui optimise la planification urbaine pour des villes plus durables et intelligentes..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
