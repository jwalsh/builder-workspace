# AI-PoweredRetailAnalytics

You are a coding agent working on AI-PoweredRetailAnalytics -- An AI-driven platform that analyzes retail trends and customer behavior to optimize inventory.

## Foundational Axiom

Existing tools treat ai-driven platform as a generic automation problem; AI-PoweredRetailAnalytics succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data ingestion and processing
- User interface: defineprojectscopeandrequirements-ai-drivenretailanalyticsplatform
- Data layer: implement data ingestion and processing

## Anti-Goals

- **General-purpose platform**: AI-PoweredRetailAnalytics solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. DefineProjectScopeandRequirements-AI-DrivenRetailAnalyticsPlatform (P5)
2. Design System Architecture for AI-Powered Retail Analytics Platform - REVISED (P5) -- (depends on: Define Project Scope and Requirements, Gather Business Requirements and Constraints, Incorporate Real-time Analytics and Edge Computing in Design)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Implement Security and Access Controls (P3) -- (depends on: Design System Architecture)
5. Implement Data Ingestion and Processing (P2) -- (depends on: Design System Architecture)
6. Build AI Models for Trend Analysis (P2) -- (depends on: Implement Data Ingestion and Processing)
7. Create User Interfaces (P2) -- (depends on: Design System Architecture)
8. Set up Testing and Quality Assurance (P3) -- (depends on: Implement Data Ingestion and Processing, Build AI Models for Trend Analysis, Create User Interfaces)
9. Write Documentation and User Guides (P3) -- (depends on: Create User Interfaces)
10. Deploy and Monitor the Platform (P2) -- (depends on: Implement Security and Access Controls, Set up Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AI-PoweredRetailAnalytics can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-driven platform that analyzes retail trends and customer behavior to optimize inventory..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
