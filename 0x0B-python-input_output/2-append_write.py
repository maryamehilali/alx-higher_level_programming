#!/usr/bin/python3
"""module that appends to a file"""


def append_write(filename="", text=""):
    """function that appends to a file
    returns the number of characters read"""
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
