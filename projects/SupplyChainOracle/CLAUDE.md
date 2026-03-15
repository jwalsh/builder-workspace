# SupplyChainOracle

You are a coding agent working on SupplyChainOracle -- Ingest and analyze data from supply chain planning, execution, and real-time status providers to create comprehensive data lake solutions.

## Foundational Axiom

Existing approaches to ingest and analyze data from supply chain planning, executio fail because they optimize for the common case while ignoring structural constraints; SupplyChainOracle makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data processing and transformation
- User interface: user interface development
- Data layer: data ingestion

## Anti-Goals

- **General-purpose platform**: SupplyChainOracle solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Kickoff (P1)
2. Architecture Design (P2) -- (depends on: Project Planning and Kickoff)
3. Data Ingestion (P3) -- (depends on: Architecture Design)
4. Data Processing and Transformation (P3) -- (depends on: Architecture Design)
5. Data Lake Implementation (P3) -- (depends on: Architecture Design)
6. Data Analysis and Reporting (P4) -- (depends on: Data Processing and Transformation, Data Lake Implementation)
7. User Interface Development (P4) -- (depends on: Data Analysis and Reporting)
8. Security and Access Control (P4) -- (depends on: Architecture Design)
9. Testing and Quality Assurance (P4) -- (depends on: Data Ingestion, Data Processing and Transformation, Data Lake Implementation, Data Analysis and Reporting, User Interface Development, Security and Access Control)
10. Deployment and Monitoring (P5) -- (depends on: Testing and Quality Assurance)
11. Documentation and Training (P5) -- (depends on: User Interface Development, Data Analysis and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SupplyChainOracle can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Ingest and analyze data from supply chain planning, execution, and real-time status providers to cre.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
