# Schema as First-Class Infrastructure

> **Why this matters:** When permit data is locked in PDFs, innovation dies. When it's structured, machine-readable schema — ecosystems flourish.

## The Core Problem

Today's permitting is **schema-blind**:

- **PDFs and scanned images** → No machine readability
- **Siloed vendor systems** → No data portability
- **Proprietary formats** → No ecosystem innovation
- **Manual re-entry** → Duplicated work across every jurisdiction

**Result:** Every permit is a dead-end. Data can't be reused, analyzed, or built upon.

## Schema-First Changes Everything

When permit applications are **structured, open-standard schema**, they become:

### 1. Machine-Readable Inputs

```json
{
  "@context": "https://schema.openpermit.org/v1",
  "@type": "BuildingPermitApplication",
  "permitType": "SingleFamilyResidential",
  "project": {
    "address": "123 Main St, Austin, TX 78701",
    "parcel": "APN-12345-67890",
    "buildingModel": {
      "@type": "IFC4x3Reference",
      "url": "https://storage.example.com/project-model.ifc",
      "globalId": "2O2Fr$t4X7Zf8NOew3FNr2"
    }
  },
  "design": {
    "squareFootage": 2400,
    "stories": 2,
    "occupancyType": "R-3",
    "constructionType": "V-B"
  },
  "codeValidation": {
    "irc2021": {
      "status": "pass",
      "checksPassed": 147,
      "checksFailed": 0
    }
  }
}
```

**This enables:**
- ✅ Automated code validation **before** submission
- ✅ Instant feedback to designers
- ✅ Cross-jurisdiction reuse of compliant designs
- ✅ Open data publication for public oversight

### 2. Linked Building Models

Schema connects permit data to **IFC building information models**:

```
Permit Application (JSON-LD)
     ↓
IFC Building Model (3D geometry + semantic data)
     ↓
BCF Review Comments (element-specific feedback)
     ↓
Inspection Results (linked to building elements)
```

**Every piece of data references IFC `GlobalId`** — enabling round-trip updates between permit systems and BIM tools.

### 3. Federal Standard Alignment

OpenPermit schema **automatically aligns** with federal reporting requirements:

| Standard | Purpose | OpenPermit Integration |
|----------|---------|----------------------|
| **NIEM 6.0** | Justice/emergency data exchange | JSON-LD schema generators |
| **BLDS** | HUD/Census permit statistics | Auto-export to BLDS format |
| **NEPA** | Environmental compliance | Link to EPA permit data standards |

**Jurisdictions get federal compliance for free** — no manual data translation.

### 4. Open Data Publication

Schema enables **instant open data publishing** via CKAN integration:

```bash
# Validate and publish permit data in one step
python integrations/ckan/push_dataset.py \
  https://data.cityofaustin.gov \
  $API_KEY \
  permit-application.jsonld \
  --name "2024-residential-permits"
```

**Result:** Machine-readable permit data on open data portals (like data.gov) for:
- Civic tech innovation
- Housing research and policy analysis
- Market transparency (e.g., permit trends by neighborhood)

## Schema Enables Ecosystem Innovation

Once permit data is **structured and open**, third-party innovation explodes:

### Pre-Approved Plan Marketplaces

```
┌──────────────────────────────────────┐
│  Designer creates ADU plan           │
│  Validates against IRC 2021          │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│  Jurisdiction A approves plan        │
│  Publishes approval + schema data    │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│  Jurisdiction B auto-accepts         │
│  (Schema shows code compliance)      │
└──────────────────────────────────────┘
```

**Like UL listings for buildings** — test once, approve everywhere.

### AI-Assisted Design Tools

- **ChatGPT/Claude integration** — "Design a 1,200 sq ft ADU compliant with Austin zoning"
- **Instant validation** — AI generates schema, OpenPermit validates, designer reviews
- **No code expertise required** — Rules are machine-checkable, not human-interpreted

### Permit Processing SaaS

Third-party companies can build permit management tools that:
- Ingest OpenPermit schema
- Add workflow/payment/tracking layers
- Export validated data back to jurisdictions

**No vendor lock-in** — schema is open standard, tools are interchangeable.

### Research & Policy Analysis

Structured permit data enables:
- **Housing production tracking** by type, neighborhood, cost
- **Code impact analysis** — "Did IRC 2021 sprinkler requirements reduce ADU permits?"
- **Equity audits** — Permit approval times by zip code

