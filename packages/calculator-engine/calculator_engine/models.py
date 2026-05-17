from __future__ import annotations

from pydantic import BaseModel, Field


class GeoPoint(BaseModel):
    lat: float
    lon: float


class RestrictionZone(BaseModel):
    zone_id: str
    severity: float = Field(ge=0.0, le=1.0)


class WeatherRisk(BaseModel):
    storm_index: float = Field(ge=0.0, le=1.0)
    fog_index: float = Field(ge=0.0, le=1.0)
    icing_index: float = Field(default=0.0, ge=0.0, le=1.0)
    wave_index: float = Field(default=0.0, ge=0.0, le=1.0)


class IceRisk(BaseModel):
    ice_index: float = Field(ge=0.0, le=1.0)
    polar_night_index: float = Field(default=0.0, ge=0.0, le=1.0)


class SecurityRisk(BaseModel):
    piracy_index: float = Field(ge=0.0, le=1.0)
    sanctions_index: float = Field(default=0.0, ge=0.0, le=1.0)


class PortRisk(BaseModel):
    origin_risk: float = Field(ge=0.0, le=1.0)
    destination_risk: float = Field(ge=0.0, le=1.0)


class ConditionBundle(BaseModel):
    weather: WeatherRisk
    ice: IceRisk
    security: SecurityRisk
    ports: PortRisk


class CostInput(BaseModel):
    base_freight_usd: float = Field(ge=0.0)
    bunker_usd: float = Field(ge=0.0)
    insurance_usd: float = Field(ge=0.0)
    port_fees_usd: float = Field(ge=0.0)
    waiting_usd: float = Field(ge=0.0)


class CalculationInput(BaseModel):
    origin_port_code: str
    destination_port_code: str
    vessel_type: str
    cargo_tons: float = Field(gt=0.0)
    route_points: list[GeoPoint]
    user_origin_point: GeoPoint
    user_destination_point: GeoPoint
    restrictions: list[RestrictionZone] = Field(default_factory=list)
    conditions: ConditionBundle
    cost_inputs: CostInput


class RiskBreakdown(BaseModel):
    weather_risk: float
    ice_risk: float
    security_risk: float
    port_risk: float
    navigation_risk: float


class CalculationResult(BaseModel):
    formula_version: str
    distance_nm: float
    eta_hours: float
    risk_score: float
    cost_before_risk_usd: float
    total_price_usd: float
    negotiation_min_usd: float
    negotiation_max_usd: float
    risk_breakdown: RiskBreakdown
    assumptions: list[str]
