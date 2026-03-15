# TelecomOptimizer

You are a coding agent working on TelecomOptimizer -- Optimize control algorithms for load balancing, mobility management, multi-connection control, quality of experience management, and network energy saving in telecom networks.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; TelecomOptimizer captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Optimize control algorithms for load balancing, mobility management, multi-connection control, quali
- User interface: gather and prioritize requirements for telecomoptimizer project

## Anti-Goals

- **General-purpose platform**: TelecomOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather and Prioritize Requirements for TelecomOptimizer Project (P5)
2. Design System Architecture (P4) -- (depends on: Gather Requirements)
3. Implement Load Balancing Module (P3) -- (depends on: Design System Architecture)
4. Implement Mobility Management Module (P3) -- (depends on: Design System Architecture)
5. Implement Multi-Connection Control Module (P3) -- (depends on: Design System Architecture)
6. Implement Quality of Experience Management Module (P3) -- (depends on: Design System Architecture)
7. Implement Network Energy Saving Module (P3) -- (depends on: Design System Architecture)
8. Set up CI/CD Pipeline (P2) -- (depends on: Design System Architecture)
9. Implement Testing Framework (P2) -- (depends on: Design System Architecture)
10. Conduct Security Audit (P2) -- (depends on: Implement Load Balancing Module, Implement Mobility Management Module, Implement Multi-Connection Control Module, Implement Quality of Experience Management Module, Implement Network Energy Saving Module)
11. Write Documentation (P1) -- (depends on: Implement Load Balancing Module, Implement Mobility Management Module, Implement Multi-Connection Control Module, Implement Quality of Experience Management Module, Implement Network Energy Saving Module)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TelecomOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Optimize control algorithms for load balancing, mobility management, multi-connection control, quali.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
