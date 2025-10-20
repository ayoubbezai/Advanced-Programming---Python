import unittest
from tp3.tp3_functions_classes import Circle, Rectangle, Shape

class TestShapesEx9(unittest.TestCase):

    def test_circle_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area(), 12.566370614359172)

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_shape_area_not_implemented(self):
        s = Shape()
        with self.assertRaises(NotImplementedError):
            s.area()

if __name__ == "__main__":
    unittest.main()
