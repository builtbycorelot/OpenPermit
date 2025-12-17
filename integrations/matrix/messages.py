"""Helpers for building JSON-LD events carried over Matrix."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

JSONLD_CONTEXT = "https://openpermit.io/ontology"

EVENT_TYPES = {
    "submission": "https://openpermit.io/ontology#Submission",
    "update": "https://openpermit.io/ontology#Update",
    "approval": "https://openpermit.io/ontology#Approval",
    "inspection": "https://openpermit.io/ontology#Inspection",
    "inspection-media": "https://openpermit.io/ontology#InspectionMedia",
}


def build_jsonld_event(
    permit_id: str,
    event_type: str,
    payload: Dict[str, Any],
    *,
    status: str | None = None,
    actor: str | None = None,
    thread_root: str | None = None,
) -> Dict[str, Any]:
    """Compose a JSON-LD event body for Matrix transport."""
    now = datetime.utcnow().isoformat() + "Z"
    type_iri = EVENT_TYPES.get(event_type, event_type)
    event = {
        "@context": JSONLD_CONTEXT,
        "@type": type_iri,
        "permitId": permit_id,
        "occurredAt": now,
        "payload": payload,
    }
    if status:
        event["status"] = status
    if actor:
        event["actor"] = actor
    if thread_root:
        event["thread"] = thread_root
    return event
