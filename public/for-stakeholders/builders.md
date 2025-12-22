# For Builders and Developers

> **Value proposition:** Get instant feedback on code compliance, reduce permitting costs by 60-80%, and reuse approved designs across jurisdictions.

## The Builder's Permitting Pain

Current reality:
- **Submit plans → Wait weeks → Get corrections → Resubmit → Wait again**
- **$7,000-22,000 per permit** in soft costs (plan prep, review fees, delays)
- **Different requirements in every jurisdiction** — can't reuse designs
- **Financing costs pile up** while waiting for approval

**Result:** Permitting adds 25-40% to project costs and kills predictability.

## How OpenPermit Helps

### 1. Instant Feedback (Before Submission)

**Traditional workflow:**
```
Design in CAD/BIM
     ↓
Submit to jurisdiction
     ↓
Wait 2-6 weeks
     ↓
Get correction list
     ↓
Redesign and resubmit
     ↓
Wait another 2-4 weeks
```

**With OpenPermit:**
```
Design in BIM tool
     ↓
Real-time validation as you work
     ↓
"Stud spacing 20\" exceeds IRC max 16\""
     ↓
Fix immediately (RED → GREEN)
     ↓
Submit when all checks pass
     ↓
APPROVED (same day)
```

**You know it's compliant BEFORE you submit.**

### 2. Massive Cost Reduction

| Cost Component | Traditional | With OpenPermit | Your Savings |
|----------------|-------------|----------------|--------------|
| **Plan preparation** | $2,500-8,000 | $800-2,500 | $1,700-5,500 |
| **Permit review fees** | $1,500-5,000 | $200-800 | $1,300-4,200 |
| **Delays (financing)** | $2,000-6,000 | $0-500 | $2,000-5,500 |
| **Back-and-forth corrections** | $1,000-3,000 | $0 | $1,000-3,000 |
| **Total** | **$7,000-22,000** | **$1,000-3,800** | **$6,000-18,200** |

**On a 10-unit project:** $60,000-180,000 in savings

### 3. Reusable Designs Across Jurisdictions

**Current:** Custom plans for every jurisdiction (even for identical designs)

**With OpenPermit:**
1. Design ADU in Portland
2. Validate against IRC 2021
3. Submit to OpenPermit-enabled jurisdictions nationwide
4. **Instant approval** (schema shows code compliance)

**Like UL listing for buildings** — design once, deploy everywhere.

## Getting Started

### Step 1: Use BIM Tools That Support OpenPermit

**Recommended tools:**
- **Revit** (Autodesk) — IFC 4x3 export
- **ArchiCAD** (Graphisoft) — Native IFC support
- **Vectorworks** — BIM and IFC export

**Coming soon:** OpenPermit plugins for real-time validation inside these tools.

### Step 2: Design Your Project

Work normally in your BIM tool. OpenPermit runs in the background, checking:
- Dimensional requirements (room sizes, ceiling heights)
- Structural elements (stud spacing, joist spans)
- Fire separation and egress
- Energy code compliance (IECC)

**Green checkmarks** as you go = confidence in compliance.

### Step 3: Pre-Submission Validation

Before submitting, run full validation:

```bash
# Export IFC model from BIM tool
project.ifc

# Validate against local code
openpermit validate project.ifc \
  --code IRC2021 \
  --jurisdiction austin-tx \
  --output report.json

# Review results
{
  "result": "pass",
  "checksPassed": 147,
  "checksFailed": 0
}
```

**If all checks pass, you're ready to submit.**

### Step 4: Submit to Jurisdiction

Submit your **IFC model + validation report** via jurisdiction portal.

**If jurisdiction uses OpenPermit:**
- Automated re-validation confirms your results
- **Instant approval** (or same-day for manual spot-check)

**If jurisdiction doesn't use OpenPermit yet:**
- Submit validation report as supplemental documentation
- Reduces reviewer workload = faster approval
- **Encourage jurisdiction to adopt OpenPermit**

## Real-World Examples

### Example 1: ADU Builder (Los Angeles)

**Project:** 800 sq ft detached ADU

**Without OpenPermit:**
- Plan prep: $3,500
- Permit wait: 8 weeks
- Corrections: 2 rounds, $1,200
- Financing cost during delays: $2,400
- **Total soft costs: $7,100**

**With OpenPermit:**
- Plan prep: $1,200 (faster, no back-and-forth)
- Permit approval: 1 day
- Corrections: $0 (validated before submission)
- Financing cost: $100
- **Total soft costs: $1,300**

