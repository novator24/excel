# FertiFreight Platform Monorepo

Production-oriented platform for fertilizer vessel freight estimation, route risk analysis, and auditable Excel export.

## Monorepo choice

This repository uses a monorepo to optimize a small team (1 engineer-analyst):

- Shared domain contracts between API, calculator, and Excel exporter.
- Single CI/CD path and versioning strategy.
- Faster local development and lower operational overhead than many repos.
- Clear boundaries through directory-level ownership.

## Repository layout

- `apps/frontend` - Next.js web UI.
- `services/backend-api` - FastAPI gateway/orchestrator.
- `packages/calculator-engine` - deterministic freight calculator.
- `packages/excel-generator` - Excel workbook renderer.
- `services/route-service` - route normalization and mapping.
- `services/weather-service` - weather/ice enrichment.
- `services/maritime-data-service` - AIS/port/restriction enrichment.
- `services/auth-service` - OIDC integration and RBAC policy evaluation.
- `apps/admin-console` - source and coefficient management UI.
- `data-pipeline` - Airflow + dbt + data contracts.
- `infra` - Terraform, Helm, Argo CD, platform operations.
- `docs` - architecture, contracts, operations, backlog.

## Quick start (local)

1. Create and activate Python 3.12 virtual environment.
2. Install dependencies:
   - `pip install -r services/backend-api/requirements.txt`
   - `pip install -r packages/calculator-engine/requirements.txt`
   - `pip install -r packages/excel-generator/requirements.txt`
3. Run API:
   - `uvicorn app.main:app --reload --app-dir services/backend-api`
4. Run tests:
   - `pytest services/backend-api/tests packages/calculator-engine/tests packages/excel-generator/tests`

## Design principles

- Deterministic calculations with versioned formula config (`YAML`).
- Full audit trail for inputs, coefficients, provider responses, and outputs.
- Strict separation: acquisition -> normalization -> calculation -> presentation -> export.
- Cloud-native deployment for AKS with GitOps.
