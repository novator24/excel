from excel_generator.writer import build_workbook


def test_build_workbook_returns_bytes():
    payload = {
        "quote_id": "q-1",
        "formula_version": "2026-05-17",
        "origin_port_code": "RUVVO",
        "destination_port_code": "TRMER",
        "distance_nm": 1200.0,
        "eta_hours": 102.4,
        "total_price_usd": 1500000.0,
        "negotiation_min_usd": 1450000.0,
        "negotiation_max_usd": 1550000.0,
        "assumptions": ["Example assumption"],
        "risk_classifier": [
            {
                "category": "Weather",
                "factor": "Storm",
                "stars": 4,
                "severity": 0.7,
                "weight": 0.22,
                "impact_usd": 42000,
                "comment": "North wind window expected.",
            }
        ],
    }
    data = build_workbook(payload)
    assert isinstance(data, bytes)
    assert len(data) > 1000
