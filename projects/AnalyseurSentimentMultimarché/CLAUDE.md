# AnalyseurSentimentMultimarché

You are a coding agent working on AnalyseurSentimentMultimarché -- Un outil d'analyse de sentiment multilingue pour les entreprises opérant sur des marchés internationaux.

## Foundational Axiom

Existing approaches to un outil d'analyse de sentiment multilingue pour les entrepr fail because they optimize for the common case while ignoring structural constraints; AnalyseurSentimentMultimarché makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: system architecture design for multilingual sentiment analysis tool with improvements: microservices approach
- User interface: requirements gathering and analysis
- Data layer: database design for multilingual sentiment analysis tool (revised)

## Anti-Goals

- **General-purpose platform**: AnalyseurSentimentMultimarché solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation (P5)
2. Requirements Gathering and Analysis (P5) -- (depends on: Project Initiation)
3. System Architecture Design for Multilingual Sentiment Analysis Tool with Improvements: Microservices Approach (P3) -- (depends on: Requirements Gathering and Analysis)
4. User Interface Design for Multilingual Sentiment Analysis Tool with Accessibility Focus - Revised (P3) -- (depends on: System Architecture Design, Multilingual Support Design)
5. Database Design for Multilingual Sentiment Analysis Tool (Revised) (P3) -- (depends on: System Architecture Design)
6. Data Pipeline Design for Multilingual Sentiment Analysis Tool (P2) -- (depends on: System Architecture Design)
7. Sentiment Analysis Model Development (P2) -- (depends on: Data Pipeline Design)
8. DevOps and Deployment for Multilingual Sentiment Analysis Tool (P2) -- (depends on: System Architecture Design)
9. DevOps and Deployment (P2) -- (depends on: System Architecture Design)
10. Testing and Quality Assurance (P2) -- (depends on: User Interface Design, Sentiment Analysis Model Development, Database Design, DevOps and Deployment)
11. Documentation and Training (P2) -- (depends on: User Interface Design, Sentiment Analysis Model Development, Database Design, DevOps and Deployment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AnalyseurSentimentMultimarché can deliver its core value proposition as described
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

- PostgreSQL
- MongoDB
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un outil d'analyse de sentiment multilingue pour les entreprises opérant sur des marchés internation.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
