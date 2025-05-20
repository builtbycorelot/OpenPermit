"""Validate the workflow.jsonld file using the pyld library."""

import json
import sys
from pyld import jsonld


def validate(path="workflow.jsonld"):
    """Load and validate the given JSON-LD file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Attempt to expand the document. If it fails, pyld will raise an error.
    jsonld.expand(data)


if __name__ == "__main__":
    try:
        validate()
    except Exception as exc:
        print(f"Invalid JSON-LD: {exc}")
        sys.exit(1)
    else:
        print("workflow.jsonld is valid JSON-LD")
