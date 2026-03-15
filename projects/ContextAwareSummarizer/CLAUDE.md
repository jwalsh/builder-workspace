# ContextAwareSummarizer

You are a coding agent working on ContextAwareSummarizer -- A summarization tool that takes into account the user's context (role, current projects, etc.) to provide relevant summaries.

## Foundational Axiom

Existing approaches to summarization tool fail because they optimize for the common case while ignoring structural constraints; ContextAwareSummarizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A summarization tool that takes into account the user's context (role, current projects, etc.) to pr
- User interface: define project scope and requirements - rfc review

## Anti-Goals

- **General-purpose platform**: ContextAwareSummarizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC Review (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop User Context Management (P3) -- (depends on: Design System Architecture)
5. Implement Summarization Algorithm (P3) -- (depends on: Design System Architecture)
6. Design User Interface (P3) -- (depends on: Define Project Scope and Requirements)
7. Set up CI/CD Pipeline (P3)
8. Implement User Interface (P2) -- (depends on: Design User Interface, Develop User Context Management, Implement Summarization Algorithm)
9. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Design User Interface)
10. Conduct Testing and Quality Assurance (P2) -- (depends on: Implement User Interface, Implement Security Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ContextAwareSummarizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A summarization tool that takes into account the user's context (role, current projects, etc.) to pr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
