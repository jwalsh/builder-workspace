# DistributedSocialNetworkPlatform

You are a coding agent working on DistributedSocialNetworkPlatform -- A decentralized social network platform that distributes user data and computation across a peer-to-peer network for enhanced privacy and scalability.

## Foundational Axiom

Existing approaches to decentralized social network platform fail because they optimize for the common case while ignoring structural constraints; DistributedSocialNetworkPlatform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: develop frontend user interface
- Data layer: create data model and schema design

## Anti-Goals

- **General-purpose platform**: DistributedSocialNetworkPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for the Platform (P2) -- (depends on: Define Project Requirements)
2. Create Data Model and Schema Design (P3) -- (depends on: Design Architecture for the Platform)
3. Implement Backend Services (P4) -- (depends on: Design Architecture for the Platform, Create Data Model and Schema Design)
4. Develop Frontend User Interface (P4) -- (depends on: Implement Backend Services)
5. Implement and Configure DevOps Pipeline (P5) -- (depends on: Implement Backend Services, Develop Frontend User Interface)
6. Perform Security Audit (P5) -- (depends on: Implement Backend Services, Develop Frontend User Interface)
7. Test Platform Functionality (P5) -- (depends on: Implement Backend Services, Develop Frontend User Interface)
8. Deploy MVP to Test Network (P5) -- (depends on: Implement Backend Services, Develop Frontend User Interface, Test Platform Functionality)
9. Iterate and Improve Based on Feedback (P5) -- (depends on: Deploy MVP to Test Network)
10. Define Comprehensive Project Requirements for DistributedSocialNetworkPlatform (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedSocialNetworkPlatform can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A decentralized social network platform that distributes user data and computation across a peer-to-.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
