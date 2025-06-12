# Project Roadmap

This roadmap outlines near-term milestones to evolve OpenPermit into a mandate-ready reference implementation.

## API façade
- Provide thin wrappers around existing modules so that permit data can be queried and updated over a REST or GraphQL API.
- These wrappers don't need complex business logic initially; their purpose is to expose the standards-first data layer through a stable interface.

## CKAN open-data push
- Finish the integration scripts that publish validated permit datasets to any CKAN portal.
- Ensure metadata and access controls propagate correctly so agencies can meet open-data requirements.

## Alpha release and FedRAMP-ready container
- Package the project as a container with dependencies locked down.
- Follow FedRAMP guidance for base images and hardening so agencies can evaluate deployment.
- Tag the release as an "alpha" to gather feedback while signalling early stability.

These efforts will move OpenPermit from a proof of concept to a practical toolkit that agencies can adopt.
