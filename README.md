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

## Additional MVP: `n1_openteam2026`

This repository also contains a standalone hackathon MVP in `n1_openteam2026` based on the first-priority track from `NICK.md` (object detection + tracking + routing simulation).

### Ubuntu deployment steps (`n1_openteam2026`)

1. Install base packages:
   - `sudo apt update`
   - `sudo apt install -y python3 python3-venv python3-pip curl`
2. Create environment:
   - `cd n1_openteam2026`
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
3. Install dependencies:
   - `pip install --upgrade pip`
   - `pip install -r requirements.txt`
4. Run demo:
   - `PYTHONPATH=src python -m n1_openteam2026.run_demo`
5. Run API:
   - `PYTHONPATH=src uvicorn n1_openteam2026.api:app --host 0.0.0.0 --port 8000`
6. Smoke test:
   - `curl http://127.0.0.1:8000/health`
   - `curl -X POST "http://127.0.0.1:8000/simulate" -H "Content-Type: application/json" -d '{"frames":80,"seed":21,"max_track_distance":20.0}'`
