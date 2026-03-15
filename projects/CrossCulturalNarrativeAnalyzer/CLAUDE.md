# CrossCulturalNarrativeAnalyzer

You are a coding agent working on CrossCulturalNarrativeAnalyzer -- A tool that analyzes literary works across cultures and languages, identifying common themes, unique cultural elements, and potential for cross-cultural adaptation.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; CrossCulturalNarrativeAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data ingestion and preprocessing
- User interface: define project scope and requirements - revision
- Data layer: develop data ingestion and preprocessing

## Anti-Goals

- **General-purpose platform**: CrossCulturalNarrativeAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISION (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements, Break down task into subtasks, Establish timeline and milestones, Choose open-source libraries and tools, Build cross-functional team, Implement iterative design process)
3. Develop Data Ingestion and Preprocessing (P3) -- (depends on: Design System Architecture)
4. Build User Interfaces (P3) -- (depends on: Design System Architecture)
5. Implement Analysis Engines (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossCulturalNarrativeAnalyzer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A tool that analyzes literary works across cultures and languages, identifying common themes, unique.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
