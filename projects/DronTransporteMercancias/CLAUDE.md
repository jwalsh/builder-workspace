# DronTransporteMercancias

You are a coding agent working on DronTransporteMercancias -- Drones autónomos para la entrega de mercancías en zonas urbanas y rurales.

## Foundational Axiom

Existing approaches to drones autónomos para la entrega de mercancías en zonas urba fail because they optimize for the common case while ignoring structural constraints; DronTransporteMercancias makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop autonomous navigation software
- User interface: define project scope and requirements
- Data layer: implement data storage and management solutions

## Anti-Goals

- **General-purpose platform**: DronTransporteMercancias solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Dron Transport System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Drone Hardware Components (P3) -- (depends on: Design Dron Transport System Architecture)
4. Develop Autonomous Navigation Software (P3) -- (depends on: Design Dron Transport System Architecture)
5. Develop User Interface for Drone Management (P3) -- (depends on: Design Dron Transport System Architecture)
6. Implement Data Storage and Management Solutions (P4) -- (depends on: Design Dron Transport System Architecture)
7. Perform Unit and Integration Testing (P5) -- (depends on: Develop Drone Hardware Components, Develop Autonomous Navigation Software, Develop User Interface for Drone Management, Implement Data Storage and Management Solutions, Set Up DevOps and CI/CD)
8. Address Security Concerns (P5) -- (depends on: Develop Drone Hardware Components, Develop Autonomous Navigation Software, Develop User Interface for Drone Management, Implement Data Storage and Management Solutions)
9. Set Up DevOps and Continuous Integration/Continuous Deployment (CI/CD) (P4) -- (depends on: Design Dron Transport System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DronTransporteMercancias can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Drones autónomos para la entrega de mercancías en zonas urbanas y rurales..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
