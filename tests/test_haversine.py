import unittest
from tectonicwavecast.chains import haversine_km


class TestHaversine(unittest.TestCase):
    def test_haversine_zero(self):
        self.assertEqual(haversine_km(0, 0, 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
