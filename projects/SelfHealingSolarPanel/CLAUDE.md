# SelfHealingSolarPanel

You are a coding agent working on SelfHealingSolarPanel -- Solar panels with self-healing capabilities, automatically repairing minor damage to maintain optimal efficiency.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; SelfHealingSolarPanel maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: software development
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: SelfHealingSolarPanel solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architectural Design (P5) -- (depends on: Project Planning and Requirements Gathering, Market Research and Feasibility Analysis)
3. Hardware Development (P3) -- (depends on: Architectural Design)
4. Software Development (P3) -- (depends on: Architectural Design)
5. Security and Compliance (P3) -- (depends on: Architectural Design)
6. Integration and Testing (P2) -- (depends on: Hardware Development, Software Development)
7. Deployment and Maintenance (P2) -- (depends on: Integration and Testing, Security and Compliance)
8. Documentation and Training (P2) -- (depends on: Integration and Testing, Deployment and Maintenance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SelfHealingSolarPanel can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Solar panels with self-healing capabilities, automatically repairing minor damage to maintain optima.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
