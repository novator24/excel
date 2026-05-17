from __future__ import annotations

import sys
from pathlib import Path

from fastapi import APIRouter, HTTPException

CURRENT_DIR = Path(__file__).resolve()
ROOT = CURRENT_DIR.parents[4]
sys.path.append(str(ROOT / "packages" / "calculator-engine"))
sys.path.append(str(ROOT / "packages" / "excel-generator"))

from calculator_engine.engine import default_calculator  # noqa: E402
from calculator_engine.models import (  # noqa: E402
    CalculationInput,
    ConditionBundle,
    CostInput,
    GeoPoint,
    IceRisk,
    PortRisk,
    RestrictionZone,
    SecurityRisk,
    WeatherRisk,
)
from excel_generator.writer import build_workbook  # noqa: E402

from ..adapters.enrichment import EnrichmentService  # noqa: E402
from ..db import session_scope  # noqa: E402
from ..models import QuoteCalculateRequest  # noqa: E402
from ..repositories.quote_repository import QuoteRepository  # noqa: E402

router = APIRouter()
_calculator = default_calculator()
_enrichment = EnrichmentService()


def _risk_classifier(result: dict) -> list[dict]:
    breakdown = result["risk_breakdown"]
    return [
        {
            "category": "Weather",
            "factor": "Storm/Fog/Icing/Waves",
            "stars": min(5, max(1, round(breakdown["weather_risk"] * 5))),
            "severity": round(breakdown["weather_risk"], 3),
            "weight": 0.22,
            "impact_usd": round(result["total_price_usd"] * breakdown["weather_risk"] * 0.1, 2),
            "comment": "Weather volatility based on forecast horizon and sea state.",
        },
        {
            "category": "Ice",
            "factor": "Arctic and seasonal ice",
            "stars": min(5, max(1, round(breakdown["ice_risk"] * 5))),
            "severity": round(breakdown["ice_risk"], 3),
            "weight": 0.20,
            "impact_usd": round(result["total_price_usd"] * breakdown["ice_risk"] * 0.1, 2),
            "comment": "Includes ice season and polar night effects.",
        },
        {
            "category": "Security",
            "factor": "Piracy/Sanctions",
            "stars": min(5, max(1, round(breakdown["security_risk"] * 5))),
            "severity": round(breakdown["security_risk"], 3),
            "weight": 0.17,
            "impact_usd": round(result["total_price_usd"] * breakdown["security_risk"] * 0.1, 2),
            "comment": "Security advisories and restricted zone implications.",
        },
    ]


@router.post("/quotes/calculate")
def calculate_quote(payload: QuoteCalculateRequest) -> dict:
    try:
        payload_dict = payload.model_dump()
        route_enrichment = _enrichment.resolve_provider("route", payload_dict)
        weather_enrichment = _enrichment.resolve_provider("weather", payload_dict)
        ports_enrichment = _enrichment.resolve_provider("ports", payload_dict)
        enrichment_bundle = {
            "route": route_enrichment,
            "weather": weather_enrichment,
            "ports": ports_enrichment,
            "health": _enrichment.health_snapshot(),
        }

        calc_input = CalculationInput(
            origin_port_code=payload.origin_port_code,
            destination_port_code=payload.destination_port_code,
            vessel_type=payload.vessel_type,
            cargo_tons=payload.cargo_tons,
            route_points=[GeoPoint(lat=p.lat, lon=p.lon) for p in payload.route_points],
            user_origin_point=GeoPoint(
                lat=payload.user_origin_point.lat, lon=payload.user_origin_point.lon
            ),
            user_destination_point=GeoPoint(
                lat=payload.user_destination_point.lat, lon=payload.user_destination_point.lon
            ),
            restrictions=[
                RestrictionZone(zone_id=i.zone_id, severity=i.severity)
                for i in payload.restrictions
            ],
            conditions=ConditionBundle(
                weather=WeatherRisk(**payload.conditions.weather.model_dump()),
                ice=IceRisk(**payload.conditions.ice.model_dump()),
                security=SecurityRisk(**payload.conditions.security.model_dump()),
                ports=PortRisk(**payload.conditions.ports.model_dump()),
            ),
            cost_inputs=CostInput(**payload.cost_inputs.model_dump()),
        )
        result = _calculator.calculate(calc_input).model_dump()
        risk_classifier = _risk_classifier(result)
        with session_scope() as session:
            repository = QuoteRepository(session)
            stored = repository.save_quote(payload_dict, result, risk_classifier, enrichment_bundle)
        return stored
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/quotes/{quote_id}/excel")
def create_excel(quote_id: str) -> dict:
    with session_scope() as session:
        repository = QuoteRepository(session)
        quote = repository.get_quote(quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    excel_bytes = build_workbook(quote)
    with session_scope() as session:
        repository = QuoteRepository(session)
        doc_info = repository.save_excel_document(quote_id, excel_bytes)
    return {
        "quote_id": quote_id,
        "file_size": len(excel_bytes),
        "blob_path": doc_info["blob_path"],
        "checksum_sha256": doc_info["checksum"],
        "content_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    }


@router.get("/providers/health")
def provider_health() -> dict[str, dict[str, int]]:
    return _enrichment.health_snapshot()
