# UserBehaviorAnalytics

You are a coding agent working on UserBehaviorAnalytics -- A platform that analyzes user behavior to detect insider threats and compromised accounts.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; UserBehaviorAnalytics makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data ingestion and processing
- User interface: requirements gathering and analysis
- Data layer: data storage and management

## Anti-Goals

- **General-purpose platform**: UserBehaviorAnalytics solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for UserBehaviorAnalytics (Revised and Approved) (P3) -- (depends on: Requirements Gathering and Analysis)
3. Data Storage and Management (P4) -- (depends on: System Architecture Design)
4. Security and Compliance (P5) -- (depends on: System Architecture Design, Data Storage and Management, User Authentication and Authorization)
5. Data Ingestion and Processing (P4) -- (depends on: System Architecture Design)
6. User Behavior Analysis (P4) -- (depends on: Data Ingestion and Processing, Data Storage and Management)
7. Reporting and Alerting (P4) -- (depends on: User Behavior Analysis)
8. Testing and Quality Assurance (P4) -- (depends on: Data Ingestion and Processing, Data Storage and Management, User Behavior Analysis, Reporting and Alerting)
9. Deployment and DevOps (P4) -- (depends on: Testing and Quality Assurance)
10. Documentation and Training (P4) -- (depends on: Reporting and Alerting)
11. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: UserBehaviorAnalytics can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform that analyzes user behavior to detect insider threats and compromised accounts..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to marketing professionals and campaign managers.
