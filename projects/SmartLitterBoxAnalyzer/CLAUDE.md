# SmartLitterBoxAnalyzer

You are a coding agent working on SmartLitterBoxAnalyzer -- An IoT-enabled litter box that analyzes pet waste for early detection of health issues and provides regular health reports to owners and veterinarians.

## Foundational Axiom

Existing approaches to iot-enabled litter box fail because they optimize for the common case while ignoring structural constraints; SmartLitterBoxAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements - revised
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: SmartLitterBoxAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Design Database Schema (P3) -- (depends on: Design System Architecture)
4. Develop Backend Services (P2) -- (depends on: Design System Architecture, Design Database Schema)
5. Develop Frontend Application (P2) -- (depends on: Design System Architecture)
6. Implement Security Measures (P4) -- (depends on: Develop Backend Services, Develop Frontend Application)
7. Implement IoT Device Integration (P3) -- (depends on: Develop Backend Services)
8. Set up CI/CD Pipeline (P3) -- (depends on: Develop Backend Services, Develop Frontend Application)
9. Write Documentation (P2) -- (depends on: Define Project Requirements, Design System Architecture)
10. Conduct Testing (P1) -- (depends on: Develop Backend Services, Develop Frontend Application, Implement IoT Device Integration)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartLitterBoxAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An IoT-enabled litter box that analyzes pet waste for early detection of health issues and provides .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
