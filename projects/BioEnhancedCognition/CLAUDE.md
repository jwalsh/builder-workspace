# BioEnhancedCognition

You are a coding agent working on BioEnhancedCognition -- A non-invasive neurostimulation device that enhances cognitive functions such as memory and focus.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BioEnhancedCognition embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop software components
- User interface: define project scope and requirements - revised
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: BioEnhancedCognition solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Software Components (P3) -- (depends on: Design System Architecture)
4. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
5. Conduct Security and Privacy Audits (P4) -- (depends on: Develop Software Components, Implement Data Storage and Management)
6. Develop Hardware Components (P3) -- (depends on: Design System Architecture)
7. Develop Testing and Validation Strategies (P3) -- (depends on: Develop Hardware Components, Develop Software Components)
8. Implement Continuous Integration and Deployment (P3) -- (depends on: Develop Software Components, Develop Testing and Validation Strategies)
9. Create User Documentation and Training Materials (P2) -- (depends on: Develop Hardware Components, Develop Software Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioEnhancedCognition can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A non-invasive neurostimulation device that enhances cognitive functions such as memory and focus..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
