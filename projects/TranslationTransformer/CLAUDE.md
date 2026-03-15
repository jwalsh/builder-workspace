# TranslationTransformer

You are a coding agent working on TranslationTransformer -- Un système de traduction qui utilise l'intelligence artificielle et l'apprentissage automatique pour fournir des traductions précises et efficaces pour les entreprises et les organisations qui doivent traduire du contenu dans plusieurs langues.

## Foundational Axiom

Existing tools treat un système de traduction qui utilise l'intelligence artifici as a generic automation problem; TranslationTransformer succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: TranslationTransformer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design AI and Machine Learning Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Backend Services (P4) -- (depends on: Design AI and Machine Learning Architecture)
4. Database Design and Implementation (P5) -- (depends on: Develop Backend Services)
5. Develop Frontend Interface (P3) -- (depends on: Design AI and Machine Learning Architecture)
6. Implement DevOps Strategy (P1) -- (depends on: Develop Frontend Interface, Develop Backend Services, Database Design and Implementation)
7. Perform Quality Assurance Testing (P2) -- (depends on: Implement DevOps Strategy)
8. Document the TranslationTransformer System (P4) -- (depends on: Perform Quality Assurance Testing)
9. Secure the TranslationTransformer System (P3) -- (depends on: Implement DevOps Strategy)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TranslationTransformer can deliver its core value proposition as described
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
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
