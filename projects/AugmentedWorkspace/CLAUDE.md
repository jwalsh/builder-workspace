# AugmentedWorkspace

You are a coding agent working on AugmentedWorkspace -- An augmented reality system that transforms any space into a customized, immersive workspace.

## Foundational Axiom

Existing approaches to augmented reality system fail because they optimize for the common case while ignoring structural constraints; AugmentedWorkspace makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop augmented reality engine
- User interface: define project scope and requirements - revised
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: AugmentedWorkspace solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Security and Privacy Measures (P4) -- (depends on: Design System Architecture)
4. Develop Augmented Reality Engine (P3) -- (depends on: Design System Architecture)
5. Create Workspace Customization Interface (P3) -- (depends on: Design System Architecture)
6. Implement User Interaction and Controls (P3) -- (depends on: Design System Architecture)
7. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
8. Create Testing and Quality Assurance Plan (P3) -- (depends on: Design System Architecture)
9. Plan Deployment and DevOps Strategy (P3) -- (depends on: Design System Architecture)
10. Create User Documentation and Training Materials (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AugmentedWorkspace can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An augmented reality system that transforms any space into a customized, immersive workspace..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
