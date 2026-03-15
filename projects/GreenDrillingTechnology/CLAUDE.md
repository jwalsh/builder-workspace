# GreenDrillingTechnology

You are a coding agent working on GreenDrillingTechnology -- Environmentally friendly drilling technologies that minimize environmental impact and reduce carbon emissions.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; GreenDrillingTechnology captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Environmentally friendly drilling technologies that minimize environmental impact and reduce carbon 
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: GreenDrillingTechnology solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Research Existing Green Drilling Technologies (P4)
3. Design System Architecture for Green Drilling Technology (P3)
4. Develop Drilling Simulation and Modeling (P3) -- (depends on: Design System Architecture)
5. Implement Emission Reduction Strategies (P3) -- (depends on: Design System Architecture)
6. Design User Interfaces and Dashboards (Revised) (P3) -- (depends on: Design System Architecture, Define Data Models and APIs)
7. Implement Security and Compliance Measures (P2) -- (depends on: Design System Architecture)
8. Set up Testing and Quality Assurance (P2) -- (depends on: Design System Architecture)
9. Plan Deployment and Maintenance (P2) -- (depends on: Design System Architecture)
10. Create Documentation and Training Materials (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GreenDrillingTechnology can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Environmentally friendly drilling technologies that minimize environmental impact and reduce carbon .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
