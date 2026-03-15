# ContinuousAuthenticationSystem

You are a coding agent working on ContinuousAuthenticationSystem -- A system that continuously authenticates users based on behavioral biometrics and context, beyond initial login.

## Foundational Axiom

Security in system fails when it is bolted on after the fact; ContinuousAuthenticationSystem makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that continuously authenticates users based on behavioral biometrics and context, beyond in
- User interface: define system requirements - revised
- Data layer: implement biometric data collection

## Anti-Goals

- **General-purpose platform**: ContinuousAuthenticationSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements - Revised (P5)
2. Design System Architecture (P5) -- (depends on: Define System Requirements, Identify Security and Compliance Requirements)
3. Design User Interface for Continuous Authentication System - Revised (P3) -- (depends on: Define System Requirements, Define Authentication Mechanisms, Define User Roles and Permissions)
4. Write User Documentation (P4) -- (depends on: Define System Requirements, Design User Interface)
5. Implement Biometric Data Collection (P3) -- (depends on: Design System Architecture)
6. Implement Context Data Collection (P3) -- (depends on: Design System Architecture)
7. Design Authentication Model: Enhancements and Clarifications (P2) -- (depends on: Implement Biometric Data Collection, Implement Context Data Collection)
8. Implement Authentication Model (P2) -- (depends on: Design Authentication Model)
9. Implement User Interface (P3) -- (depends on: Design User Interface, Implement Authentication Model)
10. Design Database Schema for Continuous Authentication System (P3) -- (depends on: Design System Architecture)
11. Implement Database (P3) -- (depends on: Design Database Schema)
12. Set up Continuous Integration/Continuous Deployment (CI/CD) (P3)
13. Create Test Plan - Revised (P3) -- (depends on: Define System Requirements)
14. Implement Tests (P3) -- (depends on: Create Test Plan, Set up Continuous Integration/Continuous Deployment (CI/CD))
15. Implement Security Measures (P2) -- (depends on: Design System Architecture)
16. Perform System Integration Testing (P2) -- (depends on: Implement User Interface, Implement Authentication Model, Implement Database, Implement Security Measures)
17. Deploy to Production (P1) -- (depends on: Perform System Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ContinuousAuthenticationSystem can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that continuously authenticates users based on behavioral biometrics and context, beyond in.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
