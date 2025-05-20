"""Minimal importer for EPA XML files.

This script parses an EPA permit XML document and converts it to a set of OpenPermit node dictionaries compatible with the JSON-Schemas in `openpermit/standards/epa-permitting/schema`.

The implementation is intentionally simple and should be expanded with full field mappings and error handling.
"""

import json
import sys
import xml.etree.ElementTree as ET

def parse_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    permit_id = root.findtext("PermitIdentifier")
    permit_name = root.findtext("PermitName")
    return {
        "identifier": permit_id,
        "name": permit_name,
        "epaTag": "PermitIdentification"
    }

def convert_to_nfl(data):
    return {
        "type": "permit.core",
        "data": data
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: epa_importer.py <permit.xml>", file=sys.stderr)
        sys.exit(1)
    permit = parse_xml(sys.argv[1])
    nfl_doc = convert_to_nfl(permit)
    json.dump(nfl_doc, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
