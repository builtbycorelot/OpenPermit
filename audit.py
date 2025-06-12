from __future__ import annotations

"""Simple audit trail utilities."""

from datetime import datetime
import json
from pathlib import Path
from typing import Iterable, List, Dict


class AuditTrail:
    """Append-only JSONL audit log."""

    def __init__(self, log_file: Path | str = "audit.log") -> None:
        self.log_file = Path(log_file)

    def record(self, file: Path | str, user: str, action: str) -> None:
        """Record an audit event."""
        entry = {
            "file": str(file),
            "user": user,
            "action": action,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_file, "a", encoding="utf-8") as f:
            json.dump(entry, f)
            f.write("\n")

    def read(self) -> List[Dict[str, str]]:
        """Return all audit entries."""
        if not self.log_file.exists():
            return []
        with open(self.log_file, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]

