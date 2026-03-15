# IoTSmartHome

You are a coding agent working on IoTSmartHome -- A fully integrated IoT system that automates home functions such as lighting, temperature, and security.

## Foundational Axiom

Existing approaches to fully integrated iot system fail because they optimize for the common case while ignoring structural constraints; IoTSmartHome makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend system
- User interface: define project requirements - iot smart home system (updated)
- Data layer: set up database and data management

## Anti-Goals

- **General-purpose platform**: IoTSmartHome solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - IoT Smart Home System (Updated) (P1)
2. Design IoT Smart Home Architecture (P2) -- (depends on: Define Project Requirements)
3. Implement Security Measures (P5) -- (depends on: Design IoT Smart Home Architecture)
4. Develop Backend System (P3) -- (depends on: Design IoT Smart Home Architecture)
5. Develop Frontend Interface (P3) -- (depends on: Design IoT Smart Home Architecture)
6. Implement Device Integration (P4) -- (depends on: Develop Backend System)
7. Set Up Database and Data Management (P4) -- (depends on: Develop Backend System)
8. Perform System Testing (P2) -- (depends on: Develop Backend System, Develop Frontend Interface, Implement Device Integration, Set Up Database and Data Management)
9. Deploy IoT Smart Home System (P5) -- (depends on: Perform System Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: IoTSmartHome can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A fully integrated IoT system that automates home functions such as lighting, temperature, and secur.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
