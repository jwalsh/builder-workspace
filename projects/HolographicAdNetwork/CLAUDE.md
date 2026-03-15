# HolographicAdNetwork

You are a coding agent working on HolographicAdNetwork -- A network for serving and interacting with holographic advertisements in public spaces, with real-time analytics and user engagement tracking.

## Foundational Axiom

Existing approaches to network fail because they optimize for the common case while ignoring structural constraints; HolographicAdNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A network for serving and interacting with holographic advertisements in public spaces, with real-ti
- User interface: define project scope and requirements
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: HolographicAdNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Ad Serving and Rendering Components (P3) -- (depends on: Design System Architecture)
4. Implement User Interaction Tracking (P3) -- (depends on: Design System Architecture)
5. Build Analytics and Reporting System (P3) -- (depends on: Design System Architecture, Implement User Interaction Tracking)
6. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
7. Develop Security and Privacy Measures (P2) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
9. Conduct System Testing and Quality Assurance (P2) -- (depends on: Develop Ad Serving and Rendering Components, Implement User Interaction Tracking, Build Analytics and Reporting System, Set up Data Storage and Management)
10. Create User Documentation and Training Materials (P1) -- (depends on: Conduct System Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HolographicAdNetwork can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A network for serving and interacting with holographic advertisements in public spaces, with real-ti.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
