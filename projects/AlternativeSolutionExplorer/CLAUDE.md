# AlternativeSolutionExplorer

You are a coding agent working on AlternativeSolutionExplorer -- A system that generates and explains alternative solutions to coding problems, broadening users' problem-solving perspectives.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; AlternativeSolutionExplorer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that generates and explains alternative solutions to coding problems, broadening users' pro
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: AlternativeSolutionExplorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design (P3) -- (depends on: Requirements Gathering and Analysis)
3. Solution Generation Module (P4) -- (depends on: System Architecture Design)
4. Solution Explanation Module (P4) -- (depends on: System Architecture Design)
5. User Interface Development (P4) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
7. Integration and Testing (P4) -- (depends on: Solution Generation Module, Solution Explanation Module, User Interface Development, Database Design and Implementation)
8. Deployment and DevOps (P4) -- (depends on: Integration and Testing)
9. Security and Compliance (P3) -- (depends on: System Architecture Design)
10. Documentation and User Support (P3) -- (depends on: Integration and Testing)
11. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AlternativeSolutionExplorer can deliver its core value proposition as described
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

- TypeScript/JavaScript
- MongoDB
- Redis
- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that generates and explains alternative solutions to coding problems, broadening users' pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
