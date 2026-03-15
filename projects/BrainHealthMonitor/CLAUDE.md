# BrainHealthMonitor

You are a coding agent working on BrainHealthMonitor -- A comprehensive brain health monitoring system that tracks various neurological indicators over time.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; BrainHealthMonitor embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements - revised
- Data layer: design data storage and management

## Anti-Goals

- **General-purpose platform**: BrainHealthMonitor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Design Data Storage and Management (P4) -- (depends on: Design System Architecture)
4. Establish Security and Compliance (P4) -- (depends on: Design System Architecture)
5. Develop User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Backend Services (P3) -- (depends on: Design System Architecture, Design Data Storage and Management)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Implement Backend Services, Develop User Interface)
8. Conduct Testing and Quality Assurance (P3) -- (depends on: Implement Backend Services, Develop User Interface)
9. Create Documentation and User Guides (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainHealthMonitor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A comprehensive brain health monitoring system that tracks various neurological indicators over time.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
