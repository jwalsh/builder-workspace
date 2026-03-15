# ThreatIntelligencePlatform

You are a coding agent working on ThreatIntelligencePlatform -- A comprehensive platform for collecting, analyzing, and disseminating threat intelligence within an organization.

## Foundational Axiom

Security in comprehensive platform fails when it is bolted on after the fact; ThreatIntelligencePlatform makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data processing and analysis components
- User interface: define project scope and requirements: threatintelligenceplatform (revised)
- Data layer: implement data ingestion component

## Anti-Goals

- **General-purpose platform**: ThreatIntelligencePlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: ThreatIntelligencePlatform (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3)
4. Implement Security Measures (P3) -- (depends on: Design System Architecture)
5. Create Testing Strategy and Plans (P3) -- (depends on: Design System Architecture)
6. Implement Data Ingestion Component (P2) -- (depends on: Design System Architecture)
7. Implement Data Processing and Analysis Components (P2) -- (depends on: Design System Architecture)
8. Design and Implement Data Storage (P2) -- (depends on: Design System Architecture)
9. Develop Reporting and Dissemination Components (P2) -- (depends on: Design System Architecture)
10. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThreatIntelligencePlatform can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A comprehensive platform for collecting, analyzing, and disseminating threat intelligence within an .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
