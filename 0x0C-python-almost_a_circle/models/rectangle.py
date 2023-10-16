#!/usr/bin/python3
"""module for class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the width, height, x and y of the Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """methode to calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """methode to display the rectangle in stdout using "#" sign"""
        for a in range(self.y):
            print()
        for i in range(self.__height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ methode to print
        the informations of the rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}".
               format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update the instance attributes with tha arguments given in *args"""
        if args != ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in dir(self):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Rectangle heightgetter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Rectangle x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Rectangle x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Rectangle y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Rectangle y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
