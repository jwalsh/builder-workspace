# assistantSantéIA

You are a coding agent working on assistantSantéIA -- Un assistant personnel qui propose des conseils de santé personnalisés basés sur des métriques en temps réel.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; assistantSantéIA embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend of assistantsantéia
- User interface: define the project scope and requirements
- Data layer: create the database schema for assistantsantéia

## Anti-Goals

- **General-purpose platform**: assistantSantéIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define the project scope and requirements (P1)
2. Design the architecture for assistantSantéIA (P2) -- (depends on: Define the project scope and requirements)
3. Develop the frontend of assistantSantéIA (P3) -- (depends on: Design the architecture for assistantSantéIA)
4. Develop the backend of assistantSantéIA (P3) -- (depends on: Design the architecture for assistantSantéIA)
5. Perform quality assurance testing on assistantSantéIA (P5) -- (depends on: Develop the frontend of assistantSantéIA, Develop the backend of assistantSantéIA)
6. Address security concerns in assistantSantéIA (P5) -- (depends on: Develop the frontend of assistantSantéIA, Develop the backend of assistantSantéIA)
7. Document the development process and user manual for assistantSantéIA (P5) -- (depends on: Develop the frontend of assistantSantéIA, Develop the backend of assistantSantéIA)
8. Create the database schema for assistantSantéIA (P4) -- (depends on: Design the architecture for assistantSantéIA)
9. Set up devops and deploy assistantSantéIA (P4) -- (depends on: Develop the frontend of assistantSantéIA, Develop the backend of assistantSantéIA, Create the database schema for assistantSantéIA)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantSantéIA can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un assistant personnel qui propose des conseils de santé personnalisés basés sur des métriques en te.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
