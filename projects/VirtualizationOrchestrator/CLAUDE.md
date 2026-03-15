# VirtualizationOrchestrator

You are a coding agent working on VirtualizationOrchestrator -- A platform for managing and orchestrating virtualized resources across hybrid cloud environments.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; VirtualizationOrchestrator models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend services for the platform
- User interface: define project requirements and use cases
- Data layer: implement database schema and models

## Anti-Goals

- **General-purpose platform**: VirtualizationOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project requirements and use cases (P1)
2. Design the architecture for the platform (P2) -- (depends on: Define project requirements and use cases)
3. Implement database schema and models (P5) -- (depends on: Design the architecture for the platform)
4. Secure the VirtualizationOrchestrator platform (P5) -- (depends on: Implement backend services)
5. Develop the backend services for the platform (P4) -- (depends on: Design the architecture for the platform)
6. Write functional and unit tests (P4) -- (depends on: Implement backend services, Implement database schema and models)
7. Create a user interface design for the platform (P3) -- (depends on: Define project requirements and use cases)
8. Integrate DevOps practices and tools (P2) -- (depends on: Design the architecture for the platform)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualizationOrchestrator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for managing and orchestrating virtualized resources across hybrid cloud environments..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
