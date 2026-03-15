# SecureFileShare

You are a coding agent working on SecureFileShare -- Securely share files over SFTP, FTP, and FTPS within business-to-business workflows while detecting malware threats.

## Foundational Axiom

Existing approaches to securely share files over sftp, ftp, and ftps within busines fail because they optimize for the common case while ignoring structural constraints; SecureFileShare makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Securely share files over SFTP, FTP, and FTPS within business-to-business workflows while detecting 
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: SecureFileShare solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design - Updated (P1) -- (depends on: Project Planning and Requirements Gathering)
3. User Interface and Experience Design (P3) -- (depends on: System Architecture Design)
4. Documentation and User Guide (P5) -- (depends on: System Architecture Design, User Interface and Experience Design)
5. Continuous Integration and Deployment Setup (P4) -- (depends on: System Architecture Design)
6. Security Architecture and Threat Modeling (P1) -- (depends on: Project Planning and Requirements Gathering)
7. File Transfer Protocol Implementation (P3) -- (depends on: System Architecture Design, Security Architecture and Threat Modeling)
8. Malware Detection and Scanning (P3) -- (depends on: System Architecture Design, Security Architecture and Threat Modeling)
9. User Authentication and Authorization (P3) -- (depends on: System Architecture Design, Security Architecture and Threat Modeling)
10. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
11. Testing and Quality Assurance (P4) -- (depends on: File Transfer Protocol Implementation, Malware Detection and Scanning, User Authentication and Authorization, User Interface and Experience Design, Database Design and Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SecureFileShare can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Securely share files over SFTP, FTP, and FTPS within business-to-business workflows while detecting .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
