from __future__ import annotations

from pydantic import BaseModel, Field


class GeoPointDto(BaseModel):
    lat: float
    lon: float


class RestrictionDto(BaseModel):
    zone_id: str
    severity: float = Field(ge=0.0, le=1.0)


class WeatherDto(BaseModel):
    storm_index: float = Field(ge=0.0, le=1.0)
    fog_index: float = Field(ge=0.0, le=1.0)
    icing_index: float = Field(default=0.0, ge=0.0, le=1.0)
    wave_index: float = Field(default=0.0, ge=0.0, le=1.0)


class IceDto(BaseModel):
    ice_index: float = Field(ge=0.0, le=1.0)
    polar_night_index: float = Field(default=0.0, ge=0.0, le=1.0)


class SecurityDto(BaseModel):
    piracy_index: float = Field(ge=0.0, le=1.0)
    sanctions_index: float = Field(default=0.0, ge=0.0, le=1.0)


class PortDto(BaseModel):
    origin_risk: float = Field(ge=0.0, le=1.0)
    destination_risk: float = Field(ge=0.0, le=1.0)


class ConditionsDto(BaseModel):
    weather: WeatherDto
    ice: IceDto
    security: SecurityDto
    ports: PortDto


class CostInputsDto(BaseModel):
    base_freight_usd: float = Field(ge=0.0)
    bunker_usd: float = Field(ge=0.0)
    insurance_usd: float = Field(ge=0.0)
    port_fees_usd: float = Field(ge=0.0)
    waiting_usd: float = Field(ge=0.0)


class QuoteCalculateRequest(BaseModel):
    tenant_id: str
    origin_port_code: str
    destination_port_code: str
    vessel_type: str
    cargo_tons: float = Field(gt=0.0)
    route_points: list[GeoPointDto]
    user_origin_point: GeoPointDto
    user_destination_point: GeoPointDto
    restrictions: list[RestrictionDto] = Field(default_factory=list)
    conditions: ConditionsDto
    cost_inputs: CostInputsDto
