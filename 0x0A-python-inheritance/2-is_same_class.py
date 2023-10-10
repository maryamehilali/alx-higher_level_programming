#!/usr/bin/python3
"""module that contains is_same_class function"""


def is_same_class(obj, a_class):
    """
    is_same_class is a function thatchecks if an object is
    an anstance of a given class

    Args:
    - obj: the object
    - a_class: the class to match the type of obj with
    Return:
    - returns True if it matche False if not

    """
    if type(obj) is a_class:
        return True
    else:
        return False
