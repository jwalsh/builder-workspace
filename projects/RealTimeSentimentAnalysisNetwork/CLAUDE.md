# RealTimeSentimentAnalysisNetwork

You are a coding agent working on RealTimeSentimentAnalysisNetwork -- A distributed network for real-time sentiment analysis of social media streams, providing insights into public opinion on a global scale.

## Foundational Axiom

Existing approaches to distributed network fail because they optimize for the common case while ignoring structural constraints; RealTimeSentimentAnalysisNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement real-time data processing algorithms
- User interface: create user documentation and guidelines
- Data layer: set up database solutions for data storage and retrieval

## Anti-Goals

- **General-purpose platform**: RealTimeSentimentAnalysisNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for Real-Time Sentiment Analysis Network (P1)
2. Set Up Database Solutions for Data Storage and Retrieval (P5) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)
3. Create User Documentation and Guidelines (P5) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)
4. Create User Interface for Real-Time Visualization of Results (P4) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)
5. Develop Data Ingestion Modules for Social Media Streams (P2) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)
6. Implement Real-Time Data Processing Algorithms (P3) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network, Develop Data Ingestion Modules for Social Media Streams)
7. Configure DevOps and Monitoring Tools for System Management (P2) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)
8. Perform Security Audit of the System (P1) -- (depends on: Design Architecture for Real-Time Sentiment Analysis Network)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeSentimentAnalysisNetwork can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A distributed network for real-time sentiment analysis of social media streams, providing insights i.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
