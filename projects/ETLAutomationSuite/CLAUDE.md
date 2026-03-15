# ETLAutomationSuite

You are a coding agent working on ETLAutomationSuite -- A suite of tools for automating the Extract, Transform, Load (ETL) processes in data pipelines.

## Foundational Axiom

Existing approaches to suite of tools fail because they optimize for the common case while ignoring structural constraints; ETLAutomationSuite makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A suite of tools for automating the Extract, Transform, Load (ETL) processes in data pipelines.
- User interface: requirements gathering for etlautomationsuite
- Data layer: database schema design

## Anti-Goals

- **General-purpose platform**: ETLAutomationSuite solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for ETLAutomationSuite (P1)
2. Design the ETLAutomationSuite Architecture (P2) -- (depends on: Requirements Gathering)
3. Decompose the ETLAutomationSuite Design into Tasks (P3) -- (depends on: Design the ETLAutomationSuite Architecture)
4. Implement the Extraction Module (P4) -- (depends on: Decompose the ETLAutomationSuite Design into Tasks)
5. Implement the Transformation Module (P4) -- (depends on: Implement the Extraction Module)
6. Database Schema Design (P5) -- (depends on: Implement the Transformation Module)
7. Implement the Loading Module (P4) -- (depends on: Implement the Transformation Module)
8. Testing ETLAutomationSuite (P2) -- (depends on: Implement the Extraction Module (COMPLETED), Implement the Transformation Module (COMPLETED), Implement the Loading Module (COMPLETED))
9. Deploy ETLAutomationSuite (P5) -- (depends on: Testing ETLAutomationSuite)
10. Review ETLAutomationSuite Deployment (P1) -- (depends on: Deploy ETLAutomationSuite)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ETLAutomationSuite can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A suite of tools for automating the Extract, Transform, Load (ETL) processes in data pipelines..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
