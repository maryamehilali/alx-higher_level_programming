#!/usr/bin/python3
"""module that creates the function add_atribute"""


def add_attribute(obj, attr, value):
    """ adds an attribute to an object"""
    if not hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
