# MultisensoryNarrativeCreator

You are a coding agent working on MultisensoryNarrativeCreator -- A platform for creating and experiencing stories that engage all senses, including touch, smell, and taste, for a fully immersive narrative experience.

## Foundational Axiom

Existing approaches to platform for creating and experiencing stories fail because they optimize for the common case while ignoring structural constraints; MultisensoryNarrativeCreator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope, requirements and identify key stakeholders - revised
- Data layer: set up database

## Anti-Goals

- **General-purpose platform**: MultisensoryNarrativeCreator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope, Requirements and Identify Key Stakeholders - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Frontend (P3) -- (depends on: Design System Architecture)
5. Develop Backend (P3) -- (depends on: Design System Architecture)
6. Set up Database (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Develop Frontend, Develop Backend)
8. Integrate Hardware and External Services (P2) -- (depends on: Develop Backend)
9. Conduct Testing and Quality Assurance (P3) -- (depends on: Develop Frontend, Develop Backend, Integrate Hardware and External Services)
10. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MultisensoryNarrativeCreator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for creating and experiencing stories that engage all senses, including touch, smell, and.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to iot engineers and embedded systems developers.
