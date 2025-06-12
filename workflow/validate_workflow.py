"""Basic validator for workflow.jsonld."""

import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import audit

WORKFLOW_FILE = os.path.join(os.path.dirname(__file__), "workflow.jsonld")


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
        trail = audit.AuditTrail(os.path.join(os.path.dirname(__file__), "workflow_audit.log"))
        trail.record(WORKFLOW_FILE, user, "validate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
