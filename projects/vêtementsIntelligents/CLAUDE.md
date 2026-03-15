# vêtementsIntelligents

You are a coding agent working on vêtementsIntelligents -- Des vêtements intelligents capables de surveiller la température corporelle et les signes vitaux en temps réel.

## Foundational Axiom

Existing approaches to des vêtements intelligents capables de surveiller la tempéra fail because they optimize for the common case while ignoring structural constraints; vêtementsIntelligents makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop a real-time data processing algorithm
- User interface: design the user interface for displaying real-time data
- Data layer: design the user interface for displaying real-time data

## Anti-Goals

- **General-purpose platform**: vêtementsIntelligents solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design the smart fabric for temperature and vital signs monitoring (P1)
2. Perform initial security assessment of the design (P5) -- (depends on: Design the smart fabric for temperature and vital signs monitoring)
3. Design the user interface for displaying real-time data (P4) -- (depends on: Design the smart fabric for temperature and vital signs monitoring)
4. Create Technical Documentation for the Smart Clothes Project (P4) -- (depends on: Design the smart fabric for temperature and vital signs monitoring)
5. Develop a real-time data processing algorithm (P3) -- (depends on: Design the smart fabric for temperature and vital signs monitoring)
6. Define the hardware requirements for temperature and vital signs sensors (P2) -- (depends on: Design the smart fabric for temperature and vital signs monitoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: vêtementsIntelligents can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Des vêtements intelligents capables de surveiller la température corporelle et les signes vitaux en .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
