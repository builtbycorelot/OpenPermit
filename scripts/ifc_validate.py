#!/usr/bin/env python3
"""Simple wrapper around IfcOpenShell validation utilities."""

import argparse
from pathlib import Path
import sys


class ValidationError(Exception):
    """Raised when the IFC file fails validation."""


def validate_ifc(path: Path):
    """Validate an IFC file using IfcOpenShell.

    Returns a tuple ``(success, errors)``. ``success`` is ``True`` if no
    errors were reported. ``errors`` is a list of string messages.
    """

    try:
        import ifcopenshell
    except ImportError as exc:
        raise RuntimeError("IfcOpenShell is required to validate IFC files") from exc

    try:
        model = ifcopenshell.open(str(path))
    except Exception as exc:  # pragma: no cover - depends on external library
        return False, [f"Failed to parse IFC: {exc}"]

    errors = []
    validator = getattr(ifcopenshell, "validate", None)
    if validator and hasattr(validator, "run_checks"):
        try:
            results = validator.run_checks(model)
        except Exception as exc:  # pragma: no cover - depends on external library
            return False, [f"Validation error: {exc}"]

        for result in results:
            if isinstance(result, dict) and result.get("severity") == "Error":
                errors.append(result.get("message", str(result)))

    return (not errors), errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate IFC using IfcOpenShell")
    parser.add_argument("ifc_file", help="Path to IFC file")
    args = parser.parse_args(argv)

    success, errors = validate_ifc(Path(args.ifc_file))
    if success:
        print("IFC validation passed")
        return 0

    print("IFC validation failed:")
    for err in errors:
        print(f"- {err}")
    return 1


if __name__ == "__main__":  # pragma: no cover - CLI execution
    raise SystemExit(main())
