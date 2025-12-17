"""JSON-LD payload helpers for Matrix transport."""
from __future__ import annotations

from typing import Any, Dict

EVENT_TYPES = {
    "submission": "PermitSubmission",
    "status-update": "PermitStatus",
    "approval": "PermitApproval",
    "inspection": "InspectionScheduled",
    "inspection-media": "InspectionMedia",
}

EVENT_CONTEXT = {
    "@context": {
        "@vocab": "https://openpermit.io/ontology#",
        "permitId": "https://openpermit.io/ontology#permitId",
        "status": "https://openpermit.io/ontology#status",
        "lat": "https://schema.org/latitude",
        "lon": "https://schema.org/longitude",
        "contentUrl": "https://schema.org/contentUrl",
        "inReplyTo": "https://schema.org/inReplyTo",
        "metadata": "https://schema.org/additionalProperty",
    }
}


def build_event_payload(event_type: str, content: Dict[str, Any]) -> Dict[str, Any]:
    if event_type not in EVENT_TYPES:
        raise ValueError(f"Unsupported event type {event_type}")
    payload = {
        "msgtype": "m.text",
        "body": content.get("summary", EVENT_TYPES[event_type]),
        "eventType": EVENT_TYPES[event_type],
        "jsonld": content,
    }
    return payload


__all__ = ["EVENT_TYPES", "EVENT_CONTEXT", "build_event_payload"]
