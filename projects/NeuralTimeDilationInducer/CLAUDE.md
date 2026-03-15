# NeuralTimeDilationInducer

You are a coding agent working on NeuralTimeDilationInducer -- A device that attempts to induce subjective time dilation for enhanced productivity or experiences.

## Foundational Axiom

Existing tools treat device as a generic automation problem; NeuralTimeDilationInducer succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate hardware and software components
- User interface: project initiation and requirements gathering
- Data layer: implement database for device management and monitoring

## Anti-Goals

- **General-purpose platform**: NeuralTimeDilationInducer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation and Requirements Gathering (P1)
2. Design the Conceptual Architecture (P2) -- (depends on: Project Initiation and Requirements Gathering)
3. Implement Database for Device Management and Monitoring (P5) -- (depends on: Design the Conceptual Architecture)
4. Develop Neural Algorithms for Time Dilation (P3) -- (depends on: Design the Conceptual Architecture)
5. Create User Interface for Device Control (P4) -- (depends on: Design the Conceptual Architecture)
6. Integrate Hardware and Software Components (P2) -- (depends on: Develop Neural Algorithms for Time Dilation, Create User Interface for Device Control, Implement Database for Device Management and Monitoring)
7. Perform Unit Testing on Individual Components (P4) -- (depends on: Develop Neural Algorithms for Time Dilation, Create User Interface for Device Control, Implement Database for Device Management and Monitoring, Integrate Hardware and Software Components)
8. Perform System Integration Testing (P5) -- (depends on: Perform Unit Testing on Individual Components)
9. Document the Device and Its Usage (P3) -- (depends on: Integrate Hardware and Software Components)
10. Address Security Concerns (P2) -- (depends on: Integrate Hardware and Software Components)
11. Prepare for User Testing and Feedback (P1) -- (depends on: Perform System Integration Testing, Document the Device and Its Usage, Address Security Concerns)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralTimeDilationInducer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that attempts to induce subjective time dilation for enhanced productivity or experiences..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
