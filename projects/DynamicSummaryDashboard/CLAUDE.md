# DynamicSummaryDashboard

You are a coding agent working on DynamicSummaryDashboard -- A dashboard that provides real-time, auto-updating summaries of key projects, metrics, and initiatives across the organization.

## Foundational Axiom

Existing approaches to dashboard fail because they optimize for the common case while ignoring structural constraints; DynamicSummaryDashboard makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend logic
- User interface: gather requirements
- Data layer: implement data ingestion

## Anti-Goals

- **General-purpose platform**: DynamicSummaryDashboard solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture for DynamicSummaryDashboard (Revised) (P5) -- (depends on: Gather Requirements)
3. Implement Data Ingestion (P3) -- (depends on: Design System Architecture)
4. Set up Data Storage (P3) -- (depends on: Design System Architecture)
5. Set up Continuous Integration/Deployment (P3)
6. Implement Backend Logic (P2) -- (depends on: Design System Architecture, Implement Data Ingestion, Set up Data Storage)
7. Develop Dashboard Frontend (P2) -- (depends on: Design System Architecture)
8. Conduct Security Audit (P3) -- (depends on: Implement Backend Logic, Develop Dashboard Frontend)
9. Write Documentation (P2) -- (depends on: Design System Architecture)
10. Test and Quality Assurance (P2) -- (depends on: Implement Backend Logic, Develop Dashboard Frontend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DynamicSummaryDashboard can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A dashboard that provides real-time, auto-updating summaries of key projects, metrics, and initiativ.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
