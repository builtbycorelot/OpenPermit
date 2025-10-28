# Programmatic Interface & API Access

OpenPermit exposes a modern API that lets businesses, permitting services, and inspection partners interact with municipal workflows programmatically. The interface is designed for resilience, security, and interoperability with existing civic technology ecosystems.

## Key capabilities
- **Permit submission and tracking.** Submit standardized payloads, monitor review status, and receive structured feedback through callbacks or polling endpoints.
- **3rd-party integration.** Connect plan reviewers, energy auditors, and inspection partners via authenticated service accounts.
- **Geo-attested inspections.** Pair with [remote inspection APIs](remote_inspections.md) to validate on-site presence through verified devices.

## Architecture highlights
- Built on the same [core engine](../src/core/worker.js) that powers the OpenPermit demo stack.
- RESTful endpoints with predictable schemas, leveraging the shared [open-data-layer](../open-data-layer) vocabulary.
- Extensible authentication model ready for municipal IAM systems, API gateways, and zero-trust overlays.

## Getting started
1. Review the [Quick Start Guide](QUICK_START.md) to launch the local environment.
2. Explore the [Node Framework Demo](../example/index.html) to visualize API-driven submissions.
3. Prototype integrations with the CLI tools documented in the [CLI README](../cli/README.md).

## Roadmap
- SDKs for common implementation languages.
- Webhooks and event streams for near-real-time status updates.
- Alignment with national data exchanges, including NIEM-based payloads.
