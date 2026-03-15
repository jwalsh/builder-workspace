# simulateurFormationXR

You are a coding agent working on simulateurFormationXR -- Des simulations immersives en XR pour la formation dans des secteurs critiques tels que l'aviation et la médecine.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; simulateurFormationXR closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for xr simulations
- User interface: define project scope and requirements (revised)
- Data layer: integrate database for data storage and retrieval

## Anti-Goals

- **General-purpose platform**: simulateurFormationXR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design XR Simulation Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface for XR Simulations (P3) -- (depends on: Design XR Simulation Architecture)
4. Develop Backend Services for XR Simulations (P3) -- (depends on: Design XR Simulation Architecture)
5. Integrate Database for Data Storage and Retrieval (P4) -- (depends on: Design XR Simulation Architecture)
6. Perform Quality Assurance Testing on XR Simulation Project (P5) -- (depends on: Develop Frontend Interface for XR Simulations, Develop Backend Services for XR Simulations, Integrate Database for Data Storage and Retrieval)
7. Implement DevOps for Continuous Integration and Deployment (P4) -- (depends on: Develop Frontend Interface for XR Simulations, Develop Backend Services for XR Simulations, Integrate Database for Data Storage and Retrieval)
8. Review Frontend Interface Design and Implementation (P3) -- (depends on: Develop Frontend Interface for XR Simulations)
9. Review Backend Services Implementation (P3) -- (depends on: Develop Backend Services for XR Simulations)
10. Review Project Architecture and Design Decisions (P2) -- (depends on: Design XR Simulation Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: simulateurFormationXR can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des simulations immersives en XR pour la formation dans des secteurs critiques tels que l'aviation e.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