**Savings: $5,800 per ADU × 10 ADUs/year = $58,000 annually**

### Example 2: Production Builder (Phoenix)

**Project:** 50-unit subdivision (model-match homes)

**Without OpenPermit:**
- Custom plans for each lot variation: $75,000
- Permit review: 6 weeks average
- Corrections: 15% of permits need resubmission
- **Total soft costs: $350,000**

**With OpenPermit:**
- Parametric BIM models with validation: $25,000
- Permit approval: 1 day (automated validation)
- Corrections: 0% (validated before submission)
- **Total soft costs: $75,000**

**Savings: $275,000 on one subdivision**

### Example 3: Manufactured Home Dealer

**Project:** Factory-built homes (HUD Code compliance)

**Without OpenPermit:**
- Local jurisdiction requires additional structural review
- Wait time: 3-6 weeks per home
- Inconsistent interpretations across jurisdictions

**With OpenPermit:**
- HUD certification + OpenPermit validation
- Local jurisdiction auto-accepts (schema confirms compliance)
- **Same-day permits nationwide**

**Impact:** Deploy 5× more homes per year (limited by construction, not permitting)

## Integration with Your Workflow

### Design Phase
- Work in BIM tool as usual
- OpenPermit validates in background
- Real-time feedback on code issues

### Pre-Construction
- Export IFC model
- Run full validation
- Fix any flagged items
- **Submit with confidence**

### Permitting
- Upload model + validation report
- Jurisdiction re-validates (confirms your results)
- **Approval** (instant or same-day)

### Construction
- Use BIM model for trade coordination
- Link inspection results to IFC elements
- Close-out with as-built model

## Tools and Resources

### OpenPermit CLI (Command Line Tool)

```bash
# Install
npm install -g openpermit-cli

# Validate IFC model
openpermit validate model.ifc --code IRC2021

# Check specific elements
openpermit check --element wall --property StudSpacing

# Export validation report
openpermit report --format pdf --output validation.pdf
```

### BIM Tool Plugins (Coming Soon)

- **Revit Plugin** — Real-time validation inside Revit
- **ArchiCAD Add-On** — Code checking as you design
- **Blender Add-On** — Open-source BIM workflow

### Pre-Approved Plan Libraries

**Coming:** Marketplace of OpenPermit-validated designs

- Browse pre-approved plans (ADUs, SFRs, commercial)
- Purchase design + validation report
- Submit to your jurisdiction (instant approval)

**Like stock plans, but with guaranteed code compliance.**

## Frequently Asked Questions

### "Do I have to change my design software?"

**No.** As long as your tool exports **IFC 4x3**, you can use OpenPermit validation.

Most modern BIM tools (Revit, ArchiCAD, Vectorworks, etc.) support IFC export.

### "What if my jurisdiction doesn't use OpenPermit yet?"

You can still benefit:
1. **Use OpenPermit for pre-checks** — catch issues before submission
2. **Include validation report** — helps reviewer, speeds approval
3. **Advocate for adoption** — show jurisdiction the time/cost savings

**Many jurisdictions adopt OpenPermit BECAUSE builders request it.**

### "Does this work for custom/high-end homes?"

**Yes, for prescriptive code compliance.**

If your design follows IRC/IBC prescriptive paths (stud walls, conventional framing, etc.), OpenPermit validates those portions.

**Engineered elements** (custom trusses, large spans, etc.) still need PE stamps, but:
- OpenPermit validates the prescriptive parts
- Reduces reviewer workload
- Faster overall approval

### "What about code amendments and local requirements?"

OpenPermit supports **jurisdiction-specific rules**:

```bash
# Validate with local amendments
openpermit validate model.ifc \
  --code IRC2021 \
  --amendments austin-tx-2024
```

Jurisdictions can add local rules to OpenPermit knowledge packs.

### "How much does OpenPermit cost?"

**$0. It's open source (MIT license).**

- CLI tools: Free
- Validation rules: Free
- Schema specification: Free

**Third-party tools** (BIM plugins, SaaS platforms) may charge, but core OpenPermit is free forever.

## Next Steps

1. **Try OpenPermit validation** on an existing project (free CLI tool)
2. **Join builder community** — Share feedback, request features
3. **Advocate with your jurisdiction** — Show them the benefits
4. **Use validated designs** — Reuse across multiple projects

**Contact:** j@corelot.net

## Key Takeaway

> **Permitting is your biggest soft cost. OpenPermit cuts it by 60-80%.**

Stop waiting weeks for approvals. Stop paying for corrections. **Validate before you submit, deploy across jurisdictions, and focus on building homes.**
