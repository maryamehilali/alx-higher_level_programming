#!/usr/bin/python3
"""module that writes to a file"""


def write_file(filename="", text=""):
    """function that writes to a file
    returns the number of characters read"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
