#!/usr/bin/python3
"""Module containing append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8).

    Args:
        filename (str, optional): name of the file. Defaults to is "".
        text (str, optional): string of text to write to file. Defaults to is "".

    Returns:
        int: number of characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """This method returns the number of characters appended to a file."""
        return f.write(text)
