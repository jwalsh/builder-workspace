# PolyglotProIa

You are a coding agent working on PolyglotProIa -- Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per fornire traduzioni personalizzate e migliorare la comunicazione globale per professionisti e imprese.

## Foundational Axiom

Existing approaches to un assistente di traduzione che utilizza l'intelligenza arti fail because they optimize for the common case while ignoring structural constraints; PolyglotProIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services (server-side logic)
- User interface: develop user interface (frontend)
- Data layer: set up database architecture

## Anti-Goals

- **General-purpose platform**: PolyglotProIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Objectives (P1)
2. Develop User Interface (Frontend) (P4) -- (depends on: Define Project Scope and Objectives)
3. Develop Backend Services (Server-side Logic) (P4) -- (depends on: Define Project Scope and Objectives)
4. Conduct Quality Assurance Tests (P5) -- (depends on: Develop User Interface (Frontend), Develop Backend Services (Server-side Logic))
5. Review and Update Documentation (P5) -- (depends on: Define Project Scope and Objectives)
6. Perform Security Audits (P5) -- (depends on: Develop User Interface (Frontend), Develop Backend Services (Server-side Logic))
7. Set Up Database Architecture (P4) -- (depends on: Define Project Scope and Objectives)
8. Implement DevOps Practices (P4) -- (depends on: Define Project Scope and Objectives)
9. Research and Analysis of Existing Solutions for PolyglotProIa (P2)
10. Design AI and Machine Learning Models for Personalized Translation (P3) -- (depends on: Research and Analysis of Existing Solutions)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PolyglotProIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
