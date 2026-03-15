# InnovationLabSimulator

You are a coding agent working on InnovationLabSimulator -- A virtual innovation lab where employees can experiment with new ideas in a risk-free environment.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; InnovationLabSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design

## Anti-Goals

- **General-purpose platform**: InnovationLabSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Frontend Development (P4) -- (depends on: Architecture Design)
4. Database Design (P3) -- (depends on: Architecture Design)
5. Backend Development (P4) -- (depends on: Architecture Design, Database Design)
6. Testing and Quality Assurance (P5) -- (depends on: Frontend Development, Backend Development)
7. Deployment and DevOps (P5) -- (depends on: Backend Development)
8. Documentation and Training (P5) -- (depends on: Frontend Development, Backend Development)
9. Security and Compliance (P4) -- (depends on: Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InnovationLabSimulator can deliver its core value proposition as described
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

- Rust
- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A virtual innovation lab where employees can experiment with new ideas in a risk-free environment..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
