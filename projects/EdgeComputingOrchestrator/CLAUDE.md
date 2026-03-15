# EdgeComputingOrchestrator

You are a coding agent working on EdgeComputingOrchestrator -- A system for managing and orchestrating computation across a network of edge devices, balancing load and ensuring data privacy.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; EdgeComputingOrchestrator captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend logic for load balancing
- User interface: develop frontend interface for user interaction
- Data layer: create data privacy policy document

## Anti-Goals

- **General-purpose platform**: EdgeComputingOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Edge Device Interaction Protocol (P3) -- (depends on: Define System Architecture)
3. Implement Backend Logic for Load Balancing (P5) -- (depends on: Design Edge Device Interaction Protocol)
4. Create Data Privacy Policy Document (P2) -- (depends on: Define System Architecture)
5. Develop Frontend Interface for User Interaction (P4) -- (depends on: Create Data Privacy Policy Document, Design Edge Device Interaction Protocol)
6. Implement Data Privacy Measures in Backend (P4) -- (depends on: Create Data Privacy Policy Document)
7. Test EdgeComputingOrchestrator System Components (P5) -- (depends on: Develop Frontend Interface for User Interaction, Implement Backend Logic for Load Balancing, Implement Data Privacy Measures in Backend)
8. Document System Functionality and Usage (P2) -- (depends on: Develop Frontend Interface for User Interaction)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EdgeComputingOrchestrator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for managing and orchestrating computation across a network of edge devices, balancing load.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
