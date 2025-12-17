from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)  # type: ignore[call-arg]
    return mod


bot_mod = _load_module(ROOT / "integrations" / "matrix" / "bot.py", "integrations.matrix.bot")
messages_mod = _load_module(
    ROOT / "integrations" / "matrix" / "messages.py", "integrations.matrix.messages"
)

MatrixEventValidator = bot_mod.MatrixEventValidator
build_jsonld_event = messages_mod.build_jsonld_event


def test_validator_accepts_valid_event():
    validator = MatrixEventValidator(ROOT / "integrations" / "matrix" / "shapes.ttl")
    event = build_jsonld_event(
        "PERMIT-123",
        "submission",
        {"submissionPath": "submissions/PERMIT-123.json"},
        status="received",
        actor="user",
    )
    validator.validate(event)


def test_validator_rejects_missing_permit():
    validator = MatrixEventValidator(ROOT / "integrations" / "matrix" / "shapes.ttl")
    event = {
        "@context": "https://openpermit.io/ontology",
        "@type": "https://openpermit.io/ontology#Submission",
        "payload": {},
    }
    with pytest.raises(ValueError):
        validator.validate(event)
