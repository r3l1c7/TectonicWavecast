"""Simple Flask dashboard for viewing quake chains and forecasts."""

from __future__ import annotations

from flask import Flask, jsonify, render_template_string

from .data import load_sample_earthquakes
from .chains import detect_chains
from .forecast import forecast_high_risk_zones

app = Flask(__name__)

HTML = """
<!doctype html>
<title>TectonicWavecast Dashboard</title>
<h1>TectonicWavecast Dashboard</h1>
<button onclick="loadData()">Load Sample Data</button>
<pre id="output"></pre>
<script>
function loadData() {
  fetch('/data').then(r => r.json()).then(d => {
    document.getElementById('output').textContent = JSON.stringify(d, null, 2);
  });
}
</script>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/data")
def data():
    quakes = load_sample_earthquakes()
    chains = detect_chains(quakes)
    risks = forecast_high_risk_zones(quakes)
    return jsonify({"chains": chains, "forecast": risks})


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
