# BiosyntheticFactoryDesigner

You are a coding agent working on BiosyntheticFactoryDesigner -- Design artificial biological systems for the production of novel materials and compounds using synthetic biology principles.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BiosyntheticFactoryDesigner embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop genetic engineering tools
- User interface: define project scope and requirements - rfc review
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: BiosyntheticFactoryDesigner solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC Review (P1)
2. Design Biosynthetic Pathways (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Genetic Engineering Tools (P3) -- (depends on: Define Project Scope and Requirements)
4. Design User Interface (P3) -- (depends on: Define Project Scope and Requirements)
5. Implement Data Storage and Management (P3) -- (depends on: Define Project Scope and Requirements)
6. Create Documentation and Training Materials (P5) -- (depends on: Design Biosynthetic Pathways, Develop Genetic Engineering Tools, Design User Interface, Implement Data Storage and Management)
7. Develop Testing and Validation Framework (P4) -- (depends on: Design Biosynthetic Pathways, Develop Genetic Engineering Tools)
8. Implement Security and Access Controls (P4) -- (depends on: Define Project Scope and Requirements)
9. Plan Deployment and Integration (P4) -- (depends on: Design Biosynthetic Pathways, Develop Genetic Engineering Tools, Design User Interface, Implement Data Storage and Management)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BiosyntheticFactoryDesigner can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Design artificial biological systems for the production of novel materials and compounds using synth.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
