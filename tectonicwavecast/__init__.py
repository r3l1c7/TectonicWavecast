"""TectonicWavecast core package."""

__all__ = [
    "fetch_recent_earthquakes",
    "load_sample_earthquakes",
    "detect_chains",
    "forecast_high_risk_zones",
]

from .data import fetch_recent_earthquakes, load_sample_earthquakes
from .chains import detect_chains
from .forecast import forecast_high_risk_zones
