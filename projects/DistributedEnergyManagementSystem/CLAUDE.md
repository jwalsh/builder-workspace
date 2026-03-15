# DistributedEnergyManagementSystem

You are a coding agent working on DistributedEnergyManagementSystem -- A system for managing and optimizing energy distribution across smart grids, balancing supply and demand in real-time.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; DistributedEnergyManagementSystem maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development for core functionality
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: DistributedEnergyManagementSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. System Design and Architecture Definition (P2) -- (depends on: Requirements Gathering and Analysis)
3. Backend Development for Core Functionality (P5) -- (depends on: System Design and Architecture Definition)
4. Frontend Development for User Interface (P4) -- (depends on: System Design and Architecture Definition)
5. Documentation and Technical Writing (P5) -- (depends on: Backend Development for Core Functionality, Frontend Development for User Interface)
6. Code Review and Audit (P4) -- (depends on: Backend Development for Core Functionality, Frontend Development for User Interface)
7. Database Design and Implementation (P3) -- (depends on: System Design and Architecture Definition)
8. Testing and Quality Assurance (P3) -- (depends on: Backend Development for Core Functionality, Frontend Development for User Interface)
9. DevOps Setup and Configuration (P2) -- (depends on: System Design and Architecture Definition)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedEnergyManagementSystem can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for managing and optimizing energy distribution across smart grids, balancing supply and de.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
