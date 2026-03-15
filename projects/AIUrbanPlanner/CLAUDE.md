# AIUrbanPlanner

You are a coding agent working on AIUrbanPlanner -- An AI system that optimizes urban housing development, considering factors like population growth, environmental impact, and quality of life metrics.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AIUrbanPlanner makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that optimizes urban housing development, considering factors like population growth, e
- User interface: define project requirements (revised)
- Data layer: design scalable data model for urban planning data storage and management (revised)

## Anti-Goals

- **General-purpose platform**: AIUrbanPlanner solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (Revised) (P5)
2. DesignSystemArchitectureforAIUrbanPlanner:Revised (P5) -- (depends on: DefineProjectRequirements, GatherDataSources)
3. Implement Comprehensive Security Measures (Updated) (P5) -- (depends on: Design System Architecture (with security considerations), Define Data Models (with provisions for secure data storage and handling, secure handling, and regular backups))
4. Design Scalable Data Model for Urban Planning Data Storage and Management (Revised) (P4) -- (depends on: Design System Architecture)
5. Develop AI Optimization Algorithms (P3) -- (depends on: Design System Architecture, Design Data Model)
6. Implement User Interface (P3) -- (depends on: Design System Architecture)
7. Create Comprehensive Test Suite (Updated) (P3) -- (depends on: Design System Architecture)
8. Set up CI/CD Pipeline with enhanced security measures (Revised) (P2) -- (depends on: Design System Architecture, Set up Version Control System)
9. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIUrbanPlanner can deliver its core value proposition as described
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
- PostgreSQL
- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that optimizes urban housing development, considering factors like population growth, e.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
