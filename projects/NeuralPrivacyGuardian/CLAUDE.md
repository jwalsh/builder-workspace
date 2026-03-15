# NeuralPrivacyGuardian

You are a coding agent working on NeuralPrivacyGuardian -- A device that protects against unauthorized access or interpretation of neural data.

## Foundational Axiom

Existing tools treat device as a generic automation problem; NeuralPrivacyGuardian succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement device hardware and software components
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: NeuralPrivacyGuardian solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Neural Privacy Guardian Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Privacy-Preserving Algorithms (P3) -- (depends on: Design Neural Privacy Guardian Architecture)
4. Implement Device Hardware and Software Components (P4) -- (depends on: Design Neural Privacy Guardian Architecture, Develop Privacy-Preserving Algorithms)
5. Integrate and Test Device Components (P5) -- (depends on: Implement Device Hardware and Software Components)
6. Prepare User Documentation and Guides (P2) -- (depends on: Implement Device Hardware and Software Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralPrivacyGuardian can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that protects against unauthorized access or interpretation of neural data..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
