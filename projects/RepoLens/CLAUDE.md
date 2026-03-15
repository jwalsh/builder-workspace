# RepoLens

You are a coding agent working on RepoLens -- A utility for packaging, analyzing, and processing project repositories with integration capabilities for various Language Models (LLMs). The tool aims to provide a flexible, standardized approach to repository analysis and LLM-assisted development workflows.

## Foundational Axiom

Existing approaches to utility fail because they optimize for the common case while ignoring structural constraints; RepoLens makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A utility for packaging, analyzing, and processing project repositories with integration capabilitie
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: RepoLens solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Implement Core Functionality (P3) -- (depends on: Design System Architecture)
4. Build User Interface (P3) -- (depends on: Design System Architecture)
5. Develop Test Suite (P3) -- (depends on: Implement Core Functionality, Build User Interface)
6. Implement Security Measures (P2) -- (depends on: Implement Core Functionality, Build User Interface)
7. Set up Continuous Integration and Deployment (P2) -- (depends on: Implement Core Functionality, Build User Interface)
8. Write Documentation (P2) -- (depends on: Implement Core Functionality, Build User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RepoLens can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A utility for packaging, analyzing, and processing project repositories with integration capabilitie.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
