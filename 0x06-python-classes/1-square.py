#!/usr/bin/python3
"""class that creats squares"""


class Square:
    """This is a class creates a square
        it gives it the private attribute size
    """
    def __init__(self, size):
        """a methode that initialise the square

        _size: private attribute size of the square
        """
        self.__size = size
