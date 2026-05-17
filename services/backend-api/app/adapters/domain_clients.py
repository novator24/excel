from __future__ import annotations

import os
from typing import Any

import httpx

from .provider_registry import PROVIDER_REGISTRY


def _env_key(domain: str, provider: str) -> str:
    return f"{domain.upper()}_{provider.upper()}_URL"


class DomainProviderClient:
    def __init__(self, domain: str, timeout_sec: float = 2.5) -> None:
        self.domain = domain
        self.timeout_sec = timeout_sec

    def fetch(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = PROVIDER_REGISTRY[self.domain]
        candidates = [config.primary, *config.fallbacks]

        for provider in candidates:
            endpoint = os.getenv(_env_key(self.domain, provider))
            if not endpoint:
                continue
            try:
                with httpx.Client(timeout=self.timeout_sec) as client:
                    response = client.post(endpoint, json=payload)
                if response.status_code == 200:
                    return {
                        "provider": provider,
                        "source": "remote",
                        "status": "ok",
                        "data": response.json(),
                    }
            except Exception:  # noqa: BLE001
                continue

        return {
            "provider": candidates[-1],
            "source": "heuristic",
            "status": "degraded",
            "data": {},
        }


class RouteClient(DomainProviderClient):
    def __init__(self) -> None:
        super().__init__(domain="route")

    def normalize(self, raw: dict[str, Any]) -> dict[str, Any]:
        return {
            "route_segments": raw.get("segments", []),
            "distance_nm": raw.get("distance_nm"),
            "canal_flags": raw.get("canal_flags", []),
        }


class WeatherClient(DomainProviderClient):
    def __init__(self) -> None:
        super().__init__(domain="weather")

    def normalize(self, raw: dict[str, Any]) -> dict[str, Any]:
        return {
            "storm_index": raw.get("storm_index"),
            "fog_index": raw.get("fog_index"),
            "ice_index": raw.get("ice_index"),
            "wave_index": raw.get("wave_index"),
        }


class PortsClient(DomainProviderClient):
    def __init__(self) -> None:
        super().__init__(domain="ports")

    def normalize(self, raw: dict[str, Any]) -> dict[str, Any]:
        return {
            "origin_constraints": raw.get("origin_constraints", []),
            "destination_constraints": raw.get("destination_constraints", []),
            "restricted_zones": raw.get("restricted_zones", []),
        }

