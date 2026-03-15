# simulateurRisquesCyber

You are a coding agent working on simulateurRisquesCyber -- Un simulateur qui évalue les risques liés à la cybersécurité en temps réel, optimisant les stratégies de défense.

## Foundational Axiom

Security in un simulateur qui évalue les risques liés à la cybersécurité fails when it is bolted on after the fact; simulateurRisquesCyber makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un simulateur qui évalue les risques liés à la cybersécurité en temps réel, optimisant les stratégie
- User interface: define project scope and requirements
- Data layer: implement database for storing and analyzing data

## Anti-Goals

- **General-purpose platform**: simulateurRisquesCyber solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Real-time Risk Evaluation System (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Database for Storing and Analyzing Data (P5) -- (depends on: Design Real-time Risk Evaluation System)
4. Create User Interface for the Simulator (P4) -- (depends on: Define Project Scope and Requirements)
5. Develop Optimization Algorithm for Defense Strategies (P3) -- (depends on: Design Real-time Risk Evaluation System)
6. Set Up Continuous Integration and Deployment Pipeline (P2) -- (depends on: Create User Interface for the Simulator, Implement Database for Storing and Analyzing Data)
7. Conduct Security Audit of the System (P1) -- (depends on: Design Real-time Risk Evaluation System, Create User Interface for the Simulator)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: simulateurRisquesCyber can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un simulateur qui évalue les risques liés à la cybersécurité en temps réel, optimisant les stratégie.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
