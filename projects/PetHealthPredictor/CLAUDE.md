# PetHealthPredictor

You are a coding agent working on PetHealthPredictor -- An AI-driven system that predicts pet health issues based on behavioral patterns, diet, and environmental factors captured through smart collars and home sensors.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; PetHealthPredictor embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data ingestion and preprocessing
- User interface: define comprehensive scope and requirements for pethealthpredictor system (revised)
- Data layer: implement data ingestion and preprocessing

## Anti-Goals

- **General-purpose platform**: PetHealthPredictor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Comprehensive Scope and Requirements for PetHealthPredictor System (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Implement Data Ingestion and Preprocessing (P2) -- (depends on: Design System Architecture)
5. Develop Machine Learning Models (P2) -- (depends on: Implement Data Ingestion and Preprocessing)
6. Build User Interface (P2) -- (depends on: Design System Architecture)
7. Integrate System Components (P2) -- (depends on: Implement Data Ingestion and Preprocessing, Develop Machine Learning Models, Build User Interface)
8. Conduct Security Audit (P3) -- (depends on: Integrate System Components)
9. Write Documentation (P3) -- (depends on: Integrate System Components)
10. Test and Validate System (P2) -- (depends on: Integrate System Components)
11. Deploy and Monitor System (P2) -- (depends on: Test and Validate System, Conduct Security Audit)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PetHealthPredictor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-driven system that predicts pet health issues based on behavioral patterns, diet, and environm.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
