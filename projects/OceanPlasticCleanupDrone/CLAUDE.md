# OceanPlasticCleanupDrone

You are a coding agent working on OceanPlasticCleanupDrone -- Autonomous drones that navigate oceans, collecting and processing plastic waste into reusable materials or fuel.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; OceanPlasticCleanupDrone guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design processing system for plastic waste
- User interface: define project scope and requirements: oceanplasticcleanupdrone
- Data layer: set up cloud infrastructure for data storage and processing

## Anti-Goals

- **General-purpose platform**: OceanPlasticCleanupDrone solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: OceanPlasticCleanupDrone (P1)
2. Design the Drone Hardware (P2) -- (depends on: Define Project Scope and Requirements)
3. Design the Drone's Navigation System (P3) -- (depends on: Design the Drone Hardware)
4. Develop AI for Object Detection and Recognition (P4) -- (depends on: Design the Drone's Navigation System)
5. Implement Waste Collection Mechanism (P4) -- (depends on: Design the Drone Hardware, Develop AI for Object Detection and Recognition)
6. Design Processing System for Plastic Waste (P5) -- (depends on: Implement Waste Collection Mechanism)
7. Test and Validate Functionality of Individual Components (P4) -- (depends on: Complete all subtasks under 'Design' and 'Development' sections)
8. Conduct Security Audit on System (P5) -- (depends on: Test and Validate Functionality of Individual Components)
9. Develop User Interface for Monitoring Drone Operations (P2) -- (depends on: Define Project Scope and Requirements)
10. Set Up Cloud Infrastructure for Data Storage and Processing (P3) -- (depends on: Develop User Interface for Monitoring Drone Operations)
11. Document System Architecture and Component Interactions - RFC (P2) -- (depends on: Complete all subtasks under 'Design' and 'Development' sections)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OceanPlasticCleanupDrone can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Autonomous drones that navigate oceans, collecting and processing plastic waste into reusable materi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
