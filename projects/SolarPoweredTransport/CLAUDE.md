# SolarPoweredTransport

You are a coding agent working on SolarPoweredTransport -- Electric vehicles that run entirely on solar power for sustainable transportation.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; SolarPoweredTransport maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Electric vehicles that run entirely on solar power for sustainable transportation.
- User interface: select and specify battery requirements

## Anti-Goals

- **General-purpose platform**: SolarPoweredTransport solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Solar-Powered Vehicle Architecture (P1)
2. Develop Charging Mechanism Design (P4) -- (depends on: Design Solar-Powered Vehicle Architecture)
3. Select and Specify Battery Requirements (P3) -- (depends on: Design Solar-Powered Vehicle Architecture)
4. Research and Select Solar Panel Manufacturer (P2)
5. Develop Solar Panel Purchase and Integration Plan (P3) -- (depends on: Research and Select Solar Panel Manufacturer)
6. Develop Solar Panels Integration Design (P2) -- (depends on: Design Solar-Powered Vehicle Architecture)
7. Create Project Roadmap (P1) -- (depends on: Design Solar-Powered Vehicle Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SolarPoweredTransport can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Electric vehicles that run entirely on solar power for sustainable transportation..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
