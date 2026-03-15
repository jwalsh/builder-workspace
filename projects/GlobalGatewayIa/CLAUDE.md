# GlobalGatewayIa

You are a coding agent working on GlobalGatewayIa -- Un système de traduction qui utilise l'intelligence artificielle et l'apprentissage automatique pour fournir des traductions précises et efficaces pour les entreprises et les organisations qui doivent communiquer avec des clients et des partenaires dans le monde entier.

## Foundational Axiom

Existing approaches to un système de traduction qui utilise l'intelligence artifici fail because they optimize for the common case while ignoring structural constraints; GlobalGatewayIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: develop frontend interface
- Data layer: integrate database solutions

## Anti-Goals

- **General-purpose platform**: GlobalGatewayIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design System Architecture (P2) -- (depends on: Define Project Requirements)
2. Develop Backend Services (P3) -- (depends on: Design System Architecture)
3. Perform Security Audit (P5) -- (depends on: Develop Backend Services)
4. Develop Frontend Interface (P3) -- (depends on: Design System Architecture)
5. Refine User Documentation (P5) -- (depends on: Develop Frontend Interface)
6. Integrate Database Solutions (P4) -- (depends on: Design System Architecture)
7. Configure DevOps Environment (P4) -- (depends on: Design System Architecture)
8. Perform Functional Testing (P2) -- (depends on: Develop Backend Services)
9. Define Comprehensive Project Requirements for Translation System (Revised) (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalGatewayIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un système de traduction qui utilise l'intelligence artificielle et l'apprentissage automatique pour.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
