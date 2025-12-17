"""Matrix protocol integration for OpenPermit workflows."""

from .bot import MatrixPermitBot, MatrixEventValidator
from .config import MatrixConfig
from .messages import build_jsonld_event, EVENT_TYPES

__all__ = [
    "MatrixPermitBot",
    "MatrixEventValidator",
    "MatrixConfig",
    "build_jsonld_event",
    "EVENT_TYPES",
]
