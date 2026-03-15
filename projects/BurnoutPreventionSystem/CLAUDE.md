# BurnoutPreventionSystem

You are a coding agent working on BurnoutPreventionSystem -- An AI tool that monitors work patterns and provides early warnings and recommendations to prevent employee burnout.

## Foundational Axiom

Existing approaches to ai tool fail because they optimize for the common case while ignoring structural constraints; BurnoutPreventionSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data ingestion and processing
- User interface: build recommendation engine
- Data layer: implement data ingestion and processing

## Anti-Goals

- **General-purpose platform**: BurnoutPreventionSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design System Architecture for BurnoutPreventionSystem (P2) -- (depends on: Define Project Scope and Requirements)
2. Implement Data Ingestion and Processing (P4) -- (depends on: Design System Architecture)
3. Develop Monitoring and Alert System (P4) -- (depends on: Design System Architecture, Implement Data Ingestion and Processing)
4. Build Recommendation Engine (P4) -- (depends on: Design System Architecture, Develop Monitoring and Alert System)
5. Create User Interface (P4) -- (depends on: Design System Architecture)
6. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
7. Set up Database and Data Storage (P4) -- (depends on: Design System Architecture)
8. Conduct System Testing (P5) -- (depends on: Implement Data Ingestion and Processing, Develop Monitoring and Alert System, Build Recommendation Engine, Create User Interface, Implement Security and Access Controls, Set up Database and Data Storage)
9. Deploy and Monitor System (P5) -- (depends on: Conduct System Testing)
10. Write Documentation and User Guides (P4) -- (depends on: Design System Architecture)
11. Set up Development Environment (P3) -- (depends on: Design System Architecture)
12. DefineProjectScopeandRequirements (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BurnoutPreventionSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Redis

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI tool that monitors work patterns and provides early warnings and recommendations to prevent em.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
