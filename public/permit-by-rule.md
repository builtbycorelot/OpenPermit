# Permit By Rule: Automated Validation for Instant Approvals

> **Core principle:** If your design meets the code, approval should be automatic. No waiting, no discretion, no delays.

## What is Permit By Rule?

**Permit by rule** means that designs meeting objective building code requirements receive **automatic approval** — no human review required.

### Traditional Permitting (Manual Review)

```
Designer submits plans (PDF)
     ↓
Wait in review queue (days to weeks)
     ↓
Plan reviewer manually checks code compliance
     ↓
Back-and-forth corrections (more weeks)
     ↓
Final approval (if compliant)
```

**Time:** 2-12 weeks
**Cost:** $1,500-5,000 in staff time
**Uncertainty:** Subjective interpretation varies by reviewer

### Permit By Rule (Automated Validation)

```
Designer validates in BIM tool (instant)
     ↓
Submit schema + validated model
     ↓
Automated check confirms compliance
     ↓
APPROVED (instant)
```

**Time:** Minutes
**Cost:** $50-200 in compute
**Certainty:** Deterministic — same input, same result

## How It Works: Rules as Code

Building codes are **deterministic rules** that can be expressed as code:

### Example: IRC R602.3 — Stud Spacing

**Code language:**
> "Studs shall be spaced at not more than 16 inches (406 mm) on center for load-bearing walls supporting one floor, roof and ceiling."

**As validation code:**

```python
def check_stud_spacing(wall_element):
    """
    IRC R602.3 - Stud spacing for load-bearing walls
    """
    # Get wall properties from IFC model
    is_load_bearing = wall_element.IsLoadBearing
    stud_spacing = wall_element.StudSpacing  # in inches
    floors_supported = wall_element.FloorsSupported

    # Check applicability
    if not is_load_bearing:
        return ValidationResult(
            status="not_applicable",
            code_ref="IRC R602.3",
            message="Non-load-bearing wall"
        )

    # Apply rule
    if floors_supported == 1 and stud_spacing <= 16:
        return ValidationResult(
            status="pass",
            code_ref="IRC R602.3",
            message=f"Stud spacing {stud_spacing}\" ≤ 16\" maximum"
        )
    else:
        return ValidationResult(
            status="fail",
            code_ref="IRC R602.3",
            message=f"Stud spacing {stud_spacing}\" exceeds 16\" maximum for single-floor load-bearing wall"
        )
```

**Result:** Designer gets instant feedback in their BIM tool, before submission.

## What Can Be Automated?

### Prescriptive Path Checks (90%+ of residential permits)

These are **objective, measurable requirements** ideal for automation:

| Code Section | Validation Type | Example |
|--------------|----------------|---------|
| **Dimensional** | Measure geometry | Room sizes, ceiling heights, stair rise/run |
| **Spacing** | Check intervals | Stud spacing, joist spans, anchor bolt spacing |
| **Material** | Verify specifications | Lumber grades, concrete strength, insulation R-value |
| **Quantity** | Count elements | Required outlets per room, smoke detectors, exits |
| **Clearance** | Measure distances | Fixture clearances, fire separation, setbacks |

**OpenPermit provides:**
- **Knowledge packs** — Pre-built validation rules for IRC, IBC, IECC
- **Deterministic checks** — Same input, same result (no AI interpretation)
- **Element-level feedback** — Results linked to IFC GlobalId for precise corrections

### Performance Path (Requires Engineering Review)

Some requirements need **professional judgment** and remain human-reviewed:

- Structural calculations for unconventional designs
- Fire protection engineering (beyond prescriptive)
- Alternative compliance methods (equivalency proposals)
- Site-specific hazard analysis (flood, seismic, wildfire)

**Permit by rule doesn't replace engineers** — it **frees them** to focus on complex cases.

## Validation Workflow

### 1. Design Phase (Instant Feedback)

Designer works in BIM tool (Revit, ArchiCAD, etc.):

