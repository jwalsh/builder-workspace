# QuantenbasierteFinanzmodellierung

You are a coding agent working on QuantenbasierteFinanzmodellierung -- Ein System zur Finanzmodellierung und Risikoanalyse unter Verwendung von Quantenalgorithmen für komplexe Marktszenarien.

## Foundational Axiom

Existing approaches to ein system zur finanzmodellierung und risikoanalyse unter ve fail because they optimize for the common case while ignoring structural constraints; QuantenbasierteFinanzmodellierung makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for quantum model
- User interface: define project scope and requirements - revised
- Data layer: integrate databases for data storage

## Anti-Goals

- **General-purpose platform**: QuantenbasierteFinanzmodellierung solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Research Quantum Algorithms for Financial Scenarios (P2) -- (depends on: Define Project Scope and Requirements)
3. Design Quantum Financial Model Architecture (P3) -- (depends on: Research Quantum Algorithms for Financial Scenarios, Define Project Scope and Requirements)
4. Implement Backend Services for Quantum Model (P5) -- (depends on: Design Quantum Financial Model Architecture)
5. Develop Frontend Interface (P4) -- (depends on: Design Quantum Financial Model Architecture)
6. Integrate Databases for Data Storage (P4) -- (depends on: Design Quantum Financial Model Architecture)
7. Configure DevOps and Deployment Strategy (P3) -- (depends on: Design Quantum Financial Model Architecture)
8. Perform Unit Testing for Components (P2) -- (depends on: Implement Backend Services for Quantum Model, Develop Frontend Interface)
9. Review and Approve RFCs (P1) -- (depends on: Define Project Scope and Requirements, Research Quantum Algorithms for Financial Scenarios)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantenbasierteFinanzmodellierung can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Ein System zur Finanzmodellierung und Risikoanalyse unter Verwendung von Quantenalgorithmen für komp.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to financial analysts and portfolio managers.
