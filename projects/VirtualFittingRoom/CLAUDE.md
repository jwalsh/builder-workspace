# VirtualFittingRoom

You are a coding agent working on VirtualFittingRoom -- A virtual fitting room using advanced 3D modeling and AR to allow customers to try on clothes virtually, with accurate sizing and style recommendations.

## Foundational Axiom

Existing approaches to virtual fitting room using advanced 3d modeling and ar fail because they optimize for the common case while ignoring structural constraints; VirtualFittingRoom makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: sizing and recommendation engine
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: VirtualFittingRoom solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for VirtualFittingRoom (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Privacy Considerations (P4) -- (depends on: System Architecture Design)
4. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
5. User Interface and Experience Design (P3) -- (depends on: System Architecture Design)
6. 3D Modeling and AR Integration (P2) -- (depends on: System Architecture Design)
7. Sizing and Recommendation Engine (P2) -- (depends on: System Architecture Design, Database Design and Implementation)
8. Testing and Quality Assurance (P3) -- (depends on: 3D Modeling and AR Integration, Sizing and Recommendation Engine, User Interface and Experience Design)
9. Deployment and DevOps (P3) -- (depends on: Testing and Quality Assurance)
10. Documentation and User Support (P3) -- (depends on: User Interface and Experience Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualFittingRoom can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A virtual fitting room using advanced 3D modeling and AR to allow customers to try on clothes virtua.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
