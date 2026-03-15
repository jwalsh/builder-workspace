# ParallelProgrammingLab

You are a coding agent working on ParallelProgrammingLab -- An environment for learning parallel programming concepts through hands-on coding challenges and visualizations.

## Foundational Axiom

The bottleneck in environment is not compute or data but the feedback loop between intent and artifact; ParallelProgrammingLab compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An environment for learning parallel programming concepts through hands-on coding challenges and vis
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: ParallelProgrammingLab solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. User Interface Design (P3) -- (depends on: Project Planning and Requirements Gathering)
4. Parallel Programming Challenges Development (P3) -- (depends on: Project Planning and Requirements Gathering, System Architecture Design)
5. Visualization Components Development (P3) -- (depends on: Project Planning and Requirements Gathering, System Architecture Design, User Interface Design)
6. Database Design and Implementation (P3) -- (depends on: Project Planning and Requirements Gathering, System Architecture Design)
7. Security and Access Control Implementation (P3) -- (depends on: Project Planning and Requirements Gathering, System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: Parallel Programming Challenges Development, Visualization Components Development, Database Design and Implementation, Security and Access Control Implementation)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and User Guides (P2) -- (depends on: User Interface Design, Parallel Programming Challenges Development, Visualization Components Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ParallelProgrammingLab can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An environment for learning parallel programming concepts through hands-on coding challenges and vis.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
