# PlataformaEducacionInteractiva

You are a coding agent working on PlataformaEducacionInteractiva -- Una plataforma educativa inmersiva basada en realidad aumentada que ofrece experiencias de aprendizaje interactivas.

## Foundational Axiom

Existing approaches to una plataforma educativa inmersiva basada en realidad aument fail because they optimize for the common case while ignoring structural constraints; PlataformaEducacionInteractiva makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Una plataforma educativa inmersiva basada en realidad aumentada que ofrece experiencias de aprendiza
- User interface: design the user interface for plataformaeducacioninteractiva

## Anti-Goals

- **General-purpose platform**: PlataformaEducacionInteractiva solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define the overall architecture of PlataformaEducacionInteractiva (P1)
2. Create educational content for PlataformaEducacionInteractiva (P4) -- (depends on: Define the overall architecture of PlataformaEducacionInteractiva)
3. Test and validate PlataformaEducacionInteractiva (P5) -- (depends on: Define the overall architecture of PlataformaEducacionInteractiva, Create educational content for PlataformaEducacionInteractiva)
4. Develop the underlying system for realidad aumentada in PlataformaEducacionInteractiva (P3) -- (depends on: Define the overall architecture of PlataformaEducacionInteractiva)
5. Design the user interface for PlataformaEducacionInteractiva (P2) -- (depends on: Define the overall architecture of PlataformaEducacionInteractiva)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlataformaEducacionInteractiva can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una plataforma educativa inmersiva basada en realidad aumentada que ofrece experiencias de aprendiza.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
