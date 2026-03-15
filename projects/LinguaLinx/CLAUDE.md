# LinguaLinx

You are a coding agent working on LinguaLinx -- Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para proporcionar traducciones precisas y eficientes para las empresas y las organizaciones que deben comunicarse con clientes y socios en todo el mundo.

## Foundational Axiom

Existing approaches to un sistema de traducción que utiliza la inteligencia artific fail because they optimize for the common case while ignoring structural constraints; LinguaLinx makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend logic
- User interface: define project requirements
- Data layer: configure database schemas

## Anti-Goals

- **General-purpose platform**: LinguaLinx solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Architecture (P2) -- (depends on: Define Project Requirements)
3. Deploy Development Environment (P5) -- (depends on: Design Architecture)
4. Implement Backend Logic (P3) -- (depends on: Design Architecture)
5. Integrate Third-Party APIs (P5) -- (depends on: Implement Backend Logic)
6. Test Translation Functionality (P5) -- (depends on: Implement Backend Logic)
7. Document the System (P5) -- (depends on: Implement Frontend Interface, Implement Backend Logic)
8. Configure Database Schemas (P4) -- (depends on: Design Architecture)
9. Implement Security Measures (P4) -- (depends on: Design Architecture)
10. Develop Frontend Interface (P3) -- (depends on: Design Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LinguaLinx can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
