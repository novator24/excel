# Product Requirements Document (PRD)

## Product vision

Web platform and API for calculating fair freight negotiation prices for fertilizer shipping under real route, weather, ice, security, and port constraints.

## Target users

- Freight analyst
- Chartering operator
- Risk manager
- External client (read-only quote access)
- Platform administrator

## Core user flow

1. User selects a regular vessel route and schedule.
2. User enters custom origin and destination ports.
3. System maps base route to user ports with directed trapezoid corridor logic.
4. System enriches with route/weather/ice/security/port constraints.
5. Calculator produces auditable quote and negotiation range.
6. User downloads a 2-sheet Excel with assumptions, risks, and commentary.

## Functional requirements

- Deterministic calculation with formula config in YAML/JSON.
- Route direction awareness and restricted zone crossing penalties.
- Risk dimensions: weather, ice, piracy/security, port, navigation.
- Cost components:
  - freight base
  - bunker
  - insurance
  - port fees
  - waiting
  - ice surcharge
  - sanctions/restricted waters penalty
  - operational safety reserve
- Versioned quote snapshots with input/output/audit payloads.
- Admin-managed coefficients and data-source activation flags.
- Role-based data and export visibility.

## Non-functional requirements

- Availability: 99.9% API in prod.
- P95 calculate API < 2.5 seconds with warm cache.
- Reproducibility: same input + version -> same output.
- Traceability: all provider responses persisted with version tags.
- Security: OIDC + RBAC + audit logs + secret vault.
- Cloud-native operation in AKS across dev/test/prod.

## Scope split

### MVP
- Route mapping + cost/risk calculator + Excel export + audit persistence.
- Admin controls for coefficients/sources.
- Airflow ingestion and dbt marts for analytics.

### Post-MVP
- Blender/Unreal logistics visualization integration.
- AnyLogic simulation model export.
- Scenario optimization and Monte Carlo pricing bands.
