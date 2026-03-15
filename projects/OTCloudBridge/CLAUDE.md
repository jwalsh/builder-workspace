# OTCloudBridge

You are a coding agent working on OTCloudBridge -- Securely extend operational technology data centers into the cloud for ingestion and analysis of critical infrastructure data.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; OTCloudBridge models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Securely extend operational technology data centers into the cloud for ingestion and analysis of cri
- User interface: implement data analysis and visualization
- Data layer: develop data transfer and ingestion components

## Anti-Goals

- **General-purpose platform**: OTCloudBridge solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design System Architecture for OTCloudBridge (Revised and Enhanced) (P2) -- (depends on: Define Project Scope and Requirements)
2. Implement Security and Compliance Measures (P3) -- (depends on: Design System Architecture)
3. Develop Data Transfer and Ingestion Components (P4) -- (depends on: Design System Architecture, Implement Security and Compliance Measures)
4. Implement Data Analysis and Visualization (P4) -- (depends on: Design System Architecture, Develop Data Transfer and Ingestion Components)
5. Build User Interfaces and Dashboards (P4) -- (depends on: Design System Architecture, Implement Data Analysis and Visualization)
6. Set up Cloud Infrastructure and Deployment (P4) -- (depends on: Design System Architecture)
7. Conduct Testing and Quality Assurance (P5) -- (depends on: Develop Data Transfer and Ingestion Components, Implement Data Analysis and Visualization, Build User Interfaces and Dashboards, Set up Cloud Infrastructure and Deployment)
8. Prepare Documentation and User Guides (P5) -- (depends on: Design System Architecture, Implement Security and Compliance Measures, Develop Data Transfer and Ingestion Components, Implement Data Analysis and Visualization, Build User Interfaces and Dashboards, Set up Cloud Infrastructure and Deployment)
9. Define Comprehensive Project Scope and Requirements (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OTCloudBridge can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Securely extend operational technology data centers into the cloud for ingestion and analysis of cri.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
