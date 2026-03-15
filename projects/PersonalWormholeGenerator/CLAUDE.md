# PersonalWormholeGenerator

You are a coding agent working on PersonalWormholeGenerator -- A device capable of creating stable micro wormholes for instantaneous travel or object transportation across short distances.

## Foundational Axiom

Existing approaches to device capable of creating stable micro wormholes fail because they optimize for the common case while ignoring structural constraints; PersonalWormholeGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: write user manual and api documentation
- User interface: define project scope and requirements
- Data layer: create database schema for storing user data and wormhole information

## Anti-Goals

- **General-purpose platform**: PersonalWormholeGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Wormhole Generator Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface for User Interaction (P3) -- (depends on: Design Wormhole Generator Architecture)
4. Write User Manual and API Documentation (P5) -- (depends on: Develop Frontend Interface for User Interaction)
5. Implement Backend Logic for Wormhole Generation (P3) -- (depends on: Design Wormhole Generator Architecture)
6. Conduct Unit Tests for Each Component of the Device (P5) -- (depends on: Implement Frontend Interface for User Interaction, Implement Backend Logic for Wormhole Generation)
7. Implement DevOps Strategy for Building and Deploying the Device (P4) -- (depends on: Design Wormhole Generator Architecture)
8. Perform Security Audit on the Device (P4) -- (depends on: Implement Backend Logic for Wormhole Generation)
9. Create Database Schema for Storing User Data and Wormhole Information (P3) -- (depends on: Design Wormhole Generator Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalWormholeGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device capable of creating stable micro wormholes for instantaneous travel or object transportatio.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
