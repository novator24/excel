from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import load_formula_config
from .models import CalculationInput, CalculationResult, RiskBreakdown
from .route_math import map_user_segment, route_distance_nm


@dataclass
class FreightCalculator:
    config_path: str

    def __post_init__(self) -> None:
        self.config = load_formula_config(self.config_path)
        self.version = self.config["meta"]["version"]

    def calculate(self, payload: CalculationInput) -> CalculationResult:
        mapped_route = map_user_segment(
            payload.route_points, payload.user_origin_point, payload.user_destination_point
        )
        distance_nm = route_distance_nm(mapped_route)
        avg_speed_knots = float(self.config["routing"]["default_speed_knots"])
        eta_hours = distance_nm / avg_speed_knots if avg_speed_knots > 0 else 0.0

        weather_risk = (
            payload.conditions.weather.storm_index * self.config["risk_weights"]["weather_storm"]
            + payload.conditions.weather.fog_index * self.config["risk_weights"]["weather_fog"]
            + payload.conditions.weather.icing_index * self.config["risk_weights"]["weather_icing"]
            + payload.conditions.weather.wave_index * self.config["risk_weights"]["weather_wave"]
        )
        ice_risk = (
            payload.conditions.ice.ice_index * self.config["risk_weights"]["ice"]
            + payload.conditions.ice.polar_night_index * self.config["risk_weights"]["polar_night"]
        )
        security_risk = (
            payload.conditions.security.piracy_index * self.config["risk_weights"]["piracy"]
            + payload.conditions.security.sanctions_index * self.config["risk_weights"]["sanctions"]
        )
        port_risk = (
            payload.conditions.ports.origin_risk + payload.conditions.ports.destination_risk
        ) / 2 * self.config["risk_weights"]["port"]

        restriction_penalty = sum(
            zone.severity * self.config["cost_coefficients"]["restricted_zone_penalty_usd"]
            for zone in payload.restrictions
        )
        navigation_risk = min(1.0, len(payload.restrictions) * 0.1)

        weighted_risk = min(
            1.0, weather_risk + ice_risk + security_risk + port_risk + navigation_risk * 0.15
        )
        risk_multiplier = 1.0 + weighted_risk * self.config["cost_coefficients"]["risk_multiplier"]

        base_cost = (
            payload.cost_inputs.base_freight_usd
            + payload.cost_inputs.bunker_usd
            + payload.cost_inputs.insurance_usd
            + payload.cost_inputs.port_fees_usd
            + payload.cost_inputs.waiting_usd
            + restriction_penalty
        )

        arctic_multiplier = (
            self.config["cost_coefficients"]["arctic_multiplier"]
            if payload.conditions.ice.ice_index >= self.config["routing"]["arctic_ice_threshold"]
            else 1.0
        )
        total_price = base_cost * risk_multiplier * arctic_multiplier

        spread = self.config["negotiation"]["spread_percent"] / 100.0
        return CalculationResult(
            formula_version=self.version,
            distance_nm=round(distance_nm, 2),
            eta_hours=round(eta_hours, 2),
            risk_score=round(weighted_risk, 4),
            cost_before_risk_usd=round(base_cost, 2),
            total_price_usd=round(total_price, 2),
            negotiation_min_usd=round(total_price * (1 - spread), 2),
            negotiation_max_usd=round(total_price * (1 + spread), 2),
            risk_breakdown=RiskBreakdown(
                weather_risk=round(weather_risk, 4),
                ice_risk=round(ice_risk, 4),
                security_risk=round(security_risk, 4),
                port_risk=round(port_risk, 4),
                navigation_risk=round(navigation_risk, 4),
            ),
            assumptions=[
                "Route remapped by nearest-index direction logic.",
                "Restricted zones add fixed penalty by severity.",
                "Arctic multiplier applied above configured ice threshold.",
            ],
        )


def default_calculator() -> FreightCalculator:
    base = Path(__file__).resolve().parent.parent
    return FreightCalculator(str(base / "config" / "default_formula.yaml"))
