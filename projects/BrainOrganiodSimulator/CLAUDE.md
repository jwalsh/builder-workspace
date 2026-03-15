# BrainOrganiodSimulator

You are a coding agent working on BrainOrganiodSimulator -- Create a computational model to simulate the development and behavior of brain organoids for neuroscience research.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; BrainOrganiodSimulator models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Create a computational model to simulate the development and behavior of brain organoids for neurosc
- User interface: define project scope and requirements
- Data layer: implement data management

## Anti-Goals

- **General-purpose platform**: BrainOrganiodSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. DesignSystemArchitecture (P5) -- (depends on: DefineProjectScopeandRequirements)
3. Develop Computational Models (P3) -- (depends on: Design System Architecture)
4. Build User Interface (P3) -- (depends on: Design System Architecture)
5. Implement Data Management (P3) -- (depends on: Design System Architecture)
6. Develop Testing Framework (P2) -- (depends on: Develop Computational Models, Build User Interface, Implement Data Management)
7. Implement Security Measures (P2) -- (depends on: Design System Architecture)
8. Set up Deployment Infrastructure (P2) -- (depends on: Develop Computational Models, Build User Interface, Implement Data Management)
9. Create Documentation (P1) -- (depends on: Develop Computational Models, Build User Interface, Implement Data Management)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainOrganiodSimulator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Create a computational model to simulate the development and behavior of brain organoids for neurosc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
