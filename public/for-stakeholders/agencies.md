# For Jurisdictions and Agencies

> **Value proposition:** Process 10× more permits with the same staff, reduce liability through consistent enforcement, and achieve open data compliance automatically.

## The Jurisdiction's Permitting Challenge

**You're facing:**
- **Chronic understaffing** — Backlog growing faster than you can hire
- **Manual plan review** — Every permit requires hours of staff time
- **Inconsistent interpretations** — Different reviewers, different rulings
- **Liability exposure** — Missed violations in manual review
- **Political pressure** — Housing crisis blamed on "slow permitting"
- **Compliance burdens** — HUD/EPA/Census reporting requirements

**Result:** You're the bottleneck in the housing crisis, even though you're working at capacity.

## How OpenPermit Helps

### 1. 10× Review Throughput (Same Staff)

**Current workflow:**
```
Application received
     ↓
Assigned to plan reviewer (1-2 days)
     ↓
Manual review (4-8 hours per permit)
     ↓
Write correction list (1-2 hours)
     ↓
Applicant resubmits → Review again (2-4 hours)
     ↓
Final approval
```

**Total time:** 8-12 staff hours per permit

**With OpenPermit:**
```
Application received (with validation report)
     ↓
Automated re-validation (2 minutes)
     ↓
Spot-check audit (15 minutes)
     ↓
APPROVED
```

**Total time:** 15-20 minutes per permit (for prescriptive residential)

**Your plan reviewers can handle 10× more permits** — or focus on complex commercial projects.

### 2. Consistent Code Enforcement

**Current risk:**
- Reviewer A interprets IRC R602.3 one way
- Reviewer B interprets it differently
- **Applicant appeals → You lose → Legal costs + delay**

**With OpenPermit:**
- **Deterministic validation** — Same input, same result every time
- **Versioned rules** — Audit trail shows which code version applied
- **Transparent logic** — Validation code is public, reviewable

**Consistency = reduced liability + fewer appeals.**

### 3. Open Data Compliance (Automatic)

**Federal reporting requirements:**
- **HUD BLDS** (Building & Land Development Specification)
- **Census Bureau** (Building Permits Survey)
- **EPA NEPA** (Environmental review data)

**Current process:** Manual data entry, reformatting, CSV uploads

**With OpenPermit:**
```bash
# One command exports to all federal formats
openpermit export permits-2024.json \
  --format blds,census,epa \
  --output federal-reports/

# Auto-publish to open data portal
openpermit publish permits-2024.json \
  --ckan https://data.yourcity.gov \
  --dataset "2024-building-permits"
```

**Instant compliance** + public transparency.

### 4. Political Cover for Housing Production

**Current narrative:**
> "Permitting delays are blocking affordable housing!"

**With permit-by-rule:**
> "Compliant designs approved same-day via automated validation."

**You become the solution, not the problem.**

## Implementation Roadmap

### Phase 1: Pilot (Months 1-6)

**Target:** Accessory Dwelling Units (ADUs)

**Why ADUs?**
- High demand, political priority
- Prescriptive code (IRC) — easy to automate
- Low risk (single-family residential)
- Visible impact (approval times drop to hours)

**Steps:**
1. **Policy:** "ADU permits passing automated validation receive same-day approval"
2. **Integration:** Connect OpenPermit API to permit portal
3. **Training:** 2-hour workshop for plan reviewers
4. **Pilot:** Process first 10 ADUs with OpenPermit
5. **Measure:** Track approval times, error rates, staff feedback

**Target metric:** 90% of ADU permits approved within 24 hours

### Phase 2: Expansion (Months 6-12)

**Add permit types:**
- Single-family residential (prescriptive IRC)
- Residential additions and alterations
- Simple commercial (prescriptive IBC)

**Refine workflow:**
- Automated validation for standard cases
- Flagged review for complex/non-compliant designs
- Audit sampling (10% spot-check for quality control)

**Target metric:** 70% of residential permits auto-approved

### Phase 3: Regional Coordination (Year 2)

**Partner with neighboring jurisdictions:**
- Share validation rule packs (local code amendments)
- Coordinate pre-approved plan lists
- Joint training for plan reviewers

