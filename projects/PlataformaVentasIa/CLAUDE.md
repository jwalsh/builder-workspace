# PlataformaVentasIa

You are a coding agent working on PlataformaVentasIa -- Una plataforma de IA que optimiza las experiencias de venta en línea analizando el comportamiento de los clientes.

## Foundational Axiom

Existing approaches to una plataforma de ia que optimiza las experiencias de venta fail because they optimize for the common case while ignoring structural constraints; PlataformaVentasIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for ai integration and data management
- User interface: define project requirements and goals
- Data layer: develop backend for ai integration and data management

## Anti-Goals

- **General-purpose platform**: PlataformaVentasIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project requirements and goals (P1)
2. Configure DevOps pipeline and tools (P5) -- (depends on: Define project requirements and goals)
3. Develop frontend for user interaction (P3) -- (depends on: Define project requirements and goals)
4. Design AI algorithm for customer behavior analysis (P2) -- (depends on: Define project requirements and goals)
5. Develop backend for AI integration and data management (P3) -- (depends on: Define project requirements and goals, Design AI algorithm for customer behavior analysis)
6. Document the development process (P5) -- (depends on: Develop frontend for user interaction, Develop backend for AI integration and data management)
7. Implement database schema and connections (P4) -- (depends on: Define project requirements and goals, Develop frontend for user interaction, Develop backend for AI integration and data management)
8. Implement security measures (P4) -- (depends on: Develop frontend for user interaction, Develop backend for AI integration and data management)
9. Test platform for functionality and performance (P2) -- (depends on: Develop frontend for user interaction, Develop backend for AI integration and data management)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlataformaVentasIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una plataforma de IA que optimiza las experiencias de venta en línea analizando el comportamiento de.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
