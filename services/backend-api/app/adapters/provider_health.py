from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class ProviderHealth:
    success: int = 0
    degraded: int = 0


class ProviderHealthRegistry:
    def __init__(self) -> None:
        self._store: dict[str, ProviderHealth] = defaultdict(ProviderHealth)

    def mark(self, key: str, status: str) -> None:
        if status == "ok":
            self._store[key].success += 1
        else:
            self._store[key].degraded += 1

    def snapshot(self) -> dict[str, dict[str, int]]:
        return {
            key: {"success": value.success, "degraded": value.degraded}
            for key, value in self._store.items()
        }

