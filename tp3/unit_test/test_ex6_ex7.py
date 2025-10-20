import unittest
from tp3.tp3_functions_classes import Person, Teacher

class TestPersonTeacher(unittest.TestCase):

    def test_person_attributes(self):
        p = Person("Alice", 30)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)

    def test_person_methods(self):
        p = Person("Alice", 30)
        # capture printed output
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        p.introduce()
        p.work()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Hello, I am Alice, 30 years old.", output)
        self.assertIn("Doing something generic...", output)

    def test_teacher_attributes(self):
        t = Teacher("Bob", 40, "Math")
        self.assertEqual(t.name, "Bob")
        self.assertEqual(t.age, 40)
        self.assertEqual(t.subject, "Math")

    def test_teacher_methods(self):
        t = Teacher("Bob", 40, "Math")
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        t.introduce()
        t.work()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Hello, I am Bob, 40 years old, and I teach Math.", output)
        self.assertIn("Teaching students...", output)

if __name__ == "__main__":
    unittest.main()
