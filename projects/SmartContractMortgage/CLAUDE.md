# SmartContractMortgage

You are a coding agent working on SmartContractMortgage -- A blockchain-based mortgage system using smart contracts to automate and streamline the entire mortgage process, from application to closing and payments.

## Foundational Axiom

Distributed systems fail when they conflate consensus with correctness; SmartContractMortgage separates mechanism from policy.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A blockchain-based mortgage system using smart contracts to automate and streamline the entire mortg
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: SmartContractMortgage solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Smart Contracts (P3) -- (depends on: Design System Architecture)
4. Build Off-Chain Components (P3) -- (depends on: Design System Architecture)
5. Set Up Blockchain Network (P3) -- (depends on: Design System Architecture)
6. Integrate with External Systems (P3) -- (depends on: Design System Architecture)
7. Implement Security Measures (P2) -- (depends on: Design System Architecture)
8. Test and Quality Assurance (P2) -- (depends on: Develop Smart Contracts, Build Off-Chain Components, Implement Security Measures, Set Up Blockchain Network, Integrate with External Systems)
9. Deploy and Monitor (P2) -- (depends on: Test and Quality Assurance)
10. Create Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartContractMortgage can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A blockchain-based mortgage system using smart contracts to automate and streamline the entire mortg.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to distributed systems developers and protocol designers.
