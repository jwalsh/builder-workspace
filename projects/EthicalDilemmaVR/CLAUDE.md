# EthicalDilemmaVR

You are a coding agent working on EthicalDilemmaVR -- A virtual reality environment that places users in complex ethical scenarios, allowing them to explore the consequences of their choices and reflect on moral philosophies.

## Foundational Axiom

Existing approaches to virtual reality environment fail because they optimize for the common case while ignoring structural constraints; EthicalDilemmaVR makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A virtual reality environment that places users in complex ethical scenarios, allowing them to explo
- User interface: defineprojectscopeandrequirements

## Anti-Goals

- **General-purpose platform**: EthicalDilemmaVR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Defineprojectscopeandrequirements (P5)
2. Design the VR environment (P4) -- (depends on: Define project scope and requirements)
3. Develop ethical scenario models (P4) -- (depends on: Define project scope and requirements)
4. Implement VR environment (P3) -- (depends on: Design the VR environment, Develop ethical scenario models)
5. Develop user tracking and analytics (P3) -- (depends on: Implement VR environment)
6. Implement security measures (P4) -- (depends on: Implement VR environment, Develop user tracking and analytics)
7. Set up testing and QA processes (P3) -- (depends on: Implement VR environment, Develop ethical scenario models)
8. Plan deployment and infrastructure (P3) -- (depends on: Implement VR environment)
9. Create documentation and tutorials (P2) -- (depends on: Implement VR environment, Develop ethical scenario models)
10. Conduct user testing and feedback (P2) -- (depends on: Implement VR environment, Set up testing and QA processes)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EthicalDilemmaVR can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A virtual reality environment that places users in complex ethical scenarios, allowing them to explo.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
