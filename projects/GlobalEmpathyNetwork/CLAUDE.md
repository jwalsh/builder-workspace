# GlobalEmpathyNetwork

You are a coding agent working on GlobalEmpathyNetwork -- A social platform that uses VR and AI to facilitate deep, empathetic connections between people from diverse backgrounds and cultures worldwide.

## Foundational Axiom

Existing approaches to social platform fail because they optimize for the common case while ignoring structural constraints; GlobalEmpathyNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: GlobalEmpathyNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design for GlobalEmpathyNetwork (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Privacy Measures for GlobalEmpathyNetwork (Revised) (P4) -- (depends on: Architecture Design)
4. Frontend Development (P3) -- (depends on: Architecture Design)
5. Backend Development (P3) -- (depends on: Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: Architecture Design)
7. VR Integration (P2) -- (depends on: Architecture Design, Frontend Development)
8. AI Integration (P2) -- (depends on: Architecture Design, Backend Development)
9. Testing and Quality Assurance (P3) -- (depends on: Frontend Development, Backend Development, VR Integration, AI Integration)
10. Deployment and DevOps (P3) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation)
11. Documentation and User Support (P2) -- (depends on: Frontend Development, Backend Development, VR Integration, AI Integration)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalEmpathyNetwork can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A social platform that uses VR and AI to facilitate deep, empathetic connections between people from.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
