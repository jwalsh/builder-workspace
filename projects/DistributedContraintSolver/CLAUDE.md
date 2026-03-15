# DistributedContraintSolver

You are a coding agent working on DistributedContraintSolver -- A system for solving large-scale constraint satisfaction problems across a distributed cluster, with applications in logistics and scheduling.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; DistributedContraintSolver makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop api for problem submission
- User interface: design user interface
- Data layer: develop data transfer mechanisms

## Anti-Goals

- **General-purpose platform**: DistributedContraintSolver solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Cluster Communication Protocol (P2) -- (depends on: Define System Architecture)
3. Implement Node Initialization Module (P3) -- (depends on: Design Cluster Communication Protocol)
4. Develop Data Transfer Mechanisms (P4) -- (depends on: Implement Node Initialization Module)
5. Create Constraint Solver Algorithms (P5) -- (depends on: Develop Data Transfer Mechanisms)
6. Design User Interface (P2) -- (depends on: Define System Architecture)
7. Develop API for Problem Submission (P3) -- (depends on: Design User Interface)
8. Write Test Cases for Constraint Solver Algorithms (P4) -- (depends on: Create Constraint Solver Algorithms)
9. Perform System Testing (P5) -- (depends on: Develop API for Problem Submission, Write Test Cases for Constraint Solver Algorithms)
10. Write User Documentation (P1) -- (depends on: Design User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedContraintSolver can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for solving large-scale constraint satisfaction problems across a distributed cluster, with.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
