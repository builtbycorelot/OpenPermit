# OpenPermit

Permitting - Distilled for Efficiency, Simplicity, interoperability, speed and security. 

Proposing an efficient method for municipal entities to host and interact with businesses/individuals.

Please comment/contribute/share/join!

## Table of Contents
- [Interoperable Data Layer](#interoperable-data-layer)
- [References](#references)
- [Security](#security)

Why this matters:

https://subnational.doingbusiness.org/en/data/exploretopics/dealing-with-construction-permits/why-matters

The basics:

## Interoperable Data Layer
- EPA Permitting schemas available in `openpermit/standards/epa-permitting`.
- Generate NIEM 6.0 JSON Schemas with `python scripts/niem6_build_schemas.py`.

### Building NIEM Schemas
Run `python scripts/niem6_build_schemas.py` to generate stub JSON Schema files under `openpermit/schema/niem/6.0/`.


A high-level architecture diagram is available in
[mermaid/architecture.mmd](mermaid/architecture.mmd).
A summary of NIEM alignment and augmentation is available in
[docs/niem-alignment-6.0.md](docs/niem-alignment-6.0.md).


Maintain state-of-the-art - maximal reliability, maximal security, standards-based-interoperability.

Culminate Projects, Comments, Feedback, Sponsors, Collaborators: Local/State/Federal Permitting Agencies

## Security
See [SECURITY.md](SECURITY.md) for the project's security policy.

## References

### Government and Policy Frameworks

- **The White House (2025).** [Fact Sheet: President Trump Brings Permitting Technology into the 21st Century for Government Efficiency](https://www.whitehouse.gov/fact-sheets/2025/04/fact-sheet-president-trump-brings-permitting-technology-into-the-21st-century-for-government-efficiency/)  
  Announces a federal permitting modernization mandate focusing on streamlining processes through digital technology, data transparency, and performance improvements.

- **U.S. Office of Management and Budget (2016).** [M‑16–21: Federal Source Code Policy – Achieving Efficiency, Transparency, and Innovation through Reusable and Open Source Software](https://digital.gov/resources/requirements-for-achieving-efficiency-transparency-and-innovation-through-reusable-and-open-source-software/)  
  Official policy encouraging federal agencies to release custom-developed code as open source and prioritize reuse, transparency, and cost efficiency.

- **General Services Administration (2023).** [GSA Open Source Policy](https://open.gsa.gov/oss/)  
  Details GSA’s open technology policy emphasizing the reuse, sharing, and release of open source software across federal projects.

- **Wikipedia Contributors (2023).** [Adoption of Free and Open‑Source Software by Public Institutions](https://en.wikipedia.org/wiki/Adoption_of_free_and_open-source_software_by_public_institutions)  
  Overview of how governments and public agencies worldwide have adopted free and open‑source software (FOSS) policies for improved transparency and innovation.

- **New America Foundation (2022).** [Building and Reusing Open Source Tools in Government](https://www.newamerica.org/digital-impact-governance-initiative/reports/building-and-reusing-open-source-tools-government/section-one-an-overview-of-open-source/)  
  Report outlining the importance and challenges of implementing open source software in U.S. government technology projects.

- **Federal Geographic Data Committee (2018).** [Geospatial Data Act of 2018 (GDA)](https://www.fgdc.gov/gda)  
  Establishes a framework for coordinated development, sharing, and management of geospatial data across federal, state, and local agencies.

- **U.S. Department of the Interior (n.d.).** [Federal Permitting Process](https://www.doi.gov/ocl/federal-permitting-process)  
  Overview of the federal permitting process, detailing coordination and regulatory requirements for major projects.

- **Federal Permitting Improvement Steering Council (n.d.).** [Our Mission](https://www.permitting.gov/about/our-mission)  
  Describes the mission to improve efficiency and transparency in federal environmental reviews and permitting processes.

- **U.S. Environmental Protection Agency (n.d.).** [What is the National Environmental Policy Act?](https://www.epa.gov/nepa/what-national-environmental-policy-act)  
  Explains the National Environmental Policy Act (NEPA), which governs environmental impact assessments for federal permitting.

- **Center for Strategic and International Studies (n.d.).** [Government Open Source Software Policies](https://www.csis.org/programs/strategic-technologies-program/resources/government-open-source-software-policies)  
  Analyzes global government policies on open source software adoption, highlighting benefits and challenges.

- **Federation of American Scientists (n.d.).** [How to Build Effective Digital Permitting Products in Government](https://fas.org/publication/how-to-build-effective-digital-permitting-products-in-government/)  
  Provides guidance on developing digital permitting systems, focusing on user-centered design and technology integration.

---

### Standards and Specifications

- **OData Organization (n.d.).** [OData (Open Data Protocol)](https://www.odata.org/) & [GitHub – OData](https://github.com/OData)  
  Official site and GitHub repository for the OData RESTful API protocol specification, libraries, and tools.

- **Open Design Alliance (2023).** [ODA Platform Technologies Overview](https://www.opendesign.com/products/oda-platform)  
  SDKs for DWG, DXF, PDF, SVG, IFC, Revit, and more, supporting interoperability across AEC file formats.

- **Adobe Systems Incorporated (2020).** [PDF Reference, Sixth Edition, Version 1.7](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_1-7.pdf)  
  Describes PDF’s vector capabilities, layers, metadata, and embedded files for document management.

- **International Organization for Standardization (ISO) (2012).** [ISO 19005-3:2012 – PDF/A‑3 for Long‑Term Archival with Embedded Files](https://www.iso.org/standard/57229.html)  
  Defines how PDFs can include embedded JSON, XML, CAD files, etc., for document and data delivery.

- **PDF Association (2023).** [PDF/E – PDF for Engineering](https://www.pdfa.org/specifications/pdf-e/)  
  ISO standard for engineering drawings, including support for 3D content and metadata.

- **Microsoft (2020).** [Open Packaging Conventions (ISO/IEC 29500)](https://docs.microsoft.com/en-us/openspecs/office_standards/ms-opc)  
  A ZIP-based container format used in Office Open XML, useful for bundling graphics and data.

- **National Institute of Standards and Technology (NIST) (2020).** [NIST SP 800‑53, Rev. 5: Security and Privacy Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)  
  Provides security and privacy controls for federal information systems.

- **World Wide Web Consortium (W3C) (2023).** [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)  
  Guidelines ensuring web accessibility for government systems, meeting Section 508 requirements.

- **Object Management Group (n.d.).** [Business Process Model and Notation (BPMN)](https://www.bpmn.org/)  
  Graphical standard for modeling business processes, useful for permitting workflows.

- **NIEMOpen (n.d.).** [National Information Exchange Model (NIEM)](https://www.niem.gov/)  
  Framework for standardized information exchange across government agencies using XML.

- **International Organization for Standardization (ISO) (2018).** [ISO 37120:2018 – Sustainable Cities and Communities](https://www.iso.org/standard/68498.html)  
  Indicators for city services and quality of life (less relevant for permitting).

- **U.S. Environmental Protection Agency (n.d.).** [Data Standards](https://www.epa.gov/data/data-standards)  
  Overview of EPA’s data standards for environmental data, including permitting information.

- **Open Data Standards (n.d.).** [Building & Land Development Specification (BLDS)](https://permitdata.org/)  
  Standard for sharing open data on building and construction permits.

- **U.S. Environmental Protection Agency (2006).** [Permitting Information Data Standard (EX000021.2)](https://www.exchangenetwork.net/standards/Permit_Info_01_06_2006_Final.pdf)  
  Data elements for identifying and tracking environmental permitting information.

- **U.S. Environmental Protection Agency (n.d.).** [ICIS‑NPDES Data Element Dictionary](https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary)  
  Data standards for National Pollutant Discharge Elimination System permits.

---

### Open Standards and Models for BIM/GIS

- **buildingSMART International (2021).** [IFC Schema Specification](https://technical.buildingsmart.org/standards/ifc/)  
  Defines the open data model for BIM, supporting geometry and metadata.

- **buildingSMART International (2022).** [IFC JSON Proposal](https://github.com/buildingSMART/ifc-json)  
  JSON serialization of Industry Foundation Classes (IFC) for web and software integration.

- **CityJSON (2023).** [CityJSON Specification](https://www.cityjson.org)  
  JSON‑based format for urban 3D models, including geometry and semantics.

- **Open Geospatial Consortium (OGC) (2021).** [OGC InfraGML Encoding Standard](https://www.ogc.org/standards/infragml)  
  XML/JSON schema for representing civil infrastructure with geospatial references.

- **buildingSMART International (n.d.).** [About openBIM](https://www.buildingsmart.org/about/openbim/)  
  Overview of openBIM principles for interoperable BIM workflows.

---

### Tools and Libraries

- **BlenderBIM Project (2023).** [Free Open Source BIM for Blender](https://blenderbim.org)  
  Outputs SVG with embedded semantic metadata for each IFC object class.

- **Autodesk Forge (2023).** [Forge Viewer and APIs](https://forge.autodesk.com)  
  Converts CAD/BIM models into streamable web formats with metadata layers.

- **Bentley Systems (2023).** [iTwin Platform](https://www.bentley.com/software/itwin-platform/)  
  Provides a unified model and metadata environment for infrastructure projects.

- **Inkscape Developers (2023).** [Inkscape: Open Source Vector Editor](https://inkscape.org)  
  Converts between DXF, SVG, and PDF with layer and shape structure preservation.

- **ezdxf Project (2023).** [ezdxf Python Library](https://ezdxf.mozman.at)  
  Programmatic access to read, write, and convert DXF files.

- **GDAL/OGR Contributors (2023).** [GDAL/OGR Library](https://gdal.org)  
  Tool for converting geospatial formats like DXF to GeoJSON.

- **Aspose Pty Ltd (2023).** [Aspose.CAD for .NET](https://products.aspose.com/cad/net)  
  Commercial SDK for converting DWG/DXF to SVG, PDF, and more.

- **USDA Forest Service (n.d.).** [fs-open-forest-platform](https://github.com/USDAForestService/fs-open-forest-platform)  
  Open‑source platform for U.S. Forest Service permitting, including Christmas tree and special use permits.

- **SJSU272LabF17 (n.d.).** [Permit-ML](https://github.com/SJSU272LabF17/Permit-ML)  
  Machine learning project for permit data analysis.

- **GitHub (n.d.).** [github-mcp-server](https://github.com/github/github-mcp-server)  
  Server infrastructure for managing permitting data.

- **Accord Project (n.d.).** [aec3po](https://github.com/Accord-Project/aec3po)  
  Ontology for digital building permit compliance checking and automation.

- **eGovernments Foundation (n.d.).** [DIGIT-OSS](https://github.com/eGovernments/DIGIT-OSS)  
  Open‑source platform for urban governance, including permitting modules.

- **opensourceBIM (n.d.).** [BIMserver](https://github.com/opensourceBIM/BIMserver)  
  Open‑source BIM server for managing IFC‑based projects.

- **Protege Project (n.d.).** [protege](https://github.com/protegeproject/protege)  
  Open‑source ontology editor, useful for developing permitting ontologies.

- **deve-sh (n.d.).** [Permit-System](https://github.com/deve-sh/Permit-System)  
  Open‑source permitting system prototype.

---

### Research and Case Studies

- **Singh, R., & Kadam, K. (2021).** [Conversion of CAD-Based Utility Drawings into 3D GeoJSON](https://www.ijcaonline.org/archives/volume183/number20/singh-2021-ijca-921573/). *International Journal of Computer Applications, 183*(20).  
  Methods for transforming 2D CAD to data-rich GeoJSON for urban planning.

- **Singapore Building and Construction Authority (2020).** [CORENET X: Regulatory Transformation](https://www.corenet.gov.sg)  
  National BIM permitting initiative demonstrating automation and efficiency.

- **Noardo, F., et al. (2025).** [Digital Building Permits in Practice: An International Survey and Future Perspectives](https://www.sciencedirect.com/science/article/pii/S2352710225005200). *Journal of Building Engineering, 85,* 109374.  
  Surveys global digital building permit practices, highlighting automation trends.

- **Chognard, S., et al. (2023).** [Digital Building Permits – Towards a Digital Built Environment](https://www.sciencedirect.com/science/article/pii/S2452414X23000924). *Digital Twin Cities, 1,* 100013.  
  Discusses digital building permit systems and their role in digital twins.

- **Andresen, E. T., et al. (2024).** [Digital Building Permits: A Review of Processes, Challenges, and Opportunities](https://www.sciencedirect.com/science/article/abs/pii/S1474034623004421). *Advanced Engineering Informatics, 62,* 102627.  
  Reviews digital permitting processes, identifying challenges and technological opportunities.

- **KnowledgeSpeak (2024).** [Digital Building Permit Ontology Released](https://www.knowledgespeak.com/ontospeak/digital-building-permit-ontology-released/)  
  Announces the release of a digital building permit ontology for compliance checking.

- **Accord Project (2024).** [Building Compliance Ontology Released](https://accordproject.eu/building-compliance-ontology-released/)  
  Details the release of the AEC3PO ontology for digital building permits.

- **Accord Project (n.d.).** [Urban Planning & Digital Building Permits Platforms](https://accordproject.eu/urban-planning-digital-building-permits-platforms/)  
  Explores platforms for digital building permits in urban planning contexts.

- **Public Digital (n.d.).** [Open Source in Government](https://github.com/publicdigital/open-source-in-government)  
  Repository documenting open source adoption strategies in government settings.

---

### Regulatory Standards

- **Occupational Safety and Health Administration (OSHA) (n.d.).** [Standard Number 1926.1205 – Permitting Process](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1205)  
  Defines permitting processes for construction-related safety regulations.  

https://link.springer.com/chapter/10.1007/978-3-031-37189-9_32

Research:
FAST‑41 Permit Standards & Guidance

Statutory Authority: Title 41 of the FAST Act (42 U.S.C. § 4370m et seq.) establishes the Federal Permitting Improvement Steering Council (FPISC), requires project‑specific Coordinated Project Plans with enforceable schedules, and mandates public tracking via the Permitting Dashboard 
Performance.gov
.

Official Guidance (M‑17‑14): FPISC’s January 13, 2017 guidance (M‑17‑14) outlines procedural requirements—e.g. facilitating agency roles, performance schedules, transparency rules, and extension protocols—for covered projects 
Performance.gov
.

Permitting Dashboard Data Standards: The Federal Infrastructure Permitting Dashboard provides a machine‑readable data portal (CSV/JSON) with standardized fields like “project_status,” “milestones,” and “agency_actions” to ensure consistent reporting across agencies 
Performance.gov
.

One Federal Decision (EO 13807): Executive Order 13807 aligns with FAST‑41 by requiring a single, coordinated environmental review and authorization record for major federal projects, with deadlines harmonized under the FAST‑41 CPP process 
Performance.gov
.

Other Permit Strategies & Standards

NEPA / CEQ Regulations (40 C.F.R. §§ 1500–1508): The Council on Environmental Quality’s implementing regulations set “action‑forcing” procedural requirements (scoping, EAs/EISs, public involvement) for all federal environmental reviews 
FHWA Environmental Programs
.

General Permits under the Clean Water Act (CWA § 402 / 40 C.F.R. Part 122): EPA’s NPDES general permit framework allows a single permit to cover multiple dischargers with similar operations—streamlining approval via predefined conditions rather than individual reviews 
US EPA
.

State‑Level Integrated Reviews: Many states operate “one‑stop shop” e‑permitting portals (e.g. California’s CEQA/permit integration, New York’s SEQR) to consolidate environmental and land‑use approvals in a single application.

Permit‑by‑Rule & General Authorization Models: Regulatory schemes (e.g. stormwater, small wind turbines, agricultural water use) use “permit‐by‐rule” approaches where compliance with standard practices automatically authorizes the activity.

Digital Engagement & Public Comment APIs: Modern platforms embed public‑comment modules and webhook‑based notifications to integrate stakeholder feedback directly into permit records.

BIM/GIS‑Enabled Permit Submissions: ISO 19650 (BIM data exchange) and OGC CityGML/InfraGML standards are increasingly adopted to submit 3D models and geospatial data as part of permit applications.

Risk‑ and Performance‑Based Permitting: Frameworks like RCRA tiered permits or EPA’s sector‑based air permits focus resources on higher‑risk sources while granting blanket coverage to low‑risk activities.

BIM Level 2 was a UK-defined benchmark for collaborative BIM working, focusing on federated models, shared information through a CDE, and defined data structures, originally based on the PAS 1192 standards.
ISO 19650 is the international standard that has adopted, refined, and formalized the principles of BIM Level 2. It provides a globally recognized framework for managing information throughout the asset lifecycle using BIM. Complying with ISO 19650 is now the standard way to implement the processes and achieve the outcomes previously associated with BIM Level 2.

![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/builtbycorelot/OpenPermit?utm_source=oss&utm_medium=github&utm_campaign=builtbycorelot%2FOpenPermit&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)
