import json
from unittest.mock import MagicMock, patch

from pathlib import Path
import importlib.util

PUSH_DATASET_PATH = Path(__file__).resolve().parents[2] / "integrations" / "ckan" / "push_dataset.py"
spec = importlib.util.spec_from_file_location("push_dataset", PUSH_DATASET_PATH)
push_dataset_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(push_dataset_module)
push_dataset = push_dataset_module.push_dataset


def test_push_dataset_makes_request():
    package = {
        'name': 'demo',
        'title': 'Demo',
        'extras': [{'key': 'jsonld', 'value': '{}'}],
    }

    fake_response = MagicMock()
    fake_response.__enter__.return_value = fake_response
    fake_response.read.return_value = json.dumps({'success': True}).encode()
    fake_response.__iter__.return_value = iter([fake_response.read.return_value])

    with patch('urllib.request.urlopen', return_value=fake_response) as mock_urlopen:
        result = push_dataset('http://example.com', 'token', package)

    assert result == {'success': True}

    req = mock_urlopen.call_args.args[0]
    assert req.full_url == 'http://example.com/api/3/action/package_create'
    assert req.headers['Authorization'] == 'token'
    assert req.data == json.dumps(package).encode()

