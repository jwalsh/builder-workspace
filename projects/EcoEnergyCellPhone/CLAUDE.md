# EcoEnergyCellPhone

You are a coding agent working on EcoEnergyCellPhone -- A smartphone powered by ambient energy harvesting, never needing to be charged and doubling as a power source for other devices.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; EcoEnergyCellPhone maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: energy harvesting software development
- User interface: requirements gathering and analysis

## Anti-Goals

- **General-purpose platform**: EcoEnergyCellPhone solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design Concept Development (P2) -- (depends on: Requirements Gathering and Analysis)
3. Component Selection and Specification (P3) -- (depends on: Design Concept Development)
4. Hardware Prototype Creation (P4) -- (depends on: Component Selection and Specification)
5. Energy Harvesting Software Development (P5) -- (depends on: Hardware Prototype Creation)
6. Power-Sharing Software Development (P5) -- (depends on: Hardware Prototype Creation)
7. Integration Testing and Validation (P5) -- (depends on: Energy Harvesting Software Development, Power-Sharing Software Development)
8. User Interface Design and Implementation (P5) -- (depends on: Hardware Prototype Creation)
9. Prepare Documentation and User Manual (P5) -- (depends on: Hardware Prototype Creation)
10. Production Readiness and Quality Assurance (P5) -- (depends on: Integration Testing and Validation, User Interface Design and Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EcoEnergyCellPhone can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A smartphone powered by ambient energy harvesting, never needing to be charged and doubling as a pow.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
