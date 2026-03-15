# FloatingOffshoreWindFarm

You are a coding agent working on FloatingOffshoreWindFarm -- A design for floating wind turbines that can be deployed in deep offshore waters, expanding wind energy potential.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; FloatingOffshoreWindFarm maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: software architecture design for floating offshore wind farm
- User interface: requirements gathering for floating offshore wind farm system

## Anti-Goals

- **General-purpose platform**: FloatingOffshoreWindFarm solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for Floating Offshore Wind Farm System (P1)
2. Design Concept for Floating Offshore Wind Turbines (P2) -- (depends on: Requirements Gathering for Floating Offshore Wind Farm System)
3. Detailed Design of Floating Offshore Wind Turbine Structure (P3) -- (depends on: Design Concept for Floating Offshore Wind Turbines)
4. Electrical Systems Design for Floating Offshore Wind Farm (P3) -- (depends on: Design Concept for Floating Offshore Wind Turbines)
5. Mechanical Systems Design for Floating Offshore Wind Farm (P3) -- (depends on: Design Concept for Floating Offshore Wind Turbines)
6. Software Architecture Design for Floating Offshore Wind Farm (P3) -- (depends on: Design Concept for Floating Offshore Wind Turbines)
7. Implementation of Floating Offshore Wind Farm System Components (P4) -- (depends on: Detailed Design of Floating Offshore Wind Turbine Structure, Electrical Systems Design for Floating Offshore Wind Farm, Mechanical Systems Design for Floating Offshore Wind Farm, Software Architecture Design for Floating Offshore Wind Farm)
8. Integration and Testing of Floating Offshore Wind Farm System Components (P4) -- (depends on: Implementation of Floating Offshore Wind Farm System Components)
9. Deployment and Installation of Floating Offshore Wind Farm (P5) -- (depends on: Integration and Testing of Floating Offshore Wind Farm System Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FloatingOffshoreWindFarm can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A design for floating wind turbines that can be deployed in deep offshore waters, expanding wind ene.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
