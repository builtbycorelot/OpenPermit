"""Simple CKAN API helper to publish JSON-LD datasets."""

import argparse
import json
from urllib import request


def push_dataset(ckan_url: str, api_key: str, package: dict) -> dict:
    """Send a CKAN ``package_create`` request with given package dict."""

    url = ckan_url.rstrip('/') + '/api/3/action/package_create'
    data = json.dumps(package).encode('utf-8')
    req = request.Request(
        url,
        data=data,
        headers={
            'Authorization': api_key,
            'Content-Type': 'application/json',
        },
    )
    with request.urlopen(req) as resp:
        return json.load(resp)


def main() -> None:
    parser = argparse.ArgumentParser(description='Publish JSON-LD dataset to CKAN')
    parser.add_argument('ckan_url', help='Base URL of the CKAN portal')
    parser.add_argument('api_key', help='API token for the CKAN user')
    parser.add_argument('dataset_file', help='Path to JSON-LD dataset file')
    parser.add_argument('--name', required=True, help='Unique dataset name')
    parser.add_argument('--title', required=True, help='Human-friendly title')
    args = parser.parse_args()

    with open(args.dataset_file, 'r', encoding='utf-8') as f:
        jsonld_text = f.read()

    package = {
        'name': args.name,
        'title': args.title,
        'extras': [{'key': 'jsonld', 'value': jsonld_text}],
    }

    result = push_dataset(args.ckan_url, args.api_key, package)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
