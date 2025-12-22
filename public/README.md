# OpenPermit: Accelerating Affordable Housing Through Schema-First Permitting

> **Schema as infrastructure.** Structured permit data as a public good to drive GDP growth and unlock housing supply.

## The Problem

Every year, **1.4+ million housing units** need permits in the United States. The permitting process:

- **Adds 25-40% to housing costs** through delays and uncertainty
- **Locks knowledge in PDFs and siloed systems** — unreadable by machines, unreusable across jurisdictions
- **Requires manual re-review** for identical designs in different cities
- **Creates friction** that reduces GDP growth and housing affordability

## The Solution: Permit By Rule

**Permit by rule** means: if your design meets the code, approval is automatic. No waiting, no discretion, no delays.

This requires:

1. **Schema as first-class data** — Structured, machine-readable permit applications
2. **Rules as code** — Building codes expressed as deterministic validation logic
3. **Automated validation** — Instant feedback on code compliance before submission

OpenPermit provides the **open standards and specifications** to make permit-by-rule real.

### What OpenPermit IS

**A set of open standards and specifications:**
- **Data schemas** (JSON-LD) for structured permit applications
- **API contracts** (OpenAPI 3.1) for how systems exchange permit data
- **Validation rule format** for expressing building codes as deterministic logic
- **Integration specifications** for CKAN, NIEM, BLDS, BCF, IFC interoperability

**Anyone can implement these standards** in their jurisdiction or software product.

### What OpenPermit is NOT

- ❌ Not a running application, SaaS, or hosted service
- ❌ Not a workflow engine or permit management system
- ❌ Not vendor-specific software requiring licenses
- ❌ Not a centralized database

**Think of this like TCP/IP or HTTP** — open protocols that enable an ecosystem, not a single implementation.

## How It Drives Affordable Housing

| Challenge | OpenPermit Solution | Impact |
|-----------|-------------------|---------|
| **Time delays** | Automated validation = instant feedback | Reduce permitting time from weeks to minutes |
| **Inconsistent interpretation** | Rules as code = deterministic checks | Eliminate subjective reviews for objective code requirements |
| **Duplicated effort** | Schema enables reuse across jurisdictions | Submit once, approve everywhere for compliant designs |
| **Locked knowledge** | Open data layer = machine-readable submissions | Enable ecosystem innovation (AI tools, pre-approved plans, etc.) |

### Economic Impact

- **Reducing permitting time by 50%** could unlock **$20B+ in annual housing GDP**
- **Standardized schema** enables **pre-approved plan marketplaces** (like UL listings for buildings)
- **Permit by rule** removes **regulatory uncertainty** that blocks affordable housing investment

## Schema as First-Class Infrastructure

OpenPermit treats **schema as public infrastructure**, not vendor lock-in:

### What We Provide

```
┌─────────────────────────────────────────────┐
│  SCHEMA LAYER (Open Standards)              │
│  • JSON-LD permit applications              │
│  • NIEM/BLDS federal alignment              │
│  • IFC building model linkage               │
│  • BCF review comment integration           │
└─────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────┐
│  VALIDATION LAYER (Rules as Code)           │
│  • Building code checks (IRC, IBC)          │
│  • Zoning compliance                        │
│  • Energy code validation (IECC)            │
│  • Prescriptive path verification           │
└─────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────┐
│  INTEGRATION LAYER (Ecosystem)              │
│  • CKAN open data publishing                │
│  • BIM tool round-tripping                  │
│  • Municipal system APIs                    │
│  • Third-party inspection endpoints         │
└─────────────────────────────────────────────┘
```

### Key Principle

> **"We emit facts. Someone else decides what to do with them."**

OpenPermit validates code compliance and structures the data. **Jurisdictions retain full authority** over approvals, variances, and policy decisions.

## Core Components

| Document | Purpose |
|----------|---------|
| [Schema Documentation](./schema.md) | How schema enables ecosystem innovation |
| [Permit By Rule](./permit-by-rule.md) | Automated validation and rules-as-code approach |
| [Ecosystem Impact](./ecosystem.md) | How this drives affordable housing and GDP growth |
| [For Builders](./for-stakeholders/builders.md) | Benefits for developers and designers |
| [For Agencies](./for-stakeholders/agencies.md) | Benefits for jurisdictions and AHJs |
| [For Public](./for-stakeholders/public.md) | Benefits for residents and civic groups |

## Who Benefits

### Builders & Developers
- **Instant feedback** on code compliance
- **Reusable designs** across jurisdictions
- **Reduced uncertainty** = lower financing costs

### Jurisdictions & AHJs
- **Faster reviews** = higher throughput with same staff
- **Consistent enforcement** = reduced liability
- **Open data compliance** = publish validated permit data to CKAN portals

### Residents & Communities
- **More affordable housing** through faster, cheaper permitting
- **Transparent process** = public oversight of code enforcement
- **Better data** for civic engagement and planning

## Standards Foundation

OpenPermit builds on proven, open standards:

- **NIEM 6.0** — Federal information exchange standard
- **BLDS (Building & Land Development Specification)** — HUD/Census permit data standard
- **IFC 4x3** — buildingSMART open BIM standard
- **BCF** — BIM Collaboration Format for review comments
- **CKAN** — Open data portal standard (used by data.gov)

## Get Started

### For Jurisdictions
1. Review [permit-by-rule.md](./permit-by-rule.md) to understand automated validation
2. See [schema.md](./schema.md) for data structure and integration options
3. Contact: j@corelot.net

### For Builders
1. Explore [for-stakeholders/builders.md](./for-stakeholders/builders.md)
2. Try the validation tools in the main repository
3. Submit feedback via GitHub Issues

### For Researchers & Civic Tech
1. Read [ecosystem.md](./ecosystem.md) for economic impact analysis
2. Access open permit data via CKAN integration
3. Build on the open schema and validation layer

## Contact & Governance

**Lead:** Jeremiah Horstick — j@corelot.net
**License:** MIT (open source, no vendor lock-in)
**Repository:** https://github.com/builtbycorelot/OpenPermit

## Key Insight

> **Housing is a schema problem, not just a policy problem.**

When permit data is trapped in PDFs and siloed systems, innovation is impossible. OpenPermit makes schema a **first-class public good** — the foundation for permit-by-rule, affordable housing, and GDP growth.
