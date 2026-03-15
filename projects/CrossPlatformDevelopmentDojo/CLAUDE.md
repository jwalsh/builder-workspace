# CrossPlatformDevelopmentDojo

You are a coding agent working on CrossPlatformDevelopmentDojo -- An environment for learning cross-platform development techniques, with challenges spanning multiple operating systems and devices.

## Foundational Axiom

Existing approaches to environment fail because they optimize for the common case while ignoring structural constraints; CrossPlatformDevelopmentDojo makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An environment for learning cross-platform development techniques, with challenges spanning multiple
- User interface: define project scope and requirements: crossplatformdevelopmentdojo (updated)

## Anti-Goals

- **General-purpose platform**: CrossPlatformDevelopmentDojo solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: CrossPlatformDevelopmentDojo (Updated) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Implement Core Functionality (P4) -- (depends on: Set up Development Environment)
5. Integrate Cross-Platform Frameworks (P4) -- (depends on: Set up Development Environment)
6. Implement Challenge Management (P4) -- (depends on: Integrate Cross-Platform Frameworks)
7. Set up Testing Framework (P4) -- (depends on: Implement Core Functionality, Integrate Cross-Platform Frameworks)
8. Implement Security Measures (P4) -- (depends on: Implement Core Functionality, Integrate Cross-Platform Frameworks)
9. Create Documentation (P4) -- (depends on: Implement Core Functionality, Integrate Cross-Platform Frameworks)
10. Deploy and Release (P5) -- (depends on: Implement Core Functionality, Integrate Cross-Platform Frameworks, Implement Challenge Management, Set up Testing Framework, Implement Security Measures, Create Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossPlatformDevelopmentDojo can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An environment for learning cross-platform development techniques, with challenges spanning multiple.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
