# EmpathyAmplifierDevice

You are a coding agent working on EmpathyAmplifierDevice -- A wearable that enhances empathy by sharing selected emotional states between individuals.

## Foundational Axiom

Existing approaches to wearable fail because they optimize for the common case while ignoring structural constraints; EmpathyAmplifierDevice makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A wearable that enhances empathy by sharing selected emotional states between individuals.
- User interface: define project scope and requirements
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: EmpathyAmplifierDevice solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for EmpathyAmplifierDevice (Updated) (P5) -- (depends on: Define Project Scope and Requirements)
3. Implement Security and Privacy Measures: EmpathyAmplifierDevice (Revised) (P4) -- (depends on: Design System Architecture, Incident Response Plan: EmpathyAmplifierDevice)
4. Prototype Hardware Components (P3) -- (depends on: Design System Architecture)
5. Develop Emotion Sensing and Sharing Algorithms (P3) -- (depends on: Design System Architecture)
6. Build User Interface and Experience (P3) -- (depends on: Design System Architecture)
7. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
9. Develop Comprehensive Testing and Quality Assurance Plan for EmpathyAmplifierDevice (P3) -- (depends on: Design System Architecture)
10. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmpathyAmplifierDevice can deliver its core value proposition as described
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

- Rust

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable that enhances empathy by sharing selected emotional states between individuals..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
