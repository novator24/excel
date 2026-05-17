from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Alembic migration drift.")
    parser.add_argument(
        "--database-url",
        default=os.getenv("DATABASE_URL", "sqlite:///./fertifreight.db"),
        help="Database URL for schema drift check.",
    )
    parser.add_argument(
        "--skip-upgrade",
        action="store_true",
        help="Skip running `alembic upgrade head` before drift check.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    alembic_ini = repo_root / "services" / "backend-api" / "alembic.ini"
    env = os.environ.copy()
    env["DATABASE_URL"] = args.database_url
    env["DB_AUTO_CREATE"] = "false"

    alembic_cmd = [sys.executable, "-m", "alembic", "-c", str(alembic_ini)]

    if not args.skip_upgrade:
        upgrade_cmd = [*alembic_cmd, "upgrade", "head"]
        upgrade_result = subprocess.run(upgrade_cmd, cwd=repo_root, env=env, check=False)
        if upgrade_result.returncode != 0:
            return upgrade_result.returncode

    check_cmd = [*alembic_cmd, "check"]
    check_result = subprocess.run(check_cmd, cwd=repo_root, env=env, check=False)
    return check_result.returncode


if __name__ == "__main__":
    sys.exit(main())

