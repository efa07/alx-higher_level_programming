#!/usr/bin/python3
"""Modele for testing Rectangle class"""


import unittest
import io
import unittest.mock
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """

    def test_create_rectangle(self):
        """
        Test case to ensure correct creation of a Rectangle instance.
        """
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_invalid_width(self):
        """
        Test case to ensure appropriate exceptions are raised for invalid width values.
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("5", 10)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 10)

    def test_invalid_height(self):
        """
        Test case to ensure appropriate exceptions are raised for invalid height values.
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, "10")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 0)

    def test_invalid_x(self):
        """
        Test case to ensure appropriate exceptions are raised for invalid x values.
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 10, "2")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, -2)

    def test_invalid_y(self):
        """
        Test case to ensure appropriate exceptions are raised for invalid y values.
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 10, 2, "2")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, 2, -2)

    def test_area(self):
        """
        Test case to calculate the area of a Rectangle.
        """
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        """
        Test case to check the display of a Rectangle.
        """
        rectangle = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        """
        Test case to update the attributes of a Rectangle.
        """
        rectangle = Rectangle(5, 10)
        rectangle.update(1, 15, 20, 2, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

        rectangle.update(width=25, height=30)
        self.assertEqual(rectangle.width, 25)
        self.assertEqual(rectangle.height, 30)

    def test_to_dictionary(self):
        """
        Test case to convert a Rectangle instance to a dictionary.
        """
        rectangle = Rectangle(5, 10, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
