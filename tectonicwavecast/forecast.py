"""Generate simple risk forecasts from stress field."""

from __future__ import annotations

from typing import List, Dict, Tuple

from .stress import compute_stress_field


def forecast_high_risk_zones(quakes: List[Dict], top_n: int = 10) -> List[Tuple[Tuple[float, float], float]]:
    """Return the locations with highest computed stress."""
    stress = compute_stress_field(quakes)
    sorted_stress = sorted(stress.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_stress[:top_n]
