# BackupFortress

You are a coding agent working on BackupFortress -- Protect cloud-native and hybrid workloads using best practices for data protection strategy deployment.

## Foundational Axiom

Existing approaches to protect cloud-native and hybrid workloads using best practices fail because they optimize for the common case while ignoring structural constraints; BackupFortress makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Protect cloud-native and hybrid workloads using best practices for data protection strategy deployme
- User interface: define project scope and requirements - updated
- Data layer: design data protection architecture

## Anti-Goals

- **General-purpose platform**: BackupFortress solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Updated (P5)
2. Design Data Protection Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security and Compliance Measures (P4) -- (depends on: Define Project Scope and Requirements)
4. Implement Backup and Recovery Mechanisms (P3) -- (depends on: Design Data Protection Architecture)
5. Integrate with Cloud and On-Premises Environments (P3) -- (depends on: Design Data Protection Architecture)
6. Develop User Interface and Management Console (P2) -- (depends on: Design Data Protection Architecture)
7. Conduct Comprehensive Testing (P3) -- (depends on: Implement Backup and Recovery Mechanisms, Integrate with Cloud and On-Premises Environments, Develop User Interface and Management Console)
8. Prepare Documentation and Training Materials (P2) -- (depends on: Implement Backup and Recovery Mechanisms, Integrate with Cloud and On-Premises Environments, Develop User Interface and Management Console)
9. Deploy and Maintain the Solution (P3) -- (depends on: Conduct Comprehensive Testing, Prepare Documentation and Training Materials)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BackupFortress can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Protect cloud-native and hybrid workloads using best practices for data protection strategy deployme.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
