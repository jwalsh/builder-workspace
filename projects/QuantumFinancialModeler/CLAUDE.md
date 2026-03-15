# QuantumFinancialModeler

You are a coding agent working on QuantumFinancialModeler -- Create quantum algorithms for financial modeling and risk analysis, leveraging quantum speedup for complex market simulations.

## Foundational Axiom

Existing approaches to create quantum algorithms fail because they optimize for the common case while ignoring structural constraints; QuantumFinancialModeler makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Create quantum algorithms for financial modeling and risk analysis, leveraging quantum speedup for c
- User interface: project planning and requirements gathering
- Data layer: data preparation and integration

## Anti-Goals

- **General-purpose platform**: QuantumFinancialModeler solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Quantum Algorithm Implementation (P4) -- (depends on: Quantum Algorithm Research and Design)
2. Project Planning and Requirements Gathering (P1)
3. User Interface and Visualization (P4) -- (depends on: Project Planning and Requirements Gathering)
4. Data Preparation and Integration (P3) -- (depends on: Project Planning and Requirements Gathering)
5. Testing and Validation (P4) -- (depends on: Quantum Algorithm Implementation, Data Preparation and Integration)
6. Security and Compliance (P4) -- (depends on: Project Planning and Requirements Gathering)
7. Deployment and Integration (P5) -- (depends on: Quantum Algorithm Implementation, User Interface and Visualization, Testing and Validation, Security and Compliance)
8. Documentation and Training (P5) -- (depends on: Quantum Algorithm Implementation, User Interface and Visualization)
9. Quantum Computing Infrastructure Setup (P3) -- (depends on: Project Planning and Requirements Gathering)
10. QuantumAlgorithmResearchandDesign(Updated) (P2) -- (depends on: ProjectPlanningandRequirementsGathering)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumFinancialModeler can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Create quantum algorithms for financial modeling and risk analysis, leveraging quantum speedup for c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to financial analysts and portfolio managers.
