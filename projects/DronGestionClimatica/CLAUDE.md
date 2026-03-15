# DronGestionClimatica

You are a coding agent working on DronGestionClimatica -- Drones autónomos para gestionar el clima en entornos agrícolas, optimizando la humedad y temperatura.

## Foundational Axiom

Existing approaches to drones autónomos para gestionar el clima en entornos agrícol fail because they optimize for the common case while ignoring structural constraints; DronGestionClimatica makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend functions for drone control and data processing
- User interface: requirements gathering for dronegestionclimatica
- Data layer: database design for climate data and drone operations

## Anti-Goals

- **General-purpose platform**: DronGestionClimatica solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for DroneGestionClimatica (P1)
2. Design Architecture for Drones and Climate Management System (P2) -- (depends on: Requirements Gathering for DroneGestionClimatica)
3. Database Design for Climate Data and Drone Operations (P3) -- (depends on: Design Architecture for Drones and Climate Management System)
4. Implement Backend Functions for Drone Control and Data Processing (P5) -- (depends on: Design Architecture for Drones and Climate Management System, Database Design for Climate Data and Drone Operations)
5. Develop Frontend Interface for User Interaction (P4) -- (depends on: Design Architecture for Drones and Climate Management System)
6. Test the DronGestionClimatica System (P4) -- (depends on: Implement Backend Functions for Drone Control and Data Processing)
7. Perform Security Audit on the System (P3) -- (depends on: Implement Backend Functions for Drone Control and Data Processing)
8. Integrate DevOps for Continuous Deployment and Monitoring (P2) -- (depends on: Implement Backend Functions for Drone Control and Data Processing)
9. Review and Approve Requirements and Design Documents (P1) -- (depends on: Requirements Gathering for DroneGestionClimatica, Design Architecture for Drones and Climate Management System, Database Design for Climate Data and Drone Operations, Security Audit on the System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DronGestionClimatica can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Drones autónomos para gestionar el clima en entornos agrícolas, optimizando la humedad y temperatura.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
