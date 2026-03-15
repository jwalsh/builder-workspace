# EnergyPositiveDesalination

You are a coding agent working on EnergyPositiveDesalination -- A desalination plant that produces more energy than it consumes, using a combination of solar power and pressure gradients.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; EnergyPositiveDesalination maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A desalination plant that produces more energy than it consumes, using a combination of solar power 
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: EnergyPositiveDesalination solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Design and Architecture (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Solar Power System Design (P3) -- (depends on: Design and Architecture)
4. Pressure Gradient System Design (P3) -- (depends on: Design and Architecture)
5. Desalination Process Design (P3) -- (depends on: Design and Architecture)
6. Database Design and Implementation (P3) -- (depends on: Design and Architecture)
7. User Interface and Monitoring System (P3) -- (depends on: Design and Architecture)
8. System Integration and Testing (P4) -- (depends on: Solar Power System Design, Pressure Gradient System Design, Desalination Process Design, Database Design and Implementation, User Interface and Monitoring System)
9. Deployment and Commissioning (P5) -- (depends on: System Integration and Testing)
10. Documentation and Training (P4) -- (depends on: System Integration and Testing)
11. Security and Compliance (P3) -- (depends on: Design and Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EnergyPositiveDesalination can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A desalination plant that produces more energy than it consumes, using a combination of solar power .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
