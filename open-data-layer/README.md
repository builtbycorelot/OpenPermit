# Open Data Layer

This directory holds small examples that demonstrate how a permit system can be structured. Each subfolder contains sample data or helper scripts.

```
├── schema/
│   ├── blds.json
│   ├── ifc.json
│   ├── iso20022.json
│   ├── geojson.json
│   ├── sample_data.jsonld
│   ├── validation.shacl
│   └── validate_schema.py
├── ontology/
│   ├── open_data_ontology.owl
│   ├── queries.sparql
│   └── generate_ontology.py
├── docs/
│   ├── README.md
│   ├── standards.md
│   └── odata_edm.xml
```

## File descriptions

### schema/
- **blds.json** – Minimal BLDS permit example.
- **ifc.json** – Snippet of an IFC model.
- **iso20022.json** – Example payment message.
- **geojson.json** – GeoJSON feature for location data.
- **sample_data.jsonld** – JSON‑LD sample referencing the ontology.
- **validation.shacl** – SHACL shapes for RDF validation (placeholder).
- **validate_schema.py** – Script to validate the JSON samples above.

### ontology/
- **open_data_ontology.owl** – OWL ontology defining `Permit`, `Applicant` and their relationship.
- **queries.sparql** – Example SPARQL queries used during development.
- **generate_ontology.py** – Regenerates `open_data_ontology.owl`.

### docs/
Documentation and standards notes related to the data layer.

## Regeneration and validation
- Run `python ontology/generate_ontology.py` to recreate the example ontology.
- Validate the JSON examples with `python schema/validate_schema.py`. The command prints whether each file conforms to its minimal schema.
- `validation.shacl` can be used with any SHACL engine to validate `sample_data.jsonld` against RDF shapes.
