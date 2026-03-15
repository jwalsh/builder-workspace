# EnergyHarvestingPaint

You are a coding agent working on EnergyHarvestingPaint -- A specialized paint that can harvest small amounts of energy from light, heat, and vibrations in the environment.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; EnergyHarvestingPaint maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A specialized paint that can harvest small amounts of energy from light, heat, and vibrations in the
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: EnergyHarvestingPaint solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design Energy Harvesting System for EnergyHarvestingPaint Project (P4) -- (depends on: Define Project Requirements, Conduct Market Research, Identify Target Applications)
3. Design Paint Formulation for Energy Harvesting Paint (P4) -- (depends on: Define Project Requirements, Research Energy Harvesting Materials and Technologies)
4. Develop Energy Harvesting Algorithms (P3) -- (depends on: Design Energy Harvesting System)
5. Develop User Interface (P2) -- (depends on: Design Energy Harvesting System)
6. Implement Security Measures (P3) -- (depends on: Design Energy Harvesting System, Develop User Interface)
7. Set up Testing Environment (P3) -- (depends on: Design Energy Harvesting System, Design Paint Formulation)
8. Plan Deployment and Maintenance - Revised (P3) -- (depends on: Design Energy Harvesting System, Design Paint Formulation, Develop User Interface, Establish Monitoring and Analytics Strategy)
9. Develop Documentation (P2) -- (depends on: Design Energy Harvesting System, Design Paint Formulation, Develop User Interface)
10. Conduct System Integration Testing (P2) -- (depends on: Develop Energy Harvesting Algorithms, Design Paint Formulation, Develop User Interface, Implement Security Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EnergyHarvestingPaint can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A specialized paint that can harvest small amounts of energy from light, heat, and vibrations in the.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
