# droneTransportÉnergie

You are a coding agent working on droneTransportÉnergie -- Des drones conçus pour transporter des matériaux et des énergies renouvelables dans des environnements difficiles.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; droneTransportÉnergie maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Des drones conçus pour transporter des matériaux et des énergies renouvelables dans des environnemen
- Data layer: develop energy storage system for drones

## Anti-Goals

- **General-purpose platform**: droneTransportÉnergie solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design the drone frame structure (P3)
2. Implement energy efficiency measures in drones (P5) -- (depends on: Design the drone frame structure)
3. Develop energy storage system for drones (P4) -- (depends on: Design the drone frame structure)
4. Develop flight control system for drones (P1) -- (depends on: Design the drone frame structure)
5. Draft Technical Documentation for Drone Design and Operation (P4) -- (depends on: Design the drone frame structure, Develop flight control system for drones)
6. Create a system for transporting materials securely (P2) -- (depends on: Design the drone frame structure)
7. Perform environmental impact analysis (P2)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: droneTransportÉnergie can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des drones conçus pour transporter des matériaux et des énergies renouvelables dans des environnemen.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
