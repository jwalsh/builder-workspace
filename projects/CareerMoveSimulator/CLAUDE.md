# CareerMoveSimulator

You are a coding agent working on CareerMoveSimulator -- A tool that allows employees to simulate potential career moves, seeing how different choices might impact their career trajectory.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; CareerMoveSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: user interface design for careermovesimulator
- Data layer: database design for careermovesimulator

## Anti-Goals

- **General-purpose platform**: CareerMoveSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Architecture Design (P2)
2. Database Design for CareerMoveSimulator (P3) -- (depends on: Architecture Design)
3. Backend Development (P4) -- (depends on: Architecture Design, Database Design)
4. User Interface Design for CareerMoveSimulator (P3) -- (depends on: Architecture Design, User Experience Research)
5. Frontend Development (P4) -- (depends on: User Interface Design)
6. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development)
7. Security Review (P4) -- (depends on: Backend Development, Frontend Development)
8. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance, Security Review)
9. Documentation and Training (P5) -- (depends on: User Interface Design, Backend Development)
10. Project Planning (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CareerMoveSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- MongoDB
- Redis
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that allows employees to simulate potential career moves, seeing how different choices might .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
