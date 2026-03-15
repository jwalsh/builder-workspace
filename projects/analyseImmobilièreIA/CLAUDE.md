# analyseImmobilièreIA

You are a coding agent working on analyseImmobilièreIA -- Un outil d'IA qui analyse les tendances du marché immobilier et prédit les fluctuations des prix.

## Foundational Axiom

Existing approaches to un outil d'ia qui analyse les tendances du marché immobilier fail because they optimize for the common case while ignoring structural constraints; analyseImmobilièreIA makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development: integration of data collection and prediction modules
- User interface: frontend development: user interface design
- Data layer: market trends data collection strategy

## Anti-Goals

- **General-purpose platform**: analyseImmobilièreIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals (P1)
2. Market Trends Data Collection Strategy (P2) -- (depends on: Define Project Scope and Goals)
3. Price Fluctuation Prediction Algorithm Design (P3) -- (depends on: Market Trends Data Collection Strategy)
4. Backend Development: Integration of Data Collection and Prediction Modules (P5) -- (depends on: Price Fluctuation Prediction Algorithm Design)
5. Security Review: Secure the Tool against Threats (P5) -- (depends on: Backend Development: Integration of Data Collection and Prediction Modules)
6. Frontend Development: User Interface Design (P4) -- (depends on: Price Fluctuation Prediction Algorithm Design)
7. Quality Assurance: Testing and Bug Fixes (P4) -- (depends on: Frontend Development: User Interface Design, Backend Development: Integration of Data Collection and Prediction Modules)
8. DevOps: Infrastructure Setup and Deployment (P3) -- (depends on: Backend Development: Integration of Data Collection and Prediction Modules)
9. Database Management: Data Storage and Retrieval Strategy (P2) -- (depends on: Market Trends Data Collection Strategy)
10. Documentation: Technical Writing for the Tool (P1) -- (depends on: Frontend Development: User Interface Design, Backend Development: Integration of Data Collection and Prediction Modules)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: analyseImmobilièreIA can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un outil d'IA qui analyse les tendances du marché immobilier et prédit les fluctuations des prix..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
