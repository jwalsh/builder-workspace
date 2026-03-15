# ArtificialPhotosynthesisPanel

You are a coding agent working on ArtificialPhotosynthesisPanel -- Panels that mimic and improve upon natural photosynthesis, converting sunlight, water, and CO2 into energy and oxygen.

## Foundational Axiom

Existing approaches to panels fail because they optimize for the common case while ignoring structural constraints; ArtificialPhotosynthesisPanel makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Panels that mimic and improve upon natural photosynthesis, converting sunlight, water, and CO2 into 
- User interface: define project scope and requirements
- Data layer: implement energy conversion and storage

## Anti-Goals

- **General-purpose platform**: ArtificialPhotosynthesisPanel solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design Artificial Photosynthesis Panel System (P5) -- (depends on: Define Project Scope and Requirements, Conduct Research on Artificial Photosynthesis Techniques)
3. Develop Panel Manufacturing Process (P3) -- (depends on: Design Artificial Photosynthesis Panel System)
4. Implement Energy Conversion and Storage (P3) -- (depends on: Design Artificial Photosynthesis Panel System)
5. Develop Monitoring and Control Systems (P3) -- (depends on: Design Artificial Photosynthesis Panel System)
6. Implement Security and Access Controls (P2) -- (depends on: Design Artificial Photosynthesis Panel System)
7. Conduct Performance and Efficiency Testing (P2) -- (depends on: Develop Panel Manufacturing Process, Implement Energy Conversion and Storage, Develop Monitoring and Control Systems)
8. Develop Deployment and Maintenance Strategies (P2) -- (depends on: Conduct Performance and Efficiency Testing)
9. Create User Documentation and Training Materials (P2) -- (depends on: Develop Deployment and Maintenance Strategies)
10. Plan and Execute Pilot Deployment (P1) -- (depends on: Conduct Performance and Efficiency Testing, Develop Deployment and Maintenance Strategies, Create User Documentation and Training Materials)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ArtificialPhotosynthesisPanel can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Panels that mimic and improve upon natural photosynthesis, converting sunlight, water, and CO2 into .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
