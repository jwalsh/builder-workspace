# VRMortgageAdvisor

You are a coding agent working on VRMortgageAdvisor -- A virtual reality platform that guides users through the mortgage process, providing immersive financial education and personalized mortgage options.

## Foundational Axiom

Existing approaches to virtual reality platform fail because they optimize for the common case while ignoring structural constraints; VRMortgageAdvisor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A virtual reality platform that guides users through the mortgage process, providing immersive finan
- User interface: project planning and requirements gathering
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: VRMortgageAdvisor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Design Virtual Reality Environment for VRMortgageAdvisor (P5) -- (depends on: Project Planning and Requirements Gathering, Define User Personas and Journey Maps)
3. Develop Security and Privacy Measures (P5) -- (depends on: Project Planning and Requirements Gathering, Define Data Models and Storage)
4. Design and Implement VR Mortgage Advisor (P4) -- (depends on: Project Planning and Requirements Gathering, Design Virtual Reality Environment, Integrate with External Financial Data APIs)
5. Develop VR User Interface (P4) -- (depends on: Design Virtual Reality Environment)
6. Develop Financial Education Content (P3) -- (depends on: Project Planning and Requirements Gathering)
7. Implement Data Storage and Management (P3) -- (depends on: Project Planning and Requirements Gathering)
8. Testing and Quality Assurance (P3) -- (depends on: Develop VR User Interface, Design and Implement VR Mortgage Advisor, Develop Financial Education Content)
9. Deployment and DevOps (P3) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VRMortgageAdvisor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A virtual reality platform that guides users through the mortgage process, providing immersive finan.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
