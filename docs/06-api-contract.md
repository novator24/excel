# API Contract (MVP)

## Authentication

- OIDC Bearer JWT.
- Required claim: `role`.

## Endpoints

### `POST /api/v1/quotes/calculate`

Request:

```json
{
  "tenant_id": "acme",
  "origin_port_code": "RUVVO",
  "destination_port_code": "TRMER",
  "vessel_type": "handysize",
  "cargo_tons": 25000,
  "route_points": [{"lat": 59.93, "lon": 30.31}],
  "restrictions": [{"zone_id": "BLACKSEA-01", "severity": 0.7}],
  "conditions": {
    "weather": {"storm_index": 0.3, "fog_index": 0.4},
    "ice": {"ice_index": 0.5},
    "security": {"piracy_index": 0.2},
    "ports": {"origin_risk": 0.2, "destination_risk": 0.4}
  },
  "cost_inputs": {
    "base_freight_usd": 850000,
    "bunker_usd": 210000,
    "insurance_usd": 75000,
    "port_fees_usd": 120000,
    "waiting_usd": 30000
  }
}
```

Response:

```json
{
  "quote_id": "uuid",
  "formula_version": "2026-05-01",
  "distance_nm": 3320.4,
  "eta_hours": 291.3,
  "risk_score": 0.46,
  "total_price_usd": 1472510.44,
  "negotiation_range_usd": {"min": 1400000, "max": 1530000},
  "assumptions": ["No canal delay", "Provider weather horizon 10d"]
}
```

### `POST /api/v1/quotes/{quote_id}/excel`

- Generates workbook in blob and returns secure download URL.

### `GET /api/v1/quotes/{quote_id}`

- Returns stored snapshot and audit references.

### `GET /api/v1/health`

- Liveness + dependency readiness.

### `GET /api/v1/providers/health`

- Returns in-process provider health counters by `domain:provider` key.

## Versioning

- URI major version (`/v1`).
- Formula version in payload.
- Breaking schema changes only on new major.
