# LeadershipStyleAnalyzer

You are a coding agent working on LeadershipStyleAnalyzer -- An AI system that analyzes leadership behaviors and provides insights on effectiveness and areas for improvement.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; LeadershipStyleAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data collection and processing pipeline
- User interface: define project scope and requirements - revised
- Data layer: develop data collection and processing pipeline

## Anti-Goals

- **General-purpose platform**: LeadershipStyleAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Data Collection and Processing Pipeline (P3) -- (depends on: Design System Architecture)
4. Implement Leadership Analysis Model (P3) -- (depends on: Design System Architecture)
5. Design and Develop User Interface (P4) -- (depends on: Design System Architecture)
6. Plan and Execute System Deployment (P5) -- (depends on: Develop Data Collection and Processing Pipeline, Implement Leadership Analysis Model, Design and Develop User Interface)
7. Create User Documentation and Training Materials (P5) -- (depends on: Design and Develop User Interface)
8. Set up Testing and Quality Assurance (P4) -- (depends on: Design System Architecture)
9. Implement Security and Compliance Measures (P4) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LeadershipStyleAnalyzer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that analyzes leadership behaviors and provides insights on effectiveness and areas for.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
