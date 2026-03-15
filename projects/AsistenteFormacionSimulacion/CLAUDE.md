# AsistenteFormacionSimulacion

You are a coding agent working on AsistenteFormacionSimulacion -- Un asistente que crea simulaciones interactivas para formación en tiempo real a través de realidad virtual.

## Foundational Axiom

Existing approaches to un asistente que crea simulaciones interactivas para formaci fail because they optimize for the common case while ignoring structural constraints; AsistenteFormacionSimulacion makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop virtual reality simulation engine
- User interface: define project scope and requirements - updated

## Anti-Goals

- **General-purpose platform**: AsistenteFormacionSimulacion solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Updated (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Virtual Reality Simulation Engine (P3) -- (depends on: Design System Architecture)
4. Develop Training Content Management System (P3) -- (depends on: Design System Architecture)
5. Implement Real-Time Interaction and Communication (P3) -- (depends on: Design System Architecture)
6. Design User Interface and Experience (Revised & Prioritized) (P2) -- (depends on: Define Project Scope and Requirements, Establish Design Guidelines and Branding, Clarify VR Performance Considerations, Identify Unique Design Challenges for VR, Feedback Mechanisms, Interaction Design, Error Handling Strategies)
7. Implement Security and Access Control (P2) -- (depends on: Design System Architecture)
8. Set up Development and Testing Environment (P2)
9. Develop Test Suite and Quality Assurance Plan (P2) -- (depends on: Define Project Scope and Requirements)
10. Write Technical Documentation (P1) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AsistenteFormacionSimulacion can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un asistente que crea simulaciones interactivas para formación en tiempo real a través de realidad v.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
