"""Validate sample JSON files against minimal JSON Schemas."""

import json
import os
import sys

try:
    from jsonschema import validate, ValidationError
except Exception:  # jsonschema not installed
    class ValidationError(Exception):
        pass

    def validate(instance, schema):
        """Very small subset of JSON Schema validation."""
        for field in schema.get("required", []):
            if field not in instance:
                raise ValidationError(f"Missing required field '{field}'")
        props = schema.get("properties", {})
        for key, rules in props.items():
            if key not in instance:
                continue
            value = instance[key]
            t = rules.get("type")
            if t == "string" and not isinstance(value, str):
                raise ValidationError(f"Field '{key}' must be a string")
            if t == "number" and not isinstance(value, (int, float)):
                raise ValidationError(f"Field '{key}' must be a number")
            if t == "array" and not isinstance(value, list):
                raise ValidationError(f"Field '{key}' must be an array")
            if t == "object" and not isinstance(value, dict):
                raise ValidationError(f"Field '{key}' must be an object")

SCHEMAS = {
    "blds.json": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "status": {"type": "string"},
            "submittedDate": {"type": "string"}
        },
        "required": ["id", "status", "submittedDate"]
    },
    "ifc.json": {
        "type": "object",
        "properties": {
            "ifcVersion": {"type": "string"},
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "id": {"type": "string"}
                    },
                    "required": ["type", "id"]
                }
            }
        },
        "required": ["ifcVersion", "entities"]
    },
    "geojson.json": {
        "type": "object",
        "properties": {
            "type": {"enum": ["Feature"]},
            "geometry": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "coordinates": {"type": "array"}
                },
                "required": ["type", "coordinates"]
            },
            "properties": {"type": "object"}
        },
        "required": ["type", "geometry", "properties"]
    },
    "iso20022.json": {
        "type": "object",
        "properties": {
            "amount": {"type": "string"},
            "currency": {"type": "string"}
        },
        "required": ["amount", "currency"]
    }
}


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_valid = True
    for fname, schema in SCHEMAS.items():
        path = os.path.join(base_dir, fname)
        with open(path) as f:
            data = json.load(f)
        try:
            validate(data, schema)
            print(f"{fname}: VALID")
        except Exception as exc:  # catch ValidationError or fallback
            all_valid = False
            print(f"{fname}: INVALID - {exc}")
    if not all_valid:
        sys.exit(1)


if __name__ == "__main__":
    main()
