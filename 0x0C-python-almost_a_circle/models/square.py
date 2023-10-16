#!/usr/bin/python3
"""module for creating a Square class that
inherits from the Rectangle Class"""
from rectangle import Rectangle


class Square(Rectangle):
    """defining the Square class that inherits from the Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializin the Square attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ methode to print
        the informations of the Square"""
        return("[Square] ({}) {}/{} - {}".
               format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter (width and height)"""
        super(Square, self.__class__).width.__set__(self, value)
        super(Square, self.__class__).height.__set__(self, value)

    def update(self, *args, **kwargs):
        """update the instance attributes with tha arguments given in *args"""
        if args != ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in dir(self):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
