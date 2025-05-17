"""Simplified stress redistribution modeling."""

from __future__ import annotations

import math
from typing import List, Dict, Tuple

from .chains import haversine_km


def compute_stress_field(quakes: List[Dict], radius_km: float = 500.0) -> Dict[Tuple[float, float], float]:
    """Compute a toy stress value around quake epicenters."""
    stress: Dict[Tuple[float, float], float] = {}
    for q in quakes:
        mag = q.get("magnitude") or 0
        for other in quakes:
            dist = haversine_km(q["latitude"], q["longitude"], other["latitude"], other["longitude"])
            if dist <= radius_km:
                key = (other["latitude"], other["longitude"])
                stress[key] = stress.get(key, 0.0) + math.pow(10, mag) / ((dist + 1) ** 2)
    return stress
