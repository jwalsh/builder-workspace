# AssistantAugmentationCognitif

You are a coding agent working on AssistantAugmentationCognitif -- Un système d'interface cerveau-ordinateur qui améliore les capacités cognitives humaines en temps réel.

## Foundational Axiom

Existing approaches to un système d'interface cerveau-ordinateur qui améliore les c fail because they optimize for the common case while ignoring structural constraints; AssistantAugmentationCognitif makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop signal processing and cognitive enhancement algorithms
- User interface: define project scope and requirements - brain-computer interface system
- Data layer: develop data storage and management system

## Anti-Goals

- **General-purpose platform**: AssistantAugmentationCognitif solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Brain-Computer Interface System (P5)
2. Research and Evaluate Existing Technologies (P4)
3. Design System Architecture for AssistantAugmentationCognitif Project: Real-Time Cognitive Enhancement System (P4) -- (depends on: Define Project Scope and Requirements, Research and Evaluate Existing Technologies)
4. Develop Signal Processing and Cognitive Enhancement Algorithms (P3) -- (depends on: Design System Architecture)
5. Design and Implement User Interface (P3) -- (depends on: Design System Architecture)
6. Develop Data Storage and Management System (P3) -- (depends on: Design System Architecture)
7. Implement Security and Privacy Measures (P2) -- (depends on: Design System Architecture)
8. Integrate System Components (P2) -- (depends on: Develop Signal Processing and Cognitive Enhancement Algorithms, Design and Implement User Interface, Develop Data Storage and Management System, Implement Security and Privacy Measures)
9. Develop Comprehensive Testing and Quality Assurance Plan for Assistant Augmentation Cognitif System (P2) -- (depends on: Design System Architecture)
10. Conduct System Testing and Validation (P2) -- (depends on: Integrate System Components, Develop Testing and Quality Assurance Plan)
11. Prepare System for Deployment (P2) -- (depends on: Conduct System Testing and Validation)
12. Develop User Documentation and Training Materials (P2) -- (depends on: Integrate System Components, Conduct System Testing and Validation)
13. Deploy and Monitor System (P1) -- (depends on: Prepare System for Deployment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AssistantAugmentationCognitif can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un système d'interface cerveau-ordinateur qui améliore les capacités cognitives humaines en temps ré.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