## What OpenPermit Provides

### Schema Specification
- **JSON-LD context** — W3C standard semantic web format
- **NIEM/BLDS alignment** — Federal reporting compliance
- **IFC linkage** — Building model integration
- **Versioning** — Semantic versioning for backward compatibility

### Schema Generators
```bash
# Generate NIEM 6.0 JSON Schema from permit data
python scripts/niem6_build_schemas.py

# Validate workflow against schema
python workflow/validate_workflow.py
```

### Schema Validators
- **Pre-submission checks** — Catch errors before AHJ review
- **Code compliance** — Automated IRC/IBC/IECC validation
- **Data quality** — Ensure completeness and format correctness

### Integration Bridges
- **IFC ↔ JSON-LD** — Round-trip between BIM and permit systems
- **CKAN publisher** — One-step open data export
- **BCF issuer** — Convert review comments to BIM issues

## Schema Design Principles

### 1. Human-Readable, Machine-Actionable
Schema should be **JSON** (not XML or binary formats) and use **semantic property names**:

```json
// GOOD
{
  "squareFootage": 2400,
  "stories": 2
}

// BAD
{
  "prop_1": "2400",
  "prop_2": "2"
}
```

### 2. Linked Data (JSON-LD)
Every entity has a **globally unique identifier** and **type**:

```json
{
  "@id": "https://permits.example.com/permit/2024-001234",
  "@type": "BuildingPermit",
  "applicant": {
    "@type": "Person",
    "name": "Jane Builder"
  }
}
```

### 3. Extensible, Not Prescriptive
Jurisdictions can **add local requirements** without breaking schema:

```json
{
  "@type": "BuildingPermitApplication",
  "austinRequirements": {
    "waterQualityReview": true,
    "heritageTreeSurvey": false
  }
}
```

### 4. Versioned and Stable
Schema changes follow **semantic versioning**:
- **Patch (1.0.x)** — Clarifications, no breaking changes
- **Minor (1.x.0)** — New optional fields
- **Major (x.0.0)** — Breaking changes (avoided when possible)

## Schema vs. Workflow

**Schema defines data structure. Workflow defines who does what when.**

OpenPermit provides **schema only**. Jurisdictions choose their own workflow:

| Component | OpenPermit Role | Jurisdiction Role |
|-----------|----------------|------------------|
| **Data format** | Provides open standard schema | Accepts schema or extends locally |
| **Validation** | Provides code checking tools | Decides which checks are required |
| **Approval** | N/A | Jurisdictions approve or deny |
| **Workflow** | N/A | Jurisdictions define review process |
| **Storage** | N/A | Jurisdictions choose backend system |

**We emit facts. Someone else decides what to do with them.**

## Economic Impact

### Reduced Transaction Costs
- **Standardized schema** eliminates manual data re-entry across jurisdictions
- **Estimated savings:** $500-2,000 per permit in staff time

### Faster Time-to-Market
- **Automated validation** reduces review time from weeks to minutes
- **Housing production impact:** Every week of delay costs ~$800 in financing

### Ecosystem Value Creation
- **Open schema** enables third-party tool innovation (like App Store for permits)
- **Network effects:** More tools → more adoption → more data → better tools

**Conservative estimate:** Schema-first permitting could unlock **$20B+ annually in housing GDP**.

## Getting Started

### For Jurisdictions
1. **Review schema specification** — See `/openpermit/schema/` in the repository
2. **Pilot with one permit type** — Start with simple residential permits
3. **Enable CKAN publishing** — Get open data compliance automatically
4. **Integrate with existing systems** — API bridges to current permit software

### For Tool Builders
1. **Implement schema validation** — Use OpenPermit validators in your tools
2. **Support IFC linkage** — Enable round-trip with BIM authoring tools
3. **Publish to open data** — Use CKAN integration for transparency

### For Researchers
1. **Access open permit data** — CKAN portals provide machine-readable datasets
2. **Analyze housing production** — Schema enables cross-jurisdiction comparison
3. **Contribute schema improvements** — Open source governance via GitHub

## Key Insight

> **Schema is not bureaucracy — it's the foundation for permit-by-rule.**

When permit applications are **structured data**, automated validation becomes possible. When validation is automated, **approval can be instant** for code-compliant designs.

**This is how we unlock affordable housing at scale.**

---

**Next:** [Permit By Rule](./permit-by-rule.md) — How automated validation works
