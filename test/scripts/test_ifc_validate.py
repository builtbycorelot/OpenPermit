from pathlib import Path
import importlib.util
import sys
import types

SCRIPT_PATH = Path(__file__).resolve().parents[2] / "scripts" / "ifc_validate.py"
spec = importlib.util.spec_from_file_location("ifc_validate", SCRIPT_PATH)
ifc_validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ifc_validate)


class DummyModel:
    pass


def _mock_ifcopenshell(valid: bool):
    mock = types.SimpleNamespace()

    def open(path):
        return DummyModel()

    validate = types.SimpleNamespace()

    def run_checks(model):
        if valid:
            return []
        return [{"severity": "Error", "message": "test error"}]

    validate.run_checks = run_checks

    mock.open = open
    mock.validate = validate
    return mock


def test_validate_ifc_pass(tmp_path, monkeypatch):
    mock = _mock_ifcopenshell(True)
    monkeypatch.setitem(sys.modules, "ifcopenshell", mock)
    model_path = tmp_path / "model.ifc"
    model_path.write_text("DATA")

    ok, errors = ifc_validate.validate_ifc(model_path)
    assert ok
    assert errors == []


def test_validate_ifc_fail(tmp_path, monkeypatch):
    mock = _mock_ifcopenshell(False)
    monkeypatch.setitem(sys.modules, "ifcopenshell", mock)
    model_path = tmp_path / "model.ifc"
    model_path.write_text("DATA")

    ok, errors = ifc_validate.validate_ifc(model_path)
    assert not ok
    assert errors == ["test error"]
