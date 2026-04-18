from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CURRICULUM_JSON = Path("curriculum/roadmap.json")


def load_curriculum() -> dict[str, Any]:
    return json.loads(CURRICULUM_JSON.read_text(encoding="utf-8"))

