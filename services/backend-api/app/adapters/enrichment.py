from __future__ import annotations

import os
from typing import Any

import httpx

from .provider_registry import PROVIDER_REGISTRY


def _env_key(domain: str, provider: str) -> str:
    return f"{domain.upper()}_{provider.upper()}_URL"


class EnrichmentService:
    """Provider adapter facade with primary/fallback lookup."""

    def resolve_provider(self, domain: str, payload: dict[str, Any]) -> dict[str, Any]:
        config = PROVIDER_REGISTRY[domain]
        candidates = [config.primary, *config.fallbacks]

        for provider in candidates:
            endpoint = os.getenv(_env_key(domain, provider))
            if not endpoint:
                continue
            try:
                with httpx.Client(timeout=2.5) as client:
                    response = client.post(endpoint, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    return {"provider": provider, "source": "remote", "data": data}
            except Exception:  # noqa: BLE001
                continue

        return {"provider": candidates[-1], "source": "heuristic", "data": {}}

