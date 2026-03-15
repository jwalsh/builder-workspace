# RedEnergiaAutonoma

You are a coding agent working on RedEnergiaAutonoma -- Una red autónoma que redistribuye la energía en tiempo real, reduciendo pérdidas y aumentando eficiencia.

## Foundational Axiom

Existing approaches to una red autónoma que redistribuye la energía en tiempo real, fail because they optimize for the common case while ignoring structural constraints; RedEnergiaAutonoma makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop real-time data collection and processing system
- User interface: develop user interface for system monitoring and control
- Data layer: create database schema for energy distribution data storage

## Anti-Goals

- **General-purpose platform**: RedEnergiaAutonoma solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for Real-Time Energy Redistribution System (P1)
2. Create Database Schema for Energy Distribution Data Storage (P5) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)
3. Develop User Interface for System Monitoring and Control (P4) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)
4. Develop Real-Time Data Collection and Processing System (P3) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)
5. Comprehensive Technical Documentation for RedEnergiaAutonoma (P3) -- (depends on: Completion of all high-level tasks)
6. Define Energy Redistribution Algorithm (P2) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)
7. Perform Security Audit of the Entire System (P2) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)
8. Implement DevOps Practices for Continuous Integration and Deployment (P1) -- (depends on: Design Architecture for Real-Time Energy Redistribution System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RedEnergiaAutonoma can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Redis

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una red autónoma que redistribuye la energía en tiempo real, reduciendo pérdidas y aumentando eficie.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
