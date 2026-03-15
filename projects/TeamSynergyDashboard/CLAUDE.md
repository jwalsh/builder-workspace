# TeamSynergyDashboard

You are a coding agent working on TeamSynergyDashboard -- A collaborative dashboard that visualizes team productivity, communication patterns, and project progress to identify areas for improvement.

## Foundational Axiom

Existing approaches to collaborative dashboard fail because they optimize for the common case while ignoring structural constraints; TeamSynergyDashboard makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: design frontend ui/ux - revised
- Data layer: design database schema for teamsynergydashboard

## Anti-Goals

- **General-purpose platform**: TeamSynergyDashboard solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design system architecture (P3) -- (depends on: Define project scope and requirements)
2. Design database schema for TeamSynergyDashboard (P4) -- (depends on: Design system architecture)
3. Implement backend services (P5) -- (depends on: Design system architecture, Design database schema)
4. Design frontend UI/UX - REVISED (P4) -- (depends on: Design system architecture, Define user personas and use cases, Conduct user research and testing)
5. Implement frontend components (P5) -- (depends on: Design frontend UI/UX)
6. Implement Security Measures (Revised) (P5) -- (depends on: Design system architecture)
7. Conduct testing and quality assurance (P5) -- (depends on: Implement backend services, Implement frontend components)
8. Set up CI/CD pipeline (P4)
9. Write documentation (P3) -- (depends on: Define project scope and requirements, Design system architecture)
10. Define Project Scope and Requirements (P2)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeamSynergyDashboard can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A collaborative dashboard that visualizes team productivity, communication patterns, and project pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
