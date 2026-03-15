# HerramientaCodigoIa

You are a coding agent working on HerramientaCodigoIa -- Una herramienta de IA que genera automáticamente código basado en los requisitos del proyecto.

## Foundational Axiom

Existing approaches to una herramienta de ia que genera automáticamente código basa fail because they optimize for the common case while ignoring structural constraints; HerramientaCodigoIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for code generation
- User interface: define project requirements for code generation tool
- Data layer: integrate database for storing and retrieving project requirements

## Anti-Goals

- **General-purpose platform**: HerramientaCodigoIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements for Code Generation Tool (P1)
2. Design the Code Generation Algorithm (P2) -- (depends on: Define Project Requirements)
3. Implement Backend Services for Code Generation (P3) -- (depends on: Design the Code Generation Algorithm)
4. Perform Unit Tests and Debugging for Code Generator (P5) -- (depends on: Implement Backend Services for Code Generation)
5. Deploy the Automatic Code Generation Tool (P5) -- (depends on: Perform Unit Tests and Debugging for Code Generator)
6. Integrate Database for Storing and Retrieving Project Requirements (P4) -- (depends on: Design the Code Generation Algorithm)
7. Develop the Frontend Interface for User Input (P3) -- (depends on: Design the Code Generation Algorithm)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HerramientaCodigoIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una herramienta de IA que genera automáticamente código basado en los requisitos del proyecto..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
