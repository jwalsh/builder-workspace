# SecureCodeAnalyzer

You are a coding agent working on SecureCodeAnalyzer -- An AI-powered tool that analyzes code in real-time for security vulnerabilities and suggests secure coding practices.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; SecureCodeAnalyzer captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop code analysis engine
- User interface: define project scope and requirements
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: SecureCodeAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Code Analysis Engine (P3) -- (depends on: Design System Architecture)
4. Implement User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
6. Implement Security Vulnerability Detection Rules (P2) -- (depends on: Develop Code Analysis Engine)
7. Develop Secure Coding Best Practices Library (P2) -- (depends on: Implement Security Vulnerability Detection Rules)
8. Integrate with CI/CD Pipelines (P2) -- (depends on: Develop Code Analysis Engine, Implement User Interface)
9. Implement Reporting and Audit Trail (P2) -- (depends on: Set up Data Storage and Management)
10. Conduct Comprehensive Testing (P1) -- (depends on: Develop Code Analysis Engine, Implement User Interface, Implement Security Vulnerability Detection Rules, Develop Secure Coding Best Practices Library, Integrate with CI/CD Pipelines, Implement Reporting and Audit Trail)
11. Deploy and Monitor (P1) -- (depends on: Conduct Comprehensive Testing)
12. Develop Documentation and Training Materials (P1) -- (depends on: Implement User Interface, Implement Security Vulnerability Detection Rules, Develop Secure Coding Best Practices Library)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SecureCodeAnalyzer can deliver its core value proposition as described
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

- Python
- TypeScript/JavaScript
- Java
- Docker
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered tool that analyzes code in real-time for security vulnerabilities and suggests secure .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
