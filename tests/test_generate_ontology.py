import importlib.util
from pathlib import Path

# Load the generate_ontology module from its file path
module_path = Path(__file__).resolve().parents[1] / 'open-data-layer' / 'ontology' / 'generate_ontology.py'
spec = importlib.util.spec_from_file_location('generate_ontology', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

build_ontology = module.build_ontology


def test_build_ontology_contains_expected_terms():
    text = build_ontology()
    assert ':Permit a owl:Class ;' in text
    assert ':Applicant a owl:Class ;' in text
    assert ':hasApplicant a owl:ObjectProperty ;' in text
