"""Command line interface for TectonicWavecast."""

from __future__ import annotations

import argparse
import json
from typing import Any

from .data import fetch_recent_earthquakes, load_sample_earthquakes
from .chains import detect_chains
from .forecast import forecast_high_risk_zones


def main(argv: Any | None = None) -> None:
    parser = argparse.ArgumentParser(description="TectonicWavecast CLI")
    parser.add_argument(
        "--chains",
        action="store_true",
        help="Detect directional quake chains",
    )
    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Print high risk zones based on simple stress model",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Use bundled sample data instead of live USGS feed",
    )
    args = parser.parse_args(argv)

    if args.sample:
        quakes = load_sample_earthquakes()
    else:
        quakes = fetch_recent_earthquakes()
    if args.chains:
        chains = detect_chains(quakes)
        print(json.dumps(chains, default=str, indent=2))
    if args.forecast:
        risks = forecast_high_risk_zones(quakes)
        print(json.dumps(risks, default=str, indent=2))
    if not args.chains and not args.forecast:
        print(json.dumps(quakes, default=str, indent=2))


if __name__ == "__main__":
    main()
