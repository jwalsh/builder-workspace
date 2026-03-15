# PersonalFusionReactor

You are a coding agent working on PersonalFusionReactor -- A compact fusion reactor providing unlimited clean energy for homes and personal vehicles.

## Foundational Axiom

Existing approaches to compact fusion reactor providing unlimited clean energy fail because they optimize for the common case while ignoring structural constraints; PersonalFusionReactor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: mechanical and electrical engineering design
- User interface: user interface and control system design
- Data layer: power conditioning and storage system design

## Anti-Goals

- **General-purpose platform**: PersonalFusionReactor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Concept Development (P1)
2. Fusion Reactor Physics Modeling (P2) -- (depends on: Concept Development)
3. Reactor Materials Research (P3)
4. System Architecture Design for Compact Fusion Reactor (P2) -- (depends on: Fusion Reactor Physics Modeling, Reactor Materials Research)
5. Safety and Regulatory Compliance (P5) -- (depends on: System Architecture Design)
6. User Interface and Control System Design (P5) -- (depends on: System Architecture Design)
7. Mechanical and Electrical Engineering Design (P4) -- (depends on: System Architecture Design)
8. Power Conditioning and Storage System Design (P3) -- (depends on: System Architecture Design)
9. Prototype Construction (P4) -- (depends on: System Architecture Design, Power Conditioning and Storage System Design, Mechanical and Electrical Engineering Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalFusionReactor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A compact fusion reactor providing unlimited clean energy for homes and personal vehicles..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
