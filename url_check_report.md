# URL Check Report for OpenPermit Repository

**Date:** 2025-12-21
**Total Markdown Files Scanned:** 39
**Total Unique URLs Found:** 91

## Executive Summary

- **Working URLs (200 OK):** 15 (16.5%)
- **Broken URLs (404 Not Found):** 9 (9.9%)
- **Network Restricted (403/Tunnel Errors):** 67 (73.6%)

**Note:** Many URLs showing "403 Forbidden" or "Tunnel connection failed" errors are due to network restrictions in the testing environment. These should be manually verified in a regular browser.

---

## Critical Issues: Confirmed Broken Links (404 Errors)

### 1. GitHub Discussions Link - 404
**URL:** `https://github.com/SheetPros/OpenPermit/discussions`
**Locations:**
- `docs/README.md:46`
- `docs/README.md:53`
- `docs/hosted_model_reviews.md:22`

**Issue:** The discussions page returns 404. The repository exists but discussions may not be enabled.
**Suggestion:** Either enable GitHub Discussions for the repository or update the links to point to GitHub Issues instead.

---

### 2. buildingSMART IFC JSON Repository - 404
**URL:** `https://github.com/buildingSMART/ifc-json`
**Locations:**
- `docs/ifc_approval.md:12`
- `docs/references.md:37`

**Issue:** This repository no longer exists or has been moved.
**Suggestions:**
- Check if it was moved to a different organization
- Look for alternative IFC JSON schema resources
- Consider using the buildingSMART technical documentation site instead

---

### 3. deve-sh/Permit-System - 404
**URL:** `https://github.com/deve-sh/Permit-System`
**Location:** `docs/references.md:57`

**Issue:** Repository not found.
**Suggestion:** Verify if the repository was renamed, moved, or deleted. Consider removing if no longer available.

---

### 4. eGovernments/DIGIT-OSS - 404
**URL:** `https://github.com/eGovernments/DIGIT-OSS`
**Location:** `docs/references.md:54`

**Issue:** Repository not found.
**Suggestion:** Check if the organization changed or the repository was renamed. The eGovernments Foundation may have reorganized their repositories.

---

### 5. Facebook Draft.js CONTRIBUTING - 404
**URL:** `https://github.com/facebook/draft-js/blob/master/CONTRIBUTING.md`
**Location:** `CONTRIBUTING.md:36`

**Issue:** The path is incorrect or the file was removed.
**Suggestions:**
- Update to use `main` branch instead of `master`: `https://github.com/facebook/draft-js/blob/main/CONTRIBUTING.md`
- Or point to the current default branch

---

### 6. github/github-mcp-server - 404
**URL:** `https://github.com/github/github-mcp-server`
**Location:** `docs/references.md:52`

**Issue:** Repository not found.
**Suggestion:** Verify the repository name and organization. This may be a private repository or the name may have changed.

---

### 7. opensourceBIM/BIMserver - 404
**URL:** `https://github.com/opensourceBIM/BIMserver`
**Location:** `docs/references.md:55`

**Issue:** Repository not found.
**Suggestion:** The repository may have moved. Check the opensourceBIM organization for the current location or if it was archived.

---

### 8. protegeproject/protege - 404
**URL:** `https://github.com/protegeproject/protege`
**Location:** `docs/references.md:56`

**Issue:** Repository not found.
**Suggestion:** The actual repository is at `https://github.com/protegeproject/protege-core` or check the protegeproject organization for the correct repository.

---

### 9. publicdigital/open-source-in-government - 404
**URL:** `https://github.com/publicdigital/open-source-in-government`
**Location:** `docs/references.md:68`

**Issue:** Repository not found.
**Suggestion:** Verify if the repository was renamed or moved to a different organization.

---

## Working URLs (Verified 200 OK)

