from __future__ import annotations

import os


class Settings:
    def __init__(self) -> None:
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./fertifreight.db")
        self.db_auto_create = os.getenv("DB_AUTO_CREATE", "true").lower() == "true"


settings = Settings()

