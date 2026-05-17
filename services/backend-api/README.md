# Backend API

FastAPI orchestrator for quote calculation and Excel export.

## Endpoints

- `GET /api/v1/health`
- `POST /api/v1/quotes/calculate`
- `POST /api/v1/quotes/{quote_id}/excel`

## Persistence

- Uses SQLAlchemy with `DATABASE_URL` (PostgreSQL for prod, SQLite for local tests).
- Schema bootstrap runs on startup via metadata creation.
- SQL migration template is stored in `migrations/001_init.sql`.

## Provider adapters

- Primary/fallback provider chain is configured in `app/adapters/provider_registry.py`.
- Optional provider URLs can be passed via env vars:
  - `ROUTE_<PROVIDER>_URL`
  - `WEATHER_<PROVIDER>_URL`
  - `PORTS_<PROVIDER>_URL`
