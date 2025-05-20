"""Run all repository validation checks."""

import os
import subprocess
import sys


def main() -> None:
    repo_dir = os.path.dirname(os.path.abspath(__file__))

    schema_validator = os.path.join(
        repo_dir, "open-data-layer", "schema", "validate_schema.py"
    )
    workflow_validator = os.path.join(repo_dir, "workflow", "validate_workflow.py")

    for script in (schema_validator, workflow_validator):
        if os.path.exists(script):
            print(f"Running {script}...")
            subprocess.run([sys.executable, script], check=True)
        else:
            print(f"Warning: {script} not found")


if __name__ == "__main__":
    main()
