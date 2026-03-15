# VehiculosAutonomos

You are a coding agent working on VehiculosAutonomos -- Una flota de vehículos completamente autónomos diseñados para entornos urbanos.

## Foundational Axiom

Existing approaches to una flota de vehículos completamente autónomos diseñados par fail because they optimize for the common case while ignoring structural constraints; VehiculosAutonomos makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Una flota de vehículos completamente autónomos diseñados para entornos urbanos.
- User interface: develop user interface for vehicles and management system
- Data layer: analyze fleet performance data

## Anti-Goals

- **General-purpose platform**: VehiculosAutonomos solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Autonomous Vehicle Architecture (P1)
2. Implement Autonomous Driving Algorithms (P3) -- (depends on: Design Autonomous Vehicle Architecture)
3. Develop Urban Mapping System (P2) -- (depends on: Design Autonomous Vehicle Architecture)
4. Test and Validate Autonomous Vehicles (P5) -- (depends on: Implement Autonomous Driving Algorithms, Develop Urban Mapping System)
5. Deploy Fleet of Autonomous Vehicles in Controlled Environment (P2) -- (depends on: Test and Validate Autonomous Vehicles)
6. Address Security Concerns (P5) -- (depends on: Deploy Fleet of Autonomous Vehicles in Controlled Environment)
7. Develop User Interface for Vehicles and Management System (P4) -- (depends on: Design Autonomous Vehicle Architecture)
8. Analyze Fleet Performance Data (P3) -- (depends on: Deploy Fleet of Autonomous Vehicles in Controlled Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VehiculosAutonomos can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una flota de vehículos completamente autónomos diseñados para entornos urbanos..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
