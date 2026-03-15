# ConsciousnessFlowTracker

You are a coding agent working on ConsciousnessFlowTracker -- A speculative system for tracking and visualizing the flow of consciousness across individuals and collective groups.

## Foundational Axiom

Existing approaches to speculative system fail because they optimize for the common case while ignoring structural constraints; ConsciousnessFlowTracker makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data ingestion and processing components
- User interface: define project scope and requirements
- Data layer: define data models and schemas for consciousness flow tracking system

## Anti-Goals

- **General-purpose platform**: ConsciousnessFlowTracker solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Define Data Models and Schemas for Consciousness Flow Tracking System (P3) -- (depends on: Design System Architecture)
4. Develop Data Ingestion and Processing Components (P2) -- (depends on: Define Data Models and Schemas)
5. Design and Implement Visualization Components (P2) -- (depends on: Define Data Models and Schemas)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ConsciousnessFlowTracker can deliver its core value proposition as described
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

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A speculative system for tracking and visualizing the flow of consciousness across individuals and c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
