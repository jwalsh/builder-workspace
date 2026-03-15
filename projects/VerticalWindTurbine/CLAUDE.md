# VerticalWindTurbine

You are a coding agent working on VerticalWindTurbine -- A compact, efficient vertical wind turbine design for urban environments, maximizing energy generation in limited spaces.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; VerticalWindTurbine maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: create detailed design and engineering drawings
- User interface: define design requirements and specifications

## Anti-Goals

- **General-purpose platform**: VerticalWindTurbine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Conduct Preliminary Research and Analysis (P1)
2. Define Design Requirements and Specifications (P2) -- (depends on: Conduct Preliminary Research and Analysis)
3. Develop Prototype Design Concepts (P3) -- (depends on: Define Design Requirements and Specifications)
4. Perform Wind Tunnel Tests on Prototype Designs (P4) -- (depends on: Develop Prototype Design Concepts)
5. Refine Selected Design based on Wind Tunnel Test Results (P5) -- (depends on: Perform Wind Tunnel Tests on Prototype Designs)
6. Create Detailed Design and Engineering Drawings (P1) -- (depends on: Refine Selected Design based on Wind Tunnel Test Results)
7. Manufacture and Assemble Prototype (P2) -- (depends on: Create Detailed Design and Engineering Drawings)
8. Perform Functional Testing on Prototype (Revised) (P3) -- (depends on: Manufacture and Assemble Prototype)
9. Address Functional Testing Issues and Revise as Necessary (P4) -- (depends on: Perform Functional Testing on Prototype)
10. Prepare Production Plan and Cost Estimate (P5) -- (depends on: Address Functional Testing Issues and Revise as Necessary)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VerticalWindTurbine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A compact, efficient vertical wind turbine design for urban environments, maximizing energy generati.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
