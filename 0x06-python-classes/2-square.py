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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
