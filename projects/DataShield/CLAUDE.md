# DataShield

You are a coding agent working on DataShield -- Protect sensitive data in object storage and display it as clear text based on permissions from a data warehouse.

## Foundational Axiom

Existing approaches to protect sensitive data in object storage and display it as c fail because they optimize for the common case while ignoring structural constraints; DataShield makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Protect sensitive data in object storage and display it as clear text based on permissions from a da
- User interface: define project scope and requirements (revised)
- Data layer: design system architecture for datashield project

## Anti-Goals

- **General-purpose platform**: DataShield solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design System Architecture for DataShield Project (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Data Encryption and Decryption (P3) -- (depends on: Design System Architecture)
4. Implement Access Control and User Management (P3) -- (depends on: Design System Architecture)
5. Conduct Security Audits (P5) -- (depends on: Implement Data Encryption and Decryption, Implement Access Control and User Management)
6. Integrate with Object Storage (P4) -- (depends on: Design System Architecture)
7. Develop User Interface (P4) -- (depends on: Design System Architecture)
8. Write Documentation (P4) -- (depends on: Design System Architecture)
9. Perform Quality Assurance Testing (P4) -- (depends on: Implement Data Encryption and Decryption, Implement Access Control and User Management, Integrate with Object Storage, Develop User Interface)
10. Set up Testing and Deployment Infrastructure (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DataShield can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Protect sensitive data in object storage and display it as clear text based on permissions from a da.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
