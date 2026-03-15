# PeerCodeBattleArena

You are a coding agent working on PeerCodeBattleArena -- A competitive coding platform where users can challenge each other to solve problems in real-time, with live spectating and commentary.

## Foundational Axiom

The bottleneck in competitive coding platform where users can challenge each other is not compute or data but the feedback loop between intent and artifact; PeerCodeBattleArena compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements
- Data layer: design database schema for peercodebattlearena

## Anti-Goals

- **General-purpose platform**: PeerCodeBattleArena solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements, Conduct Market Research and Competitive Analysis)
3. Design Database Schema for PeerCodeBattleArena (P3) -- (depends on: Define Project Scope and Requirements)
4. Develop Backend Services (P2) -- (depends on: Design System Architecture, Design Database Schema)
5. Design User Interface and Experience - RFC Review (P3) -- (depends on: Define Project Scope and Requirements)
6. Develop Frontend Application (P2) -- (depends on: Design User Interface and Experience, Develop Backend Services)
7. Implement Security Measures (P4) -- (depends on: Develop Backend Services, Develop Frontend Application)
8. Implement Real-time Communication (P3) -- (depends on: Develop Backend Services)
9. Set up Continuous Integration and Deployment (P3) -- (depends on: Develop Backend Services, Develop Frontend Application)
10. Write Technical Documentation (P3) -- (depends on: Develop Backend Services, Develop Frontend Application)
11. Conduct Quality Assurance Testing (P2) -- (depends on: Develop Backend Services, Develop Frontend Application)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PeerCodeBattleArena can deliver its core value proposition as described
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

- MongoDB

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A competitive coding platform where users can challenge each other to solve problems in real-time, w.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
