import unittest
from tp3.tp3_functions_classes import celsius_to_fahrenheit 

class TestEx2(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(celsius_to_fahrenheit([]), [])

    def test_single_value(self):
        """Test conversion of a single Celsius value."""
        self.assertAlmostEqual(celsius_to_fahrenheit([0])[0], 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit([100])[0], 212.0)

    def test_multiple_values(self):
        """Test conversion of multiple Celsius values."""
        celsius = [0, 20, 37, 100]
        expected = [32.0, 68.0, 98.6, 212.0]
        result = celsius_to_fahrenheit(celsius)
        # Use almost equal because of float precision
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=1)

    def test_negative_values(self):
        """Test conversion of negative Celsius values."""
        celsius = [-40, -10, -273.15]
        expected = [-40.0, 14.0, -459.67]
        result = celsius_to_fahrenheit(celsius)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=2)

if __name__ == "__main__":
    unittest.main()
