You are a coding agent working on PeerLearningNetwork -- a platform that facilitates peer-to-peer learning and knowledge sharing across the organization.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; PeerLearningNetwork closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing code, confirm: does this change close the gap between instruction and verified comprehension? If not, stop and reassess.

## What You Are Building

- A peer-to-peer learning platform where users can teach, learn, and share knowledge within an organization
- Backend APIs and database layer for managing users, content, learning sessions, and knowledge artifacts
- A frontend interface enabling collaboration, with authentication and role-based access control

## Anti-Goals

- **General-purpose platform**: Solve the specific peer-learning problem, not every education problem. Feature sprawl kills core value.
- **Manual-first workflow**: If a human must babysit routine operations, the automation has failed.
- **Demo-ware**: Optimize for production reliability, not impressive demos that break under real conditions.

## Build Order

1. Define project scope and requirements (acceptance: documented requirements)
2. Design system architecture (acceptance: architecture doc reviewed; depends on 1)
3. Set up development environment with CI/CD (acceptance: pipeline green; depends on 2)
4. Design UI/UX wireframes and prototypes (acceptance: mockups approved; depends on 1)
5. Set up database schema and migrations (acceptance: schema deployed; depends on 2)
6. Implement backend APIs and business logic (acceptance: API tests pass; depends on 2, 3)
7. Implement authentication and authorization (acceptance: auth flows verified; depends on 6)
8. Implement frontend components (acceptance: UI renders correctly; depends on 4, 3)
9. Set up testing and QA processes (acceptance: test suites running; depends on 6, 8)
10. Implement monitoring and logging (acceptance: dashboards live; depends on 6, 8)
11. Prepare documentation (acceptance: docs published; depends on 1, 2, 4)
12. Implement peer learning and knowledge sharing features (acceptance: e2e workflow works; depends on 6, 8, 5)
13. Deploy and release to production (acceptance: production accessible; depends on all above)

### Failure Handler

If an acceptance test fails, stop. Document what failed, what was tried, and the blocker. Surface the failure as a CPRR refutation candidate. Do not proceed to the next step.

## Stack

- Python (default)

## Open Conjectures

- **C-001**: PeerLearningNetwork can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Success Criteria

1. All build steps completed with passing acceptance tests
2. End-to-end workflow demonstrates peer-to-peer learning and knowledge sharing
3. All open conjectures either confirmed with evidence or refuted with data
4. System deployed and accessible to educators and learners
