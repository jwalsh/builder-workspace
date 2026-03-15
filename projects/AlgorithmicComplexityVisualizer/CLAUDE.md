# AlgorithmicComplexityVisualizer

You are a coding agent working on AlgorithmicComplexityVisualizer -- A platform that visually demonstrates the time and space complexity of different algorithms, helping users understand big O notation.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; AlgorithmicComplexityVisualizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform that visually demonstrates the time and space complexity of different algorithms, helping
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: AlgorithmicComplexityVisualizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architectural Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Algorithm Research and Selection (P3) -- (depends on: Project Planning and Requirements Gathering)
4. Back-end Development (P2) -- (depends on: Architectural Design, Algorithm Research and Selection)
5. User Interface Design (P3) -- (depends on: Project Planning and Requirements Gathering, Architectural Design)
6. Front-end Development (P2) -- (depends on: User Interface Design, Back-end Development)
7. Security and Compliance (P4) -- (depends on: Architectural Design, Back-end Development, Front-end Development)
8. Documentation and User Guides (P3) -- (depends on: Back-end Development, Front-end Development)
9. Testing and Quality Assurance (P2) -- (depends on: Back-end Development, Front-end Development)
10. Deployment and DevOps (P2) -- (depends on: Back-end Development, Front-end Development, Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AlgorithmicComplexityVisualizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- PostgreSQL
- MongoDB
- Redis
- Docker
- Kubernetes
- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that visually demonstrates the time and space complexity of different algorithms, helping.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
