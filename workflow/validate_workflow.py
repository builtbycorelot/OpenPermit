"""Basic validator for workflow.jsonld."""

import json
import os
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1]))

import audit

WORKFLOW_FILE = str(Path(__file__).resolve().with_name("workflow.jsonld"))


def main() -> int:
    try:
        with open(WORKFLOW_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:  # file missing or invalid JSON
        print(f"Error loading {WORKFLOW_FILE}: {exc}")
        return 1

    errors = []
    if "@id" not in data:
        errors.append("missing @id")
    if "schema:itemListElement" not in data:
        errors.append("missing schema:itemListElement")
    else:
        item_list = data["schema:itemListElement"]
        if not isinstance(item_list, list) or not item_list:
            errors.append("schema:itemListElement should be a non-empty list")

    if errors:
        print("workflow.jsonld INVALID:", "; ".join(errors))
        return 2

    print("workflow.jsonld VALID: contains @id and schema:itemListElement list")
    user = os.environ.get("AUDIT_USER")
    if user:
        trail = audit.AuditTrail(Path(__file__).resolve().with_name("workflow_audit.log"))
        trail.record(WORKFLOW_FILE, user, "validate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
