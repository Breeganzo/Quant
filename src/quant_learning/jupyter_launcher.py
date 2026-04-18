from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(".").resolve()
    command = [
        sys.executable,
        "-m",
        "jupyterlab",
        "--notebook-dir",
        str(root),
        "--ServerApp.open_browser=True",
        "--ServerApp.token=",
        "--ServerApp.password=",
    ]
    raise SystemExit(subprocess.call(command))
