import unittest
from tp3.tp3_functions_classes import Dog, Cat, Bird
import io
import sys

class TestAnimalSpeak(unittest.TestCase):

    def capture_output(self, func):
        """Helper to capture print output."""
        captured = io.StringIO()
        sys.stdout = captured
        func()
        sys.stdout = sys.__stdout__
        return captured.getvalue().strip()

    def test_dog_speak(self):
        dog = Dog()
        output = self.capture_output(dog.speak)
        self.assertEqual(output, "Woof!")

    def test_cat_speak(self):
        cat = Cat()
        output = self.capture_output(cat.speak)
        self.assertEqual(output, "Meow!")

    def test_bird_speak(self):
        bird = Bird()
        output = self.capture_output(bird.speak)
        self.assertEqual(output, "Chirp!")

if __name__ == "__main__":
    unittest.main()
