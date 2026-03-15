# PiezoelectricRoadway

You are a coding agent working on PiezoelectricRoadway -- A roadway system that generates electricity from the pressure and vibration of passing vehicles.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; PiezoelectricRoadway maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate hardware and software components

## Anti-Goals

- **General-purpose platform**: PiezoelectricRoadway solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Sensor System (P2) -- (depends on: Define System Architecture)
3. Develop Power Management System (P3) -- (depends on: Define System Architecture)
4. Integrate Hardware and Software Components (P3) -- (depends on: Design Sensor System, Develop Power Management System)
5. Conduct Security Audit (P5) -- (depends on: Integrate Hardware and Software Components)
6. Comprehensive Technical Documentation for Piezoelectric Roadway System (P4) -- (depends on: Define System Architecture)
7. Perform System Integration Tests (P4) -- (depends on: Integrate Hardware and Software Components)
8. Test Sensor Performance (P2) -- (depends on: Design Sensor System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PiezoelectricRoadway can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A roadway system that generates electricity from the pressure and vibration of passing vehicles..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
