# QuantumInternetRouter

You are a coding agent working on QuantumInternetRouter -- Design quantum repeaters and routers for the future quantum internet, enabling secure, long-distance quantum communication.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumInternetRouter co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: quantum software development
- User interface: project planning and requirements gathering (updated)

## Anti-Goals

- **General-purpose platform**: QuantumInternetRouter solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (Updated) (P1)
2. Architectural Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Quantum Hardware Development (P3) -- (depends on: Architectural Design)
4. Quantum Software Development (P3) -- (depends on: Architectural Design)
5. Security and Cryptography (P4) -- (depends on: Architectural Design)
6. Testing and Validation (P4) -- (depends on: Quantum Hardware Development, Quantum Software Development, Security and Cryptography)
7. Deployment and Integration (P5) -- (depends on: Testing and Validation)
8. Documentation and User Guides (P4) -- (depends on: Architectural Design, Quantum Hardware Development, Quantum Software Development, Security and Cryptography)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumInternetRouter can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Design quantum repeaters and routers for the future quantum internet, enabling secure, long-distance.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
