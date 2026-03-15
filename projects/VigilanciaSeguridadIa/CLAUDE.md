# VigilanciaSeguridadIa

You are a coding agent working on VigilanciaSeguridadIa -- Un sistema de IA para detectar y prevenir amenazas de seguridad de manera autónoma.

## Foundational Axiom

Existing approaches to un sistema de ia para detectar y prevenir amenazas de seguri fail because they optimize for the common case while ignoring structural constraints; VigilanciaSeguridadIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un sistema de IA para detectar y prevenir amenazas de seguridad de manera autónoma.
- User interface: create user interface for system management

## Anti-Goals

- **General-purpose platform**: VigilanciaSeguridadIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop AI Algorithm for Threat Detection (P2) -- (depends on: Define System Architecture)
3. Develop Algorithm for Threat Prevention (P5) -- (depends on: Develop AI Algorithm for Threat Detection)
4. Create User Interface for System Management (P4) -- (depends on: Define System Architecture)
5. Implement Real-time Monitoring Capabilities (with improvements) (P3) -- (depends on: Define System Architecture)
6. Perform System Testing and Integration (P2) -- (depends on: Develop AI Algorithm for Threat Detection, Implement Real-time Monitoring Capabilities, Create User Interface for System Management, Develop Algorithm for Threat Prevention)
7. Document the System Design and Implementation (P3) -- (depends on: Define System Architecture, Develop AI Algorithm for Threat Detection, Implement Real-time Monitoring Capabilities, Create User Interface for System Management, Develop Algorithm for Threat Prevention, Perform System Testing and Integration)
8. Implement Comprehensive Security Measures (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VigilanciaSeguridadIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema de IA para detectar y prevenir amenazas de seguridad de manera autónoma..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
