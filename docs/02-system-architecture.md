# System Architecture (Azure Cloud-Native)

## Architectural style

- Domain-driven modular monorepo.
- Microservice-ready modules with shared contracts.
- Event-driven ingestion + synchronous quote API.
- GitOps-managed AKS deployment.

## Key services

- `backend-api`: orchestration facade for UI and external clients.
- `calculator-engine`: deterministic formula execution and risk aggregation.
- `excel-generator`: export workbook rendering from quote snapshot.
- `route-service`: baseline route retrieval + trapezoid remapping.
- `weather-service`: weather/ice enrichment and risk features.
- `maritime-data-service`: AIS, port, sanctions/restricted waters enrichment.
- `auth-service`: OIDC token introspection and RBAC/ABAC policy checks.
- `admin-console`: management UI for coefficients, providers, field controls.
- `data-pipeline`: Airflow ingestion and dbt transformation to ClickHouse marts.

## Data stores

- PostgreSQL: OLTP, transactional quote/audit metadata.
- ClickHouse: analytical warehouse, historical trends, risk analytics.
- Object storage (Azure Blob): raw provider payloads, Excel files, model artifacts.
- Redis (optional in MVP): API response cache and idempotency keys.

## Security and governance

- Azure Entra ID / OIDC for identity.
- API gateway + JWT validation + service RBAC.
- Key Vault CSI driver for runtime secrets.
- Immutable audit events and signed quote versions.
- Tenant and role scoped access for Excel documents.

## Reliability and operations

- AKS in multi-AZ.
- HPA on CPU and request latency.
- Prometheus + Grafana + Loki + Tempo + OTEL.
- Velero + Postgres backups + ClickHouse replication.
- RTO target: 4h, RPO target: 15m for critical datasets.

## Multi-environment strategy

- `dev`: rapid iteration, synthetic data.
- `test`: integrated external sandbox providers.
- `prod`: controlled releases, strict policy gates.

All environments are isolated by namespace, separate secrets, and environment overlays for Helm + Argo CD.
