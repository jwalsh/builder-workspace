# LinguaNextIa

You are a coding agent working on LinguaNextIa -- Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para proporcionar traducciones precisas y eficientes para las empresas y las organizaciones.

## Foundational Axiom

Existing approaches to un sistema de traducción que utiliza la inteligencia artific fail because they optimize for the common case while ignoring structural constraints; LinguaNextIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para pro
- User interface: define project requirements
- Data layer: implement database schema

## Anti-Goals

- **General-purpose platform**: LinguaNextIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Requirements)
3. Design AI and ML Components (P3) -- (depends on: Design System Architecture)
4. Develop AI and ML Models (P5) -- (depends on: Design AI and ML Components)
5. Implement User Interface (UI) (P5) -- (depends on: Design UI)
6. Integrate AI and UI (P5) -- (depends on: Develop AI and ML Models, Implement UI)
7. Implement Database Schema (P4) -- (depends on: Design System Architecture)
8. Test Translation System (P4) -- (depends on: Integrate AI and UI)
9. Design User Interface (UI) (P3) -- (depends on: Design System Architecture)
10. Deploy Translation System (P2) -- (depends on: Test Translation System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LinguaNextIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
