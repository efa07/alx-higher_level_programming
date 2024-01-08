#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """
    Lookup function
    Returns: a list of available attributes and functions of an object
    """
    return dir(obj)
