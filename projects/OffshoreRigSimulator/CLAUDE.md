# OffshoreRigSimulator

You are a coding agent working on OffshoreRigSimulator -- A virtual reality training platform for offshore oil rig workers, simulating various scenarios and emergency situations.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; OffshoreRigSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: simulation engine development
- User interface: project planning and requirements gathering (revised)
- Data layer: data management and reporting

## Anti-Goals

- **General-purpose platform**: OffshoreRigSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (Revised) (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Virtual Reality Environment Development (P3) -- (depends on: System Architecture Design)
4. Simulation Engine Development (P3) -- (depends on: System Architecture Design)
5. User Interface Development (P3) -- (depends on: System Architecture Design)
6. Data Management and Reporting (P2) -- (depends on: System Architecture Design)
7. Security and Access Control (P2) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: Virtual Reality Environment Development, Simulation Engine Development, User Interface Development, Data Management and Reporting, Security and Access Control)
9. Deployment and Infrastructure Setup (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and Training Materials (P2) -- (depends on: Virtual Reality Environment Development, Simulation Engine Development, User Interface Development, Data Management and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OffshoreRigSimulator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A virtual reality training platform for offshore oil rig workers, simulating various scenarios and e.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
