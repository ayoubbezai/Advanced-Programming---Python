import unittest
from tp3.tp3_functions_classes import multiplier 

class TestClosureMultiplier(unittest.TestCase):
    
    def test_multiplier_double(self):
        double = multiplier(2)  # creates a function that doubles input
        self.assertEqual(double(5), 10)
        self.assertEqual(double(-3), -6)
        self.assertEqual(double(0), 0)
    
    def test_multiplier_triple(self):
        triple = multiplier(3)  # creates a function that triples input
        self.assertEqual(triple(4), 12)
        self.assertEqual(triple(-2), -6)
        self.assertEqual(triple(0), 0)
    
    def test_multiplier_float(self):
        factor = multiplier(1.5)  # test float multiplication
        self.assertAlmostEqual(factor(2), 3.0)
        self.assertAlmostEqual(factor(4), 6.0)

if __name__ == "__main__":
    unittest.main()
