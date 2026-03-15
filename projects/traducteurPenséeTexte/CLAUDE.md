# traducteurPenséeTexte

You are a coding agent working on traducteurPenséeTexte -- Un système BCI qui traduit les schémas de pensée en texte écrit, facilitant la communication des personnes avec des troubles de la parole.

## Foundational Axiom

Existing approaches to un système bci qui traduit les schémas de pensée en texte éc fail because they optimize for the common case while ignoring structural constraints; traducteurPenséeTexte makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un système BCI qui traduit les schémas de pensée en texte écrit, facilitant la communication des per
- User interface: design bci interface

## Anti-Goals

- **General-purpose platform**: traducteurPenséeTexte solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design BCI Interface (P2) -- (depends on: Define System Architecture)
3. Develop BCI Algorithm (P3) -- (depends on: Define System Architecture)
4. Develop Text Generation Module (P4) -- (depends on: Develop BCI Algorithm)
5. Integrate System Components (P5) -- (depends on: Design BCI Interface, Develop BCI Algorithm, Develop Text Generation Module)
6. Test System Functionality (P1) -- (depends on: Integrate System Components)
7. Review System Design (P2) -- (depends on: Integrate System Components)
8. Write Technical Documentation (P3) -- (depends on: Test System Functionality, Review System Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: traducteurPenséeTexte can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un système BCI qui traduit les schémas de pensée en texte écrit, facilitant la communication des per.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
