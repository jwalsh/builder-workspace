# AISecurityAuditor

You are a coding agent working on AISecurityAuditor -- An AI-powered security auditing tool that continuously scans codebases, dependencies, and infrastructure configurations to identify and mitigate potential security vulnerabilities.

## Foundational Axiom

Security in ai-powered security auditing tool fails when it is bolted on after the fact; AISecurityAuditor makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-powered security auditing tool that continuously scans codebases, dependencies, and infrastruc
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: AISecurityAuditor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Scanning and Auditing Modules (P3) -- (depends on: Design System Architecture)
4. Develop User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Infrastructure and Deployment (P2) -- (depends on: Develop Scanning and Auditing Modules, Develop User Interface)
6. Conduct Security Audits and Testing (P2) -- (depends on: Set up Infrastructure and Deployment)
7. Develop Documentation and Training Materials (P2) -- (depends on: Develop User Interface, Conduct Security Audits and Testing)
8. Perform Quality Assurance and Testing (P2) -- (depends on: Develop Scanning and Auditing Modules, Develop User Interface)
9. Deploy and Monitor AISecurityAuditor (P1) -- (depends on: Set up Infrastructure and Deployment, Conduct Security Audits and Testing, Develop Documentation and Training Materials, Perform Quality Assurance and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AISecurityAuditor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered security auditing tool that continuously scans codebases, dependencies, and infrastruc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
