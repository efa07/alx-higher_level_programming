#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_create_rectangle(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("10", 20)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 20)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, "20")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 0)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, "30")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, 30, "40")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, 30, -1)

    def test_area(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.area(), 200)

    def test_display(self):
        rectangle = Rectangle(3, 2, 1, 1)
        expected_output = "\n" \
                          " ###\n" \
                          " ###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        rectangle = Rectangle(10, 20)
        rectangle.update(1, 5, 5, 2, 2)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

        rectangle.update(width=15, height=25)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)

    def test_to_dictionary(self):
        rectangle = Rectangle(10, 20, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 10, 'height': 20, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
