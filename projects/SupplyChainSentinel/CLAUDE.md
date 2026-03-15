# SupplyChainSentinel

You are a coding agent working on SupplyChainSentinel -- Monitor and optimize global supply chains using IoT sensors, blockchain for traceability, and AI for predictive analytics.

## Foundational Axiom

Existing approaches to monitor and optimize global supply chains using iot sensors, blockchain fail because they optimize for the common case while ignoring structural constraints; SupplyChainSentinel makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Monitor and optimize global supply chains using IoT sensors, blockchain for traceability, and AI for
- User interface: define project scope and requirements - revised
- Data layer: implement iot sensor data ingestion

## Anti-Goals

- **General-purpose platform**: SupplyChainSentinel solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Implement IoT Sensor Data Ingestion (P4) -- (depends on: Design System Architecture, Set up Development Environment)
5. Integrate Blockchain for Traceability (P4) -- (depends on: Design System Architecture, Set up Development Environment)
6. Develop AI Models for Predictive Analytics (P4) -- (depends on: Design System Architecture, Set up Development Environment)
7. Design and Implement User Interfaces (P4) -- (depends on: Design System Architecture, Set up Development Environment)
8. Conduct Security Audits (P5) -- (depends on: Implement IoT Sensor Data Ingestion, Integrate Blockchain for Traceability, Develop AI Models for Predictive Analytics, Design and Implement User Interfaces)
9. Implement Testing and Quality Assurance (P5) -- (depends on: Implement IoT Sensor Data Ingestion, Integrate Blockchain for Traceability, Develop AI Models for Predictive Analytics, Design and Implement User Interfaces)
10. Deploy and Monitor System (P5) -- (depends on: Conduct Security Audits, Implement Testing and Quality Assurance)
11. Create Documentation and Training Materials (P5) -- (depends on: Design System Architecture, Implement IoT Sensor Data Ingestion, Integrate Blockchain for Traceability, Develop AI Models for Predictive Analytics, Design and Implement User Interfaces)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SupplyChainSentinel can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Monitor and optimize global supply chains using IoT sensors, blockchain for traceability, and AI for.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
