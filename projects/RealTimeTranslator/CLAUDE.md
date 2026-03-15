# RealTimeTranslator

You are a coding agent working on RealTimeTranslator -- An AI-powered real-time language translation system for law enforcement to communicate with non-native speakers during investigations.

## Foundational Axiom

Existing approaches to ai-powered real-time language translation system fail because they optimize for the common case while ignoring structural constraints; RealTimeTranslator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: translation engine development
- User interface: requirements gathering and analysis
- Data layer: data management and storage

## Anti-Goals

- **General-purpose platform**: RealTimeTranslator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for RealTimeTranslator - Revised (P3) -- (depends on: Requirements Gathering and Analysis)
3. Translation Engine Development (P4) -- (depends on: System Architecture Design)
4. User Interface Design and Development (P4) -- (depends on: System Architecture Design)
5. Data Management and Storage (P4) -- (depends on: System Architecture Design)
6. Integration and Testing (P5) -- (depends on: Translation Engine Development, User Interface Design and Development, Data Management and Storage)
7. Security and Compliance (P4) -- (depends on: System Architecture Design)
8. Deployment and DevOps (P5) -- (depends on: Integration and Testing, Security and Compliance)
9. Documentation and Training (P5) -- (depends on: User Interface Design and Development, Integration and Testing)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeTranslator can deliver its core value proposition as described
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

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered real-time language translation system for law enforcement to communicate with non-nati.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
