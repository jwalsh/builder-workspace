# VirtualCourtroom

You are a coding agent working on VirtualCourtroom -- A platform for conducting virtual court proceedings, including evidence presentation and witness testimonies.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; VirtualCourtroom makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend logic
- User interface: define project scope and requirements (revised)
- Data layer: develop the database structure

## Anti-Goals

- **General-purpose platform**: VirtualCourtroom solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Develop the Database Structure (P3) -- (depends on: Define Project Scope and Requirements)
3. Design the User Interface (UI) (P2) -- (depends on: Define Project Scope and Requirements)
4. Develop the Backend Logic (P2) -- (depends on: Define Project Scope and Requirements)
5. Integrate Frontend with Backend (P4) -- (depends on: Design the User Interface (UI), Develop the Backend Logic)
6. Test the Virtual Courtroom Platform (P5) -- (depends on: Develop the Database Structure, Integrate Frontend with Backend)
7. Write Documentation for the Virtual Courtroom Platform (P5) -- (depends on: Test the Virtual Courtroom Platform)
8. Secure the Virtual Courtroom Platform (P1) -- (depends on: Define Project Scope and Requirements)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualCourtroom can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for conducting virtual court proceedings, including evidence presentation and witness tes.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
