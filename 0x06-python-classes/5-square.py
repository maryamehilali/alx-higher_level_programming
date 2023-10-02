#!/usr/bin/python3
"""class that creats squares"""


class Square:
    """This is a class creates a square
        it gives it the private attribute size
    """
    def __init__(self, size=0):
        """a methode that initialise the square

        _size: private attribute size of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """a methode that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
