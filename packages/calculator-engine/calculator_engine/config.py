from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def load_formula_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    if config_path.suffix.lower() == ".json":
        return json.loads(config_path.read_text(encoding="utf-8"))
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))
