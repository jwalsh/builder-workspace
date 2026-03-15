# CarbonCaptureTextiles

You are a coding agent working on CarbonCaptureTextiles -- Fabrics and textiles that actively capture CO2 from the air, usable in clothing and interior design.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; CarbonCaptureTextiles captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Fabrics and textiles that actively capture CO2 from the air, usable in clothing and interior design.
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: CarbonCaptureTextiles solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Research and Evaluate Existing Technologies (P4)
3. Design Carbon Capture Mechanism - Revised (P5) -- (depends on: Define Project Scope and Requirements, Research and Evaluate Existing Technologies, Consult with Textile Manufacturing Experts)
4. Develop Textile Manufacturing Process (P4) -- (depends on: Design Carbon Capture Mechanism)
5. Build Prototype and Conduct Testing (P3) -- (depends on: Develop Textile Manufacturing Process)
6. Develop Production and Scaling Strategy (P2) -- (depends on: Build Prototype and Conduct Testing)
7. Conduct Life Cycle Assessment (P3) -- (depends on: Develop Production and Scaling Strategy)
8. Develop Marketing and Commercialization Strategy (P2) -- (depends on: Conduct Life Cycle Assessment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CarbonCaptureTextiles can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Fabrics and textiles that actively capture CO2 from the air, usable in clothing and interior design..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
