# VirtualMusicCollaborationSpace

You are a coding agent working on VirtualMusicCollaborationSpace -- A platform for musicians to collaborate and create music together in a virtual environment.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; VirtualMusicCollaborationSpace makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: build backend services
- User interface: define project requirements
- Data layer: set up database schema

## Anti-Goals

- **General-purpose platform**: VirtualMusicCollaborationSpace solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Architecture of the Platform (P2) -- (depends on: Define Project Requirements)
3. Set Up Database Schema (P5) -- (depends on: Design Architecture of the Platform)
4. Develop Frontend Interface (P3) -- (depends on: Design Architecture of the Platform)
5. Build Backend Services (P4) -- (depends on: Design Architecture of the Platform)
6. Implement DevOps Pipeline (P3) -- (depends on: Develop Frontend Interface, Build Backend Services, Set Up Database Schema)
7. Document the Platform (P5) -- (depends on: Develop Frontend Interface, Build Backend Services, Set Up Database Schema, Implement DevOps Pipeline)
8. Conduct Quality Assurance Tests (P4) -- (depends on: Develop Frontend Interface, Build Backend Services, Set Up Database Schema, Implement DevOps Pipeline)
9. Ensure Platform Security (P2) -- (depends on: Develop Frontend Interface, Build Backend Services, Set Up Database Schema)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualMusicCollaborationSpace can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for musicians to collaborate and create music together in a virtual environment..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and media producers.
