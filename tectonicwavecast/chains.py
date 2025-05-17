"""Directional chain detection for earthquakes."""

from __future__ import annotations

from typing import List, Dict

import math


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute haversine distance between two points in kilometers."""
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def detect_chains(
    quakes: List[Dict],
    *,
    distance_km: float = 400.0,
    window_hours: float = 24.0,
) -> List[List[Dict]]:
    """Detect directional quake chains via simple spatial-temporal clustering."""
    quakes_sorted = sorted(quakes, key=lambda q: q["time"])
    chains: List[List[Dict]] = []

    for quake in quakes_sorted:
        placed = False
        for chain in chains:
            last = chain[-1]
            dt = (quake["time"] - last["time"]).total_seconds() / 3600.0
            dist = haversine_km(
                quake["latitude"], quake["longitude"], last["latitude"], last["longitude"]
            )
            if 0 < dt <= window_hours and dist <= distance_km:
                chain.append(quake)
                placed = True
                break
        if not placed:
            chains.append([quake])
    return [c for c in chains if len(c) > 1]
