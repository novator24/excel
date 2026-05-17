from __future__ import annotations

from math import asin, cos, radians, sin, sqrt

from .models import GeoPoint

EARTH_RADIUS_KM = 6371.0
KM_TO_NM = 0.539957


def haversine_nm(a: GeoPoint, b: GeoPoint) -> float:
    lat1, lon1 = radians(a.lat), radians(a.lon)
    lat2, lon2 = radians(b.lat), radians(b.lon)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    km = 2 * EARTH_RADIUS_KM * asin(sqrt(h))
    return km * KM_TO_NM


def route_distance_nm(points: list[GeoPoint]) -> float:
    if len(points) < 2:
        return 0.0
    return sum(haversine_nm(points[i], points[i + 1]) for i in range(len(points) - 1))


def nearest_point_index(target: GeoPoint, points: list[GeoPoint]) -> int:
    distances = [haversine_nm(target, p) for p in points]
    return min(range(len(distances)), key=distances.__getitem__)


def map_user_segment(
    points: list[GeoPoint], origin: GeoPoint, destination: GeoPoint
) -> list[GeoPoint]:
    if len(points) < 2:
        return points
    idx_a = nearest_point_index(origin, points)
    idx_b = nearest_point_index(destination, points)
    if idx_a <= idx_b:
        return points[idx_a : idx_b + 1]
    reversed_points = list(reversed(points))
    rev_a = len(points) - idx_a - 1
    rev_b = len(points) - idx_b - 1
    return reversed_points[rev_a : rev_b + 1]
