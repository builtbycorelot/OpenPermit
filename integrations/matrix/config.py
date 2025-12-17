"""Configuration primitives for the Matrix integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Set


@dataclass(slots=True)
class MatrixConfig:
    """Settings required to operate the Matrix bot."""

    homeserver: str
    user_id: str
    access_token: str
    device_id: str | None = None
    room_alias_prefix: str = "openpermit"
    default_participants: Set[str] = field(default_factory=set)
    shacl_shapes_path: Path = field(
        default_factory=lambda: Path(__file__).with_name("shapes.ttl")
    )

    def alias_for_permit(self, permit_id: str) -> str:
        """Build a stable, URL-safe room alias."""
        safe = permit_id.replace(" ", "-").lower()
        return f"#{self.room_alias_prefix}-{safe}:openpermit"

    def participants(self, extra: Iterable[str] | None = None) -> Set[str]:
        """Return the configured participant list with any extras merged in."""
        merged = set(self.default_participants)
        if extra:
            merged.update(extra)
        return merged
