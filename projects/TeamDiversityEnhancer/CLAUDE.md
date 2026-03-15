# TeamDiversityEnhancer

You are a coding agent working on TeamDiversityEnhancer -- A tool that analyzes team composition and suggests ways to increase diversity and inclusion in team formation and project assignments.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; TeamDiversityEnhancer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements
- Data layer: create database schema

## Anti-Goals

- **General-purpose platform**: TeamDiversityEnhancer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements, Gather and Analyze Diversity Data Sources)
3. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
4. Create Database Schema (P3) -- (depends on: Design System Architecture)
5. Develop Backend Services (P3) -- (depends on: Design System Architecture, Create Database Schema)
6. Build User Interface (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Develop Backend Services, Build User Interface)
8. Develop Test Suite (P3) -- (depends on: Develop Backend Services, Build User Interface)
9. Write Documentation (P2) -- (depends on: Develop Backend Services, Build User Interface)
10. Conduct User Acceptance Testing (P2) -- (depends on: Develop Test Suite, Write Documentation)
11. Deploy and Monitor (P2) -- (depends on: Set up Continuous Integration and Deployment, Conduct User Acceptance Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeamDiversityEnhancer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A tool that analyzes team composition and suggests ways to increase diversity and inclusion in team .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
