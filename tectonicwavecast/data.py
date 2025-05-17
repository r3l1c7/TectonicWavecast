"""Data ingestion utilities for TectonicWavecast."""

from __future__ import annotations

import datetime as _dt
from typing import List, Dict

from pathlib import Path

import json
from urllib.request import urlopen

USGS_FEED_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
)

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
    """Load bundled sample earthquake data."""
    with open(SAMPLE_DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    quakes = []
    for feat in data.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        coords = geom.get("coordinates", [None, None, None])
        quakes.append(
            {
                "time": _dt.datetime.fromtimestamp(
                    props.get("time", 0) / 1000,
                    tz=_dt.timezone.utc,
                ),
                "place": props.get("place"),
                "magnitude": props.get("mag"),
                "longitude": coords[0],
                "latitude": coords[1],
                "depth": coords[2],
            }
        )
    return quakes
