# Data Providers and Adapter Strategy

## Provider matrix

- AIS / vessel tracking:
  - Commercial: MarineTraffic, FleetMon, Orbcomm.
  - Free fallback: AISHub (limited coverage).
- Route planning:
  - Commercial: Searoutes, Veson APIs.
  - Free fallback: OpenRouteService (not marine-precise), custom graph.
- Weather and ice:
  - Commercial: StormGeo, Spire Weather, DTN.
  - Public fallback: Open-Meteo Marine, NOAA, Copernicus, FMI.
- Marine warnings / notices:
  - Hydrographic offices, IMO feeds, NAVAREA bulletins.
- Port data:
  - Commercial: Dataloy, Lloyd's datasets.
  - Public fallback: UN/LOCODE + port authority open data.
- Restricted and sanctions waters:
  - UKHO notices, OFAC/EU sanctions lists, insurer advisories.
- Geospatial maps/geocoding:
  - Azure Maps, Mapbox.
  - Fallback: OpenStreetMap + Nominatim (license constraints).
- Fuel and FX:
  - Fuel: Ship&Bunker (commercial), exchange platform feeds.
  - FX: ECB/OpenExchangeRates.

## Production suitability rules

- Every source must pass:
  - contractual license review
  - uptime/SLA check
  - explicit redistribution rights
  - retention and caching compliance

## Adapter architecture

- `acquisition`: provider-specific client and retry policy.
- `normalization`: map provider schema -> internal canonical contract.
- `quality`: schema, ranges, and freshness checks.
- `cache`: keyed by route/time window/provider version.
- `fallback`: provider priority chain with confidence score.

## Caching and normalization

- TTL by domain:
  - weather: 1-3h
  - AIS live: minutes
  - sanctions/port restrictions: 24h
- Always store:
  - raw payload
  - normalized payload
  - source metadata/version
