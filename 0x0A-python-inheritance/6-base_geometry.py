#!/usr/bin/python3
"""module that creates the class BaseGeometry"""


class BaseGeometry(object):
    """
        This is the BaseGeometryclass
    """
    def area(self):
        """area() method that rasise an exception"""
        raise Exception("area() is not implemented")
