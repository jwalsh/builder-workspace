# ImmutableDataStructureLibrary

You are a coding agent working on ImmutableDataStructureLibrary -- A comprehensive library of persistent, immutable data structures optimized for functional programming paradigms.

## Foundational Axiom

Existing approaches to comprehensive library of persistent, immutable data structures optimized fail because they optimize for the common case while ignoring structural constraints; ImmutableDataStructureLibrary makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A comprehensive library of persistent, immutable data structures optimized for functional programmin
- User interface: requirements gathering & analysis
- Data layer: design immutable data structure library architecture

## Anti-Goals

- **General-purpose platform**: ImmutableDataStructureLibrary solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation Meeting (P1)
2. Requirements Gathering & Analysis (P2) -- (depends on: Project Initiation Meeting)
3. Design Immutable Data Structure Library Architecture (P3) -- (depends on: Requirements Gathering & Analysis)
4. Implement Persistent Immutable Data Structures (P4) -- (depends on: Design Immutable Data Structure Library Architecture)
5. Perform Code Review & Quality Assurance Testing (P5) -- (depends on: Implement Persistent Immutable Data Structures)
6. Optimize Data Structure Implementations (if necessary) (P4) -- (depends on: Perform Code Review & Quality Assurance Testing)
7. Document the Immutable Data Structure Library (P3) -- (depends on: Optimize Data Structure Implementations (if necessary))
8. Prepare Library for Public Release (P2) -- (depends on: Document the Immutable Data Structure Library)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ImmutableDataStructureLibrary can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive library of persistent, immutable data structures optimized for functional programmin.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
