# BrainStatesClassifier

You are a coding agent working on BrainStatesClassifier -- An AI-powered system that classifies various brain states for research and diagnostic purposes.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; BrainStatesClassifier models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data acquisition and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data acquisition and preprocessing

## Anti-Goals

- **General-purpose platform**: BrainStatesClassifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for BrainStatesClassifier Project (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Acquisition and Preprocessing (P3) -- (depends on: System Architecture Design)
4. AI Model Development (P3) -- (depends on: System Architecture Design, Data Acquisition and Preprocessing)
5. User Interface Design and Development (P3) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
7. Security and Compliance (P3) -- (depends on: System Architecture Design)
8. Integration and Testing (P2) -- (depends on: AI Model Development, User Interface Design and Development, Database Design and Implementation)
9. Deployment and Monitoring (P2) -- (depends on: Integration and Testing, Security and Compliance)
10. Documentation and User Training (P2) -- (depends on: User Interface Design and Development, Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainStatesClassifier can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust
- Docker
- Kubernetes
- AWS
- TensorFlow
- PyTorch
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered system that classifies various brain states for research and diagnostic purposes..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
