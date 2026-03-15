# DronAgricolaInteligente

You are a coding agent working on DronAgricolaInteligente -- Drones autónomos capaces de monitorear cultivos y optimizar el uso de recursos agrícolas.

## Foundational Axiom

Existing approaches to drones autónomos capaces de monitorear cultivos y optimizar fail because they optimize for the common case while ignoring structural constraints; DronAgricolaInteligente makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Drones autónomos capaces de monitorear cultivos y optimizar el uso de recursos agrícolas.
- User interface: requirements gathering for droneagro project
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: DronAgricolaInteligente solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for DroneAgro Project (P1)
2. Design Drone Architecture (P2) -- (depends on: Requirements Gathering)
3. Develop Drone Firmware (P3) -- (depends on: Design Drone Architecture)
4. Develop Mobile Application Interface (P3) -- (depends on: Design Drone Architecture)
5. Database Design and Implementation (P4) -- (depends on: Requirements Gathering)
6. Integration of Components (P2) -- (depends on: Develop Drone Firmware, Develop Mobile Application Interface, Database Design and Implementation)
7. Unit Testing (P4) -- (depends on: Develop Drone Firmware, Develop Mobile Application Interface, Database Design and Implementation, Integration of Components)
8. System Integration Testing (P5) -- (depends on: Unit Testing, Integration of Components)
9. Security Review (P5) -- (depends on: System Integration Testing)
10. Deployment Planning (P3) -- (depends on: System Integration Testing)
11. Deployment and Monitoring (P5) -- (depends on: Deployment Planning)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DronAgricolaInteligente can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Drones autónomos capaces de monitorear cultivos y optimizar el uso de recursos agrícolas..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to agricultural scientists and farm operators.
