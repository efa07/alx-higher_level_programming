#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int number.
        b: second int number, 98 is default input.

    Raises:
        TypeError: if a, b are not int or float.

    Returns:
        Addtion of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
