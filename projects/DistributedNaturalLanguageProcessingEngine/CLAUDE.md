# DistributedNaturalLanguageProcessingEngine

You are a coding agent working on DistributedNaturalLanguageProcessingEngine -- A distributed system for processing and analyzing natural language at scale, suitable for large-scale text analytics and language model training.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; DistributedNaturalLanguageProcessingEngine embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend components (rfc-7185)
- User interface: requirements gathering and analysis
- Data layer: database design and integration

## Anti-Goals

- **General-purpose platform**: DistributedNaturalLanguageProcessingEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design Architecture for Distributed System (P2) -- (depends on: Requirements Gathering and Analysis)
3. Database Design and Integration (P3) -- (depends on: Design Architecture for Distributed System)
4. DevOps Configuration and Deployment (P5) -- (depends on: Backend Components Implementation, Frontend Interface Development, Database Design and Integration)
5. Documentation and Technical Writing (P5) -- (depends on: Frontend Interface Development)
6. Develop Frontend Interface (P4) -- (depends on: Design Architecture for Distributed System)
7. Security Review and Implementation (P4) -- (depends on: Backend Components Implementation)
8. Implement Backend Components (RFC-7185) (P3) -- (depends on: Design Architecture for Distributed System)
9. System Integration Testing (P3) -- (depends on: Backend Components Implementation, Frontend Interface Development)
10. Unit Testing (P2) -- (depends on: Backend Components Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedNaturalLanguageProcessingEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system for processing and analyzing natural language at scale, suitable for large-scal.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
