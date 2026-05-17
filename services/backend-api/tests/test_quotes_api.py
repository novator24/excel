import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_calculate_and_excel(client):
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
    calc_resp = client.post("/api/v1/quotes/calculate", json=payload)
    assert calc_resp.status_code == 200
    quote_id = calc_resp.json()["quote_id"]
    excel_resp = client.post(f"/api/v1/quotes/{quote_id}/excel")
    assert excel_resp.status_code == 200
    assert excel_resp.json()["file_size"] > 1000
    assert excel_resp.json()["checksum_sha256"]
