# BioSolarLeaf

You are a coding agent working on BioSolarLeaf -- An artificial leaf that uses sunlight, CO2, and water to produce renewable energy and organic compounds.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; BioSolarLeaf maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An artificial leaf that uses sunlight, CO2, and water to produce renewable energy and organic compou
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: BioSolarLeaf solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P4)
4. Develop Photosynthesis Module (P3) -- (depends on: Design System Architecture)
5. Develop Energy Conversion Module (P3) -- (depends on: Design System Architecture)
6. Develop Organic Compound Production Module (P3) -- (depends on: Design System Architecture)
7. Implement Testing Framework (P3) -- (depends on: Design System Architecture)
8. Design User Interface for BioSolarLeaf System (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Define Data Models and APIs)
9. Implement User Interface (P2) -- (depends on: Design User Interface)
10. Conduct Security Audit (P3) -- (depends on: Develop Photosynthesis Module, Develop Energy Conversion Module, Develop Organic Compound Production Module, Implement User Interface)
11. Write Technical Documentation (P2) -- (depends on: Design System Architecture, Design User Interface)
12. Deploy and Monitor System (P1) -- (depends on: Develop Photosynthesis Module, Develop Energy Conversion Module, Develop Organic Compound Production Module, Implement User Interface, Conduct Security Audit)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioSolarLeaf can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An artificial leaf that uses sunlight, CO2, and water to produce renewable energy and organic compou.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
