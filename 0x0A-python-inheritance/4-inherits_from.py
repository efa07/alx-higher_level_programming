#!/usr/bin/python3
"""inherits_from method"""


def inherits_from(obj, a_class):
    """
    Returns:
        True: if the object is an instance of a class that 
        inherited from the specified class;
        False: else
    """
    return isinstance(obj, a_class) and type(obj) != a_class
