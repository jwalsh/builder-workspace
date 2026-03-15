# AIPoweredEnergyAuditor

You are a coding agent working on AIPoweredEnergyAuditor -- An AI system that conducts comprehensive energy audits of buildings, suggesting optimizations for energy efficiency.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; AIPoweredEnergyAuditor maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data collection and processing
- User interface: project planning and requirements gathering
- Data layer: data collection and processing

## Anti-Goals

- **General-purpose platform**: AIPoweredEnergyAuditor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for AI-Powered Energy Auditor (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Collection and Processing (P3) -- (depends on: System Architecture Design)
4. AI Model Development (P3) -- (depends on: Data Collection and Processing)
5. User Interface Design and Development (P3) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
7. Security and Access Control (P3) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: User Interface Design and Development, AI Model Development, Data Collection and Processing)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and User Guides (P2) -- (depends on: User Interface Design and Development, AI Model Development, Data Collection and Processing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIPoweredEnergyAuditor can deliver its core value proposition as described
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
- PostgreSQL
- MongoDB
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that conducts comprehensive energy audits of buildings, suggesting optimizations for en.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
