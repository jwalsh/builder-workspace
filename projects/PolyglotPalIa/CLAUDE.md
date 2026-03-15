# PolyglotPalIa

You are a coding agent working on PolyglotPalIa -- Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per fornire traduzioni personalizzate e migliorare la comunicazione globale.

## Foundational Axiom

Existing approaches to un assistente di traduzione che utilizza l'intelligenza arti fail because they optimize for the common case while ignoring structural constraints; PolyglotPalIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend api for integration with ai and ml model
- User interface: develop frontend interface for user interaction
- Data layer: integrate database for storing user data and translations

## Anti-Goals

- **General-purpose platform**: PolyglotPalIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and goals (P1)
2. Design AI and machine learning model architecture (P2) -- (depends on: Define project scope and goals)
3. Develop frontend interface for user interaction (P3) -- (depends on: Define project scope and goals)
4. Integrate database for storing user data and translations (P5) -- (depends on: Design AI and machine learning model architecture, Develop frontend interface for user interaction)
5. Develop backend API for integration with AI and ML model (P4) -- (depends on: Design AI and machine learning model architecture)
6. Implement DevOps strategies for deployment and scaling (P1) -- (depends on: Define project scope and goals, Develop frontend interface for user interaction, Develop backend API for integration with AI and ML model)
7. Perform QA testing on the complete system (P2) -- (depends on: Implement DevOps strategies for deployment and scaling)
8. Create user documentation and guides (P4) -- (depends on: Perform QA testing on the complete system)
9. Address security concerns and implement safeguards (P3) -- (depends on: Perform QA testing on the complete system)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PolyglotPalIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
