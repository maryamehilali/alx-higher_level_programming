#!/usr/bin/python3
"""class that creats squares"""


class Square:
    """This is a class creates a square
        it gives it the private attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """a methode that initialise the square

        _size: private attribute size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """a methode that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size, end='')
            print()
