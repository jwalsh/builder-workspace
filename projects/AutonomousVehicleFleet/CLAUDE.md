# AutonomousVehicleFleet

You are a coding agent working on AutonomousVehicleFleet -- A fleet of fully autonomous vehicles optimized for urban transportation.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; AutonomousVehicleFleet guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A fleet of fully autonomous vehicles optimized for urban transportation.
- User interface: define comprehensive requirements for autonomous vehicle fleet

## Anti-Goals

- **General-purpose platform**: AutonomousVehicleFleet solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Comprehensive Requirements for Autonomous Vehicle Fleet (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Implement Security and Privacy Measures (P4) -- (depends on: Design System Architecture)
4. Develop Vehicle Control System (P3) -- (depends on: Design System Architecture)
5. Implement Route Planning and Optimization (P3) -- (depends on: Design System Architecture)
6. Build Fleet Management System (P3) -- (depends on: Design System Architecture)
7. Develop Testing and Validation Framework (P3) -- (depends on: Design System Architecture)
8. Develop User Interface and Mobile App (P2) -- (depends on: Design System Architecture)
9. Integrate with Urban Infrastructure (P2) -- (depends on: Design System Architecture)
10. PlanDeploymentandOperations:AutonomousVehicleFleet (P2) -- (depends on: DesignSystemArchitecture, DevelopVehicleControlandNavigationSystems, ImplementFleetManagementandOptimizationAlgorithms)
11. Create Documentation and Training Materials (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AutonomousVehicleFleet can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A fleet of fully autonomous vehicles optimized for urban transportation..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
