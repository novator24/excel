# Database Schema

## PostgreSQL (OLTP)

```sql
CREATE TABLE quote_request (
  id UUID PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  created_by TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  origin_port_code TEXT NOT NULL,
  destination_port_code TEXT NOT NULL,
  vessel_type TEXT NOT NULL,
  schedule_id TEXT,
  input_payload JSONB NOT NULL,
  formula_version TEXT NOT NULL
);

CREATE TABLE quote_result (
  id UUID PRIMARY KEY,
  request_id UUID NOT NULL REFERENCES quote_request(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  currency TEXT NOT NULL,
  total_price NUMERIC(14,2) NOT NULL,
  negotiate_min NUMERIC(14,2) NOT NULL,
  negotiate_max NUMERIC(14,2) NOT NULL,
  result_payload JSONB NOT NULL
);

CREATE TABLE quote_audit_event (
  id UUID PRIMARY KEY,
  request_id UUID NOT NULL REFERENCES quote_request(id),
  event_time TIMESTAMPTZ NOT NULL DEFAULT now(),
  actor_type TEXT NOT NULL,
  actor_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  event_payload JSONB NOT NULL
);

CREATE TABLE excel_document (
  id UUID PRIMARY KEY,
  request_id UUID NOT NULL REFERENCES quote_request(id),
  blob_path TEXT NOT NULL,
  checksum_sha256 TEXT NOT NULL,
  access_scope TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE formula_config_version (
  version TEXT PRIMARY KEY,
  source_type TEXT NOT NULL,
  checksum_sha256 TEXT NOT NULL,
  config_payload JSONB NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT FALSE,
  activated_at TIMESTAMPTZ
);
```

## ClickHouse (analytics)

- `fact_quote_daily`
- `fact_risk_component`
- `dim_port`
- `dim_route`
- `dim_weather_condition`
- `dim_provider`

## Audit retention

- OLTP audit: 2 years online.
- Raw provider payload in object storage: 5 years with lifecycle tiers.
- PII minimization: external client data separated by tenant partition key.
