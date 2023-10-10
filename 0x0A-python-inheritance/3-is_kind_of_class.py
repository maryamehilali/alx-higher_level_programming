#!/usr/bin/python3
"""module that contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class is a function thatchecks if an object is
    an anstance of a given class or a class that inherits from it

    Args:
    - obj: the object
    - a_class: the class to match the type of obj with
    Return:
    - returns True if it matche False if not

    """
    return isinstance(obj, a_class)
