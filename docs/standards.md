OpenPermit Data Standards
Overview
OpenPermit defines a standards-based data layer for permitting and tax transactions, ensuring interoperability across municipalities and agencies, incorporating diverse standards for building, geospatial, and infrastructure data.
Standards

BLDS (Building and Land Development Specification): For Application and Permit data.
Schema: JSON-LD with id, status, submittedDate.
Validation: JSON Schema.
Purpose: Structures data for building and land development processes in permitting workflows.


IFC (Industry Foundation Classes): For Document (DWG/DXF).
Schema: JSON-LD with ifcVersion, entities.
Validation: IFC EXPRESS.
Purpose: Represents building and construction data, aligning with BIM ontologies.


ISO 20022: For Transaction.
Schema: JSON-LD with amount, currency.
Validation: ISO 20022 JSON schema.


GeoJSON: For Location.
Schema: GeoJSON Feature with geometry, properties.
Validation: GeoJSON schema.
Purpose: Encodes geographic data structures for geospatial representation.


CityJSON: For 3D city models.
Schema: JSON-based encoding, part of CityGML family.
Validation: CityJSON schema.
Purpose: Supports urban planning and geospatial data in permitting.


InfraGML (Infrastructure GML): For infrastructure data.
Schema: OGC standard with GML encoding.
Validation: InfraGML schema.
Purpose: Encodes infrastructure data for geospatial and permitting models.


JSON-LD: For semantic metadata.
Schema: @context linking to BLDS, IFC, ISO 20022, CityJSON, InfraGML.


OData (Open Data Protocol): For queryable metadata.
Schema: EDM with entities (Application, Document).
Validation: OData CSDL.
Purpose: Extends RESTful API interoperability for permitting data.


RDF/OWL: For semantic relationships.
Schema: OWL ontology in ontology/open_data_ontology.owl.
Validation: SHACL.



Example
{
  "@context": ["http://schema.org", "http://standards.buildingsmart.org/IFC", "http://cityjson.org", "http://ogc.org/infragml"],
  "@type": "PermitApplication",
  "id": "APP123",
  "status": "submitted",
  "submittedDate": "2025-04-20",
  "documents": [
    {
      "@type": "DWGDocument",
      "id": "DOC789",
      "ifcVersion": "IFC4"
    }
  ],
  "location": {
    "@type": "GeoJSON",
    "geometry": {
      "type": "Point",
      "coordinates": [ -122.4194, 37.7749 ]
    }
  },
  "cityModel": {
    "@type": "CityJSON",
    "version": "1.1"
  }
}

