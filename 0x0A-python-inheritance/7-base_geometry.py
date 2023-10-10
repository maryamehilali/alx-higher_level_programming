#!/usr/bin/python3
"""module that creates the class BaseGeometry"""


class BaseGeometry(object):
    """
        This is the BaseGeometryclass
    """
    def area(self):
        """area() method that rasise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
