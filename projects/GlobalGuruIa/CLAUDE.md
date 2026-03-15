# GlobalGuruIa

You are a coding agent working on GlobalGuruIa -- Un système de traduction qui utilise l'intelligence artificielle et l'apprentissage automatique pour fournir des traductions précises et efficaces pour les entreprises et les organisations qui doivent communiquer avec des clients et des partenaires dans le monde entier.

## Foundational Axiom

Existing approaches to un système de traduction qui utilise l'intelligence artifici fail because they optimize for the common case while ignoring structural constraints; GlobalGuruIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: develop frontend components
- Data layer: set up and configure databases

## Anti-Goals

- **General-purpose platform**: GlobalGuruIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design overall system architecture (P2) -- (depends on: Define project scope and requirements)
2. Implement AI and machine learning models (P4) -- (depends on: Design overall system architecture)
3. Develop frontend components (P3) -- (depends on: Design overall system architecture)
4. Develop backend services (P3) -- (depends on: Design overall system architecture)
5. Set up and configure databases (P3) -- (depends on: Design overall system architecture)
6. Implement DevOps and CI/CD pipelines (P3) -- (depends on: Design overall system architecture)
7. Perform QA and testing (P4) -- (depends on: Develop frontend components, Develop backend services, Implement AI and machine learning models, Set up and configure databases, Implement DevOps and CI/CD pipelines)
8. Develop User Registration and Authentication (P2) -- (depends on: Define System Architecture)
9. Document system design and implementation (P2) -- (depends on: Develop frontend components, Develop backend services, Implement AI and machine learning models, Set up and configure databases, Implement DevOps and CI/CD pipelines)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalGuruIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un système de traduction qui utilise l'intelligence artificielle et l'apprentissage automatique pour.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
