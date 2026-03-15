# BrainwaveVirtualAssistant

You are a coding agent working on BrainwaveVirtualAssistant -- A virtual assistant that responds to thought commands and adapts to the user's cognitive patterns.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; BrainwaveVirtualAssistant models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integration with external services
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: BrainwaveVirtualAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Brain-Computer Interface Development (P5) -- (depends on: System Architecture Design)
4. Machine Learning Model Development (P5) -- (depends on: System Architecture Design)
5. Security and Privacy Implementation (P5) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P4) -- (depends on: System Architecture Design)
7. User Interface Design (P3) -- (depends on: Project Planning and Requirements Gathering)
8. Integration with External Services (P3) -- (depends on: System Architecture Design)
9. Testing and Quality Assurance (P4) -- (depends on: User Interface Design, Brain-Computer Interface Development, Machine Learning Model Development, Database Design and Implementation, Integration with External Services, Security and Privacy Implementation)
10. Deployment and DevOps (P3) -- (depends on: Testing and Quality Assurance)
11. Documentation and User Support (P3) -- (depends on: User Interface Design, Brain-Computer Interface Development, Machine Learning Model Development, Database Design and Implementation, Integration with External Services, Security and Privacy Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainwaveVirtualAssistant can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A virtual assistant that responds to thought commands and adapts to the user's cognitive patterns..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
