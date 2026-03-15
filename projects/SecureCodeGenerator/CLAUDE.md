# SecureCodeGenerator

You are a coding agent working on SecureCodeGenerator -- An AI system that assists developers in writing secure code by suggesting secure alternatives and best practices.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; SecureCodeGenerator captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop code analysis engine
- User interface: define project scope and requirements: securecodegenerator (updated)

## Anti-Goals

- **General-purpose platform**: SecureCodeGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: SecureCodeGenerator (Updated) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Code Analysis Engine (P3) -- (depends on: Design System Architecture)
4. Build Secure Code Suggestion Module (P3) -- (depends on: Design System Architecture)
5. Create User Interface (P3) -- (depends on: Design System Architecture)
6. Conduct Security Audits (P4) -- (depends on: Develop Code Analysis Engine, Build Secure Code Suggestion Module, Create User Interface)
7. Set up Testing and Continuous Integration (P3) -- (depends on: Develop Code Analysis Engine, Build Secure Code Suggestion Module, Create User Interface)
8. Integrate with Development Tools (P2) -- (depends on: Develop Code Analysis Engine, Build Secure Code Suggestion Module)
9. Deploy and Maintain System (P3) -- (depends on: Develop Code Analysis Engine, Build Secure Code Suggestion Module, Create User Interface, Integrate with Development Tools)
10. Prepare Documentation (P2) -- (depends on: Develop Code Analysis Engine, Build Secure Code Suggestion Module, Create User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SecureCodeGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that assists developers in writing secure code by suggesting secure alternatives and be.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
