# VirtualPetCompanion

You are a coding agent working on VirtualPetCompanion -- An augmented reality pet companion app that allows users to interact with virtual pets in their real environment, offering companionship without the responsibilities of pet ownership.

## Foundational Axiom

Existing approaches to augmented reality pet companion app fail because they optimize for the common case while ignoring structural constraints; VirtualPetCompanion makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: VirtualPetCompanion solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for VirtualPetCompanion (Updated) (P3) -- (depends on: Requirements Gathering and Analysis)
3. Backend Development (P4) -- (depends on: System Architecture Design)
4. UI/UX Design for VirtualPetCompanion app: Final Draft (P3) -- (depends on: Requirements Gathering and Analysis)
5. Frontend Development (P4) -- (depends on: System Architecture Design, UI/UX Design)
6. Database Design and Implementation (P4) -- (depends on: System Architecture Design)
7. Deployment and DevOps (P5) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation)
8. Security and Privacy Considerations (P4) -- (depends on: System Architecture Design)
9. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development)
10. Documentation and User Support (P4) -- (depends on: Backend Development, Frontend Development)
11. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualPetCompanion can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An augmented reality pet companion app that allows users to interact with virtual pets in their real.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
