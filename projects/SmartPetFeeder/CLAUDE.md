# SmartPetFeeder

You are a coding agent working on SmartPetFeeder, an IoT-enabled pet feeder that adjusts portion sizes and feeding schedules based on pet activity levels, health conditions, and owner-set goals.

## Foundational Axiom

Existing approaches to IoT-enabled pet feeders fail because they optimize for the common case while ignoring structural constraints; SmartPetFeeder makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in full.
2. You understand the build order and dependencies.
3. You will not skip a failing acceptance test.

## What You Are Building

- An IoT backend (Python) that ingests pet activity data and computes adaptive feeding schedules and portion sizes.
- A secure API layer with authentication, authorization, and encrypted communication for device and client interaction.
- Mobile/web frontend applications for pet owners and veterinary professionals to monitor and configure feeding behavior.

## Anti-Goals

- **General-purpose platform**: Solve the specific feeding-adaptation problem, not a platform for all pet IoT.
- **Manual-first workflow**: If a human must babysit routine operations, the automation has failed.
- **Demo-ware**: Optimize for production reliability, not impressive demos that break under real conditions.

## Build Order

1. Define Project Requirements (Revised) -- priority 5
2. Design System Architecture -- priority 4, depends on (1)
3. Implement Security Measures -- priority 4, depends on (2)
4. Design User Interface -- priority 3, depends on (1)
5. Develop Backend Services -- priority 3, depends on (2)
6. Develop Frontend Applications -- priority 3, depends on (4)
7. Set up Database and Data Storage -- priority 3, depends on (2)
8. Set up Continuous Integration and Deployment -- priority 3
9. Conduct Testing and Quality Assurance -- priority 3, depends on (5, 6)
10. Write Documentation and User Guides -- priority 2, depends on (1, 4)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartPetFeeder can deliver its core value proposition as described.
  - Falsification: Integration test of end-to-end workflow fails to produce expected output.
- **C-002**: AI/ML components achieve sufficient accuracy for production use.
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold.
- **C-003**: System meets real-time latency requirements under load.
  - Falsification: P95 latency exceeds target under simulated production load.
- **C-004**: Architecture scales horizontally to meet projected demand.
  - Falsification: Load test shows non-linear degradation before target throughput.
- **C-005**: Security implementation meets compliance requirements.
  - Falsification: Penetration test or security audit reveals critical vulnerability.

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: adaptive feeding based on pet activity and health.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
