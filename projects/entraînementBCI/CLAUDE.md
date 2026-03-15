# entraînementBCI

You are a coding agent working on entraînementBCI -- Une plateforme BCI dédiée à l'accélération de l'apprentissage et de l'acquisition de compétences.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; entraînementBCI models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for data processing
- User interface: develop frontend interface for user interaction
- Data layer: set up database and data storage solutions

## Anti-Goals

- **General-purpose platform**: entraînementBCI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals (P1)
2. Design BCI Platform Architecture (P2) -- (depends on: Define Project Scope and Goals)
3. Set Up Database and Data Storage Solutions (P5) -- (depends on: Design BCI Platform Architecture)
4. Implement Backend Services for Data Processing (P4) -- (depends on: Design BCI Platform Architecture)
5. Develop Frontend Interface for User Interaction (P3) -- (depends on: Design BCI Platform Architecture)
6. Create Comprehensive Technical Documentation for the BCI Platform (P4) -- (depends on: Develop Frontend Interface for User Interaction, Implement Backend Services for Data Processing)
7. Integrate DevOps Practices for Continuous Deployment (P1) -- (depends on: Define Project Scope and Goals, Design BCI Platform Architecture)
8. Conduct Security Audit of the Platform (P3) -- (depends on: Set Up Database and Data Storage Solutions, Integrate DevOps Practices for Continuous Deployment)
9. Perform Quality Assurance Testing on the Platform (P2) -- (depends on: Develop Frontend Interface for User Interaction, Implement Backend Services for Data Processing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: entraînementBCI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une plateforme BCI dédiée à l'accélération de l'apprentissage et de l'acquisition de compétences..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
