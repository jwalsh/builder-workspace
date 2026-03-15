# RealTimeTrafficManagementSystem

You are a coding agent working on RealTimeTrafficManagementSystem -- A distributed system for real-time traffic management in smart cities, processing data from various sensors and controlling traffic signals.

## Foundational Axiom

Existing approaches to distributed system fail because they optimize for the common case while ignoring structural constraints; RealTimeTrafficManagementSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement real-time data processing module
- User interface: develop user interface for traffic managers
- Data layer: develop sensor data collection module

## Anti-Goals

- **General-purpose platform**: RealTimeTrafficManagementSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop Sensor Data Collection Module (P2) -- (depends on: Define System Architecture)
3. Implement Real-time Data Processing Module (P3) -- (depends on: Develop Sensor Data Collection Module)
4. Develop User Interface for Traffic Managers (P5) -- (depends on: Implement Real-time Data Processing Module)
5. Design Traffic Signal Control Algorithm (P4) -- (depends on: Define System Architecture)
6. Set Up Database Schema for Traffic Data Storage (P2) -- (depends on: Implement Real-time Data Processing Module)
7. Perform Quality Assurance Tests (P4) -- (depends on: Develop Sensor Data Collection Module, Implement Real-time Data Processing Module, Design Traffic Signal Control Algorithm, Develop User Interface for Traffic Managers, Set Up Database Schema for Traffic Data Storage)
8. Configure and Deploy Cloud Infrastructure (P3) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeTrafficManagementSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system for real-time traffic management in smart cities, processing data from various .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
