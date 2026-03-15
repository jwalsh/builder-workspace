# GeneticOptimizationPlatform

You are a coding agent working on GeneticOptimizationPlatform -- A platform for analyzing personal genetic data and providing recommendations for optimizing health and performance.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; GeneticOptimizationPlatform embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: create frontend user interface design
- Data layer: implement data security measures

## Anti-Goals

- **General-purpose platform**: GeneticOptimizationPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Conduct Unit Testing (P5) -- (depends on: Backend Services Development, Frontend Development)
2. Integration Testing (P5) -- (depends on: Backend Services Development, Frontend Development)
3. Perform Code Reviews (P5) -- (depends on: Backend Services Development, Frontend Development)
4. Design Platform Architecture (P2) -- (depends on: Define Project Requirements)
5. Implement Data Security Measures (P4) -- (depends on: Design Platform Architecture)
6. Deploy GeneticOptimizationPlatform (P5) -- (depends on: Design Platform Architecture, Implement Data Security Measures)
7. Test in Staging Environment (P5) -- (depends on: Deploy GeneticOptimizationPlatform)
8. Prepare for Production Deployment (P5) -- (depends on: Test in Staging Environment)
9. Production Deployment (P5) -- (depends on: Prepare for Production Deployment)
10. Develop Backend Services (P4) -- (depends on: Design Platform Architecture)
11. Set Up Database Schema (P4) -- (depends on: Design Platform Architecture)
12. Create Frontend User Interface Design (P3) -- (depends on: Design Platform Architecture)
13. Define Comprehensive Project Requirements for GeneticOptimizationPlatform (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeneticOptimizationPlatform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for analyzing personal genetic data and providing recommendations for optimizing health a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
