#!/usr/bin/python3
"""Module for test Square class"""


import unittest
import io
import unittest.mock
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class.
    """

    def test_create_square(self):
        """
        Test case to ensure correct creation of a Square instance.
        """
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_invalid_size(self):
        """
        Test case to ensure appropriate exceptions are raised for invalid size values.
        """
        with self.assertRaises(TypeError):
            square = Square("5")

        with self.assertRaises(ValueError):
            square = Square(0)

    def test_area(self):
        """
        Test case to calculate the area of a Square.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """
        Test case to check the display of a Square.
        """
        square = Square(3, 1, 1)
        expected_output = "\n" \
                          " ###\n" \
                          " ###\n" \
                          " ###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            square.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        """
        Test case to update the attributes of a Square.
        """
        square = Square(5)
        square.update(1, 10, 2, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

        square.update(size=15)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)

    def test_to_dictionary(self):
        """
        Test case to convert a Square instance to a dictionary.
        """
        square = Square(5, 1, 2, 3)
        expected_dict = {'id': 3, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
