# CognitiveWorkloadOptimizer

You are a coding agent working on CognitiveWorkloadOptimizer -- A system that monitors cognitive load in real-time and adjusts work environments to optimize productivity.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; CognitiveWorkloadOptimizer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that monitors cognitive load in real-time and adjusts work environments to optimize product
- User interface: define project scope and requirements (updated)
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: CognitiveWorkloadOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Updated) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Cognitive Load Monitoring Module (P3) -- (depends on: Design System Architecture)
4. Develop Work Environment Adjustment Module (P3) -- (depends on: Design System Architecture)
5. Design and Implement User Interface (P3) -- (depends on: Design System Architecture)
6. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
7. Implement Security and Access Control (P3) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
9. Develop Test Suite and Quality Assurance Plan (P2) -- (depends on: Design System Architecture)
10. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CognitiveWorkloadOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that monitors cognitive load in real-time and adjusts work environments to optimize product.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
