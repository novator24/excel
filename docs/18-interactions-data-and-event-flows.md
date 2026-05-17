# Service Descriptions, Interactions, and Flows

## Service descriptions

- `backend-api`: validates request, enforces policy, orchestrates quote lifecycle.
- `route-service`: retrieves baseline route and maps to user route directionally.
- `weather-service`: computes weather/ice features by route segment and ETA window.
- `maritime-data-service`: provides AIS status, port constraints, restricted areas, sanctions overlays.
- `calculator-engine`: deterministic modular formula execution.
- `excel-generator`: workbook export with summary and classifier sheets.
- `auth-service`: OIDC token validation + role decision.
- `admin-console`: controls formula versions, provider flags, field exposure.
- `airflow/dbt`: ingestion and transformations for historical analytics.

## Interaction scheme

1. Frontend calls `POST /quotes/calculate`.
2. Backend checks role and tenant scope.
3. Backend requests route/weather/maritime context.
4. Calculator computes result using active formula version.
5. Backend stores quote snapshot and audit event.
6. User requests Excel export, backend builds workbook and stores in object storage.

## Data flow

- Operational:
  - Input payload -> normalized domain model -> calculation result -> quote storage.
- Analytical:
  - Raw provider payloads -> normalized staging -> dbt marts -> ClickHouse analytics.
- Export:
  - Quote snapshot -> Excel bytes -> object storage -> signed URL.

## Event flow

- `quote.calculated`
- `quote.export.requested`
- `quote.export.generated`
- `provider.ingestion.failed`
- `formula.version.activated`
- `policy.override.applied`

Every event includes:

- event id, timestamp, tenant id
- actor id + role
- source service
- payload hash and schema version