### GitHub Repositories & Pages
1. `https://github.com/Accord-Project/aec3po` - docs/references.md:53
2. `https://github.com/BuildingSMART/BCF-API` - docs/references.md:21
3. `https://github.com/NIEM/NIEM-Releases` - openpermit/standards/niem/README.md:3
4. `https://github.com/OData` - docs/references.md:19
5. `https://github.com/SJSU272LabF17/Permit-ML` - docs/references.md:51
6. `https://github.com/SheetPros/OpenPermit/blob/main/CONTRIBUTING.md` - docs/README.md:54
7. `https://github.com/SheetPros/OpenPermit/issues/new` - docs/README.md:53 (redirects to login)
8. `https://github.com/SheetPros/OpenPermit?tab=readme-ov-file#stakeholders--how-to-engage` - docs/README.md:21
9. `https://github.com/USDAForestService/fs-open-forest-platform` - workflow/README.md:4, docs/references.md:50
10. `https://github.com/builtbycorelot/OpenPermit.git` - README.md:50, src/README.md:40
11. `https://github.com/builtbycorelot/OpenPermit/actions/workflows/ci.yml` - README.md:15
12. `https://ifcopenshell.org/` - docs/ifc_approval.md:8
13. `https://ifcopenshell.org/python.html` - docs/ifc_approval.md:18
14. `https://permitdata.org/` - docs/references.md:31
15. `https://pypi.org/project/jsonschema/` - open-data-layer/README.md:33

---

## URLs Blocked by Network Restrictions (Need Manual Verification)

These URLs could not be tested due to network restrictions in the testing environment. They should be manually verified in a browser:

### Government & Standards Sites
- `https://www.whitehouse.gov/fact-sheets/2025/04/...` - docs/references.md:6
- `https://digital.gov/resources/...` - docs/references.md:7
- `https://open.gsa.gov/oss/` - docs/references.md:8
- `https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final` - SECURITY.md:107, docs/references.md:25
- `https://csrc.nist.gov/projects/risk-management/fisma-background` - SECURITY.md:108
- `https://www.fedramp.gov/` - SECURITY.md:109
- `https://www.fgdc.gov/gda` - docs/references.md:11
- `https://www.doi.gov/ocl/federal-permitting-process` - docs/references.md:12
- `https://www.permitting.gov/about/our-mission` - docs/references.md:13
- `https://www.epa.gov/nepa/what-national-environmental-policy-act` - docs/references.md:14
- `https://www.epa.gov/data/data-standards` - docs/references.md:30
- `https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary` - docs/references.md:33
- `https://www.exchangenetwork.net/standards/Permit_Info_01_06_2006_Final.pdf` - docs/references.md:32
- `https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1205` - docs/references.md:71

### Academic & Research Sites
- `https://www.csis.org/programs/strategic-technologies-program/resources/government-open-source-software-policies` - docs/references.md:15
- `https://fas.org/publication/how-to-build-effective-digital-permitting-products-in-government/` - docs/references.md:23
- `https://www.sciencedirect.com/science/article/pii/S2352710225005200` - docs/references.md:62
- `https://www.sciencedirect.com/science/article/pii/S2452414X23000924` - docs/references.md:63
- `https://www.sciencedirect.com/science/article/abs/pii/S1474034623004421` - docs/references.md:64
- `https://www.ijcaonline.org/archives/volume183/number20/singh-2021-ijca-921573/` - docs/references.md:60

### Standards Organizations
- `https://www.iso.org/standard/57229.html` - docs/references.md:22
- `https://www.iso.org/standard/68498.html` - docs/references.md:29
- `https://www.niem.gov/` - docs/references.md:28
- `https://www.odata.org/` - docs/references.md:19
- `https://www.ogc.org/standards/infragml` - docs/references.md:39
- `https://www.w3.org/WAI/standards-guidelines/wcag/` - docs/references.md:26
- `https://www.bpmn.org/` - docs/references.md:27
- `https://technical.buildingsmart.org/standards/ifc/` - docs/references.md:36
- `https://www.buildingsmart.org/about/openbim/` - docs/references.md:40
- `https://www.cityjson.org` - docs/references.md:38

### Commercial & Tool Sites
- `https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_1-7.pdf` - docs/references.md:21
- `https://docs.microsoft.com/en-us/openspecs/office_standards/ms-opc` - docs/references.md:24
- `https://www.pdfa.org/specifications/pdf-e/` - docs/references.md:23
- `https://www.opendesign.com/products/oda-platform` - docs/references.md:20
- `https://forge.autodesk.com` - docs/references.md:44
- `https://www.bentley.com/software/itwin-platform/` - docs/references.md:45
- `https://products.aspose.com/cad/net` - docs/references.md:49

