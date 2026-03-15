# interfaceHCIAvancée

You are a coding agent working on interfaceHCIAvancée -- Une interface homme-machine avancée offrant des expériences interactives immersives et réactives.

## Foundational Axiom

Existing approaches to une interface homme-machine avancée offrant des expériences fail because they optimize for the common case while ignoring structural constraints; interfaceHCIAvancée makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: document user manual and api reference
- User interface: define project requirements
- Data layer: integrate database for data storage

## Anti-Goals

- **General-purpose platform**: interfaceHCIAvancée solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Interactive and Immersive Experiences (P2) -- (depends on: Define Project Requirements)
3. Develop Core Interface Components (P3) -- (depends on: Design Interactive and Immersive Experiences)
4. Implement Advanced Functionality (P4) -- (depends on: Design Interactive and Immersive Experiences)
5. Integrate Database for Data Storage (P5) -- (depends on: Develop Core Interface Components, Implement Advanced Functionality)
6. Document User Manual and API Reference (P3) -- (depends on: Develop Core Interface Components, Implement Advanced Functionality)
7. Implement Security Measures (P2) -- (depends on: Develop Core Interface Components, Implement Advanced Functionality)
8. Perform Quality Assurance Tests (P1) -- (depends on: Develop Core Interface Components, Implement Advanced Functionality)
9. Deploy and Launch the InterfaceHCIAvancée (P1) -- (depends on: Develop Core Interface Components, Implement Advanced Functionality)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: interfaceHCIAvancée can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une interface homme-machine avancée offrant des expériences interactives immersives et réactives..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
