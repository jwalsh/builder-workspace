# KIgesteuerteKlimaschutzPlattform

You are a coding agent working on KIgesteuerteKlimaschutzPlattform -- Eine KI-gesteuerte Plattform zur Modellierung und Optimierung von Klimaschutzmaßnahmen auf globaler Ebene.

## Foundational Axiom

Existing approaches to eine ki-gesteuerte plattform zur modellierung und optimierun fail because they optimize for the common case while ignoring structural constraints; KIgesteuerteKlimaschutzPlattform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Eine KI-gesteuerte Plattform zur Modellierung und Optimierung von Klimaschutzmaßnahmen auf globaler 
- User interface: define project requirements
- Data layer: setup database structure

## Anti-Goals

- **General-purpose platform**: KIgesteuerteKlimaschutzPlattform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design KI Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop User Interface for Platform (P3) -- (depends on: Design KI Architecture)
4. Setup Database Structure (P3) -- (depends on: Design KI Architecture)
5. Develop Climate Modeling Module (P3) -- (depends on: Design KI Architecture)
6. Test Climate Modeling Module (P4) -- (depends on: Develop Climate Modeling Module)
7. Deploy KIgesteuerteKlimaschutzPlattform (P5) -- (depends on: Develop User Interface for Platform, Setup Database Structure, Test Climate Modeling Module)
8. Perform Security Audit (P4) -- (depends on: Develop Climate Modeling Module)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: KIgesteuerteKlimaschutzPlattform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Eine KI-gesteuerte Plattform zur Modellierung und Optimierung von Klimaschutzmaßnahmen auf globaler .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
