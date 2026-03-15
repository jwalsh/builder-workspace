# EnergyPositiveHomes

You are a coding agent working on EnergyPositiveHomes -- A system for designing and managing homes that produce more energy than they consume, integrating renewable sources and advanced energy storage solutions.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; EnergyPositiveHomes maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system for designing and managing homes that produce more energy than they consume, integrating re
- User interface: project planning and requirements gathering
- Data layer: energy storage solutions

## Anti-Goals

- **General-purpose platform**: EnergyPositiveHomes solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Renewable Energy Integration (P3) -- (depends on: System Architecture Design)
4. Energy Storage Solutions (P3) -- (depends on: System Architecture Design)
5. Home Energy Management System (P4) -- (depends on: System Architecture Design, Renewable Energy Integration, Energy Storage Solutions)
6. Data Storage and Analytics (P4) -- (depends on: System Architecture Design)
7. Testing and Quality Assurance (P5) -- (depends on: Renewable Energy Integration, Energy Storage Solutions, Home Energy Management System, Data Storage and Analytics)
8. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
9. Documentation and User Guides (P5) -- (depends on: Home Energy Management System)
10. Security and Privacy (P4) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EnergyPositiveHomes can deliver its core value proposition as described
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

- PostgreSQL

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for designing and managing homes that produce more energy than they consume, integrating re.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
