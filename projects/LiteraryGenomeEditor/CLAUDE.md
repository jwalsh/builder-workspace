# LiteraryGenomeEditor

You are a coding agent working on LiteraryGenomeEditor -- A tool for authors to 'genetically modify' their stories, splicing in elements from different genres or styles to create unique literary hybrids.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; LiteraryGenomeEditor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop text processing and manipulation engine
- User interface: define project scope and requirements for literarygenomeeditor
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: LiteraryGenomeEditor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and requirements for LiteraryGenomeEditor (P5)
2. Design system architecture (P4) -- (depends on: Define project scope and requirements)
3. Implement security measures (P4) -- (depends on: Design system architecture)
4. Design user interface (P3) -- (depends on: Define project scope and requirements)
5. Set up database and data storage (P3) -- (depends on: Design system architecture)
6. Set up continuous integration and deployment (P3)
7. Develop text processing and manipulation engine (P2) -- (depends on: Design system architecture)
8. Implement user interface (P2) -- (depends on: Design user interface, Develop text processing and manipulation engine)
9. Write user documentation (P2) -- (depends on: Implement user interface)
10. Conduct testing and quality assurance (P2) -- (depends on: Implement user interface, Develop text processing and manipulation engine, Set up database and data storage, Implement security measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LiteraryGenomeEditor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A tool for authors to 'genetically modify' their stories, splicing in elements from different genres.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
