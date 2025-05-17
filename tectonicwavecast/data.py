"""Data ingestion utilities for TectonicWavecast."""

from __future__ import annotations

import datetime as _dt
from typing import List, Dict

import json
from urllib.request import urlopen
from pathlib import Path

USGS_FEED_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
)

# Path to bundled sample dataset relative to this file
SAMPLE_DATA_FILE = Path(__file__).with_name("data") / "sample_earthquakes.json"


def fetch_recent_earthquakes(url: str = USGS_FEED_URL) -> List[Dict]:
    """Fetch the last 24h of earthquakes from the USGS feed.

    Parameters
    ----------
    url:
        Feed URL to fetch.

    Returns
    -------
    List of dictionaries with earthquake information.
    """
    with urlopen(url, timeout=10) as resp:
        data = json.load(resp)

    quakes = []
    for feat in data.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        coords = geom.get("coordinates", [None, None, None])
        quake = {
            "time": _dt.datetime.fromtimestamp(props.get("time", 0) / 1000, tz=_dt.timezone.utc),
            "place": props.get("place"),
            "magnitude": props.get("mag"),
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2],
        }
        quakes.append(quake)
    return quakes


def load_sample_earthquakes() -> List[Dict]:
    """Load bundled sample earthquake dataset."""
    with open(SAMPLE_DATA_FILE) as f:
        raw = json.load(f)

    quakes: List[Dict] = []
    for entry in raw:
        quakes.append(
            {
                "time": _dt.datetime.fromisoformat(entry["time"]),
                "place": entry.get("place"),
                "magnitude": entry.get("magnitude"),
                "longitude": entry.get("longitude"),
                "latitude": entry.get("latitude"),
                "depth": entry.get("depth"),
            }
        )
    return quakes
