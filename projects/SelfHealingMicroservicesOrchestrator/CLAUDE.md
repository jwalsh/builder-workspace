# SelfHealingMicroservicesOrchestrator

You are a coding agent working on SelfHealingMicroservicesOrchestrator -- An orchestration system for microservices that automatically detects and recovers from failures, ensuring high availability.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; SelfHealingMicroservicesOrchestrator models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design monitoring and logging components for selfhealing microservices orchestrator
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: SelfHealingMicroservicesOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture - Revised (P5) -- (depends on: Define Project Scope and Requirements)
3. Design Failure Detection and Recovery Mechanisms (P4) -- (depends on: Design System Architecture)
4. Design Monitoring and Logging Components for SelfHealing Microservices Orchestrator (P3) -- (depends on: Design System Architecture, Design Monitoring and Alerting Strategy)
5. Design User Interface and API - Revised (P3) -- (depends on: Design System Architecture, Define Monitoring and Logging Requirements)
6. Review and Finalize System Design (P4) -- (depends on: Design System Architecture, Design Failure Detection and Recovery Mechanisms, Design Monitoring and Logging Components, Design User Interface and API)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SelfHealingMicroservicesOrchestrator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An orchestration system for microservices that automatically detects and recovers from failures, ens.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
