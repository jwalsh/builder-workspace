# InterdisciplinaryInsightGenerator

You are a coding agent working on InterdisciplinaryInsightGenerator -- An AI-powered system that generates novel insights and research questions by analyzing connections between diverse academic fields in a knowledge graph.

## Foundational Axiom

Existing approaches to ai-powered system fail because they optimize for the common case while ignoring structural constraints; InterdisciplinaryInsightGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-powered system that generates novel insights and research questions by analyzing connections b
- User interface: define project scope and requirements
- Data layer: develop data ingestion pipeline

## Anti-Goals

- **General-purpose platform**: InterdisciplinaryInsightGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design System Architecture for Interdisciplinary Insight Generator (P2) -- (depends on: Define Project Scope and Requirements)
3. Design User Interfaces - RFC (P3) -- (depends on: Design System Architecture, Define User Personas and Use Cases)
4. Build Knowledge Graph (P3) -- (depends on: Design System Architecture)
5. Develop AI Models (P4) -- (depends on: Build Knowledge Graph)
6. Implement User Interfaces (P4) -- (depends on: Design User Interfaces, Develop AI Models)
7. Develop Data Ingestion Pipeline (P3) -- (depends on: Design System Architecture)
8. Conduct Testing and Quality Assurance (P4) -- (depends on: Implement User Interfaces, Develop AI Models, Develop Data Ingestion Pipeline, Build Knowledge Graph)
9. Set up CI/CD Pipeline (P3)
10. Deploy and Monitor System (P5) -- (depends on: Conduct Testing and Quality Assurance, Set up CI/CD Pipeline)
11. Implement Security Measures (Revised) (P4) -- (depends on: Design System Architecture)
12. Prepare Documentation and User Guides (P4) -- (depends on: Design System Architecture, Design User Interfaces)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InterdisciplinaryInsightGenerator can deliver its core value proposition as described
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

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered system that generates novel insights and research questions by analyzing connections b.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
