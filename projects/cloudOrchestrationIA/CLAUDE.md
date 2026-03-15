# cloudOrchestrationIA

You are a coding agent working on cloudOrchestrationIA -- Un outil d'orchestration cloud qui optimise l'utilisation des ressources en fonction des besoins en temps réel.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; cloudOrchestrationIA models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend system
- User interface: define project requirements
- Data layer: implement database integration

## Anti-Goals

- **General-purpose platform**: cloudOrchestrationIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design CloudOrchestrationIA Architecture (P2) -- (depends on: Define Project Requirements)
3. Implement Database Integration (P5) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture)
4. Develop Frontend Interface (P3) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture)
5. Develop Backend System (P4) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture)
6. Perform DevOps Setup and Deployment (P2) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture, Develop Frontend Interface, Develop Backend System, Implement Database Integration)
7. Test and Validate cloudOrchestrationIA (P5) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture, Develop Frontend Interface, Develop Backend System, Implement Database Integration, Perform DevOps Setup and Deployment)
8. Secure cloudOrchestrationIA (P4) -- (depends on: Define Project Requirements, Design CloudOrchestrationsIA Architecture, Develop Frontend Interface, Develop Backend System, Implement Database Integration, Perform DevOps Setup and Deployment)
9. Document cloudOrchestrationIA (P3) -- (depends on: Define Project Requirements, Design CloudOrchestrationIA Architecture, Develop Frontend Interface, Develop Backend System, Implement Database Integration, Perform DevOps Setup and Deployment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: cloudOrchestrationIA can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un outil d'orchestration cloud qui optimise l'utilisation des ressources en fonction des besoins en .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
