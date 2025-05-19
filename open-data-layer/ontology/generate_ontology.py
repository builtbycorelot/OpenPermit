"""Simple example for converting the sample OWL ontology to JSON-LD."""

from pathlib import Path
from rdflib import Graph


def convert_ontology(owl_path: Path, output_path: Path) -> None:
    """Load ``owl_path`` and write a JSON-LD representation to ``output_path``."""
    g = Graph()
    g.parse(owl_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    g.serialize(destination=str(output_path), format="json-ld", indent=2)


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    owl_file = here / "open_data_ontology.owl"
    root = here.parent.parent
    workflow_jsonld = root / "workflow" / "workflow.jsonld"
    convert_ontology(owl_file, workflow_jsonld)
    print(f"Generated {workflow_jsonld}")
