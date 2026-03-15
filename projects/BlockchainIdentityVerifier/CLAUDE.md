# BlockchainIdentityVerifier

You are a coding agent working on BlockchainIdentityVerifier -- A secure, privacy-focused identity verification system for banking, using blockchain to give users control over their personal data while meeting regulatory requirements.

## Foundational Axiom

Distributed systems fail when they conflate consensus with correctness; BlockchainIdentityVerifier separates mechanism from policy.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A secure, privacy-focused identity verification system for banking, using blockchain to give users c
- User interface: define project scope and requirements (revised)
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: BlockchainIdentityVerifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Blockchain Integration (P3) -- (depends on: Design System Architecture)
4. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
5. Build User Interfaces (P3) -- (depends on: Design System Architecture)
6. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
7. Document System Architecture and Usage (P3) -- (depends on: Design System Architecture)
8. Implement Security and Compliance Measures (P2) -- (depends on: Design System Architecture)
9. Conduct System Testing (P2) -- (depends on: Develop Blockchain Integration, Implement Data Storage and Management, Build User Interfaces, Implement Security and Compliance Measures)
10. Deploy and Launch System (P1) -- (depends on: Conduct System Testing, Document System Architecture and Usage)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BlockchainIdentityVerifier can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A secure, privacy-focused identity verification system for banking, using blockchain to give users c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to distributed systems developers and protocol designers.
