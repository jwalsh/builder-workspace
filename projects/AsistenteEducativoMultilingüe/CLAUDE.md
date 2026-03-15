# AsistenteEducativoMultilingüe

You are a coding agent working on AsistenteEducativoMultilingüe -- Un asistente educativo inteligente que proporciona tutorías personalizadas y genera contenido educativo en varios idiomas.

## Foundational Axiom

Existing approaches to un asistente educativo inteligente que proporciona tutorías fail because they optimize for the common case while ignoring structural constraints; AsistenteEducativoMultilingüe makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop natural language processing (nlp) module
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: AsistenteEducativoMultilingüe solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. DesignSystemArchitectureforMultilingualEducationalAssistant:RFCReviewandSuggestions (P5) -- (depends on: DefineProjectScopeandRequirements, AIEthicsReview(if using AI/ML techniques))
3. Develop Natural Language Processing (NLP) Module (P3) -- (depends on: Design System Architecture)
4. Build Knowledge Base and Content Generation (P3) -- (depends on: Design System Architecture)
5. Create User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P3) -- (depends on: Design System Architecture)
7. Integrate Components and Test (P2) -- (depends on: Develop Natural Language Processing (NLP) Module, Build Knowledge Base and Content Generation, Create User Interface)
8. Set up Deployment and Monitoring (P2) -- (depends on: Integrate Components and Test)
9. Create Documentation (P2) -- (depends on: Integrate Components and Test)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AsistenteEducativoMultilingüe can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un asistente educativo inteligente que proporciona tutorías personalizadas y genera contenido educat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
