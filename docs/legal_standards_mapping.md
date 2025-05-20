# Mapping Building Code Requirements to IFC Elements

This document outlines how legal requirements from building codes can be linked to BIM elements defined in the Industry Foundation Classes (IFC) standard. It also proposes a structure for crosswalking these requirements to automated model checks.

## Overview

Building codes such as the International Building Code (IBC) specify safety and performance requirements for the built environment. To evaluate compliance within a Building Information Model (BIM), each requirement needs to reference the appropriate IFC entities and attributes. Once mapped, rules can be executed automatically to verify that the model satisfies the code.

## Crosswalk Structure

The following structure captures the key aspects of a legal requirement and its relationship to IFC-based model checks:

| Field | Description |
|-------|-------------|
| `codeReference` | Identifier for the code section (e.g., `IBC 2021 \u00a7 717`). |
| `requirementText` | Text excerpt summarizing the obligation. |
| `ifcElement` | Relevant IFC entity or property set (e.g., `IfcBrace`, `Pset_FireProtection`). |
| `modelCheck` | Rule or algorithm used to evaluate compliance. |
| `severity` | Priority level or consequence of non-compliance. |

This information can be serialized in JSON, YAML, or another structured format for exchange between systems.

### Prototype JSON Schema

```json
{
  "codeReference": "IBC 2021 \u00a7 717",
  "requirementText": "Fire protection systems in Seismic Design Category C or higher shall be braced against lateral movement.",
  "ifcElement": "IfcDistributionElement",
  "modelCheck": {
    "type": "query",
    "expression": "CHECK EXISTS('IfcDistributionElement' WHERE IsSeismicallyBraced = TRUE)"
  },
  "severity": "high"
}
```

## Example Mapping

Below is a simplified example linking an IBC requirement to an IFC element and a model check:

1. **IBC 2021 Section 717** – "Fire protection systems shall be braced for seismic loads."
2. **IFC Element** – `IfcDistributionElement` with property `IsSeismicallyBraced`.
3. **Model Check** – Query the BIM to ensure that all instances of `IfcDistributionElement` serving fire protection systems have `IsSeismicallyBraced` set to `TRUE`.

This approach can be repeated for other code provisions. Over time, the crosswalk can expand to cover additional sections and property sets across various disciplines.

## Future Work

- Expand the schema with versioning information and jurisdictional variations.
- Incorporate references to other standards (e.g., NFPA, ASHRAE) alongside IBC.
- Build a library of reusable model checks that directly correspond to legal requirements.

