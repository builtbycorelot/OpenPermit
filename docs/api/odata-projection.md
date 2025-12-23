# OData Projection (2026-ready)

OData is the durable enterprise query surface that vendors and jurisdictions can expose without changing internal systems. The ontology sits underneath; OData is the projection layer.

## Suggested OData Entity Sets (v0.1)
- `/Permits`
- `/Parcels`
- `/Applicants`
- `/Reviews`
- `/ReviewComments`
- `/Inspections`
- `/InspectionResults`
- `/Fees`
- `/Payments` (optional)

## Example Query Patterns
- Filter: `GET /Fees?$filter=permitId eq 'VA-Spot-2025-001234'`
- Expand: `GET /Permits?$filter=...&$expand=Fees,Inspections`
- Time: `GET /Inspections?$filter=ts ge 2026-01-01T00:00:00Z`

## Mapping Note
Each provider maps internal entities → OpenPermit ontology concepts → OData view. No requirement to change internal schemas.
