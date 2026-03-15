# SmartCityOrchestrator

You are a coding agent working on SmartCityOrchestrator -- Integrate various urban systems including traffic management, waste collection, and public safety using IoT devices and centralized data analytics.

## Foundational Axiom

Existing approaches to integrate various urban systems including traffic management fail because they optimize for the common case while ignoring structural constraints; SmartCityOrchestrator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Integrate various urban systems including traffic management, waste collection, and public safety us
- User interface: user interface design for smartcityorchestrator
- Data layer: designofthecentralizeddataanalyticsplatformforsmartcityorchestrator

## Anti-Goals

- **General-purpose platform**: SmartCityOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation (P5)
2. System Architecture Design (P5) -- (depends on: Project Initiation, Requirements Gathering)
3. DesignoftheCentralizedDataAnalyticsPlatformforSmartCityOrchestrator (P5) -- (depends on: SystemArchitectureDesign, DataModelingandSchemaDesign)
4. IoT Device Integration: Update and Improvements Proposal - Revised (P4) -- (depends on: System Architecture Design)
5. Security and Compliance for SmartCityOrchestrator (P4) -- (depends on: System Architecture Design)
6. User Interface Design for SmartCityOrchestrator (P3) -- (depends on: System Architecture Design, Data Visualization Requirements, Accessibility Guidelines for Web Applications)
7. Infrastructure and Deployment Planning (P3) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartCityOrchestrator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Integrate various urban systems including traffic management, waste collection, and public safety us.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
