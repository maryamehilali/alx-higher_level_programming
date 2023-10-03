#!/usr/bin/python3
"""class rectangles"""


class Rectangle:
    """This is a class creates a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializing of a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """method to calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """method to calculate perimeter"""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """return the string representation of a rectangle"""
        if self.__height == 0 or self.width == 0:
            return ''
        string = ''
        for i in range(self.__height):
            string += "#" * self.__width
            if i < (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        """repr built in"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del built-in"""
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
