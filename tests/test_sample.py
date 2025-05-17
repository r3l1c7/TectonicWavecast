import unittest

from tectonicwavecast.data import load_sample_earthquakes
from tectonicwavecast.chains import detect_chains
from tectonicwavecast.forecast import forecast_high_risk_zones


class TestSampleDataset(unittest.TestCase):
    def setUp(self):
        self.quakes = load_sample_earthquakes()

    def test_chain_detection(self):
        chains = detect_chains(self.quakes, distance_km=500, window_hours=24)
        self.assertEqual(len(chains), 2)
        self.assertEqual(len(chains[0]), 2)
        self.assertEqual(len(chains[1]), 2)

    def test_forecast(self):
        risks = forecast_high_risk_zones(self.quakes, top_n=1)
        self.assertTrue(risks)
        self.assertIsInstance(risks[0][1], float)


if __name__ == "__main__":
    unittest.main()
