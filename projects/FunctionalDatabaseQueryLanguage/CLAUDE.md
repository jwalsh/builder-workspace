# FunctionalDatabaseQueryLanguage

You are a coding agent working on FunctionalDatabaseQueryLanguage -- A new database query language that embraces functional programming concepts, making complex queries more composable and reasoning about data transformations easier.

## Foundational Axiom

Existing approaches to new database query language fail because they optimize for the common case while ignoring structural constraints; FunctionalDatabaseQueryLanguage makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A new database query language that embraces functional programming concepts, making complex queries 
- User interface: define functional database query language requirements
- Data layer: define functional database query language requirements

## Anti-Goals

- **General-purpose platform**: FunctionalDatabaseQueryLanguage solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Functional Database Query Language Requirements (P1)
2. Design Functional Database Query Language Syntax (P2) -- (depends on: Define Functional Database Query Language Requirements)
3. Implement Core Features of Functional Database Query Language (P3) -- (depends on: Design Functional Database Query Language Syntax)
4. Optimize Performance of Functional Database Query Language (P5) -- (depends on: Implement Core Features of Functional Database Query Language)
5. Create a Test Suite for Functional Database Query Language (P4) -- (depends on: Implement Core Features of Functional Database Query Language)
6. Integrate Functional Database Query Language into Existing Database Systems (P3) -- (depends on: Implement Core Features of Functional Database Query Language, Create a Test Suite for Functional Database Query Language)
7. Document Functional Database Query Language Design and Implementation (P2) -- (depends on: Implement Core Features of Functional Database Query Language)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalDatabaseQueryLanguage can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A new database query language that embraces functional programming concepts, making complex queries .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
