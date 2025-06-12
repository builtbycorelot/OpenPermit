from pathlib import Path
import importlib.util

# Load audit module from repository root
AUDIT_PATH = Path(__file__).resolve().parents[2] / "audit.py"
spec = importlib.util.spec_from_file_location("audit", AUDIT_PATH)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

# Load submission utilities
SUBMISSION_PATH = Path(__file__).resolve().parents[2] / "workflow" / "submission.py"
sspec = importlib.util.spec_from_file_location("submission", SUBMISSION_PATH)
submission = importlib.util.module_from_spec(sspec)
sspec.loader.exec_module(submission)


def test_create_update_log(tmp_path):
    log_file = tmp_path / "audit.log"
    trail = audit.AuditTrail(log_file)
    submission_file = tmp_path / "submission.json"

    submission.create_submission(submission_file, {"foo": 1}, "alice", trail)
    submission.update_submission(submission_file, {"foo": 2}, "alice", trail)

    events = trail.read()
    assert len(events) == 2
    assert events[0]["action"] == "create"
    assert events[1]["action"] == "update"
    assert events[0]["user"] == "alice"
    assert events[0]["file"] == str(submission_file)
