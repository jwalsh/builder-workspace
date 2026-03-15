# SyncPerformanceOptimizer

You are a coding agent working on SyncPerformanceOptimizer -- A tool that analyzes and optimizes the performance of data synchronization processes, reducing latency and improving efficiency.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; SyncPerformanceOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A tool that analyzes and optimizes the performance of data synchronization processes, reducing laten
- User interface: gather requirements

## Anti-Goals

- **General-purpose platform**: SyncPerformanceOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture for SyncPerformanceOptimizer (P4) -- (depends on: Gather Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Performance Analysis Module (P3) -- (depends on: Design System Architecture)
5. Develop Optimization Module (P3) -- (depends on: Design System Architecture)
6. Implement User Interface (P2) -- (depends on: Design System Architecture)
7. Set up Testing Infrastructure (P3) -- (depends on: Develop Performance Analysis Module, Develop Optimization Module, Implement User Interface)
8. Prepare Deployment Strategy (P2) -- (depends on: Set up Testing Infrastructure, Implement Security Measures)
9. Write Documentation (P2) -- (depends on: Implement User Interface, Prepare Deployment Strategy)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SyncPerformanceOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that analyzes and optimizes the performance of data synchronization processes, reducing laten.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
