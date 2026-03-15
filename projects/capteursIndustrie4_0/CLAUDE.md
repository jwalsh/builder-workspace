# capteursIndustrie4_0

You are a coding agent working on capteursIndustrie4_0 -- Un réseau de capteurs IoT qui surveille en temps réel les processus industriels pour améliorer l'efficacité.

## Foundational Axiom

Existing approaches to un réseau de capteurs iot qui surveille en temps réel les pr fail because they optimize for the common case while ignoring structural constraints; capteursIndustrie4_0 makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: test sensor network and software
- User interface: design user interface
- Data layer: implement data analytics module

## Anti-Goals

- **General-purpose platform**: capteursIndustrie4_0 solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design IoT Sensor Network Architecture (P1)
2. Define Sensor Specifications (P2) -- (depends on: Design IoT Sensor Network Architecture)
3. Develop Real-Time Monitoring System (P3) -- (depends on: Design IoT Sensor Network Architecture, Define Sensor Specifications)
4. Implement Data Analytics Module (P4) -- (depends on: Develop Real-Time Monitoring System)
5. Design User Interface (P5) -- (depends on: Develop Real-Time Monitoring System, Implement Data Analytics Module)
6. Test Sensor Network and Software (P1) -- (depends on: Design IoT Sensor Network Architecture, Define Sensor Specifications, Develop Real-Time Monitoring System, Implement Data Analytics Module, Design User Interface)
7. Secure IoT Sensor Network and Software (P2) -- (depends on: Test Sensor Network and Software)
8. Document Project Design and Implementation (P5) -- (depends on: Test Sensor Network and Software, Secure IoT Sensor Network and Software)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: capteursIndustrie4_0 can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un réseau de capteurs IoT qui surveille en temps réel les processus industriels pour améliorer l'eff.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
