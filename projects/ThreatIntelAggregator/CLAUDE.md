# ThreatIntelAggregator

You are a coding agent working on ThreatIntelAggregator -- A platform that aggregates and analyzes threat intelligence from multiple sources, providing actionable insights.

## Foundational Axiom

Security in platform fails when it is bolted on after the fact; ThreatIntelAggregator makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data processing and enrichment
- User interface: project planning and requirements gathering
- Data layer: data processing and enrichment

## Anti-Goals

- **General-purpose platform**: ThreatIntelAggregator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Data Processing and Enrichment (P3) -- (depends on: Architecture Design)
4. Data Storage and Indexing (P3) -- (depends on: Architecture Design)
5. Threat Intelligence Analysis (P4) -- (depends on: Data Processing and Enrichment, Data Storage and Indexing)
6. User Interface and Reporting (P4) -- (depends on: Threat Intelligence Analysis)
7. Testing and Quality Assurance (P4) -- (depends on: User Interface and Reporting, Threat Intelligence Analysis)
8. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
9. Documentation and Training (P5) -- (depends on: User Interface and Reporting, Threat Intelligence Analysis)
10. Security and Compliance (P4) -- (depends on: Architecture Design)
11. Data Source Integration (P3) -- (depends on: Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThreatIntelAggregator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform that aggregates and analyzes threat intelligence from multiple sources, providing actiona.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
