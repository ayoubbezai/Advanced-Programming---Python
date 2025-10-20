import unittest
from tp3.tp3_functions_classes import power, sum_of_powers

class TestExercise1(unittest.TestCase):
    
    def test_power_basic(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, 1), 3)
        self.assertAlmostEqual(power(2.5, 2), 6.25)
        
    def test_sum_of_powers_basic(self):
        self.assertEqual(sum_of_powers([1, 2, 3], 2), 1**2 + 2**2 + 3**2)
        self.assertEqual(sum_of_powers([2, 3, 4], 3), 2**3 + 3**3 + 4**3)
        self.assertAlmostEqual(sum_of_powers([1.5, 2.5], 2), 1.5**2 + 2.5**2)
        
    def test_sum_empty_list(self):
        self.assertEqual(sum_of_powers([], 2), 0)
        
    def test_negative_numbers(self):
        self.assertEqual(sum_of_powers([-1, -2], 2), (-1)**2 + (-2)**2)

if __name__ == "__main__":
    unittest.main()
