#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the num
    of char written.

    Args:
        filename (str, optional): name of the file. Defaults to is "".
        text (str, optional): string of text to write to file. Defaults to is "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
