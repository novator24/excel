from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProviderConfig:
    primary: str
    fallbacks: list[str]
    cache_ttl_seconds: int


PROVIDER_REGISTRY: dict[str, ProviderConfig] = {
    "ais": ProviderConfig(primary="marinetraffic", fallbacks=["aishub"], cache_ttl_seconds=300),
    "weather": ProviderConfig(
        primary="stormgeo", fallbacks=["openmeteo", "noaa"], cache_ttl_seconds=3600
    ),
    "ports": ProviderConfig(primary="dataloy", fallbacks=["unlocode"], cache_ttl_seconds=86400),
    "route": ProviderConfig(
        primary="searoutes", fallbacks=["custom_graph"], cache_ttl_seconds=21600
    ),
    "sanctions": ProviderConfig(
        primary="ofac_bundle", fallbacks=["eu_sanctions"], cache_ttl_seconds=86400
    ),
    "fuel_fx": ProviderConfig(
        primary="shipandbunker", fallbacks=["ecb_rates"], cache_ttl_seconds=10800
    ),
}
