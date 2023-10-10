#!/usr/bin/python3
"""module that contains inherits_from function"""


def inherits_from(obj, a_class):
    """
    inherits_fromis a function thatchecks if an object is
    an anstance of a class that inherited (directly or indirectly)
    from the specified class

    Args:
    - obj: the object
    - a_class: the class to match the type of obj with
    Return:
    - returns True if it matche False if not

    """
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class
