# SensoresIndustria4_0

You are a coding agent working on SensoresIndustria4_0 -- Una red de sensores IoT que monitorea los procesos industriales en tiempo real para mejorar la eficiencia.

## Foundational Axiom

Existing approaches to una red de sensores iot que monitorea los procesos industria fail because they optimize for the common case while ignoring structural constraints; SensoresIndustria4_0 makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop real-time data processing algorithms
- User interface: design user interface for monitoring dashboard
- Data layer: develop real-time data processing algorithms

## Anti-Goals

- **General-purpose platform**: SensoresIndustria4_0 solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Sensor Network Architecture (P1)
2. Define Sensor Types and Functionalities (P2) -- (depends on: Design Sensor Network Architecture)
3. Develop IoT Communication Protocol (P3) -- (depends on: Define Sensor Types and Functionalities, Design Sensor Network Architecture)
4. Develop Real-Time Data Processing Algorithms (P4) -- (depends on: Develop IoT Communication Protocol)
5. Design User Interface for Monitoring Dashboard (P5) -- (depends on: Develop Real-Time Data Processing Algorithms)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SensoresIndustria4_0 can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una red de sensores IoT que monitorea los procesos industriales en tiempo real para mejorar la efici.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to iot engineers and embedded systems developers.
