# GeneradorContenidoMultilingüe

You are a coding agent working on GeneradorContenidoMultilingüe -- Una plataforma de generación de contenido multilingüe para marketing y comunicaciones corporativas.

## Foundational Axiom

Existing approaches to una plataforma de generación de contenido multilingüe para m fail because they optimize for the common case while ignoring structural constraints; GeneradorContenidoMultilingüe makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements
- Data layer: integrate content generation system with database

## Anti-Goals

- **General-purpose platform**: GeneradorContenidoMultilingüe solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Content Generation Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Backend Services (P4) -- (depends on: Design Content Generation Architecture)
4. Develop Frontend Interface (P5) -- (depends on: Develop Backend Services)
5. Integrate Content Generation System with Database (P5) -- (depends on: Develop Backend Services)
6. Create User Interface Designs (P3) -- (depends on: Design Content Generation Architecture)
7. Test Content Generation Platform (P2) -- (depends on: Create User Interface Designs, Develop Backend Services, Develop Frontend Interface, Integrate Content Generation System with Database)
8. Fix Bugs and Make Necessary Improvements (P3) -- (depends on: Test Content Generation Platform)
9. Deploy Content Generation Platform (P1) -- (depends on: Fix Bugs and Make Necessary Improvements)
10. Monitor and Maintain the Platform (P5) -- (depends on: Deploy Content Generation Platform)
11. Document Technical Aspects of the Project (P4) -- (depends on: Test Content Generation Platform)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeneradorContenidoMultilingüe can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una plataforma de generación de contenido multilingüe para marketing y comunicaciones corporativas..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
