# SmartGunTechnology

You are a coding agent working on SmartGunTechnology -- Firearms with integrated biometric authentication to prevent unauthorized use and track discharge events.

## Foundational Axiom

Existing approaches to firearms with integrated biometric authentication fail because they optimize for the common case while ignoring structural constraints; SmartGunTechnology makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Firearms with integrated biometric authentication to prevent unauthorized use and track discharge ev
- User interface: project planning and requirements gathering
- Data layer: secure database design and implementation for smartguntechnology

## Anti-Goals

- **General-purpose platform**: SmartGunTechnology solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering, Legal and Regulatory Review, Ethical and Social Impact Assessment)
3. Secure Database Design and Implementation for SmartGunTechnology (P5) -- (depends on: System Architecture Design, Security and Privacy Requirements Analysis)
4. Security and Compliance (P4) -- (depends on: System Architecture Design)
5. Biometric Authentication Module (P3) -- (depends on: System Architecture Design)
6. Firearm Integration (P3) -- (depends on: System Architecture Design)
7. Event Tracking and Logging (P3) -- (depends on: System Architecture Design)
8. User Interface and Reporting (P2) -- (depends on: System Architecture Design, Database Design and Implementation)
9. Testing and Quality Assurance (P3) -- (depends on: Biometric Authentication Module, Firearm Integration, Event Tracking and Logging, User Interface and Reporting)
10. Deployment and Operations (P2) -- (depends on: Testing and Quality Assurance)
11. Documentation and Training (P2) -- (depends on: User Interface and Reporting, Deployment and Operations)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartGunTechnology can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Firearms with integrated biometric authentication to prevent unauthorized use and track discharge ev.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
