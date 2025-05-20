"""Validate workflow JSON-LD using pyld."""
import json
import sys
from pyld import jsonld


def validate(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if '@context' not in data:
        raise ValueError('Missing @context in workflow')
    jsonld.expand(data)


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'workflow.jsonld'
    try:
        validate(target)
    except Exception as exc:
        print(f'Validation error: {exc}')
        sys.exit(1)
    print('Workflow JSON-LD is valid.')
