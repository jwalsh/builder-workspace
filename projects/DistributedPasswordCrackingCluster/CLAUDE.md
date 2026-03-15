# DistributedPasswordCrackingCluster

You are a coding agent working on DistributedPasswordCrackingCluster -- An ethical hacking tool that distributes password cracking tasks across a large cluster of machines for security research and testing.

## Foundational Axiom

Existing approaches to ethical hacking tool fail because they optimize for the common case while ignoring structural constraints; DistributedPasswordCrackingCluster makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An ethical hacking tool that distributes password cracking tasks across a large cluster of machines 
- User interface: create user interface for client interaction
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: DistributedPasswordCrackingCluster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Develop Password Cracking Algorithms (P3) -- (depends on: Design Architecture for Distributed System)
2. Create User Interface for Client Interaction (P4) -- (depends on: Design Architecture for Distributed System)
3. Implement Cluster Management and Scheduling System (P3) -- (depends on: Design Architecture for Distributed System)
4. Database Design and Implementation (P4) -- (depends on: Design Architecture for Distributed System)
5. Unit Testing and Quality Assurance (P5) -- (depends on: Develop Password Cracking Algorithms, Create User Interface for Client Interaction, Implement Cluster Management and Scheduling System, Database Design and Implementation)
6. Deploy the DistributedPasswordCrackingCluster (P5) -- (depends on: Unit Testing and Quality Assurance)
7. Requirements Gathering and Analysis (P1)
8. Design Architecture for Distributed Password Cracking Cluster (P2) -- (depends on: Requirements Gathering and Analysis)
9. Security Audit and Implementation (P2) -- (depends on: Design Architecture for Distributed System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedPasswordCrackingCluster can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An ethical hacking tool that distributes password cracking tasks across a large cluster of machines .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
