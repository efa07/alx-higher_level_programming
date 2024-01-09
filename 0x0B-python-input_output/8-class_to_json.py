#!/usr/bin/python3
"""Module containing class_to_json function"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure,
    for JSON serialization of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """

    return obj.__dict__
