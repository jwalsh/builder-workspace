# CybersecurityAI

You are a coding agent working on CybersecurityAI -- An AI-driven system that autonomously detects and mitigates cybersecurity threats.

## Foundational Axiom

Security in ai-driven system fails when it is bolted on after the fact; CybersecurityAI makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-driven system that autonomously detects and mitigates cybersecurity threats.
- User interface: define project scope and requirements - ai for cybersecurity
- Data layer: set up database schema and integrations

## Anti-Goals

- **General-purpose platform**: CybersecurityAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - AI for Cybersecurity (P1)
2. Design AI Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop AI Models for Threat Detection (P3) -- (depends on: Design AI Architecture)
4. Implement Threat Mitigation Strategies (P4) -- (depends on: Develop AI Models for Threat Detection)
5. Conduct Security Audits and Penetration Tests (P5) -- (depends on: Implement Threat Mitigation Strategies)
6. Perform Quality Assurance Testing (P5) -- (depends on: Complete Development)
7. Write Technical Documentation (P4) -- (depends on: Complete Development)
8. Set Up Database Schema and Integrations (P3) -- (depends on: Design AI Architecture)
9. Design User Interface (Frontend) (P2) -- (depends on: Design AI Architecture)
10. Implement DevOps Practices for Continuous Integration and Deployment (P2) -- (depends on: Design AI Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CybersecurityAI can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-driven system that autonomously detects and mitigates cybersecurity threats..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
