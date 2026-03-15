# CloudOrquestacionIa

You are a coding agent working on CloudOrquestacionIa -- Una herramienta de orquestación en la nube que optimiza el uso de recursos en tiempo real.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; CloudOrquestacionIa models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop cloudorquestacionia backend
- User interface: define project requirements
- Data layer: implement database integration

## Anti-Goals

- **General-purpose platform**: CloudOrquestacionIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design CloudOrquestacionIa Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop CloudOrquestacionIa Backend (P3) -- (depends on: Design CloudOrquestacionIa Architecture)
4. Develop CloudOrquestacionIa Frontend (P3) -- (depends on: Design CloudOrquestacionIa Architecture)
5. Secure CloudOrquestacionIa (P5) -- (depends on: Develop CloudOrquestacionIa Backend, Develop CloudOrquestacionIa Frontend)
6. Implement Database Integration (P4) -- (depends on: Develop CloudOrquestacionIa Backend)
7. Set up DevOps Pipeline (P3) -- (depends on: Develop CloudOrquestacionIa Backend, Develop CloudOrquestacionIa Frontend)
8. Conduct Unit Tests for CloudOrquestacionIa (P3) -- (depends on: Develop CloudOrquestacionIa Backend, Develop CloudOrquestacionIa Frontend)
9. Test CloudOrquestacionIa End-to-End (P2) -- (depends on: Conduct Unit Tests for CloudOrquestacionIa)
10. Deploy CloudOrquestacionIa to Production (P4) -- (depends on: Set up DevOps Pipeline, Test CloudOrquestacionIa End-to-End)
11. Perform Code Reviews (P2) -- (depends on: Develop CloudOrquestacionIa Backend, Develop CloudOrquestacionIa Frontend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CloudOrquestacionIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Una herramienta de orquestación en la nube que optimiza el uso de recursos en tiempo real..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
