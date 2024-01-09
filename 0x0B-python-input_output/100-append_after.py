#!/usr/bin/python3
"""Module that contains append_after function """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line,
    containing a specific string.

    Args:
        filename (str, optional): name of file. Defaults to is "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
