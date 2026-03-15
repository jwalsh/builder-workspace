# BionicConstructionExoskeleton

You are a coding agent working on BionicConstructionExoskeleton -- A powered exoskeleton system for construction workers, enhancing strength and endurance while reducing the risk of injuries on construction sites.

## Foundational Axiom

Existing approaches to powered exoskeleton system fail because they optimize for the common case while ignoring structural constraints; BionicConstructionExoskeleton makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: software development
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: BionicConstructionExoskeleton solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Design and Architecture (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Hardware Development (P3) -- (depends on: Design and Architecture)
4. Software Development (P3) -- (depends on: Design and Architecture)
5. Integration and Testing (P4) -- (depends on: Hardware Development, Software Development)
6. Security and Compliance (P4) -- (depends on: Design and Architecture)
7. Documentation and Training (P5) -- (depends on: Integration and Testing, Security and Compliance)
8. Deployment and Support (P5) -- (depends on: Integration and Testing, Documentation and Training)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BionicConstructionExoskeleton can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A powered exoskeleton system for construction workers, enhancing strength and endurance while reduci.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to real estate professionals and property developers.
