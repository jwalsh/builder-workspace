# réseauÉnergieAutonome

You are a coding agent working on réseauÉnergieAutonome -- Un réseau autonome qui redistribue l'énergie en temps réel, réduisant les pertes et augmentant l'efficacité.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; réseauÉnergieAutonome maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop energy management software
- User interface: create user interface for monitoring and control - rfc review

## Anti-Goals

- **General-purpose platform**: réseauÉnergieAutonome solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Real-time Energy Distribution System (P2) -- (depends on: Define System Architecture)
3. Implement Loss Reduction Techniques (P5) -- (depends on: Design Real-time Energy Distribution System)
4. Develop Energy Management Software (P3) -- (depends on: Design Real-time Energy Distribution System)
5. Create User Interface for Monitoring and Control - RFC Review (P4) -- (depends on: Develop Energy Management Software)
6. Write User Manual and Technical Documentation (P2) -- (depends on: Develop Energy Management Software, Create User Interface for Monitoring and Control)
7. Conduct System Audit and Security Assessment (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: réseauÉnergieAutonome can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Redis

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un réseau autonome qui redistribue l'énergie en temps réel, réduisant les pertes et augmentant l'eff.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
