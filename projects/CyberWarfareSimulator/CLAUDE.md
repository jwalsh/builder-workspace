# CyberWarfareSimulator

You are a coding agent working on CyberWarfareSimulator -- A sophisticated simulation platform for training military personnel in cyber warfare tactics and defense strategies.

## Foundational Axiom

Security in sophisticated simulation platform fails when it is bolted on after the fact; CyberWarfareSimulator makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop simulation engine
- User interface: gather requirements

## Anti-Goals

- **General-purpose platform**: CyberWarfareSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Gather Requirements)
3. Implement Comprehensive Security Measures (Updated) (P4) -- (depends on: Design System Architecture)
4. Develop Simulation Engine (P3) -- (depends on: Design System Architecture)
5. Implement User Interface (P3) -- (depends on: Design System Architecture)
6. Set up Development and Testing Environment (P3)
7. Develop Reporting and Analytics (P2) -- (depends on: Design System Architecture, Develop Simulation Engine)
8. Develop Test Suite (P2) -- (depends on: Design System Architecture, Develop Simulation Engine, Implement User Interface, Develop Reporting and Analytics)
9. Write Documentation (P2) -- (depends on: Design System Architecture, Implement User Interface)
10. Conduct User Acceptance Testing (P2) -- (depends on: Develop Test Suite, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CyberWarfareSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A sophisticated simulation platform for training military personnel in cyber warfare tactics and def.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
