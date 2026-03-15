# RetailAnalytics

You are a coding agent working on RetailAnalytics -- A comprehensive analytics platform for retail businesses, providing insights on customer behavior, sales trends, and inventory optimization.

## Foundational Axiom

Existing approaches to comprehensive analytics platform fail because they optimize for the common case while ignoring structural constraints; RetailAnalytics makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for analytics platform
- User interface: define project scope and requirements
- Data layer: develop database scheme

## Anti-Goals

- **General-purpose platform**: RetailAnalytics solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Implement DevOps Strategy (P5) -- (depends on: Define Project Scope and Requirements)
3. Design User Interface (P3) -- (depends on: Define Project Scope and Requirements)
4. Perform Quality Assurance Tests (P5) -- (depends on: Implement Backend for Analytics Platform, Design User Interface)
5. Develop Database Scheme (P4) -- (depends on: Define Project Scope and Requirements)
6. Develop Backend for Analytics Platform (P3) -- (depends on: Define Project Scope and Requirements)
7. Design Customer Behavior Module (P2) -- (depends on: Define Project Scope and Requirements)
8. Design Sales Trends Module (P2) -- (depends on: Define Project Scope and Requirements)
9. Design Inventory Optimization Module (P2) -- (depends on: Define Project Scope and Requirements)
10. Review and Approve Code (P2) -- (depends on: Implement Backend for Analytics Platform)
11. Review and Approve Design Documents (P1) -- (depends on: Design Customer Behavior Module, Design Sales Trends Module, Design Inventory Optimization Module, Design User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RetailAnalytics can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive analytics platform for retail businesses, providing insights on customer behavior, s.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to marketing professionals and campaign managers.
