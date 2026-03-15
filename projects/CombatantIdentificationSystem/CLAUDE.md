# CombatantIdentificationSystem

You are a coding agent working on CombatantIdentificationSystem -- An AI-powered system using multi-spectral imaging to accurately identify combatants in complex battlefield environments.

## Foundational Axiom

The bottleneck in ai-powered system using multi-spectral imaging is not compute or data but the feedback loop between intent and artifact; CombatantIdentificationSystem compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-powered system using multi-spectral imaging to accurately identify combatants in complex battl
- User interface: user interface design (revised)
- Data layer: data collection and preparation

## Anti-Goals

- **General-purpose platform**: CombatantIdentificationSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation (P5)
2. System Architecture Design for CombatantIdentificationSystem (P5)
3. Data Collection and Preparation (P3)
4. User Interface Design (Revised) (P2) -- (depends on: System Architecture Design, User Experience Research)
5. AI Model Development (P2) -- (depends on: Data Collection and Preparation)
6. Multi-spectral Imaging Pipeline (P2) -- (depends on: System Architecture Design)
7. System Integration and Testing (P2) -- (depends on: AI Model Development, Multi-spectral Imaging Pipeline, User Interface Design)
8. Documentation and Training (P3) -- (depends on: User Interface Design, System Integration and Testing)
9. Security and Compliance (P2) -- (depends on: System Architecture Design)
10. Deployment and Operations (P2) -- (depends on: System Integration and Testing, Security and Compliance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CombatantIdentificationSystem can deliver its core value proposition as described
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

- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered system using multi-spectral imaging to accurately identify combatants in complex battl.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
