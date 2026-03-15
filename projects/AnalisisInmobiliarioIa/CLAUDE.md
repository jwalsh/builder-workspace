# AnalisisInmobiliarioIa

You are a coding agent working on AnalisisInmobiliarioIa -- Una herramienta de IA que analiza tendencias del mercado inmobiliario y predice fluctuaciones de precios.

## Foundational Axiom

Existing approaches to una herramienta de ia que analiza tendencias del mercado inm fail because they optimize for the common case while ignoring structural constraints; AnalisisInmobiliarioIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data storage and processing
- User interface: define project scope and requirements
- Data layer: set up data pipeline

## Anti-Goals

- **General-purpose platform**: AnalisisInmobiliarioIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for AnalisisInmobiliarioIa (P5) -- (depends on: Define Project Scope and Requirements)
3. Set up Data Pipeline (P3) -- (depends on: Design System Architecture)
4. Develop Data Storage and Processing (P3) -- (depends on: Design System Architecture)
5. Implement Security and Access Controls (P3) -- (depends on: Design System Architecture)
6. Implement Machine Learning Models (P2) -- (depends on: Set up Data Pipeline, Develop Data Storage and Processing)
7. Build User Interface (P2) -- (depends on: Implement Machine Learning Models)
8. Set up Continuous Integration and Deployment (P3) -- (depends on: Implement Machine Learning Models, Build User Interface)
9. Conduct Testing and Quality Assurance (P2) -- (depends on: Implement Machine Learning Models, Build User Interface, Set up Continuous Integration and Deployment)
10. Write Documentation and User Guides (P2) -- (depends on: Implement Machine Learning Models, Build User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AnalisisInmobiliarioIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Una herramienta de IA que analiza tendencias del mercado inmobiliario y predice fluctuaciones de pre.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
