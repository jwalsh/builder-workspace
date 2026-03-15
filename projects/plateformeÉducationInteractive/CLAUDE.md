# plateformeÉducationInteractive

You are a coding agent working on plateformeÉducationInteractive -- Une plateforme éducative immersive basée sur la réalité augmentée, offrant des expériences d'apprentissage interactives.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; plateformeÉducationInteractive closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for the platform
- User interface: develop frontend interface design
- Data layer: implement database design for user data management

## Anti-Goals

- **General-purpose platform**: plateformeÉducationInteractive solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Use Cases for Interactive Education Platform (P3)
2. Design the Architecture of the Interactive Education Platform (P2) -- (depends on: Define Use Cases for Interactive Education Platform)
3. Develop Frontend Interface Design (P4) -- (depends on: Design the Architecture of the Interactive Education Platform)
4. Develop AR Experience for the Platform (P1) -- (depends on: Design the Architecture of the Interactive Education Platform)
5. Conduct QA Testing on the Interactive Education Platform (P5) -- (depends on: Develop Frontend Interface Design, Develop AR Experience for the Platform)
6. Review and Update RFC for Interactive Education Platform (P4) -- (depends on: Define Use Cases for Interactive Education Platform)
7. Implement Database Design for User Data Management (P3) -- (depends on: Design the Architecture of the Interactive Education Platform)
8. Develop Backend Services for the Platform (P2) -- (depends on: Design the Architecture of the Interactive Education Platform)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: plateformeÉducationInteractive can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une plateforme éducative immersive basée sur la réalité augmentée, offrant des expériences d'apprent.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
