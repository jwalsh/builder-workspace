# P2PContentDeliveryNetwork

You are a coding agent working on P2PContentDeliveryNetwork -- A peer-to-peer content delivery network that efficiently distributes large files and streaming content without centralized servers.

## Foundational Axiom

Existing approaches to peer-to-peer content delivery network fail because they optimize for the common case while ignoring structural constraints; P2PContentDeliveryNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop node implementation - backend
- User interface: develop node implementation - frontend

## Anti-Goals

- **General-purpose platform**: P2PContentDeliveryNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Document System Architecture and Design Decisions (P5) -- (depends on: Define System Architecture)
3. Develop Content Delivery Algorithm (P3) -- (depends on: Define System Architecture)
4. Implement Content Request and Response Mechanisms (P4) -- (depends on: Develop Content Delivery Algorithm)
5. Develop Node Implementation - Frontend (P2) -- (depends on: Define System Architecture)
6. Develop Node Implementation - Backend (P2) -- (depends on: Define System Architecture)
7. Test Node Functionality (P4) -- (depends on: Develop Node Implementation - Frontend, Develop Node Implementation - Backend)
8. Review and Provide Feedback on System Design Document (P2) -- (depends on: Document System Architecture and Design Decisions)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: P2PContentDeliveryNetwork can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A peer-to-peer content delivery network that efficiently distributes large files and streaming conte.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
