# BlockchainRentalPlatform

You are a coding agent working on BlockchainRentalPlatform -- A decentralized platform for long-term rentals, using smart contracts to automate payments, deposits, and conflict resolution between landlords and tenants.

## Foundational Axiom

Distributed systems fail when they conflate consensus with correctness; BlockchainRentalPlatform separates mechanism from policy.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements
- Data layer: define data models and database schema for blockchainrentalplatform

## Anti-Goals

- **General-purpose platform**: BlockchainRentalPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for Blockchain Rental Platform (P5) -- (depends on: Define Project Scope and Requirements, Conduct Market Research and Competitor Analysis)
3. Design User Interface and Experience (UI/UX) for Blockchain Rental Platform (P3) -- (depends on: Define Project Scope and Requirements, Design Smart Contract Architecture, Define Data Models and Storage Requirements)
4. Define Data Models and Database Schema for BlockchainRentalPlatform (P3) -- (depends on: Define Project Scope and Requirements, Design UI/UX for BlockchainRentalPlatform)
5. Create Documentation and User Guides (P3) -- (depends on: Define Project Scope and Requirements, Design User Interface and Experience)
6. Develop Smart Contracts (P2) -- (depends on: Design System Architecture, Define Data Models and Database Schema)
7. Develop Backend Services (P2) -- (depends on: Design System Architecture, Define Data Models and Database Schema)
8. Develop Frontend Application (P2) -- (depends on: Design User Interface and Experience, Develop Backend Services)
9. Implement Comprehensive Security Measures (P2) -- (depends on: Design System Architecture)
10. Set up CI/CD Pipeline with Authentication and Integration (P2)
11. Conduct Testing and Quality Assurance (P2) -- (depends on: Develop Smart Contracts, Develop Backend Services, Develop Frontend Application)
12. Deploy and Monitor the Platform (P1) -- (depends on: Conduct Testing and Quality Assurance, Set up CI/CD Pipeline)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BlockchainRentalPlatform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes
- AWS
- GraphQL

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A decentralized platform for long-term rentals, using smart contracts to automate payments, deposits.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to distributed systems developers and protocol designers.
