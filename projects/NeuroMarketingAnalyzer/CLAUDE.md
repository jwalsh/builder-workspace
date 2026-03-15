# NeuroMarketingAnalyzer

You are a coding agent working on NeuroMarketingAnalyzer -- An ethical neuromarketing tool that analyzes consumer brain responses to products and advertisements.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroMarketingAnalyzer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for data processing
- User interface: define project scope and requirements - revised
- Data layer: implement backend services for data processing

## Anti-Goals

- **General-purpose platform**: NeuroMarketingAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Design NeuroMarketingAnalyzer Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface for User Input (P3) -- (depends on: Design NeuroMarketingAnalyzer Architecture)
4. Implement Backend Services for Data Processing (P3) -- (depends on: Design NeuroMarketingAnalyzer Architecture)
5. Integrate Frontend with Backend Services (P4) -- (depends on: Develop Frontend Interface for User Input, Implement Backend Services for Data Processing)
6. Test and Validate NeuroMarketingAnalyzer (P4) -- (depends on: Integrate Frontend with Backend Services)
7. Document NeuroMarketingAnalyzer Functionality and Usage (P5) -- (depends on: Test and Validate NeuroMarketingAnalyzer)
8. Setup Database for Data Storage and Management (P3) -- (depends on: Design NeuroMarketingAnalyzer Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroMarketingAnalyzer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An ethical neuromarketing tool that analyzes consumer brain responses to products and advertisements.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
