#!/usr/bin/python3
"""module that read a file and prints to stdout"""


def read_file(filename=""):
    """function that opens a file and print it's content on stdout"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
