"""TectonicWavecast core package."""

__all__ = [
    "fetch_recent_earthquakes",
    "load_sample_earthquakes",
    "detect_chains",
]

from .data import fetch_recent_earthquakes, load_sample_earthquakes
from .chains import detect_chains
