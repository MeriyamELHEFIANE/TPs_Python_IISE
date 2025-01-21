import unittest
import conversion

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        # Test avec un montant positif
        self.assertAlmostEqual(conversion.dollars_to_dirhams(100), 975.0)
        # Test avec un montant nul
        self.assertAlmostEqual(conversion.dollars_to_dirhams(0), 0.0)
        # Test avec un montant négatif
        self.assertAlmostEqual(conversion.dollars_to_dirhams(-50), -487.5)

    def test_meters_to_kilometers(self):
        # Test avec une distance positive
        self.assertAlmostEqual(conversion.meters_to_kilometers(1000), 1.0)
        # Test avec une distance nulle
        self.assertAlmostEqual(conversion.meters_to_kilometers(0), 0.0)
        # Test avec une distance négative
        self.assertAlmostEqual(conversion.meters_to_kilometers(-2500), -2.5)

if __name__ == "__main__":
    unittest.main()