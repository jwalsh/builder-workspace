# ThreatSimulationEngine

You are a coding agent working on ThreatSimulationEngine -- A system that simulates various cyber threats in a controlled environment for testing and improving defense mechanisms.

## Foundational Axiom

Security in system fails when it is bolted on after the fact; ThreatSimulationEngine makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop threat simulation engine
- User interface: define project scope and requirements - v2
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: ThreatSimulationEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - v2 (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Threat Simulation Engine (P3) -- (depends on: Design System Architecture)
5. Implement Testing Environment (P3) -- (depends on: Design System Architecture)
6. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)
7. Create Test Plans and Test Cases (P3) -- (depends on: Define Project Scope and Requirements)
8. Develop User Interface (P2) -- (depends on: Design System Architecture)
9. Implement Reporting and Analytics (P2) -- (depends on: Develop Threat Simulation Engine)
10. Conduct System Testing (P2) -- (depends on: Create Test Plans and Test Cases, Develop Threat Simulation Engine, Implement Testing Environment, Develop User Interface, Implement Reporting and Analytics, Set up Database and Data Storage, Implement Security Measures)
11. Prepare Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
12. Deploy and Release (P1) -- (depends on: Conduct System Testing, Prepare Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThreatSimulationEngine can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that simulates various cyber threats in a controlled environment for testing and improving .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
