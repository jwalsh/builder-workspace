# InclusivityAnalyzer

You are a coding agent working on InclusivityAnalyzer -- A tool that analyzes company communications and decisions to ensure inclusivity and diversity in the workplace.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; InclusivityAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design system architecture (revised) - including microservices approach for improved scalability and modularity
- User interface: define project scope and requirements (revised)
- Data layer: define data model and storage - inclusivityanalyzer (updated)

## Anti-Goals

- **General-purpose platform**: InclusivityAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (Revised) - Including Microservices Approach for Improved Scalability and Modularity (P5) -- (depends on: Define Project Scope and Requirements, Conduct Market Research and Competitor Analysis, Determine Accessibility Requirements)
3. Define Data Model and Storage - InclusivityAnalyzer (Updated) (P4) -- (depends on: Design System Architecture)
4. Develop Analysis Algorithms (P3) -- (depends on: Design System Architecture, Define Data Model and Storage)
5. Build User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Data Integration (P3) -- (depends on: Define Data Model and Storage)
7. Implement Security and Access Controls (Updated) (P3) -- (depends on: Design System Architecture)
8. Set up CI/CD Pipeline (P2)
9. Create Test Suite (P2) -- (depends on: Develop Analysis Algorithms, Build User Interface, Implement Data Integration)
10. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InclusivityAnalyzer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A tool that analyzes company communications and decisions to ensure inclusivity and diversity in the.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