**Unlock:** Regional pre-approved plan marketplace (design once, approve everywhere)

### Phase 4: Full Deployment (Year 3+)

**All permit types:**
- Residential prescriptive: Instant approval
- Commercial prescriptive: Same-day approval
- Engineered/performance: Hybrid (auto-check prescriptive portions, flag for PE review)
- Zoning compliance: Automated GIS checks

**Outcome:** Your jurisdiction is a national model for efficient permitting.

## Technical Integration

### Option 1: API Integration (Recommended)

Connect OpenPermit API to your existing permit portal:

```javascript
// Applicant submits IFC model via portal
const model = await uploadIFC(file);

// Your system calls OpenPermit API
const validation = await openpermit.validate({
  model: model.url,
  code: 'IRC2021',
  jurisdiction: 'austin-tx',
  amendments: ['austin-2024-water-quality']
});

// If pass → Auto-approve
if (validation.result === 'pass') {
  await approvePermit(application.id);
  await notifyApplicant('Approved');
} else {
  await flagForReview(application.id, validation.issues);
}
```

**Your portal, OpenPermit validation** — seamless integration.

### Option 2: SaaS Portal (Turnkey)

Use OpenPermit-compatible permit management platforms:
- Submit applications
- Automated validation
- Workflow management
- Payment processing
- Public portal

**Third-party vendors** (coming soon) will offer turnkey solutions.

### Option 3: Hybrid (Manual Upload)

For small jurisdictions without IT resources:
1. Applicant submits IFC model + validation report (PDF)
2. Staff uploads model to OpenPermit web validator
3. Confirms validation results match applicant's report
4. **Approves** if compliant

**No custom integration required** — just a web browser.

## Addressing Concerns

### "Will this eliminate plan reviewer jobs?"

**No. It reallocates their time to higher-value work.**

**Current:** 80% of staff time on prescriptive residential (objective checks)
**With OpenPermit:** 10% on prescriptive (audit sampling), 90% on complex projects

**Your reviewers shift to:**
- Commercial plan review
- Performance-based designs
- Variance hearings and appeals
- Code development and amendments
- Quality audits of automated validations

**The backlog is so large** that freeing up capacity just lets you **catch up**, not downsize.

### "What if automated validation makes mistakes?"

**Safeguards:**
1. **Spot-check audits** — Sample 10% of auto-approved permits for quality control
2. **Versioned validators** — Each permit logs which validator version was used
3. **Audit trails** — Full record of which checks passed/failed
4. **Override authority** — Jurisdiction can always require human review
5. **Validator certification** — ICC/third-party certification (like structural software)

**Validators are tools, not replacements for authority.**

### "What about our local code amendments?"

**OpenPermit is fully extensible:**

```python
# Add local amendment to knowledge pack
# austin-tx-2024-water-quality.py

def check_water_quality_review(project):
    """
    Austin-specific: Projects in Edwards Aquifer
    recharge zone require water quality review
    """
    if project.location.in_recharge_zone:
        return ValidationResult(
            status="requires_review",
            code_ref="Austin LDC 25-8-122",
            message="Water quality review required (Edwards Aquifer recharge zone)"
        )
    return ValidationResult(status="not_applicable")
```

**Your amendments are first-class citizens** in OpenPermit validation.

### "How do we ensure data privacy?"

**You control the data:**
- OpenPermit validates **on your infrastructure** (not cloud)
- No permit data sent to third parties (unless you choose CKAN publishing)
- Applicant data stored per your policies

**OpenPermit is software, not a service** — you run it locally.

### "What's the cost?"

**$0 for the software (open source, MIT license).**

**Optional costs:**
- **Implementation consulting** ($10K-30K for integration)
- **Staff training** ($2K-5K one-time)
- **Infrastructure** (server costs ~$500/month for cloud hosting)

**ROI:** First year savings in staff time = 10-20× implementation cost.

**Grants available:** HUD, EPA, DOT often fund permit modernization.

## Case Study: Example Jurisdiction

**City of [Pilot City], Population 250,000**

**Before OpenPermit:**
- 3,200 residential permits/year
- 6 plan reviewers
- Average review time: 3-6 weeks
- Backlog: 400+ permits

