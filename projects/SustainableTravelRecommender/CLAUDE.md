# SustainableTravelRecommender

You are a coding agent working on SustainableTravelRecommender -- A recommendation system that suggests eco-friendly travel options, calculating and offsetting carbon footprints for environmentally conscious travelers.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; SustainableTravelRecommender captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design for sustainabletravelrecommender

## Anti-Goals

- **General-purpose platform**: SustainableTravelRecommender solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Design System Architecture (Revised) (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design for SustainableTravelRecommender (P3) -- (depends on: Design System Architecture, Gather Data Requirements)
4. User Interface Design (Revised) (P3) -- (depends on: Design System Architecture, Define Data Models)
5. Travel Recommendation Algorithm (P2) -- (depends on: Design System Architecture, Database Design)
6. Carbon Footprint Calculation (P2) -- (depends on: Design System Architecture, Database Design)
7. Carbon Offsetting Integration (P2) -- (depends on: Design System Architecture, Database Design)
8. Backend Development (P2) -- (depends on: Travel Recommendation Algorithm, Carbon Footprint Calculation, Carbon Offsetting Integration)
9. Frontend Development (P2) -- (depends on: User Interface Design, Backend Development)
10. Testing and Quality Assurance (P2) -- (depends on: Backend Development, Frontend Development)
11. Security Audit (P2) -- (depends on: Backend Development, Frontend Development)
12. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance, Security Audit)
13. Documentation and User Guides (P1) -- (depends on: Backend Development, Frontend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SustainableTravelRecommender can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A recommendation system that suggests eco-friendly travel options, calculating and offsetting carbon.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
