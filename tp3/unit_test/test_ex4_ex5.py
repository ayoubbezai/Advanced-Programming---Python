# test_ex4_ex5.py
import unittest
from io import StringIO
import sys

from tp3.tp3_functions_classes import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        """Create a sample student for testing."""
        self.student = Student("Alice", 20, 85.0)

    def test_initial_attributes(self):
        """Test that initial attributes are correctly set."""
        self.assertEqual(self.student.name, "Alice")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.grade, 85.0)

    def test_display_info_output(self):
        """Test the display_info method prints correct information."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.student.display_info()
        sys.stdout = sys.__stdout__

        expected_output = "Name: Alice, Age: 20, Grade: 85.0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_grade(self):
        """Test that update_grade modifies the grade and prints confirmation."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.student.update_grade(90.0)
        sys.stdout = sys.__stdout__

        # Check that the grade was updated
        self.assertEqual(self.student.grade, 90.0)

        # Check printed confirmation message
        expected_msg = "Alice's grade updated from 85.0 to90.0 \n"
        self.assertIn("Alice's grade updated", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