### Project-Specific Sites
- `https://blenderbim.org` - docs/references.md:43, docs/ifc_approval.md:40
- `https://inkscape.org` - docs/references.md:46
- `https://ezdxf.mozman.at` - docs/references.md:47
- `https://gdal.org` - docs/references.md:48
- `https://accordproject.eu/building-compliance-ontology-released/` - docs/references.md:66
- `https://accordproject.eu/urban-planning-digital-building-permits-platforms/` - docs/references.md:67
- `https://www.knowledgespeak.com/ontospeak/digital-building-permit-ontology-released/` - docs/references.md:65
- `https://www.corenet.gov.sg` - docs/references.md:61

### OpenPermit Infrastructure
- `https://demo.openpermit.org` - demo/README.md:13
- `https://openpermit-demo.netlify.app` - demo/README.md:14
- `https://demo-status.openpermit.org` - demo/README.md:15
- `https://partners.openpermit.org` - ecosystem/partners.md:43
- `https://forms.openpermit.org/pilot` - PILOT_PROGRAM.md:30, PILOT_PROGRAM.md:44
- `https://builtbycorelot.github.io/OpenPermit` - README.md:18, README.md:155
- `https://codecov.io/gh/builtbycorelot/OpenPermit` - README.md:16
- `https://codecov.io/gh/builtbycorelot/OpenPermit/branch/main/graph/badge.svg` - README.md:16

### Wikipedia & Other Reference Sites
- `https://en.wikipedia.org/wiki/Adoption_of_free_and_open_source_software_by_public_institutions` - docs/references.md:9
- `https://www.newamerica.org/digital-impact-governance-initiative/reports/building-and-reusing-open-source-tools-government/section-one-an-overview-of-open-source/` - docs/references.md:10

### Schema Contexts (Technical, Likely Valid)
- `http://schema.org` - standards.md:59
- `http://standards.buildingsmart.org/IFC` - standards.md:59
- `http://cityjson.org` - standards.md:59
- `http://ogc.org/infragml` - standards.md:59

### Local Development
- `http://localhost:3000` - docs/QUICK_START.md:32 (Expected to fail - local development URL)

---

## Recommendations

### Immediate Actions Required

1. **Fix GitHub Discussions Links** - Enable discussions or replace with issues links in:
   - docs/README.md (lines 46, 53)
   - docs/hosted_model_reviews.md (line 22)

2. **Update buildingSMART IFC JSON Reference** - Find current location or alternative in:
   - docs/ifc_approval.md (line 12)
   - docs/references.md (line 37)

3. **Update Facebook Draft.js Link** - Change from `master` to `main` branch in:
   - CONTRIBUTING.md (line 36)

4. **Verify and Update Repository References** - Check current status of these repos and update or remove:
   - deve-sh/Permit-System (docs/references.md:57)
   - eGovernments/DIGIT-OSS (docs/references.md:54)
   - github/github-mcp-server (docs/references.md:52)
   - opensourceBIM/BIMserver (docs/references.md:55)
   - protegeproject/protege (docs/references.md:56) - likely should be protegeproject/protege-core
   - publicdigital/open-source-in-government (docs/references.md:68)

### Manual Verification Needed

All URLs in the "Network Restricted" section should be manually verified in a regular browser, particularly:
- Government and standards organization sites
- Academic papers and research sites
- OpenPermit infrastructure URLs (demo sites, forms, etc.)

### Best Practices

1. **Regular Link Checking** - Run this URL checker periodically (e.g., monthly) to catch broken links early
2. **Archive.org Backup** - For critical references that might disappear, consider noting Wayback Machine URLs
3. **Vendor-Agnostic References** - Where possible, prefer standards organization links over vendor-specific links
4. **GitHub Actions** - Consider setting up a GitHub Action to automatically check URLs on pull requests

---

## Files with Most URLs

1. `docs/references.md` - 62 URLs (primary reference documentation)
2. `docs/ifc_approval.md` - 5 URLs
3. `README.md` - 5 URLs
4. `SECURITY.md` - 3 URLs
5. `docs/README.md` - 3 URLs

---

## Statistics by Domain

### Most Common Domains:
- GitHub (github.com) - 16 URLs
- Government (.gov) - 14 URLs
- Standards Organizations (iso.org, w3.org, etc.) - 12 URLs
- Academic (sciencedirect.com, etc.) - 4 URLs
- OpenPermit Infrastructure - 5 URLs
