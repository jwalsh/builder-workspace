# InteractiveCodePlayground

You are a coding agent working on InteractiveCodePlayground -- A web-based IDE that allows users to experiment with code snippets, test algorithms, and collaborate with others in real-time.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; InteractiveCodePlayground captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project requirements - updated
- Data layer: set up database

## Anti-Goals

- **General-purpose platform**: InteractiveCodePlayground solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - Updated (P5)
2. Design System Architecture - InteractiveCodePlayground (Revised) (P5) -- (depends on: Define Project Requirements, Identify External Dependencies and Integrations)
3. Develop Frontend (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P3) -- (depends on: Design System Architecture)
5. Set up Database (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P2) -- (depends on: Develop Frontend, Develop Backend)
7. Set up Continuous Integration and Deployment (P2) -- (depends on: Develop Frontend, Develop Backend)
8. Write Documentation (P2) -- (depends on: Develop Frontend, Develop Backend)
9. Test and Quality Assurance (P1) -- (depends on: Develop Frontend, Develop Backend, Set up Database)
10. Deploy and Monitor (P1) -- (depends on: Set up Continuous Integration and Deployment, Test and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InteractiveCodePlayground can deliver its core value proposition as described
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

- TypeScript/JavaScript
- MongoDB
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A web-based IDE that allows users to experiment with code snippets, test algorithms, and collaborate.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
