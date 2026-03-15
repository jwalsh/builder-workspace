# FunctionalReactiveProgrammingForIoT

You are a coding agent working on FunctionalReactiveProgrammingForIoT -- A framework for IoT devices that uses functional reactive programming to handle streams of sensor data and device control.

## Foundational Axiom

The bottleneck in framework for iot devices is not compute or data but the feedback loop between intent and artifact; FunctionalReactiveProgrammingForIoT compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A framework for IoT devices that uses functional reactive programming to handle streams of sensor da
- User interface: define project requirements for functionalreactiveprogrammingforiot

## Anti-Goals

- **General-purpose platform**: FunctionalReactiveProgrammingForIoT solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements for FunctionalReactiveProgrammingForIoT (P1)
2. Design Framework Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Core Functionalities (P3) -- (depends on: Design Framework Architecture)
4. Create User Interface Design (P4) -- (depends on: Develop Core Functionalities)
5. Implement User Interface (P5) -- (depends on: Create User Interface Design)
6. Test Framework Functionality (P1) -- (depends on: Develop Core Functionalities, Create User Interface Design)
7. Deploy IoT Framework to Production (P5) -- (depends on: Test Framework Functionality)
8. Integrate Security Measures (P2) -- (depends on: Develop Core Functionalities)
9. Prepare Detailed and Comprehensive Documentation (P4) -- (depends on: Integrate Security Measures)
10. Perform Code Audit and Optimization (P3) -- (depends on: Implement User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalReactiveProgrammingForIoT can deliver its core value proposition as described
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

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A framework for IoT devices that uses functional reactive programming to handle streams of sensor da.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
