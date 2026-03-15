# QuantumSensorPollutionDetector

You are a coding agent working on QuantumSensorPollutionDetector -- Highly sensitive quantum sensors for detecting and monitoring various types of pollution at extremely low levels.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; QuantumSensorPollutionDetector captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for data processing
- User interface: define quantum sensor requirements
- Data layer: implement backend services for data processing

## Anti-Goals

- **General-purpose platform**: QuantumSensorPollutionDetector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Quantum Sensor Requirements (P1)
2. Design Quantum Sensor Architecture (P2) -- (depends on: Define Quantum Sensor Requirements)
3. Implement Backend Services for Data Processing (P4) -- (depends on: Design Quantum Sensor Architecture)
4. Establish Database Structure for Data Storage (P5) -- (depends on: Implement Backend Services for Data Processing)
5. Review Database Structure Design and Implementation (P5) -- (depends on: Establish Database Structure for Data Storage)
6. Review Backend Services Implementation (P4) -- (depends on: Implement Backend Services for Data Processing)
7. Develop Frontend Interface for User Interaction (P3) -- (depends on: Design Quantum Sensor Architecture)
8. Review Frontend Interface Design and Implementation (P3) -- (depends on: Develop Frontend Interface for User Interaction)
9. Review Quantum Sensor Design Documents (P2) -- (depends on: Design Quantum Sensor Architecture)
10. Perform System Integration Testing (P1) -- (depends on: Develop Frontend Interface for User Interaction, Implement Backend Services for Data Processing, Establish Database Structure for Data Storage)
11. Document System Design and Implementation (P1) -- (depends on: Perform System Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumSensorPollutionDetector can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Highly sensitive quantum sensors for detecting and monitoring various types of pollution at extremel.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
