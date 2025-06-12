# Technical Explanation

OpenPermit is built around a node-based ontology for representing permits, standards and project documents. Each node is validated against JSON Schema definitions generated from NIEM and BLDS templates. The `src/core` library provides functions to create, link and validate nodes, while the API wrapper exposes these features to browser-based clients.

Documents such as IFC models or PDF plans are typed using subclasses like `JSONDocument` or `PDFDocument`. Validation results feed into a workflow engine that can automatically publish approved datasets to CKAN portals. All interactions are designed to be secure by default, with NIST 800‑53 controls in mind.

The architecture diagram in `mermaid/architecture.mmd` illustrates how the API gateway routes requests to core services and the underlying data layer. External systems like GIS platforms or payment processors can integrate through these services.
