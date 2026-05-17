from __future__ import annotations

import pytest
from app.entities import Base
from app.repositories.quote_repository import QuoteRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

try:
    from testcontainers.postgres import PostgresContainer
except Exception:  # noqa: BLE001
    PostgresContainer = None  # type: ignore[assignment]


@pytest.mark.integration
def test_quote_repository_persists_roundtrip():
    if PostgresContainer is None:
        pytest.skip("testcontainers is not installed")

    with PostgresContainer("postgres:16-alpine") as postgres:
        engine = create_engine(postgres.get_connection_url(), future=True)
        Base.metadata.create_all(bind=engine)

        with Session(engine) as session:
            repo = QuoteRepository(session)
            payload = {
                "tenant_id": "acme",
                "origin_port_code": "RUVVO",
                "destination_port_code": "TRMER",
                "vessel_type": "handysize",
            }
            result = {
                "formula_version": "2026-05-17",
                "distance_nm": 1000.0,
                "eta_hours": 80.0,
                "risk_score": 0.2,
                "cost_before_risk_usd": 1000000.0,
                "total_price_usd": 1120000.0,
                "negotiation_min_usd": 1080000.0,
                "negotiation_max_usd": 1160000.0,
                "risk_breakdown": {
                    "weather_risk": 0.1,
                    "ice_risk": 0.05,
                    "security_risk": 0.03,
                    "port_risk": 0.02,
                    "navigation_risk": 0.02,
                },
                "assumptions": ["integration test"],
            }
            stored = repo.save_quote(payload, result, [], {"route": {}, "weather": {}, "ports": {}})
            session.commit()
            fetched = repo.get_quote(stored["quote_id"])

        assert fetched is not None
        assert fetched["total_price_usd"] == 1120000.0

