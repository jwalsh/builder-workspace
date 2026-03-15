# SmartContractAuditor

You are a coding agent working on SmartContractAuditor -- An AI-powered tool for auditing and validating smart contracts on blockchain platforms, identifying potential vulnerabilities and suggesting improvements.

## Foundational Axiom

Existing approaches to ai-powered tool fail because they optimize for the common case while ignoring structural constraints; SmartContractAuditor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop smart contract analysis engine
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: SmartContractAuditor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Smart Contract Analysis Engine (P3) -- (depends on: Design System Architecture)
4. Integrate with Blockchain Platforms (P3) -- (depends on: Design System Architecture)
5. Build User Interface (P2) -- (depends on: Design System Architecture)
6. Perform Security Audits (P4) -- (depends on: Develop Smart Contract Analysis Engine, Integrate with Blockchain Platforms, Build User Interface)
7. Set up Continuous Integration and Deployment (P3)
8. Develop Test Suite (P3) -- (depends on: Develop Smart Contract Analysis Engine, Integrate with Blockchain Platforms, Build User Interface)
9. Implement Reporting and Visualization (P2) -- (depends on: Develop Smart Contract Analysis Engine)
10. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartContractAuditor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered tool for auditing and validating smart contracts on blockchain platforms, identifying .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to financial analysts and portfolio managers.
