from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import nbformat as nbf
from nbclient import NotebookClient


def notebook_paths(root: Path) -> list[Path]:
    return sorted(root.glob("week-*/notebooks/*.ipynb"))


def execute_notebook(path: Path, timeout: int, kernel_name: str, write_executed: bool) -> dict:
    started_at = time.perf_counter()
    notebook = nbf.read(path.open("r", encoding="utf-8"), as_version=4)

    try:
        client = NotebookClient(
            notebook,
            timeout=timeout,
            kernel_name=kernel_name,
            allow_errors=False,
        )
        client.execute()
        if write_executed:
            path.write_text(nbf.writes(notebook), encoding="utf-8")
        return {
            "path": str(path),
            "status": "passed",
            "duration_seconds": round(time.perf_counter() - started_at, 3),
            "error": "",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "path": str(path),
            "status": "failed",
            "duration_seconds": round(time.perf_counter() - started_at, 3),
            "error": f"{type(exc).__name__}: {exc}",
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Execute all generated curriculum notebooks.")
    parser.add_argument(
        "--curriculum-dir",
        default="curriculum",
        help="Path to curriculum directory (default: curriculum).",
    )
    parser.add_argument(
        "--report",
        default="exports/notebook-validation.json",
        help="JSON report output path (default: exports/notebook-validation.json).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Per-notebook execution timeout seconds (default: 180).",
    )
    parser.add_argument(
        "--kernel",
        default="python3",
        help="Notebook kernel name (default: python3).",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop on first failure.",
    )
    parser.add_argument(
        "--write-executed",
        action="store_true",
        help="Write executed outputs back into notebook files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    curriculum_dir = Path(args.curriculum_dir)
    paths = notebook_paths(curriculum_dir)

    if not paths:
        raise SystemExit(f"No notebooks found under {curriculum_dir}.")

    results: list[dict] = []
    print(f"Executing {len(paths)} notebooks from {curriculum_dir}...")
    for index, path in enumerate(paths, start=1):
        result = execute_notebook(path, args.timeout, args.kernel, args.write_executed)
        results.append(result)
        print(f"[{index}/{len(paths)}] {result['status'].upper()} {path}")
        if result["status"] == "failed" and args.fail_fast:
            break

    passed = sum(1 for item in results if item["status"] == "passed")
    failed = len(results) - passed
    report = {
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
            "kernel": args.kernel,
            "timeout": args.timeout,
        },
        "results": results,
    }

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Notebook validation report written to {report_path}")

    if failed:
        failed_paths = [item["path"] for item in results if item["status"] == "failed"]
        print("Failed notebooks:")
        for path in failed_paths:
            print(f"- {path}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
