from __future__ import annotations

import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient


@pytest.mark.integration
@pytest.mark.integration_service
def test_api_roundtrip_against_postgres_with_migrations():
    db_url = os.getenv("INTEGRATION_DATABASE_URL")
    if not db_url:
        pytest.skip("INTEGRATION_DATABASE_URL is not configured")

    os.environ["DATABASE_URL"] = db_url
    os.environ["DB_AUTO_CREATE"] = "false"

    backend_api_dir = Path(__file__).resolve().parents[2]
    alembic_ini = backend_api_dir / "alembic.ini"
    config = Config(str(alembic_ini))
    config.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(config, "head")

    from app.main import app

    with TestClient(app) as client:
        payload = {
            "tenant_id": "acme",
            "origin_port_code": "RUVVO",
            "destination_port_code": "TRMER",
            "vessel_type": "handysize",
            "cargo_tons": 25000,
            "route_points": [
                {"lat": 59.93, "lon": 30.31},
                {"lat": 58.0, "lon": 27.0},
                {"lat": 52.0, "lon": 18.0},
                {"lat": 40.9, "lon": 29.1},
            ],
            "user_origin_point": {"lat": 58.0, "lon": 27.0},
            "user_destination_point": {"lat": 40.9, "lon": 29.1},
            "restrictions": [{"zone_id": "BOSPHORUS-RULE", "severity": 0.5}],
            "conditions": {
                "weather": {
                    "storm_index": 0.3,
                    "fog_index": 0.2,
                    "icing_index": 0.1,
                    "wave_index": 0.2,
                },
                "ice": {"ice_index": 0.2, "polar_night_index": 0.1},
                "security": {"piracy_index": 0.2, "sanctions_index": 0.1},
                "ports": {"origin_risk": 0.2, "destination_risk": 0.3},
            },
            "cost_inputs": {
                "base_freight_usd": 850000,
                "bunker_usd": 210000,
                "insurance_usd": 75000,
                "port_fees_usd": 120000,
                "waiting_usd": 30000,
            },
        }
        quote_resp = client.post("/api/v1/quotes/calculate", json=payload)
        assert quote_resp.status_code == 200
        quote_id = quote_resp.json()["quote_id"]

        excel_resp = client.post(f"/api/v1/quotes/{quote_id}/excel")
        assert excel_resp.status_code == 200
        assert excel_resp.json()["file_size"] > 1000

        health_resp = client.get("/api/v1/providers/health")
        assert health_resp.status_code == 200
