import unittest
from tp3.tp3_functions_classes import Person, Student, Teacher

class TestSchoolEx10(unittest.TestCase):

    def test_person_introduce(self):
        p = Person("John", 30)
        self.assertEqual(p.introduce(), "Hello, I am John, 30 years old.")

    def test_student_introduce(self):
        s = Student("Alice", 16, 88.5)
        self.assertEqual(s.introduce(), "Hello, I am Alice, 16 years old, and my grade is 88.5.")

    def test_teacher_introduce(self):
        t = Teacher("Mr. Bob", 40, "Math")
        self.assertEqual(t.introduce(), "Hello, I am Mr. Bob, 40 years old, and I teach Math.")

if __name__ == "__main__":
    unittest.main()
