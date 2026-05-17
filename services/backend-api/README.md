# Backend API

FastAPI orchestrator for quote calculation and Excel export.

## Endpoints

- `GET /api/v1/health`
- `POST /api/v1/quotes/calculate`
- `POST /api/v1/quotes/{quote_id}/excel`

## Persistence

- Uses SQLAlchemy with `DATABASE_URL` (PostgreSQL for prod, SQLite for local tests).
- Schema bootstrap can run automatically via `DB_AUTO_CREATE=true` (default local).
- Alembic migration chain is in `alembic/versions`.
- SQL migration template is stored in `migrations/001_init.sql`.
- Recommended production mode:
  - `DB_AUTO_CREATE=false`
  - run `alembic upgrade head` in deployment job.

## Provider adapters

- Primary/fallback provider chain is configured in `app/adapters/provider_registry.py`.
- Domain-specific clients and normalizers:
  - `app/adapters/domain_clients.py`
  - `app/adapters/enrichment.py`
- Provider health counters are exposed in `GET /api/v1/providers/health`.
- Optional provider URLs can be passed via env vars:
  - `ROUTE_<PROVIDER>_URL`
  - `WEATHER_<PROVIDER>_URL`
  - `PORTS_<PROVIDER>_URL`

## Integration tests

- Install extras: `pip install -r services/backend-api/requirements-dev.txt`
- Service-DB integration tests (existing Postgres):
  - `pytest -o addopts= -m integration_service services/backend-api/tests/integration`
- Testcontainers integration tests:
  - `pytest -o addopts= -m integration_container services/backend-api/tests/integration`
- Migration-backed API integration test against existing Postgres:
  - set `INTEGRATION_DATABASE_URL`
  - `pytest -o addopts= -m integration_service services/backend-api/tests/integration/test_api_postgres_migrated.py`

## Schema contract test

- `tests/test_alembic_schema_contract.py` validates Alembic `head` equals expected application schema contract.
