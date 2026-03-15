# RealTimeLanguageTranslationService

You are a coding agent working on RealTimeLanguageTranslationService -- A distributed service for real-time language translation, capable of handling millions of concurrent translation requests with low latency.

## Foundational Axiom

Existing approaches to distributed service fail because they optimize for the common case while ignoring structural constraints; RealTimeLanguageTranslationService makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop api for client integration
- User interface: develop ui for user interaction
- Data layer: set up database and data modeling

## Anti-Goals

- **General-purpose platform**: RealTimeLanguageTranslationService solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Implement Real-Time Communication Layer (P3) -- (depends on: Define System Architecture)
3. Develop API for Client Integration (P4) -- (depends on: Implement Real-Time Communication Layer, Define System Architecture)
4. Develop UI for User Interaction (P5) -- (depends on: Develop API for Client Integration)
5. Create Comprehensive Technical Documentation for RealTimeLanguageTranslationService (P5) -- (depends on: Develop UI for User Interaction)
6. Perform Security Audit (P3) -- (depends on: Implement Real-Time Communication Layer, Develop API for Client Integration)
7. Develop Core Translation Engine (P2) -- (depends on: Define System Architecture)
8. Set Up Database and Data Modeling (P2) -- (depends on: Define System Architecture)
9. Implement Load Balancing and Auto-Scaling (P1) -- (depends on: Define System Architecture)
10. Review System Architecture Design (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeLanguageTranslationService can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A distributed service for real-time language translation, capable of handling millions of concurrent.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
