#!/usr/bin/python3
"""tests for the class Rectangle"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """suite tests for Rectangle Class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle1(self):
        """test new rectangle instance"""
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_rectangle2(self):
        """test new rectangle with id"""
        new = Rectangle(2, 4, 3, 4, 18)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.x, 3)
        self.assertEqual(new.y, 4)
        self.assertEqual(new.id, 18)

    def test_missing_args(self):
        """case of missing args"""
        with self.assertRaises(TypeError):
            new = Rectangle(2)
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_acces_private(self):
        """accessing private attributes"""
        new = Rectangle(2, 4, 2, 3, 25)
        with self.assertRaises(AttributeError):
            new.__width
        with self.assertRaises(AttributeError):
            new.__height
        with self.assertRaises(AttributeError):
            new.__x
        with self.assertRaises(AttributeError):
            new.__y
        self.assertEqual(new._Rectangle__width, 2)

    def test_typeerror(self):
        """test for type errors"""
        with self.assertRaises(TypeError) as e:
            Rectangle(width=2.5, height=3)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(width=[2], height=5)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(width=2, height=float('inf'))
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 'j', 5)
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 4, {})
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_valueError(self):
        """tests for value errors"""
        with self.assertRaises(ValueError) as e:
            Rectangle(width=-2, height=5)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(width=2, height=0)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -5, 1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 0, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """test area method"""
        new = Rectangle(4, 7)
        self.assertEqual(new.area(), 28)

    def test_display(self):
        """test for display method"""
        new = Rectangle(2, 3)
        