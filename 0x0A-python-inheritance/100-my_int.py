#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """inverts != operator"""
        return int(self) == int(other)
