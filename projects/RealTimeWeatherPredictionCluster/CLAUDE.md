# RealTimeWeatherPredictionCluster

You are a coding agent working on RealTimeWeatherPredictionCluster -- A distributed system for real-time weather prediction using data from global weather stations and satellites, running complex meteorological models.

## Foundational Axiom

Existing approaches to distributed system fail because they optimize for the common case while ignoring structural constraints; RealTimeWeatherPredictionCluster makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A distributed system for real-time weather prediction using data from global weather stations and sa
- User interface: design user interface for realtimeweatherpredictioncluster
- Data layer: develop data acquisition module

## Anti-Goals

- **General-purpose platform**: RealTimeWeatherPredictionCluster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design User Interface for RealTimeWeatherPredictionCluster (P5) -- (depends on: Define System Architecture)
3. Implement DevOps for Deployment and Scaling (P5) -- (depends on: Define System Architecture)
4. Secure System Against Potential Threats (P5) -- (depends on: Define System Architecture)
5. Develop Data Acquisition Module (P2) -- (depends on: Define System Architecture)
6. Implement Meteorological Models for RealTimeWeatherPredictionCluster (P3) -- (depends on: Define System Architecture)
7. Create Real-Time Prediction Algorithm (P4) -- (depends on: Develop Data Acquisition Module, Implement Meteorological Models)
8. Document System Design and Functionality (P4) -- (depends on: Define System Architecture)
9. Set Up Database and Data Storage for RealTimeWeatherPredictionCluster (P2) -- (depends on: Define System Architecture)
10. Conduct Quality Assurance Testing (P1) -- (depends on: Develop Data Acquisition Module, Implement Meteorological Models, Create Real-Time Prediction Algorithm, Design User Interface, Set Up Database and Data Storage, Implement DevOps for Deployment and Scaling)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeWeatherPredictionCluster can deliver its core value proposition as described
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

- MongoDB

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system for real-time weather prediction using data from global weather stations and sa.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
