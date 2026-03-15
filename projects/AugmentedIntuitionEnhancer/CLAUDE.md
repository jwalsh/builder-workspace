# AugmentedIntuitionEnhancer

You are a coding agent working on AugmentedIntuitionEnhancer -- A device that enhances intuition and pattern recognition by tapping into subconscious brain processes.

## Foundational Axiom

Existing approaches to device fail because they optimize for the common case while ignoring structural constraints; AugmentedIntuitionEnhancer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A device that enhances intuition and pattern recognition by tapping into subconscious brain processe
- User interface: project planning and requirements gathering
- Data layer: design and implement data storage and management

## Anti-Goals

- **General-purpose platform**: AugmentedIntuitionEnhancer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Develop Technical Specifications for AugmentedIntuitionEnhancer (P5) -- (depends on: Project Planning and Requirements Gathering, User Experience and Interface Design, Legal and Regulatory Compliance Review)
3. Develop Comprehensive Security and Privacy Measures (P5) -- (depends on: Develop Technical Specifications, Define Data Models and Flows)
4. Design User Interface and Experience (P3) -- (depends on: Develop Technical Specifications)
5. Design and Implement Data Storage and Management (P3) -- (depends on: Develop Technical Specifications)
6. Develop Brain-Computer Interface (P2) -- (depends on: Develop Technical Specifications)
7. Implement Pattern Recognition Algorithms (P2) -- (depends on: Develop Technical Specifications)
8. Integrate Components and Test (P2) -- (depends on: Design User Interface and Experience, Develop Brain-Computer Interface, Implement Pattern Recognition Algorithms, Design and Implement Data Storage and Management, Develop Security and Privacy Measures)
9. Develop Deployment and Maintenance Plan (P3) -- (depends on: Integrate Components and Test)
10. Write Documentation and User Guides (P3) -- (depends on: Integrate Components and Test)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AugmentedIntuitionEnhancer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that enhances intuition and pattern recognition by tapping into subconscious brain processe.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
