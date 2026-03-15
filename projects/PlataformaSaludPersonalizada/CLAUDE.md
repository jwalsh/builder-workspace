# PlataformaSaludPersonalizada

You are a coding agent working on PlataformaSaludPersonalizada -- Una plataforma que utiliza IA para proporcionar atención médica personalizada basada en datos genéticos.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; PlataformaSaludPersonalizada embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for genetic data processing
- User interface: define project scope and requirements
- Data layer: design genetic data collection system

## Anti-Goals

- **General-purpose platform**: PlataformaSaludPersonalizada solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Genetic Data Collection System (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Backend Services for Genetic Data Processing (P4) -- (depends on: Design Genetic Data Collection System)
4. Integrate AI Models for Personalized Healthcare Recommendations (P5) -- (depends on: Implement Backend Services for Genetic Data Processing)
5. Develop Frontend Interface for Genetic Data Input (P3) -- (depends on: Design Genetic Data Collection System)
6. Create Database Schema and Setup Storage Solutions (P2) -- (depends on: Design Genetic Data Collection System)
7. Perform Security Audit of the Entire System (P4) -- (depends on: Design Genetic Data Collection System, Develop Frontend Interface for Genetic Data Input, Implement Backend Services for Genetic Data Processing, Integrate AI Models for Personalized Healthcare Recommendations, Create Database Schema and Setup Storage Solutions)
8. Develop Unit and Integration Tests for Each Component (P3) -- (depends on: Develop Frontend Interface for Genetic Data Input, Implement Backend Services for Genetic Data Processing, Integrate AI Models for Personalized Healthcare Recommendations, Create Database Schema and Setup Storage Solutions)
9. Document System Architecture and API Documentation (P2) -- (depends on: Design Genetic Data Collection System, Develop Frontend Interface for Genetic Data Input, Implement Backend Services for Genetic Data Processing, Integrate AI Models for Personalized Healthcare Recommendations, Create Database Schema and Setup Storage Solutions)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlataformaSaludPersonalizada can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una plataforma que utiliza IA para proporcionar atención médica personalizada basada en datos genéti.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
