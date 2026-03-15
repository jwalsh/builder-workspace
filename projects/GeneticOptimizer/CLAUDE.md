# GeneticOptimizer

You are a coding agent working on GeneticOptimizer -- A home genetics lab for analyzing and optimizing personal genetics, from disease prevention to enhancing desirable traits.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; GeneticOptimizer embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project requirements
- Data layer: set up database schema

## Anti-Goals

- **General-purpose platform**: GeneticOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Overall System Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop User Interface (Frontend) (P3) -- (depends on: Design Overall System Architecture)
4. Implement Backend Services (P3) -- (depends on: Design Overall System Architecture)
5. Integrate Frontend with Backend Services (P5) -- (depends on: Develop User Interface, Implement Backend Services)
6. Conduct Security Audit (P5) -- (depends on: Develop User Interface, Implement Backend Services, Integrate Frontend with Backend Services)
7. Perform Unit Tests and Debug (P4) -- (depends on: Develop User Interface, Implement Backend Services, Integrate Frontend with Backend Services)
8. Deploy GeneticOptimizer (P5) -- (depends on: Perform Unit Tests and Debug)
9. Set Up Database Schema (P4) -- (depends on: Design Overall System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeneticOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A home genetics lab for analyzing and optimizing personal genetics, from disease prevention to enhan.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
