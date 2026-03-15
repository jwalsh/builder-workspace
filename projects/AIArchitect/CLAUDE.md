# AIArchitect

You are a coding agent working on AIArchitect -- An AI system that generates and evaluates software architecture designs based on project requirements, considering factors such as scalability, maintainability, and performance.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AIArchitect makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that generates and evaluates software architecture designs based on project requirement
- User interface: define project requirements - revised
- Data layer: implement data storage

## Anti-Goals

- **General-purpose platform**: AIArchitect solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - Revised (P5)
2. Design System Architecture (Approved and Ready for Task Decomposition) (P5) -- (depends on: Define Project Requirements)
3. Develop AI Model (P3) -- (depends on: Design System Architecture)
4. Build User Interface (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage (P3) -- (depends on: Design System Architecture)
6. Establish Deployment and Monitoring (P2) -- (depends on: Develop AI Model, Build User Interface, Implement Data Storage)
7. Conduct Security Audits (P2) -- (depends on: Develop AI Model, Build User Interface, Implement Data Storage)
8. Create Documentation (P2) -- (depends on: Develop AI Model, Build User Interface, Implement Data Storage)
9. Test and Validate (P1) -- (depends on: Develop AI Model, Build User Interface, Implement Data Storage, Establish Deployment and Monitoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIArchitect can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that generates and evaluates software architecture designs based on project requirement.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
