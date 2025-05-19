# Open Data Layer

This directory contains reference materials and sample files for the OpenPermit data layer.
It mirrors the structure described in the project documentation.  Each subfolder
contains placeholder content that can be replaced with real implementations.

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
├── .gitignore
├── LICENSE
└── README.md
```

## Generating the Example Ontology

The `ontology` folder includes a small OWL file and a helper script for
converting it to JSON-LD. To generate `workflow/workflow.jsonld` run:

```bash
pip install rdflib
python ontology/generate_ontology.py
```

The script loads `ontology/open_data_ontology.owl` and writes a JSON-LD
representation in the repository's `workflow` directory. The produced
`workflow.jsonld` aligns with the classes and properties defined in the OWL
example.
