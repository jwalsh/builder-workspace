# BioLuminescent_StreetLights

You are a coding agent working on BioLuminescent_StreetLights -- Street lighting systems using engineered bioluminescent organisms, providing light without electricity consumption.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BioLuminescent_StreetLights embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: organism engineering and cultivation
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: BioLuminescent_StreetLights solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for BioLuminescent Street Lights (Revised) (P5) -- (depends on: Project Planning and Requirements Gathering, Bioluminescent Organism Research and Development, Regulatory and Environmental Impact Assessment, Energy Efficiency Research, Collaboration with Biotechnology Experts)
3. Organism Engineering and Cultivation (P4) -- (depends on: Project Planning and Requirements Gathering)
4. Security and Compliance (P4) -- (depends on: System Architecture Design)
5. Enclosure Design and Manufacturing (Revised) (P3) -- (depends on: System Architecture Design, Organism Selection and Cultivation, Regulatory Compliance and Safety Standards)
6. Control Systems Development (P3) -- (depends on: System Architecture Design)
7. User Interface and Visualization (P3) -- (depends on: System Architecture Design, Control Systems Development)
8. Testing and Quality Assurance (P3) -- (depends on: Organism Engineering and Cultivation, Enclosure Design and Manufacturing, Control Systems Development, User Interface and Visualization)
9. Deployment and Integration (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and Training (P2) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioLuminescent_StreetLights can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Street lighting systems using engineered bioluminescent organisms, providing light without electrici.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
