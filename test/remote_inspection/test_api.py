import base64
from pathlib import Path
import importlib.util
import sys

MODULE_PATH = Path(__file__).resolve().parents[2] / "remote_inspection" / "api.py"
spec = importlib.util.spec_from_file_location("remote_inspection.api", MODULE_PATH)
api_mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api_mod
spec.loader.exec_module(api_mod)
PhotoInspectionAPI = api_mod.PhotoInspectionAPI

PNG_DATA = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/woAAgMBAKRkYj8AAAAASUVORK5CYII="
)


def _write_png(tmp_path: Path) -> Path:
    path = tmp_path / "img.png"
    path.write_bytes(PNG_DATA)
    return path


def test_upload_photo(tmp_path):
    api = PhotoInspectionAPI()
    img = _write_png(tmp_path)
    record = api.upload_photo(img, 1.0, 2.0)
    assert record.location == (1.0, 2.0)
    assert record.metadata["validation"]["valid"] is True
