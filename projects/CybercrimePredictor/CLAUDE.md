# CybercrimePredictor

You are a coding agent working on CybercrimePredictor -- An AI system that analyzes patterns in cyber activities to predict and prevent potential cybercrime incidents.

## Foundational Axiom

Security in ai system fails when it is bolted on after the fact; CybercrimePredictor makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that analyzes patterns in cyber activities to predict and prevent potential cybercrime 
- User interface: project planning and requirements gathering
- Data layer: data modeling and database design

## Anti-Goals

- **General-purpose platform**: CybercrimePredictor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for CybercrimePredictor (P1) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Compliance (P5) -- (depends on: System Architecture Design)
4. Data Modeling and Database Design (P3) -- (depends on: System Architecture Design, Data Ingestion and Processing Requirements)
5. Cybercrime Pattern Analysis and Prediction Algorithm Development (P4) -- (depends on: System Architecture Design, Data Modeling and Database Design)
6. User Interface Design and Development (P4) -- (depends on: System Architecture Design)
7. Testing and Quality Assurance (P5) -- (depends on: Cybercrime Pattern Analysis and Prediction Algorithm Development, User Interface Design and Development)
8. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
9. Documentation and User Training (P5) -- (depends on: User Interface Design and Development, Cybercrime Pattern Analysis and Prediction Algorithm Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CybercrimePredictor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that analyzes patterns in cyber activities to predict and prevent potential cybercrime .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
