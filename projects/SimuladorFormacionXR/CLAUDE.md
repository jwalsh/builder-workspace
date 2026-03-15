# SimuladorFormacionXR

You are a coding agent working on SimuladorFormacionXR -- Simulaciones inmersivas en XR para formación en sectores críticos como aviación y medicina.

## Foundational Axiom

Existing approaches to simulaciones inmersivas en xr para formación en sectores crí fail because they optimize for the common case while ignoring structural constraints; SimuladorFormacionXR makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend components for xr simulations
- User interface: define xr simulation requirements for aviation sector
- Data layer: develop database schema for xr simulations

## Anti-Goals

- **General-purpose platform**: SimuladorFormacionXR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define XR Simulation Requirements for Aviation Sector (P3)
2. Define XR Simulation Requirements for Medical Sector (P3)
3. Design XR Simulation Architecture (P1) -- (depends on: Define XR Simulation Requirements for Aviation Sector, Define XR Simulation Requirements for Medical Sector)
4. Develop Frontend Components for XR Simulations (P2) -- (depends on: Design XR Simulation Architecture)
5. Develop Backend Components for XR Simulations (P2) -- (depends on: Design XR Simulation Architecture)
6. Perform Quality Assurance Testing on XR Simulations (P5) -- (depends on: Develop Frontend Components for XR Simulations, Develop Backend Components for XR Simulations)
7. Develop Database Schema for XR Simulations (P4) -- (depends on: Design XR Simulation Architecture)
8. Implement DevOps Pipeline for XR Simulations (P2) -- (depends on: Develop Frontend Components for XR Simulations, Develop Backend Components for XR Simulations)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SimuladorFormacionXR can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Simulaciones inmersivas en XR para formación en sectores críticos como aviación y medicina..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