```
Designer models wall
     ↓
OpenPermit plugin validates stud spacing
     ↓
RED HIGHLIGHT: "Stud spacing 20\" exceeds IRC R602.3 max 16\""
     ↓
Designer adjusts to 16\" spacing
     ↓
GREEN CHECKMARK: "Wall complies with IRC R602.3"
```

**Before submission, designer knows design is compliant.**

### 2. Pre-Submission Check

```bash
# Export IFC model from BIM tool
model.ifc

# Run full code validation
openpermit validate model.ifc --code IRC2021 --output report.json

# Review results
{
  "validationDate": "2024-01-15T10:30:00Z",
  "code": "IRC2021",
  "result": "pass",
  "checksPassed": 147,
  "checksFailed": 0,
  "details": [...]
}
```

**If all checks pass, designer submits.**

### 3. Submission (Automated Approval)

```json
{
  "@type": "BuildingPermitApplication",
  "buildingModel": {
    "url": "https://storage.example.com/model.ifc",
    "sha256": "abc123..."
  },
  "codeValidation": {
    "irc2021": {
      "status": "pass",
      "validator": "OpenPermit v1.2.0",
      "checksPassed": 147,
      "timestamp": "2024-01-15T10:30:00Z"
    }
  }
}
```

**AHJ system:**
1. Downloads model
2. Re-runs validation (verify designer's results)
3. If pass → **INSTANT APPROVAL**
4. If fail → Flag for human review

## Trust and Verification

### "How do we trust automated validation?"

**Answer:** The same way we trust elevators, airbags, and structural engineering software:

1. **Deterministic logic** — Code rules are unambiguous, implementation is testable
2. **Open source** — Validation code is public, auditable, improvable
3. **Versioned** — Specific validator version logged with each permit
4. **Test suites** — Validation rules tested against known-good/known-bad designs
5. **Jurisdiction override** — AHJs can always require human review for specific cases

**We're not replacing judgment — we're automating the objective 90%.**

### Validator Certification

Like mechanical code calculators or structural software, validation tools can be **certified**:

```
┌────────────────────────────────────────┐
│  ICC Evaluation Service                │
│  Certifies "OpenPermit IRC Validator"  │
│  Version 1.2.0 for IRC 2021            │
└────────────────────────────────────────┘
```

**Jurisdictions accept certified validators** just like they accept certified engineers.

## Economic Impact

### Time Savings

| Permit Type | Traditional Review | Automated Validation | Time Saved |
|-------------|-------------------|---------------------|------------|
| **Residential (prescriptive)** | 2-6 weeks | Minutes | 95%+ |
| **Simple commercial** | 4-12 weeks | Minutes to hours | 90%+ |
| **Complex commercial** | 3-6 months | Days (with human review) | 60%+ |

### Cost Savings

**Per permit:**
- **Designer time:** $800-2,000 saved (no back-and-forth corrections)
- **AHJ staff time:** $500-1,500 saved (no manual plan review)
- **Financing costs:** $800-3,000 saved (reduced delay = lower carrying costs)

**Total:** $2,100-6,500 per permit

**At scale (1.4M permits/year):** $3-9 billion annually in direct savings

### Affordable Housing Impact

**Case study:** 400 sq ft ADU (Accessory Dwelling Unit)

| Cost Component | Without Permit-by-Rule | With Permit-by-Rule | Savings |
|----------------|----------------------|-------------------|---------|
| **Permit fees** | $3,000 | $500 | $2,500 |
| **Plan prep** | $2,500 | $800 | $1,700 |
| **Delays (financing)** | $2,000 | $0 | $2,000 |
| **Total** | **$7,500** | **$1,300** | **$6,200 (83%)** |

**$6,200 savings per ADU** = More units built = More affordable housing supply

## Implementation Roadmap

### Phase 1: Residential Prescriptive (Immediate)

**Target:** Single-family homes, ADUs, additions following IRC prescriptive path

**Requirements:**
- IFC 4x3 models from BIM tools
- OpenPermit IRC validation rules
- Jurisdiction policy: "Pass = auto-approve"

**Pilot:** 3-6 months in friendly jurisdiction

### Phase 2: Commercial Prescriptive (6-12 months)

**Target:** Small commercial buildings following IBC prescriptive path

**Expansion:**
- IBC validation rules
- Accessibility (ADA/ICC A117.1) checks
- Energy code (IECC) validation

### Phase 3: Zoning and Site (12-18 months)

**Target:** Automated zoning compliance checks

**Requirements:**
- GIS integration for setbacks, lot coverage
- Overlay districts (historic, flood, etc.)
- Machine-readable zoning ordinances

### Phase 4: Performance Path (18+ months)

**Target:** Hybrid workflow for engineered designs

**Approach:**
- Automated checks for portions meeting prescriptive
- Flagged sections requiring PE review
- Streamlined human review for non-automated items

## Knowledge Packs: Rules as Open Source

OpenPermit provides **knowledge packs** — pre-built validation rule sets:

```
/knowledge-packs
├── IRC-2021/
│   ├── R302-fire-separation.py
│   ├── R403-foundations.py
│   ├── R602-wall-framing.py
│   └── ...
├── IBC-2021/
│   ├── 503-building-height.py
│   ├── 1005-egress-width.py
│   └── ...
└── IECC-2021/
    ├── R402-envelope.py
    └── ...
```

**Each rule:**
- ✅ **MIT licensed** — Free to use, modify, redistribute
- ✅ **Versioned** — Semantic versioning tied to code edition
- ✅ **Tested** — Unit tests with known-good/bad examples
- ✅ **Documented** — Code reference, applicability, limitations

**Jurisdictions can:**
- Use as-is for standard code adoption
- Fork and modify for local amendments
- Contribute improvements back upstream

## Boundaries: What This Is Not

### ❌ Not an AI Code Interpreter

We do **NOT** use LLMs to "interpret" building codes. Rules are:
- Written by human experts (code officials, engineers)
- Deterministic (no probabilistic reasoning)
- Testable (unit tests, not prompt engineering)

**Why?** Building safety requires **certainty**, not "probably compliant."

### ❌ Not a Permit Management System

OpenPermit provides **validation only**. We do NOT provide:
- Workflow engines (who reviews when)
- Payment processing
- Applicant portals
- Storage backends
- Authentication systems

**Why?** Jurisdictions should choose their own systems. We just validate the data.

### ❌ Not a Replacement for Engineering

Performance-based designs **still require professional engineers**. Permit by rule applies to:
- Prescriptive residential (IRC)
- Prescriptive commercial (IBC)
- Standard engineered elements (with pre-approved tables)

**Complex/novel designs** still need human review.

## Getting Started

### For Jurisdictions

1. **Adopt policy:** "Prescriptive residential permits passing automated validation receive instant approval"
2. **Pilot with ADUs:** Low-risk, high-demand permit type
3. **Monitor:** Track approval times, error rates, appeals
4. **Expand:** Add commercial prescriptive, then zoning

**Contact:** j@corelot.net for pilot program details

### For Designers

1. **Use BIM tools** that export IFC 4x3
2. **Install OpenPermit validator** (plugin or CLI)
3. **Validate before submission** — fix issues in design phase
4. **Submit with validation report** — instant approval if compliant

### For Tool Vendors

1. **Integrate OpenPermit validators** into BIM tools (Revit, ArchiCAD, etc.)
2. **Real-time feedback** — highlight non-compliant elements as designer works
3. **One-click submission** — Export IFC + validation report together

## Key Insight

> **Permit by rule is not radical — it's how most of the world works.**

Electrical panels don't require custom approval if they're UL-listed. Cars don't need DMV inspection if they meet federal standards. **Buildings should work the same way.**

**Prescriptive code compliance is objective.** We can measure it. We can automate it. **We should.**

---

**Next:** [Ecosystem Impact](./ecosystem.md) — How this drives affordable housing and GDP growth
