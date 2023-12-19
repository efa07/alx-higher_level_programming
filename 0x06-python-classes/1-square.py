#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
