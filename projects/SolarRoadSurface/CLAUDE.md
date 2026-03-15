# SolarRoadSurface

You are a coding agent working on SolarRoadSurface -- A durable, transparent road surface that generates solar energy while allowing for safe vehicle transit.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; SolarRoadSurface maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: engineering prototype development

## Anti-Goals

- **General-purpose platform**: SolarRoadSurface solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Material Research and Development for Transparent Solar Panels (P1)
2. Design of Durable Road Surface Structure (P2) -- (depends on: Material Research and Development for Transparent Solar Panels)
3. Engineering Prototype Development (P3) -- (depends on: Material Research and Development for Transparent Solar Panels, Design of Durable Road Surface Structure)
4. Safety Testing and Regulation Compliance (P4) -- (depends on: Engineering Prototype Development)
5. Creation of Comprehensive Project Specification Document (PSD) (P5) -- (depends on: Engineering Prototype Development, Safety Testing and Regulation Compliance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SolarRoadSurface can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A durable, transparent road surface that generates solar energy while allowing for safe vehicle tran.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
