# OpenPermit Documentation Hub

Welcome to the public documentation index for the OpenPermit project. Use this page as a launchpad to product overviews, technical references, community programs, and contributor resources across the repository.

## Quick Starts & Interactive Demos
- [Quick Start Guide](QUICK_START.md) — Install the CLI, configure a municipality, and launch the local demo in minutes.
- [Node Framework Demo](../example/index.html) — Explore the in-browser demo that generates nodes, validates submissions, and builds crosswalks.
- [Spotsylvania Innovation Sandbox Call to Action](../example/spotsylvania-innovation-sandbox.html) — Sample outreach page used in statewide pilots.

## Mission, Story & Engagement
- [OpenPermit White Paper](white_paper.md) — Mission, vision, and high-level objectives.
- [Simple Outline (Infographic)](outline_infographic.html) — Visual summary of the OpenPermit workflow.
- [Public Engagement Program](public_engagement.md) — Community outreach and participation framework.
- [Stakeholders & How to Engage](https://github.com/SheetPros/OpenPermit?tab=readme-ov-file#stakeholders--how-to-engage) — Audience-specific value propositions from the repository README.
- [Project Discussion Board](https://github.com/SheetPros/OpenPermit/discussions) — Join conversations, propose ideas, or ask questions.

## How It Works
- [Technical Explanation](technical_explanation.md) — Architecture, data model, and systems integration overview.
- [User Roles and Primary Actions](ui_roles.md) — Who does what within the permitting workflow.
- [Remote Inspection API](remote_inspections.md) — Submit geo-tagged inspections with device attestation.
- [Documentation Roadmap](roadmap.md) — Upcoming milestones including API façades and integrations.

## Data & Standards Alignment
- [IFC File Validation Workflow](ifc_approval.md) — Checklist for model validation before submission.
- [Mapping Building Code Requirements to IFC Elements](legal_standards_mapping.md) — Crosswalking regulations to BIM elements and automated checks.
- [NIEM ↔ NFL Alignment (6.0)](niem-alignment-6.0.md) — Schema alignment notes for NIEM 6.0 interoperability.
- [Relevant ISO Standards](iso_standard.md) — International standards referenced throughout OpenPermit.
- [References](references.md) — Policy and standards bibliography.
- [Data Relationships Diagram](data_relationships.html) — Visualizing linked datasets, APIs, and validation layers.
- [Open Data Layer Schema Validation](../open-data-layer/schema/validation.shacl) — SHACL shapes for structured data governance.
- [Schema Validation Script](../open-data-layer/schema/validate_schema.py) — Python helper for executing SHACL checks.

## Programs, Pilots & Policy
- [Municipal Pilot Program Overview](../PILOT_PROGRAM.md) — Strategy for launching prescriptive reviews.
- [Virginia Playbook](../Virginia/README.md) — Regional implementation example with coalition partners.
- [Remote Inspection Playbook](remote_inspections.md) — Guidance for virtual site checks and compliance evidence.
- [Public Policy Alignment](nfl-standards-plan.md) — Standards roadmap covering ISO 27001, NIEM, and related frameworks.
- [Legal Standards Mapping](legal_standards_mapping.md) — Aligning building code requirements with digital representations.

## Repository, Governance & Contribution
- [Repository Overview](../README.md) — Mission statement, quick links, and project scope.
- [Standards & Processes](../standards.md) — Coding conventions and decision records.
- [Security Policy](../SECURITY.md) — Vulnerability disclosure process and security expectations.
- [Certification Program](../CERTIFICATION.md) — Pathways for training and certification.
- [Contributing Guide](https://github.com/SheetPros/OpenPermit/blob/main/CONTRIBUTING.md) — How to open issues, submit PRs, and join development.
- [Issue Labels & Support](https://github.com/SheetPros/OpenPermit/issues) — Browse open tasks and feature requests.

## Additional Resources
- [CLI Documentation](../cli/README.md) — Command-line tooling usage and configuration.
- [API Source](../src/api/index.js) — Entry point to the API surface (JavaScript).
- [Core Engine Worker](../src/core/worker.js) — Background processing logic for node operations.
- [Scripts & Automation](../scripts) — Utilities including NIEM 6 schema builders and data loaders.
- [Example Payloads](../example) — HTML demos and sample permit data packages.

If you discover a missing resource, please [open an issue](https://github.com/SheetPros/OpenPermit/issues/new) or start a [discussion](https://github.com/SheetPros/OpenPermit/discussions/new) so we can keep this index current.
