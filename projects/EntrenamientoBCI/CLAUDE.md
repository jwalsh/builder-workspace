# EntrenamientoBCI

You are a coding agent working on EntrenamientoBCI -- Una plataforma BCI diseñada para acelerar el aprendizaje y la adquisición de habilidades.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; EntrenamientoBCI models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: requirements gathering for entrenamientobci project
- Data layer: database design

## Anti-Goals

- **General-purpose platform**: EntrenamientoBCI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for EntrenamientoBCI Project (P1)
2. Design BCI Platform Architecture (P2) -- (depends on: Requirements Gathering)
3. Database Design (P3) -- (depends on: Design BCI Platform Architecture)
4. Backend Development (P4) -- (depends on: Design BCI Platform Architecture, Database Design)
5. Frontend Development (P4) -- (depends on: Design BCI Platform Architecture)
6. Test Design and Implementation (P5) -- (depends on: Backend Development, Frontend Development)
7. Security Review (P5) -- (depends on: Backend Development, Frontend Development)
8. Deployment and Monitoring (P5) -- (depends on: Test Design and Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EntrenamientoBCI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una plataforma BCI diseñada para acelerar el aprendizaje y la adquisición de habilidades..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
