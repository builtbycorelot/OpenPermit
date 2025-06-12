"""Utilities for managing workflow submissions with audit trail."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import importlib.util

_AUDIT_PATH = Path(__file__).resolve().parents[1] / "audit.py"
spec = importlib.util.spec_from_file_location("audit", _AUDIT_PATH)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

# Default audit log stored alongside this module
_DEFAULT_TRAIL = audit.AuditTrail(Path(__file__).with_name("submission_audit.log"))


def _write(path: Path | str, data: Any) -> None:
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def create_submission(path: Path | str, data: Any, user: str, trail: audit.AuditTrail | None = None) -> None:
    """Create a submission file and record an audit entry."""
    _write(path, data)
    (trail or _DEFAULT_TRAIL).record(path, user, "create")


def update_submission(path: Path | str, data: Any, user: str, trail: audit.AuditTrail | None = None) -> None:
    """Update a submission file and record an audit entry."""
    _write(path, data)
    (trail or _DEFAULT_TRAIL).record(path, user, "update")