**After OpenPermit (Year 1):**
- 4,800 residential permits/year (+50%)
- 6 plan reviewers (same staff)
- Average review time: 2 days (prescriptive), 2 weeks (complex)
- Backlog: 0

**Impact:**
- **Staff satisfaction up** — Less tedious work, more complex challenges
- **Builder satisfaction up** — Predictable, fast approvals
- **Political wins** — "City approves ADUs same-day"
- **Open data compliance** — HUD/Census reporting automated

**Cost:** $25K implementation, $6K/year software hosting
**Savings:** $180K/year in staff time + $2M/year in community economic value (reduced delays)

## Federal Alignment Benefits

### HUD (Housing & Urban Development)

**BLDS Compliance:**
- OpenPermit auto-generates BLDS reports
- One-click submission to HUD systems
- **Eligibility for federal housing grants**

### EPA (Environmental Protection Agency)

**Stormwater Permits:**
- Construction permit data feeds NPDES tracking
- Environmental review linkage
- **NEPA compliance reporting**

### Census Bureau

**Building Permits Survey (BPS):**
- Automated monthly submissions
- Real-time housing starts data
- **Better federal statistics** for policy decisions

## Regional Coordination Opportunities

### Multi-Jurisdiction Partnerships

**Scenario:** 5 cities in metro area adopt OpenPermit

**Benefits:**
- **Shared validation rules** — Split development cost
- **Pre-approved regional plans** — Design approved in one city = auto-approved in all
- **Consistent standards** — Builders face same requirements across region

**Example:**
> "Metro Denver ADU Standards" — Pre-approved ADU designs acceptable in 8 jurisdictions

### State-Level Programs

**State building official pre-approves plans:**
- OpenPermit validation confirms compliance
- **400+ local jurisdictions auto-accept**

**Like UL listing for buildings** — test once, accept everywhere.

## Getting Started

### Step 1: Designate Pilot Lead

Assign a **permitting modernization champion** (often IT + Building Official collaboration).

### Step 2: Join Pilot Program

Contact: j@corelot.net

**We provide:**
- Implementation guide
- Training materials
- Technical support
- Community of practice (monthly calls with other pilot jurisdictions)

### Step 3: Policy Adoption

**Sample ordinance language:**

> *"Building permit applications for single-family residential structures meeting prescriptive code requirements (IRC 2021) and passing automated validation via OpenPermit-certified validators shall receive approval within 24 hours of submission, subject to spot-check quality audits."*

### Step 4: Technical Integration

- API integration (recommended) or web portal
- Training for plan reviewers (2-hour workshop)
- Soft launch with first 10 permits

### Step 5: Measure and Refine

**Track:**
- Average approval times (before/after)
- Error rates (false positives/negatives)
- Staff time savings
- Applicant satisfaction

**Refine:**
- Adjust sampling rates for audits
- Add local validation rules
- Expand to additional permit types

## Key Metrics for Success

| Metric | Target (Year 1) |
|--------|-----------------|
| **Prescriptive residential approval time** | < 24 hours (90% of permits) |
| **Auto-approval rate** | 70%+ (prescriptive IRC) |
| **Error rate** | < 2% (false positives/negatives) |
| **Staff time savings** | 50%+ (on prescriptive permits) |
| **Applicant satisfaction** | 4.5/5 average rating |

## Support and Resources

### Technical Support
- **Documentation:** https://docs.openpermit.org
- **GitHub:** https://github.com/builtbycorelot/OpenPermit
- **Community forum:** (coming soon)

### Policy Resources
- Sample ordinances
- Council presentation templates
- FAQ for elected officials

### Training
- Plan reviewer workshops
- IT integration guides
- Public communication materials

## Call to Action

**The housing crisis is a permitting crisis. You can be the solution.**

- Adopt permit-by-rule for prescriptive residential
- Process 10× more permits with the same staff
- Become a national model for efficient, transparent permitting

**Contact:** j@corelot.net to join the pilot program

---

## Key Takeaway

> **You're not the bottleneck — the manual process is.**

OpenPermit gives you the tools to approve compliant designs instantly, focus staff on complex projects, and lead on affordable housing.

**Let's modernize permitting together.**
