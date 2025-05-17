import unittest
from tectonicwavecast.data import load_sample_earthquakes
from tectonicwavecast.chains import detect_chains
from tectonicwavecast.forecast import forecast_high_risk_zones


class TestSampleDataset(unittest.TestCase):
    def setUp(self):
        self.quakes = load_sample_earthquakes()

    def test_chain_detection(self):
        chains = detect_chains(self.quakes, distance_km=60.0, window_hours=2.0)
        self.assertEqual(len(chains), 1)
        self.assertEqual(len(chains[0]), 3)

    def test_forecast_top_location(self):
        risks = forecast_high_risk_zones(self.quakes, top_n=1)
        self.assertEqual(len(risks), 1)
        (lat, lon), value = risks[0]
        self.assertIsInstance(value, float)


if __name__ == "__main__":
    unittest.main()
