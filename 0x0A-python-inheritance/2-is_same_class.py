#!/usr/bin/python3
"""is_same_class method"""


def is_same_class(obj, a_class):
    """
    Returns:
        True: if the object is exactly an instance of the specified class
        False: Else
        """
    return type(obj) == a_class
