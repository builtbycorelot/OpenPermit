"""Generate a small example ontology in Turtle format.

The ontology is defined using simple Python data structures.  Running this script
will create ``open_data_ontology.owl`` in the same directory.
"""

from pathlib import Path

# Basic class and property definitions used to build the ontology
CLASSES = {
    "Permit": "A permit record.",
    "Applicant": "An applicant for a permit.",
}

PROPERTIES = [
    {
        "name": "hasApplicant",
        "domain": "Permit",
        "range": "Applicant",
        "comment": "Links a permit to its applicant.",
    }
]

PREFIXES = """@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix : <http://open-permit.org/ontology/> .
"""


def build_ontology() -> str:
    """Return the ontology as a Turtle string."""
    lines = [PREFIXES]
    for name, comment in CLASSES.items():
        lines.extend([
            f":{name} a owl:Class ;",
            f"    rdfs:label \"{name}\" ;",
            f"    rdfs:comment \"{comment}\" .",
            "",
        ])
    for prop in PROPERTIES:
        lines.extend([
            f":{prop['name']} a owl:ObjectProperty ;",
            f"    rdfs:domain :{prop['domain']} ;",
            f"    rdfs:range :{prop['range']} ;",
            f"    rdfs:label \"{prop['name'].replace('_', ' ')}\" ;",
            f"    rdfs:comment \"{prop['comment']}\" .",
            "",
        ])
    return "\n".join(lines)


def main(output: str = "open_data_ontology.owl") -> None:
    """Write the ontology to ``output``."""
    text = build_ontology()
    Path(output).write_text(text, encoding="utf-8")
    print(f"Wrote ontology to {output}")


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "open_data_ontology.owl"
    main(target)
