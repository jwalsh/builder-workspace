# LinguaFusionPro

You are a coding agent working on LinguaFusionPro -- Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para proporcionar traducciones precisas y eficientes para las empresas y las organizaciones.

## Foundational Axiom

Existing approaches to un sistema de traducción que utiliza la inteligencia artific fail because they optimize for the common case while ignoring structural constraints; LinguaFusionPro makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development task decomposition
- User interface: requirements gathering for linguafusionpro
- Data layer: database schema design

## Anti-Goals

- **General-purpose platform**: LinguaFusionPro solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. System Deployment (P5) -- (depends on: System Deployment Planning)
2. Requirements Gathering for LinguaFusionPro (P1)
3. System Architecture Design (P2) -- (depends on: Requirements Gathering)
4. Backend Development Task Decomposition (P3) -- (depends on: System Architecture Design)
5. Backend Development Implementation (P4) -- (depends on: Backend Development Task Decomposition)
6. Frontend Development Task Decomposition (P3) -- (depends on: System Architecture Design)
7. Frontend Development Implementation (P4) -- (depends on: Frontend Development Task Decomposition)
8. Integration Testing (P4) -- (depends on: Backend Development Implementation, Frontend Development Implementation)
9. Database Schema Design (P2) -- (depends on: System Architecture Design)
10. Comprehensive Deployment Strategy for LinguaFusionPro Translation System - DRAFT FOR REVIEW (Updated) (P2) -- (depends on: Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LinguaFusionPro can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
