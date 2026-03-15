# SecureDataLineage

You are a coding agent working on SecureDataLineage -- A system that tracks the lineage of sensitive data across an organization's systems, ensuring compliance and security.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; SecureDataLineage makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that tracks the lineage of sensitive data across an organization's systems, ensuring compli
- User interface: define project scope and requirements
- Data layer: implement data ingestion and tracking

## Anti-Goals

- **General-purpose platform**: SecureDataLineage solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Data Ingestion and Tracking (P3) -- (depends on: Design System Architecture)
4. Build Compliance and Security Monitoring (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage and Querying (P3) -- (depends on: Design System Architecture)
6. Conduct Security Audits and Penetration Testing (P4) -- (depends on: Implement Data Ingestion and Tracking, Build Compliance and Security Monitoring, Implement Data Storage and Querying)
7. Develop User Interface (P2) -- (depends on: Design System Architecture)
8. Conduct User Acceptance Testing (P3) -- (depends on: Implement Data Ingestion and Tracking, Build Compliance and Security Monitoring, Develop User Interface, Implement Data Storage and Querying)
9. Set up Continuous Integration and Deployment (P2)
10. Write Documentation and User Guides (P2) -- (depends on: Develop User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SecureDataLineage can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that tracks the lineage of sensitive data across an organization's systems, ensuring compli.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
