# AICodeReviewer

You are a coding agent working on AICodeReviewer -- An AI-powered code review system that automatically analyzes pull requests, suggests improvements, and checks for potential bugs or security vulnerabilities.

## Foundational Axiom

The bottleneck in ai-powered code review system is not compute or data but the feedback loop between intent and artifact; AICodeReviewer compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop code analysis engine
- User interface: define project scope and requirements (revised)

## Anti-Goals

- **General-purpose platform**: AICodeReviewer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (Revised and Expanded) - RFC Review and Suggestions (P5) -- (depends on: Define Project Scope and Requirements, Assess Real-Time Analysis Feasibility)
3. Develop Code Analysis Engine (P3) -- (depends on: Design System Architecture)
4. Implement User Interface (P3) -- (depends on: Design System Architecture)
5. Implement Security and Compliance Checks (P3) -- (depends on: Develop Code Analysis Engine)
6. Develop Testing and Quality Assurance Strategy (P3) -- (depends on: Develop Code Analysis Engine, Implement User Interface)
7. Set up Continuous Integration and Deployment (P2) -- (depends on: Develop Code Analysis Engine, Implement User Interface)
8. Write Documentation and User Guides (P2) -- (depends on: Implement User Interface, Develop Testing and Quality Assurance Strategy)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AICodeReviewer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered code review system that automatically analyzes pull requests, suggests improvements, a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
