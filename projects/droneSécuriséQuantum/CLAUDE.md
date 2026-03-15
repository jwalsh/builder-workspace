# droneSécuriséQuantum

You are a coding agent working on droneSécuriséQuantum -- Des drones équipés de technologies de communication quantique pour des missions militaires sécurisées.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; droneSécuriséQuantum guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for drones
- User interface: develop frontend interface for drones

## Anti-Goals

- **General-purpose platform**: droneSécuriséQuantum solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Quantum Communication System Architecture (P2) -- (depends on: Define Quantum Communication Technology for Drones)
2. Develop Frontend Interface for Drones (P3) -- (depends on: Design Quantum Communication System Architecture)
3. Develop Backend Services for Drones (P3) -- (depends on: Design Quantum Communication System Architecture)
4. Integrate Quantum Communication into Drones (P4) -- (depends on: Design Quantum Communication System Architecture, Develop Frontend Interface for Drones, Develop Backend Services for Drones)
5. Test and Validate Quantum Communication System (P5) -- (depends on: Integrate Quantum Communication into Drones)
6. Defining Quantum Communication Technology for Secure Drone Communications: Research Proposal (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: droneSécuriséQuantum can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des drones équipés de technologies de communication quantique pour des missions militaires sécurisée.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
