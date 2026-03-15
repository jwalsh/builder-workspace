# AIEcoSystemOrchestrator

You are a coding agent working on AIEcoSystemOrchestrator -- An AI system that manages a personal ecosystem of smart devices, robots, and virtual assistants in perfect harmony.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; AIEcoSystemOrchestrator captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that manages a personal ecosystem of smart devices, robots, and virtual assistants in p
- User interface: define project scope and requirements
- Data layer: design and implement scalable database schema for aiecosystemorchestrator

## Anti-Goals

- **General-purpose platform**: AIEcoSystemOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop Device Integration Framework (P3) -- (depends on: Design System Architecture)
4. Implement Virtual Assistant Integration (P3) -- (depends on: Design System Architecture)
5. Design User Interface and Experience for AIEcoSystemOrchestrator (P2) -- (depends on: Design System Architecture, Define User Roles and Permissions, Identify Supported Devices and Platforms)
6. Implement Security and Access Control - Revised (P2) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P2)
8. Develop Comprehensive Testing Strategy and Automation for AIEcoSystemOrchestrator (P2) -- (depends on: Design System Architecture)
9. Design and Implement Scalable Database Schema for AIEcoSystemOrchestrator (P2) -- (depends on: Design System Architecture)
10. Create Documentation and User Guides (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIEcoSystemOrchestrator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust
- MongoDB
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that manages a personal ecosystem of smart devices, robots, and virtual assistants in p.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
