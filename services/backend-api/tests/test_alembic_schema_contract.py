from __future__ import annotations

from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory
from app.schema_version import EXPECTED_ALEMBIC_HEAD


def test_alembic_head_matches_expected_contract() -> None:
    backend_api_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_api_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_api_dir / "alembic"))
    script = ScriptDirectory.from_config(config)
    assert script.get_current_head() == EXPECTED_ALEMBIC_HEAD

