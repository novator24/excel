from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT / "packages" / "calculator-engine"))
sys.path.append(str(ROOT / "packages" / "excel-generator"))
sys.path.append(str(ROOT / "services" / "backend-api"))

TEST_DB_FILE = ROOT / "test_backend.db"
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_backend.db")


def pytest_sessionstart() -> None:
    if TEST_DB_FILE.exists():
        TEST_DB_FILE.unlink()
