#!/usr/bin/env python3
"""Generate JSON Schema stubs from NIEM 6.0 metadata.

This script reads the NIEM 6.0 Common Model Format (CMF) and JSON-LD
context from the `openpermit/standards/niem/NIEM-Releases` submodule
and writes JSON Schema stub files under `openpermit/schema/niem/6.0/`.
"""

import argparse
import json
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Build NIEM 6.0 JSON Schemas")
    parser.add_argument(
        "--src",
        default="openpermit/standards/niem/NIEM-Releases",
        help="Path to the NIEM-Releases repository",
    )
    parser.add_argument(
        "--out",
        default="openpermit/schema/niem/6.0",
        help="Output directory for generated schemas",
    )
    return parser.parse_args()


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return {}


def build_schema(name, description=""):
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": name,
        "description": description,
        "type": "object",
        "properties": {},
    }


def main():
    args = parse_args()
    os.makedirs(args.out, exist_ok=True)

    cmf_path = os.path.join(args.src, "cmf", "niem6", "niem6.json")
    ctx_path = os.path.join(args.src, "json", "niem6", "niem6.jsonld")

    cmf = load_json(cmf_path)
    context = load_json(ctx_path).get("@context", {})

    for cls in cmf.get("classes", []):
        name = cls.get("name")
        schema = build_schema(name, cls.get("definition", ""))
        out_file = os.path.join(args.out, f"{name}.schema.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2)

    if context:
        ctx_out = os.path.join(args.out, "context.jsonld")
        with open(ctx_out, "w", encoding="utf-8") as f:
            json.dump({"@context": context}, f, indent=2)


if __name__ == "__main__":
    main()
