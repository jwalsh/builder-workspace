# EVChargeOps

You are a coding agent working on EVChargeOps -- Build a highly-scalable, low-latency EV charge point operator system using IoT and serverless technologies.

## Foundational Axiom

Existing approaches to build a highly-scalable, low-latency ev charge point operato fail because they optimize for the common case while ignoring structural constraints; EVChargeOps makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements - revised
- Data layer: implement data storage and analytics

## Anti-Goals

- **General-purpose platform**: EVChargeOps solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Backend Services (P3) -- (depends on: Design System Architecture)
4. Develop Frontend Applications (P3) -- (depends on: Design System Architecture)
5. Set up IoT Infrastructure (P3) -- (depends on: Design System Architecture)
6. Implement Data Storage and Analytics (P3) -- (depends on: Design System Architecture)
7. Develop Security and Compliance Measures (P2) -- (depends on: Design System Architecture)
8. Create Testing and Deployment Pipelines (P2) -- (depends on: Implement Backend Services, Develop Frontend Applications, Set up IoT Infrastructure, Implement Data Storage and Analytics)
9. Conduct System Testing and Quality Assurance (P2) -- (depends on: Create Testing and Deployment Pipelines)
10. Prepare Documentation and User Guides (P2) -- (depends on: Implement Backend Services, Develop Frontend Applications, Set up IoT Infrastructure, Implement Data Storage and Analytics)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EVChargeOps can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Build a highly-scalable, low-latency EV charge point operator system using IoT and serverless techno.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
