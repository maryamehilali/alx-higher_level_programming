#!/usr/bin/python3
"""module that creates the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """
        Instantiation with width and height
        and validation them with integer_validator method
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
