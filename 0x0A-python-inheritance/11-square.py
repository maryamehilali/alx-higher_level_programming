#!/usr/bin/python3
"""module that creates the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size):
        """
        Instantiation with size
        and validating it with integer_validator method
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        str returns the informations of the rectangle
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
