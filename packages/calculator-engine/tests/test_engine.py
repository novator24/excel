from calculator_engine.engine import default_calculator
from calculator_engine.models import (
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


def test_calculate_returns_positive_total():
    calculator = default_calculator()
    payload = CalculationInput(
        origin_port_code="RUVVO",
        destination_port_code="TRMER",
        vessel_type="handysize",
        cargo_tons=25000,
        route_points=[
            GeoPoint(lat=59.93, lon=30.31),
            GeoPoint(lat=58.0, lon=27.0),
            GeoPoint(lat=52.0, lon=18.0),
            GeoPoint(lat=40.9, lon=29.1),
        ],
        user_origin_point=GeoPoint(lat=58.0, lon=27.0),
        user_destination_point=GeoPoint(lat=40.9, lon=29.1),
        restrictions=[RestrictionZone(zone_id="BOSPHORUS-RULE", severity=0.5)],
        conditions=ConditionBundle(
            weather=WeatherRisk(storm_index=0.3, fog_index=0.2, icing_index=0.1, wave_index=0.2),
            ice=IceRisk(ice_index=0.2, polar_night_index=0.1),
            security=SecurityRisk(piracy_index=0.2, sanctions_index=0.1),
            ports=PortRisk(origin_risk=0.2, destination_risk=0.3),
        ),
        cost_inputs=CostInput(
            base_freight_usd=850000,
            bunker_usd=210000,
            insurance_usd=75000,
            port_fees_usd=120000,
            waiting_usd=30000,
        ),
    )
    result = calculator.calculate(payload)
    assert result.total_price_usd > result.cost_before_risk_usd
    assert result.negotiation_min_usd < result.total_price_usd < result.negotiation_max_usd
