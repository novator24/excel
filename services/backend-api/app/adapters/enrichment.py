from __future__ import annotations

from typing import Any

from .domain_clients import PortsClient, RouteClient, WeatherClient
from .provider_health import ProviderHealthRegistry


class EnrichmentService:
    """Provider adapter facade with primary/fallback and health tracking."""

    def __init__(self) -> None:
        self.route_client = RouteClient()
        self.weather_client = WeatherClient()
        self.ports_client = PortsClient()
        self.health = ProviderHealthRegistry()

    def resolve_provider(self, domain: str, payload: dict[str, Any]) -> dict[str, Any]:
        clients = {
            "route": self.route_client,
            "weather": self.weather_client,
            "ports": self.ports_client,
        }
        client = clients[domain]
        response = client.fetch(payload)
        self.health.mark(f"{domain}:{response['provider']}", response["status"])
        normalized = client.normalize(response["data"])
        return {**response, "normalized": normalized}

    def health_snapshot(self) -> dict[str, dict[str, int]]:
        return self.health.snapshot()

