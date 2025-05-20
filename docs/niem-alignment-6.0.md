# NIEM ↔ NFL Alignment (6.0)

This document summarizes how the OpenPermit Node Framework (NFL) maps to the National Information Exchange Model (NIEM) 6.0. It explains the augmentation rules used to extend NIEM schemas and describes the process for keeping mappings up to date.

## NIEM ↔ NFL Mappings

- **Person**: NIEM `nc:Person` elements correspond to NFL `person` nodes capturing name, address and contact information.
- **Organization**: NIEM `nc:Organization` aligns with the NFL `organization` node for agencies or companies.
- **Document**: NIEM `nc:Document` structures map to NFL `document` nodes referencing external files or URLs.
- **Permit**: NIEM permit types (e.g., `ext:Permit`) become NFL `permit` nodes holding application metadata and status.
- Relationships mirror NIEM associations; each NFL node retains a `niemTag` property for round‑tripping.

## Augmentation Rules

- When NIEM lacks required properties, extensions are created in the `openpermit` namespace.
- Augmentation adds new attributes or enumerations without changing base NIEM definitions.
- NFL nodes reference augmented types and preserve original NIEM tags for traceability.
- This approach ensures that updates to NIEM can be merged without losing local fields.

## Update Process

1. Monitor NIEM release notes for schema changes.
2. Regenerate mapping tables using the importer scripts in `agent/`.
3. Review differences and create new augmentations as needed.
4. Commit revised schemas and mappings under a new version directory (for example `niem-6.1`).
5. Update this document and related importer scripts to reflect the new mappings.

---

Following these guidelines keeps the OpenPermit data layer interoperable with NIEM while maintaining the flexibility of the Node Framework.
